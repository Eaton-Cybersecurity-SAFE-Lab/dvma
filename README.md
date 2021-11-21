# Damn Vulnerable Modbus Application

## Setup
```shell
python -c 'from django.core.management.utils import get_random_secret_key;print(get_random_secret_key())' # Generate SECRET key
```
Create `local_settings.py` in `/dvma` with following contents:
```python
SECRET_KEY = '${SECRET_KEY_FROM_PREVIOUS_STEP}'
DEBUG = True
ALLOWED_HOSTS = ["localhost", "127.0.0.1"]
```

Web Server Setup
```shell
pip install -r requirements.txt
python manage.py migrate
python manage.py createsuperuser ## Create admin user for your local instancep
```

Modbus Backend
```shell
cd modbus
python server.py
```

Dam Sensor Simulators
```shell
cd modbus
python sensor_simulator.py
```
