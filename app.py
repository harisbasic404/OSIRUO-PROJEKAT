from flask import Flask, render_template, request, flash, jsonify  # Uvozi Flask i potrebne funkcije za web aplikaciju
import requests  # Za HTTP zahtjeve prema vanjskim API-ima
import os        # Za rad s okruženjem i varijablama okoline
from datetime import datetime  # Za rad s datumima i vremenom
from collections import defaultdict  # Za automatsko kreiranje listi u rječniku

app = Flask(__name__)  # Inicijalizacija Flask aplikacije
app.secret_key = "tajna"  # Tajni ključ za sesije i flash poruke

# API ključ za OpenWeatherMap, uzima iz okoline ili koristi podrazumijevani
API_KEY = os.getenv("OPENWEATHER_API_KEY", "9c15604876e0870af0a48a7e860e53ce")
WEATHER_URL = "http://api.openweathermap.org/data/2.5/weather"  # URL za trenutnu prognozu
FORECAST_URL = "http://api.openweathermap.org/data/2.5/forecast"  # URL za vremensku prognozu

def format_time(utc, tz):
    # Pretvara UTC timestamp i vremensku zonu u lokalno vrijeme (HH:MM)
    return datetime.utcfromtimestamp(utc + tz).strftime('%H:%M')

def group_forecast_by_day(forecast_data):
    # Grupira prognozu po danima i bira najbliži podatak podnevu za svaki dan
    days = defaultdict(list)
    for item in forecast_data.get("list", []):  # Iterira kroz sve vremenske tačke
        date = item["dt_txt"][:10]  # Izvlači datum (YYYY-MM-DD)
        days[date].append(item)     # Dodaje podatak u odgovarajući dan
    daily = []
    dani = ["Ponedjeljak", "Utorak", "Srijeda", "Četvrtak", "Petak", "Subota", "Nedjelja"]  # Dani u sedmici
    for date, items in days.items():
        target = min(items, key=lambda x: abs(int(x["dt_txt"][11:13]) - 12))  # Bira podatak najbliži 12h
        dt_obj = datetime.strptime(date, "%Y-%m-%d")  # Pretvara string u datum
        day_name = dani[dt_obj.weekday()]  # Dobija ime dana
        target["day_name"] = day_name      # Dodaje ime dana u podatak
        daily.append(target)               # Dodaje u listu dnevnih prognoza
    return daily

@app.route("/", methods=["GET", "POST"])
def index():
    # Glavna ruta: prikazuje formu i rezultate prognoze
    weather_data = None
    forecast_data = None
    forecast_hourly = None
    forecast_daily = None
    city = None
    error = None

    if request.method == "POST":
        # Ako je forma poslana (POST), uzima grad iz forme
        city = request.form.get("city", "").strip()
        if not city:
            error = "Unesite naziv grada."  # Ako nije unesen grad, javlja grešku
        else:
            params = {
                "q": city,
                "appid": API_KEY,
                "units": "metric",
                "lang": "hr"
            }
            try:
                response = requests.get(WEATHER_URL, params=params, timeout=5)  # Traži trenutnu prognozu
                if response.status_code == 200:
                    data = response.json()
                    weather_data = {
                        "main": data["main"],  # Osnovni meteorološki podaci
                        "wind": data["wind"],  # Podaci o vjetru
                        "weather": data["weather"],  # Opis vremena
                        "clouds": data.get("clouds", {}),  # Oblaci
                        "visibility": data.get("visibility"),  # Vidljivost
                        "sys": data.get("sys", {}),  # Sistemski podaci (izlazak/zalazak sunca)
                        "coord": data.get("coord", {}),  # Koordinate
                        "timezone": data.get("timezone", 0),  # Vremenska zona
                        "name": data.get("name"),  # Ime grada
                        "sunrise": format_time(data["sys"]["sunrise"], data["timezone"]) if "sys" in data and "sunrise" in data["sys"] else None,
                        # Izlazak sunca (formatiran)
                        "sunset": format_time(data["sys"]["sunset"], data["timezone"]) if "sys" in data and "sunset" in data["sys"] else None,
                        # Zalazak sunca (formatiran)
                    }
                else:
                    error = "Grad nije pronađen ili došlo je do greške."
            except requests.RequestException:
                error = "Greška u komunikaciji s vremenskim servisom."

            if not error:
                # Ako nema greške, traži i vremensku prognozu (5 dana, svakih 3h)
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
                        forecast_hourly = forecast_data["list"][:8]  # Prvih 8 tačaka (24h)
                        forecast_daily = group_forecast_by_day(forecast_data)  # Grupisano po danima
                    else:
                        forecast_data = None
                except requests.RequestException:
                    forecast_data = None

        if error:
            flash(error, "danger")  # Prikazuje grešku korisniku

    # Renderuje HTML šablon i šalje podatke za prikaz
    return render_template(
        "index.html",
        weather=weather_data,
        city=city,
        forecast_hourly=forecast_hourly,
        forecast_daily=forecast_daily
    )

@app.route("/geo")
def geo_proxy():
    # Proxy ruta za autocomplete gradova (preusmjerava prema OpenWeatherMap geo API-ju)
    q = request.args.get("q", "")
    if not q:
        return jsonify([])  # Ako nema upita, vraća praznu listu
    url = "https://api.openweathermap.org/geo/1.0/direct"
    params = {
        "q": q,
        "limit": 7,
        "appid": API_KEY
    }
    try:
        r = requests.get(url, params=params, timeout=5)
        return jsonify(r.json())  # Vraća rezultat kao JSON
    except Exception:
        return jsonify([])  # U slučaju greške, vraća praznu listu

if __name__ == "__main__":
    # Pokreće Flask aplikaciju lokalno
    import os
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
