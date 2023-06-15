import board
import busio
from digitalio import DigitalInOut
from adafruit_ble import BLERadio
from adafruit_ble.advertising.standard import ProvideServicesAdvertisement
from adafruit_ble.services.nordic import UARTService
from adafruit_esp32spi import adafruit_esp32spi
from adafruit_airlift.esp32 import ESP32

test_data = []

esp32 = ESP32()

adapter = esp32.start_bluetooth()
ble = BLERadio(adapter)
uart = UARTService()
advertisement = ProvideServicesAdvertisement(uart)


def connect_ble():
    ble.start_advertising(advertisement)
    print("waiting to connect")
    while not ble.connected:
        pass
    print("connected: trying to read input")
    while ble.connected:
        # Returns b'' if nothing was read.
        one_byte = uart.read(1)
        if one_byte:
            print(one_byte)
            uart.write(one_byte)

def read_ble():
    if not bluefruit.connected:
        return
    # OK we're still connected, see if we have any data waiting
    if ble.connected:
        s = uart.readline()
        if s:
            try:
                result = str(s+"yay")
                commander.msg=s
            except Exception as e:
                result = str(s+"yayexcept")

def write_ble(msg):
    # Now write it!
    global test_data
    print(test_data)
    if isinstance(msg,list):
        m= {"data":{"t":0,"v":0,"i":0}}
        for i in test_data:
            m["data"]["t"]+=i["t"]
            m["data"]["v"]+=i["v"]
            m["data"]["i"]+=i["i"]
        m["data"]["t"]=m["data"]["t"]/len(test_data)
        m["data"]["v"]=m["data"]["v"]/len(test_data)
        m["data"]["i"]=m["data"]["i"]/len(test_data)
        m["done"]=test_data[-1].get("done",False)
        msg = str(msg) + '$'
        print(str.encode(msg))
        uart.write(str.encode(msg))
        test_data=[]
    else:
        msg = str(msg) + '$'
        print(str.encode(msg))
        uart.write(str.encode(msg))
