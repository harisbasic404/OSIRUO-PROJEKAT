#!/bin/bash
# filepath: run_docker.sh

# Zaustavi i obriši stari kontejner ako postoji
docker stop osiruo-projekat 2>/dev/null
docker rm osiruo-projekat 2>/dev/null

# Buildaj novi image
docker build -t osiruo-projekat .

# Pokreni kontejner na portu 5000
docker run -d --name osiruo-projekat -p 5000:5000 osiruo-projekat

echo "Aplikacija je pokrenuta na http://localhost:5000"