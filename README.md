# Simple Port Scanner

## Aprašymas

**Simple Port Scanner** – minimalistinė Python Flask aplikacija, skirta TCP portų skenavimui nurodytam tinklo adresui. Programėlė leidžia per paprastą web sąsają įvesti tikslinį IP adresą arba domeną bei portų diapazoną, ir patikrina, kurie portai yra atidaryti.

Projektas taip pat demonstruoja, kaip sukurti Flask aplikaciją, ją konteinerizuoti naudojant Docker ir paleisti izoliuotoje aplinkoje.

---

## Funkcionalumas

- TCP portų skenavimas pagal vartotojo įvestus portų diapazonus
- Rezultatai pateikiami aiškioje web sąsajoje
- Flask pagrindu sukurta lengvai suprantama aplikacija
- Docker konteineris paprastam paleidimui ir diegimui

---

## Technologijos

- Python 3
- Flask web framework
- Docker (konteinerizavimui)

---

## Kaip naudotis

### 1. Paleisti lokaliai (reikalauja Python ir virtualios aplinkos)

```bash
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
python app.py

Aplikacija veiks adresu:
http://127.0.0.1:5001

2. Paleisti per Docker

docker build -t simple-port-scanner .
docker run -p 5001:5001 simple-port-scanner

Aplikacija veiks adresu:
http://localhost:5001

Projekto tikslas

Šis projektas sukurtas demonstruoti pagrindinius tinklo saugumo ir web aplikacijų kūrimo įgūdžius bei Docker konteinerizavimo pagrindus. Puikiai tinka kaip demonstracinis projektas į CV.
Autorius

Darius Lukošius
https://github.com/Dariuslukosius
