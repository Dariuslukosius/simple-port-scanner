============================
Simple Port Scanner
📝 APRAŠYMAS

Minimalistinė Python Flask aplikacija, skirta TCP portų skenavimui nurodytam tinklo adresui.
Per paprastą web sąsają galima įvesti IP adresą arba domeną bei portų diapazoną ir matyti, kurie portai atidaryti.

Projektas taip pat parodo, kaip sukurti Flask aplikaciją, ją konteinerizuoti naudojant Docker ir paleisti izoliuotoje aplinkoje.
⚙️ FUNKCIONALUMAS

    TCP portų skenavimas pagal vartotojo įvestus portų diapazonus

    Rezultatai pateikiami aiškioje web sąsajoje

    Flask pagrindu sukurta lengvai suprantama aplikacija

    Docker konteineris paprastam paleidimui ir diegimui

🧰 TECHNOLOGIJOS

    Python 3

    Flask web framework

    Docker (konteinerizavimui)

🚀 PALEIDIMO BŪDAI

Galima paleisti trimis būdais – pasirink tau patogiausią.

⚠️ Pastaba: Pirmiausia nusiklonavus repozitoriją privaloma įeiti į projekto katalogą:
cd simple-port-scanner
🐳 1. Docker (rekomenduojamas)

Pats paprasčiausias būdas, jei turi Docker:

docker build -t simple-port-scanner .
docker run -p 5001:5001 simple-port-scanner

Atverk naršyklėje:
http://localhost:5001
🐍 2. Lokalus paleidimas su Python (Unix/macOS)

Atidaryk terminalą projekto kataloge ir paleisk start skriptą:

./start.sh

Jei neturi start.sh, susikurk su tokiu turiniu:
#!/bin/bash
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
python app.py

Atverk naršyklėje:
http://localhost:5001
🪟 3. Lokalus paleidimas su Python (Windows)

Atidaryk komandų eilutę projekto kataloge ir paleisk:

start.bat

Jei neturi start.bat, susikurk su tokiu turiniu:
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
python app.py
pause

Atverk naršyklėje:
http://localhost:5001
📦 Projekto struktūra (pavyzdys)

simple-port-scanner/
├── app.py
├── requirements.txt
├── Dockerfile
├── start.sh
├── start.bat
└── README.md

Sėkmės naudojant! 😊
