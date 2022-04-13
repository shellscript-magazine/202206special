import time
from machine import Pin, SoftI2C
import mpu6050
from umqtt.simple import MQTTClient
import json

mqtt_topic = "home/seismometer1"
publisher_id = "place_esp32"
broker_address = "192.168.1.100"
interval_time = "1"

i2c = SoftI2C(scl=Pin(22), sda=Pin(21))
accelerometer = mpu6050.accel(i2c)

time.sleep(5)

while True:
  iot_value = accelerometer.get_values()
  iot_value_json = json.dumps(iot_value)
  print(iot_value_json)
  publisher = MQTTClient(publisher_id,broker_address)  publisher.connect()
  publisher.publish(mqtt_topic, msg=str(iot_value_json))
  publisher.disconnect()
  time.sleep(int(interval_time))
