# Projekat iz Operativnih sistema i računarstva u oblaku  
**Naziv projekta:** Vremenska prognoza za BiH  
**Grupa:** Jašarević Adnan, Bektaš Kenan, Čamdžić Hamza , Bašić Haris  
**Cloud platforma:** Render  
**Domena:** prognozaza.me  
**GitHub repozitorij:** [https://github.com/harisbasic404/OSIRUO-PROJEKAT](https://github.com/harisbasic404/OSIRUO-PROJEKAT)  
**Link do aplikacije:** [https://vremenska-prognoza.onrender.com](https://vremenska-prognoza.onrender.com)  
**Domena:** [https://prognozaza.me](https://prognozaza.me)

---

## 1. Kratak opis projekta

Ovaj projekat je web aplikacija za prikaz vremenske prognoze za gradove u Bosni i Hercegovini i šire. Aplikacija koristi Flask, Docker, Bootstrap Icons i OpenWeatherMap API.

---

## 2. Cloud platforma

**Odabrana platforma:**  
Render  
**Razlog odabira:**  
Render nudi besplatan tier za web aplikacije, jednostavan deploy direktno sa GitHub repozitorija, podršku za Docker i lako povezivanje vlastite domene.

---

## 3. Dockerizacija aplikacije

### Dockerfile
```dockerfile
FROM python:3.10-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

EXPOSE 5000

CMD ["python", "app.py"]
```

### Pokretanje lokalno (ručno)
```bash
docker build -t osiruo-projekat .
docker run -p 5000:5000 osiruo-projekat
```

### Automatizovana skripta (`run_docker.sh`)
```bash
#!/bin/bash
docker stop osiruo-projekat 2>/dev/null
docker rm osiruo-projekat 2>/dev/null
docker build -t osiruo-projekat .
docker run -d --name osiruo-projekat -p 5000:5000 osiruo-projekat
echo "Aplikacija je pokrenuta na http://localhost:5000"
```
Pokretanje:
```bash
bash run_docker.sh
```

---

## 4. Deploy na cloud – korak po korak

1. **Registracija na Render**  
   Napravljen nalog na platformi Render.

   ![Registracija na Render](img/renderlogin.png)

2. **Povezivanje GitHub repozitorija**  
   Povezan GitHub repozitorij sa Render cloud platformom.

   ![Povezivanje repozitorija](img/gitlink.png)

3. **Konfiguracija servisa**  
   Izabrana opcija za Docker deploy, unesen naziv servisa, branch i region.

   ![Konfiguracija servisa](img/postavke.png)

4. **Podesio environment varijable**  
   Dodan API ključ za OpenWeatherMap kao environment variable.

   ![Environment varijable](img/apykeyy.png)

5. **Deploy aplikacije**  
   Deploy aplikacije (auto-deploy na svaki commit).

   ![Deploy proces](img/deployanje.png)

6. **Provjera aplikacije na javnom URL-u**  
   Provjera da aplikacija radi na javnom URL-u:  
   [https://vremenska-prognoza.onrender.com](https://vremenska-prognoza.onrender.com)

   ![Aplikacija live](img/pokrenutaaplikacija.png)

---

## 5. Konfiguracija domene

1. **Registracija domene**  
   Registrirana domena: **prognozaza.me**

   ![Custom domena](img/domena.jpg)

2. **Povezivanje domene sa Render aplikacijom**  
   Dodan CNAME/A zapis prema Render aplikaciji.

   ![Custom domena](img/customdomena.jpg)

---


## 6. Automatizacija (bash skripta)

- Skripta `run_docker.sh` automatski builda i pokreće Docker kontejner.
- Omogućava brzo testiranje lokalno bez ručnog unosa komandi.

---

## 7. Korištene komande i alati

- `docker build -t osiruo-projekat .`
- `docker run -p 5000:5000 osiruo-projekat`
- `bash run_docker.sh`
- `git clone https://github.com/harisbasic404/OSIRUO-PROJEKAT.git`
- `pip install -r requirements.txt`
- `ssh` (za pristup serverima po potrebi)
- `scp` (za kopiranje fajlova po potrebi)
- Render cloud panel za deploy i monitoring

---

## 8. Korištene tehnologije

- **Python 3.10**
- **Flask**
- **Docker**
- **Bootstrap Icons**
- **OpenWeatherMap API**
- **HTML/CSS/JS**
- **Cloud platforma:** Render

---

## 9. Linkovi

- **GitHub repozitorij:** [https://github.com/harisbasic404/OSIRUO-PROJEKAT](https://github.com/harisbasic404/OSIRUO-PROJEKAT)
- **Aplikacija na cloudu:** [https://vremenska-prognoza.onrender.com](https://vremenska-prognoza.onrender.com)
- **Domena:** [https://prognozaza.me](https://prognozaza.me)

---

## 10. Kratka refleksija: šta ste naučili

Kroz rad na ovom projektu naučili smo:
- Kako dockerizirati Python/Flask aplikaciju i koristiti Docker za razvoj i deploy.
- Kako koristiti cloud platformu Render za automatski deploy aplikacije direktno sa GitHub-a.
- Kako postaviti environment varijable i raditi sa API ključevima na cloudu.
- Kako povezati vlastitu domenu i podesiti SSL certifikat.
- Automatizaciju procesa pokretanja aplikacije putem bash skripte.
- Timsku saradnju kroz GitHub i podjelu zadataka.
- Praktičnu upotrebu OpenWeatherMap API-ja i rad sa vanjskim servisima.

---

## 11. Slike ekrana aplikacije 

- **Početna:**  
  ![Slika aplikacije](img/pocetna.png)

- **Prikaz vremena:**  
  ![Slika aplikacije](img/vrijeme.png)

- **Dark mode:**  
  ![Slika aplikacije](img/darkmode.png)

- **Light mode:**  
  ![Slika aplikacije](img/lightmode.png)

---

## 12. Dodatne napomene

- Projekat je moguće proširiti dodavanjem više funkcionalnosti (npr. prikaz vremenske prognoze na mapi, višejezičnost, itd).
- Svi koraci su dokumentovani i mogu se ponoviti za slične projekte.

---

**Kraj dokumentacije**