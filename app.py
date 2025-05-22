from flask import Flask, render_template, request, flash, jsonify
import requests
import os
from datetime import datetime
from collections import defaultdict

app = Flask(__name__)
app.secret_key = "tajna"

API_KEY = os.getenv("OPENWEATHER_API_KEY", "9c15604876e0870af0a48a7e860e53ce")
WEATHER_URL = "http://api.openweathermap.org/data/2.5/weather"
FORECAST_URL = "http://api.openweathermap.org/data/2.5/forecast"

def format_time(utc, tz):
    return datetime.utcfromtimestamp(utc + tz).strftime('%H:%M')

def group_forecast_by_day(forecast_data):
    days = defaultdict(list)
    for item in forecast_data.get("list", []):
        date = item["dt_txt"][:10]
        days[date].append(item)
    daily = []
    dani = ["Ponedjeljak", "Utorak", "Srijeda", "Četvrtak", "Petak", "Subota", "Nedjelja"]
    for date, items in days.items():
        target = min(items, key=lambda x: abs(int(x["dt_txt"][11:13]) - 12))
        dt_obj = datetime.strptime(date, "%Y-%m-%d")
        day_name = dani[dt_obj.weekday()]
        target["day_name"] = day_name
        daily.append(target)
    return daily

@app.route("/", methods=["GET", "POST"])
def index():
    weather_data = None
    forecast_data = None
    forecast_hourly = None
    forecast_daily = None
    city = None
    error = None

    if request.method == "POST":
        city = request.form.get("city", "").strip()
        if not city:
            error = "Unesite naziv grada."
        else:
            params = {
                "q": city,
                "appid": API_KEY,
                "units": "metric",
                "lang": "hr"
            }
            try:
                response = requests.get(WEATHER_URL, params=params, timeout=5)
                if response.status_code == 200:
                    data = response.json()
                    weather_data = {
                        "main": data["main"],
                        "wind": data["wind"],
                        "weather": data["weather"],
                        "clouds": data.get("clouds", {}),
                        "visibility": data.get("visibility"),
                        "sys": data.get("sys", {}),
                        "coord": data.get("coord", {}),
                        "timezone": data.get("timezone", 0),
                        "name": data.get("name"),
                        "sunrise": format_time(data["sys"]["sunrise"], data["timezone"]) if "sys" in data and "sunrise" in data["sys"] else None,
                        "sunset": format_time(data["sys"]["sunset"], data["timezone"]) if "sys" in data and "sunset" in data["sys"] else None,
                    }
                else:
                    error = "Grad nije pronađen ili došlo je do greške."
            except requests.RequestException:
                error = "Greška u komunikaciji s vremenskim servisom."

            if not error:
                params_forecast = {
                    "q": city,
                    "appid": API_KEY,
                    "units": "metric",
                    "lang": "hr"
                }
                try:
                    response_forecast = requests.get(FORECAST_URL, params=params_forecast, timeout=5)
                    if response_forecast.status_code == 200:
                        forecast_data = response_forecast.json()
                        forecast_hourly = forecast_data["list"][:8]
                        forecast_daily = group_forecast_by_day(forecast_data)
                    else:
                        forecast_data = None
                except requests.RequestException:
                    forecast_data = None

        if error:
            flash(error, "danger")

    return render_template(
        "index.html",
        weather=weather_data,
        city=city,
        forecast_hourly=forecast_hourly,
        forecast_daily=forecast_daily
    )

@app.route("/geo")
def geo_proxy():
    q = request.args.get("q", "")
    if not q:
        return jsonify([])
    url = "https://api.openweathermap.org/geo/1.0/direct"
    params = {
        "q": q,
        "limit": 7,
        "appid": API_KEY
    }
    try:
        r = requests.get(url, params=params, timeout=5)
        return jsonify(r.json())
    except Exception:
        return jsonify([])

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
