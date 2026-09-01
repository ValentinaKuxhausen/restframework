🚀 Projekt starten (Django)
1. In Projektordner gehen
(cd dahin, wo manage.py liegt)
cd projektname

2. Virtual Environment aktivieren
Windows (PowerShell):
.\.venv\Scripts\activate
Git Bash:
source .venv/Scripts/activate

3. Server starten (Git Bash)
python manage.py runserver

4. Im Browser öffnen
http://127.0.0.1:8000/
Beispiel Endpoint:
http://127.0.0.1:8000/market/

🛠️ Falls etwas nicht funktioniert
❌ Fehler: Module nicht gefunden
→ .venv nicht aktiv
✔ Lösung:
pip install -r requirements.txt

❌ Port belegt
✔ Lösung:
python manage.py runserver 8001

❌ Datenbank fehlt / neu
✔ Lösung:
python manage.py migrate

❌ Neue Models hinzugefügt
✔ Lösung:
python manage.py makemigrations
python manage.py migrate