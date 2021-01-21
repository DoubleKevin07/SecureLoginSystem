powershell -Command "& {pip3 install -r requirements.txt; $env:FLASK_APP='application.py'; $env:FLASK_DEBUG='true'; $env:DATABASE_URL='<DATABASE URL HERE>';flask run;}"
pause