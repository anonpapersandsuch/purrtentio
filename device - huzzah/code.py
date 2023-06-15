import time
import board
import busio as io
import pyrebase
import os
import ipaddress
import wifi
import socketpool

print()
print("Connecting to WiFi")

#  connect to your SSID
wifi.radio.connect(os.getenv('CIRCUITPY_WIFI_SSID'), os.getenv('CIRCUITPY_WIFI_PASSWORD'))

print("Connected to WiFi")

#pool = socketpool.SocketPool(wifi.radio)

#  prints MAC address to REPL
print("My MAC addr:", [hex(i) for i in wifi.radio.mac_address])

#  prints IP address to REPL
print("My IP address is", wifi.radio.ipv4_address)

#  pings Google
# ipv4 = ipaddress.ip_address("8.8.4.4")
# print("Ping google.com: %f ms" % (wifi.radio.ping(ipv4)*1000))

# import adafruit_requests as requests
#
# # Initialize a requests object with a socket and esp32spi interface
# socketpool.set_interface(wifi)
# requests.set_socket(socketpool, wifi)
#
# TEXT_URL = "http://wifitest.adafruit.com/testwifi/index.html"
# JSON_GET_URL = "https://httpbin.org/get"
# JSON_POST_URL = "https://httpbin.org/post"
#
# print("Fetching text from %s" % TEXT_URL)
# response = requests.get(TEXT_URL)
# print("-" * 40)
#
# print("Text Response: ", response.text)
# print("-" * 40)
# response.close()
#
# print("Fetching JSON data from %s" % JSON_GET_URL)
# response = requests.get(JSON_GET_URL)
# print("-" * 40)
#
# print("JSON Response: ", response.json())
# print("-" * 40)
# response.close()
#
# data = "31F"
# print("POSTing data to {0}: {1}".format(JSON_POST_URL, data))
# response = requests.post(JSON_POST_URL, data=data)
# print("-" * 40)
#
# json_resp = response.json()
# # Parse out the 'data' key from json_resp dict.
# print("Data received from server:", json_resp["data"])
# print("-" * 40)
# response.close()
#
# json_data = {"Date": "July 25, 2019"}
# print("POSTing data to {0}: {1}".format(JSON_POST_URL, json_data))
# response = requests.post(JSON_POST_URL, json=json_data)
# print("-" * 40)
#
# json_resp = response.json()
# # Parse out the 'json' key from json_resp dict.
# print("JSON Data received from server:", json_resp["json"])
# print("-" * 40)
# response.close()


config = {
  "apiKey": "AIzaSyD43mKUcEDXiLyIhbSDRBFX7SQ5GTPDwNE",
  "authDomain": "purrtentio.firebaseapp.com",
  "databaseURL": "https://purrtentio-default-rtdb.firebaseio.com/",
  "storageBucket": "purrtentio.appspot.com"
}

firebase = pyrebase.initialize_app(config)
db = firebase.database()

print("Send Data to Firebase Using Raspberry Pi")
print("----------------------------------------")
print()

while True:
  ambientString = "hihihihihihi"
  objectString = "hjhjkhjkhjk"

  ambientCelsius = ambientString
  objectCelsius = objectString

  print("Ambient Temp: {} °C".format(ambientString))
  print("Object Temp: {} °C".format(objectString))
  print()

  data = {
    "ambient": ambientCelsius,
    "object": objectCelsius,
  }
  db.child("mlx90614").child("1-set").set(data)
  db.child("mlx90614").child("2-push").push(data)

  time.sleep(2)
