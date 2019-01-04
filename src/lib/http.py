"""
HTTP API functions
"""
try:
    import urequests as requests
except ImportError:
    import requests


HEADERS = {
    'content-type': "application/json"
}


def emit_sensor(url, device_id, device_name, temperature, humidity):
    payload = {"device_id": device_id, "device_name": device_name, "temperature": temperature, "humidity": humidity }
    response = requests.post(url, json=payload, headers=HEADERS)
    print(response.text)
