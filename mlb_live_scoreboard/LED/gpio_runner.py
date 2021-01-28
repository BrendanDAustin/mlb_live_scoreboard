import RPi.GPIO as GPIO
from numpy import array
from LED.pin_map import gpio_map
from LED.values_matrix import Matrix
from time import sleep
matrix = Matrix()
gpio_addresses = gpio_map()
pin_addresses = gpio_addresses.pin_set
GPIO.setup(pin_addresses,GPIO.OUT)
def run_dummy(time_sleep):
    while True:
        for i in matrix.values:
            matrix.lock.acquire()
            print(i)
            matrix.lock.release()
            sleep(time_sleep)

def run():
    while True:
        for i in matrix.values:
            matrix.lock.acquire()
            GPIO.output(pin_addresses,i)
            matrix.lock.release()


