# Damn Vulnerable Modbus Application

## Setup
```shell
pip instal -r requirements.txt
python manage.py migrate
python manage.py createsuperuser ## Create admin user for your local instancep
python -c 'from django.core.management.utils import get_random_secret_key;print(get_random_secret_key())' # Generated SECRET key
```

Create `local_settings.py` in `/dvma` with following contents:
```python
SECRET_KEY = '${SECRET_KEY_FROM_PREVIOUS_STEP}'
DEBUG = True
ALLOWED_HOSTS = []
```
