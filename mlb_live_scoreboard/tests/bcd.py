from LED import gpio_runner
from datetime import datetime, timedelta
from threading import Thread
matrix = gpio_runner.matrix
def bcd_0():
    counter = 0
    for key in matrix.LED_VALUE_MATRIX_INDICES.keys():
        if 'top_' in key and '9' not in key and '10' not in key:
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
        if 'top_' in key and '9' not in key and '10' not in key:
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
        if 'bottom_' in key and '9' not in key and '10' not in key:
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
        if 'bottom_' in key and '9' not in key and '10' not in key:
            matrix.set_inning_score(key,counter)
            counter-=1
    startTime = datetime.now()
    endTime = startTime + timedelta(seconds=10)
    while True:
        if datetime.now()>=endTime:
            break
    matrix.all_off()

def bcd_2():
    counter = 0
    for key in matrix.LED_VALUE_MATRIX_INDICES.keys():
        if '9' in key or '10' in key or 'runs' in key:
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
        if '9' in key or '10' in key or 'runs' in key:
            matrix.set_inning_score(key,counter)
            counter-=1
    startTime = datetime.now()
    endTime = startTime + timedelta(seconds=10)
    while True:
        if datetime.now()>=endTime:
            break
    matrix.all_off()

def main():
    print('testing bcd0 (top innings 1-8)')
    bcd_0()
    print('testing bcd1 (bottom innings 1-8)')
    bcd_1()
    print("testing bcd2 (top/bottom innings 9-10, home runs, away runs)")
    bcd_2()
    print('done with bcd test')

if __name__=="__main__":
    main()


    


