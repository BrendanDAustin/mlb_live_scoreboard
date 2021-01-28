from LED import gpio_runner
from datetime import datetime, timedelta
from threading import Thread
matrix = gpio_runner.matrix
def bcd_0():
    counter = 0
    for key in matrix.LED_VALUE_MATRIX_INDICES.keys():
        if 'top_' in key:
            matrix.set_inning_score(key,counter)
            counter+=1
    startTime = datetime.now()
    endTime = startTime + timedelta(seconds=10)
    runner = Thread(target=gpio_runner.run)
    runner.daemon=True
    runner.start()
    while True:
        if datetime.now()>=endTime:
            break
    counter = 8
    for key in matrix.LED_VALUE_MATRIX_INDICES.keys():
        if 'top_' in key:
            matrix.set_inning_score(key,counter)
            counter-=1
    startTime = datetime.now()
    endTime = startTime + timedelta(seconds=10)
    while True:
        if datetime.now()>=endTime:
            break
    matrix.all_off()

def bcd_1():
    counter = 0
    for key in matrix.LED_VALUE_MATRIX_INDICES.keys():
        if 'bottom_' in key:
            matrix.set_inning_score(key,counter)
            counter+=1
    startTime = datetime.now()
    endTime = startTime + timedelta(seconds=10)
    runner = Thread(target=gpio_runner.run)
    runner.daemon=True
    runner.start()
    while True:
        if datetime.now()>=endTime:
            break
    counter = 8
    for key in matrix.LED_VALUE_MATRIX_INDICES.keys():
        if 'bottom_' in key:
            matrix.set_inning_score(key,counter)
            counter-=1
    startTime = datetime.now()
    endTime = startTime + timedelta(seconds=10)
    while True:
        if datetime.now()>=endTime:
            break
    matrix.all_off()


    


