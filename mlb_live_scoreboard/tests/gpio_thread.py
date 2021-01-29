from LED import gpio_runner
from threading import Thread
from time import sleep
matrix = gpio_runner.matrix

if __name__=="__main__":
    runner = Thread(target=gpio_runner.run_dummy,args=(1,))
    runner.start()
    runner.daemon=True
    sleep(5)
    print("setting outs")
    matrix.set_outs(2)
    sleep(10)
    print('settings top_1 to 2')
    matrix.set_inning_score('top_1',2)
    sleep(5)
    matrix.clear_outs()
    sleep(5)
    print('settings bottom_1 to 0')
    matrix.set_inning_score('bottom_1',0)
    sleep(1)
    print('setting strikes to one')
    matrix.set_strikes(1)
    sleep(3)
    print('settings first base to true')
    matrix.set_bases({'first_base':True})
    sleep(4)
    print('setting bottom_1 to 2')
    matrix.set_inning_score('bottom_1',2)
    print('clearing innings')
    matrix.clear_inning()
    sleep(5)
    print('setting balls to 2')
    matrix.set_balls(2)
    sleep(3)
    print('done')


