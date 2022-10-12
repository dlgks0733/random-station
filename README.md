# random-station

## Create venv and Install requirements.txt

    \random-station > python -m venv venv
    \random-station > cd venv
    \random-station\venv > .\Scripts\Activate.ps1
    \random-station\venv > cd ..
    \random-station > pip install -r requirements.txt

## Migration

    \random-station > python manage.py makemigrations
    \random-station > python manage.py migrate
    
## Run

    \random-station > python manage.py runserver
