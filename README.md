# Projekat iz Operativnih sistema i računarstva u oblaku  
**Naziv projekta:** Vremenska prognoza za BiH  
**Grupa:** (ovdje upiši imena članova grupe)  
**Cloud platforma:** Render  
**Domena:** (upiši svoju domenu, npr. osiruo2025.freenom.com ili Namecheap domena)  
**GitHub repozitorij:** [https://github.com/harisbasic404/OSIRUO-PROJEKAT](https://github.com/harisbasic404/OSIRUO-PROJEKAT)  
**Link do aplikacije:** [https://vremenska-prognoza.onrender.com](https://vremenska-prognoza.onrender.com)

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

## 4. Deploy na cloud

**Opis koraka:**
1. Napravljen nalog na platformi Render.
2. Povezan GitHub repozitorij sa Render cloud platformom.
3. Podesio environment varijable (API ključ, SECRET_KEY ako treba).
4. Deploy aplikacije (auto-deploy na svaki commit).
5. Provjera da aplikacija radi na javnom URL-u: [https://vremenska-prognoza.onrender.com](https://vremenska-prognoza.onrender.com)

**Slike ekrana (screenshotovi):**  
_(ovdje ubaci slike iz Render deploy panela, logova, i sl.)_

---

## 5. Konfiguracija domene

1. Registracija besplatne domene na Freenom/Namecheap:  
   _(upiši naziv domene)_  
2. Povezivanje domene sa Render aplikacijom (A-zapis ili CNAME).
3. Provjera da domena radi.

**Slike ekrana:**  
_(ovdje ubaci slike iz Freenom/Namecheap panela, DNS podešavanja, i sl.)_

---

## 6. Automatizacija (bash skripta)

- Skripta `run_docker.sh` automatski builda i pokreće Docker kontejner.
- Omogućava brzo testiranje lokalno bez ručnog unosa komandi.

---

## 7. Korištene komande i alati

- `docker build -t osiruo-projekat .`
- `docker run -p 5000:5000 osiruo-projekat`
- `bash run_docker.sh`
- `git clone ...`
- `pip install -r requirements.txt`
- _(dodaj još komandi koje ste koristili, npr. za cloud, SSH, scp, ...)_  

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
- **Domena:** [ovdje link]

---

## 10. Potrebni kredencijali za prijavu

_(Nije potrebno za ovu aplikaciju, ali ostavi prostor ako bude potrebno)_

---

## 11. Kratka refleksija: šta ste naučili

_(Ovdje napiši šta ste naučili kroz rad na projektu: rad sa Dockerom, cloud deploy, rad u timu, rad sa API-jem, automatizacija, ...)_  

---

## 12. Slike ekrana aplikacije

_(Ubaci slike početne stranice, pretrage, mape, mobilnog prikaza, ...)_  

---

## 13. Dodatne napomene

_(Ovdje možeš dodati sve što je specifično za vaš projekat, izazove, ideje za poboljšanje, ...)_  

---

## 14. TODO / DOPUNITE

- [ ] Upisati imena članova grupe
- [ ] Upisati domenu
- [ ] Ubaciti slike ekrana (deploy, domena, aplikacija)
- [ ] Dopuniti refleksiju i iskustva
- [ ] Dodati sve relevantne linkove

---

**Kraj dokumentacije**