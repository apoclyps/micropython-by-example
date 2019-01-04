from time import sleep

from lib import config
from lib import gpio
from lib import http
from lib import wifi


def main():
    # establish a wifi connection
    device_id = config.get(config_file="config/device_config.json", key="device_id")
    device_name = config.get(config_file="config/device_config.json", key="device_name")
    ssid = config.get(config_file="config/device_config.json", key="ssid")
    password = config.get(config_file="config/device_config.json", key="password")
    url = config.get(config_file="config/device_config.json", key="url")

    if ssid in wifi.scan():
        wifi.connect(ssid, password)
        wifi.status()

        while wifi.status():
            gpio.toggle_leds()
            temperature, humidity = gpio.read_sensor()

            print('Temp: {0:.2f}, Humidity {1:.2f}'.format(temperature, humidity))

            http.emit_sensor(url, device_id, device_name, temperature, humidity)
            sleep(60)

if __name__ == '__main__':
    main()
