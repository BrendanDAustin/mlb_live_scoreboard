#set pin state
from threading import Thread, Event
from numpy import array
from pin_map import gpio_map
import gpio_runner

gpio_flag = Event()
runner = Thread(target=gpio_runner.run,args=(gpio_flag,))
BCD_SET = {-1:(False,False,False,False,False),
                        0:(True,False,False,False,False),
                        1:(True,False,False,False,True),
                        2:(True,False,False,True,False),
                        3:(True,False,False,True,True),
                        4:(True,False,True,False,False),
                        5:(True,False,True,False,True),
                        6:(True,False,True,True,False),
                        7:(True,False,True,True,True),
                        8:(True,True,False,False,False),
                        9:(True,True,False,False,True)}

MUX_SET = {'OFF':(False,False,False,False),
                '0':(True,False,False,False),
                '1':(True,False,False,True),
                '2':(True,False,True,False),
                '3':(True,False,True,True),
                '4':(True,True,False,False),
                '5':(True,True,False,True),
                '6':(True,True,True,False),
                '7':(True,True,True,True)}

BASES_BALLS_STRIKES_SET = {'FIRST_BASE':False,
                                'SECOND_BASE':False,
                                'THIRD_BASE':False,
                                'BALL_ONE':False,
                                'BALL_TWO':False,
                                'BALL_THREE':False,
                                'STRIKE_ONE':False,
                                'STRIKE_TWO':False}

LED_VALUE_MATRIX_INDICIES = {'top_1':[0,slice(4,9)],
                            'top_2':[1,slice(4,9)],
                            'top_3':[2,slice(4,9)],
                            'top_4':[3,slice(4,9)],
                            'top_5':[4,slice(4,9)],
                            'top_6':[5,slice(4,9)],
                            'top_7':[6,slice(4,9)],
                            'top_8':[7,slice(4,9)],
                            'bottom_1':[0,slice(9,14)],
                            'bottom_2':[1,slice(9,14)],
                            'bottom_3':[2,slice(9,14)],
                            'bottom_4':[3,slice(9,14)],
                            'bottom_5':[4,slice(9,14)],
                            'bottom_6':[5,slice(9,14)],
                            'bottom_7':[6,slice(9,14)],
                            'bottom_8':[7,slice(9,14)],
                            'top_9':[0,slice(14,19)],
                            'top_10':[1,slice(14,19)],
                            'home_runs_0':[2,slice(14,19)],
                            'home_runs_1':[3,slice(14,19)],
                            'away_runs_1':[4,slice(14,19)],
                            'away_runs_0':[5,slice(14,19)],
                            'bottom_10':[6,slice(14,19)],
                            'bottom_9':[7,slice(14,19)],
                            'first_base':[0,19],
                            'second_base':[1,19],
                            'third_base':[2,19],
                            'ball_one':[3,19],
                            'ball_two':[4,19],
                            'ball_three':[5,19],
                            'strike_one':[6,19],
                            'strike_two':[7,19],
                            'outs_one':[[0,2,4,6],20],
                            'outs_two':[[1,3,5,7],20]}

OUTS_INDICES = {1:LED_VALUE_MATRIX_INDICIES['outs_one'],
                2:LED_VALUE_MATRIX_INDICIES['outs_two']}

BALLS_INDICES = {1:LED_VALUE_MATRIX_INDICIES['ball_one'],
                 2:LED_VALUE_MATRIX_INDICIES['ball_two'],
                 3:LED_VALUE_MATRIX_INDICIES['ball_three']}
STRIKES_INDICES ={1:LED_VALUE_MATRIX_INDICIES['strike_one'],
                  2:LED_VALUE_MATRIX_INDICIES['strike_two']}
BASES_LIST = ['first_base','second_base','third_base']
def set_outs(num_outs: int):
    while num_outs!=0:
        gpio_runner.values_matrix[OUTS_INDICES[num_outs]]=True
        num_outs-=1
    return

def clear_outs():
    for x in [1,2]:
        gpio_runner.values_matrix[OUTS_INDICES[x]]=False
    return

def set_balls(num_balls: int):
    gpio_runner.values_matrix[BALLS_INDICES[num_balls]] = True
    return

def clear_balls():
    for index in BALLS_INDICES.values():
        gpio_runner.values_matrix[index] = False
    return

def set_strikes(num_strikes: int):
    gpio_runner.values_matrix[STRIKES_INDICES[num_strikes]] = True
    return

def clear_strikes():
    for index in STRIKES_INDICES.values():
        gpio_runner.values_matrix[index]=False
    return

def set_bases(bases_status: dict):
    for key, val in bases_status.items():
        gpio_runner.values_matrix[LED_VALUE_MATRIX_INDICIES[key]]=val
    return

def clear_bases():
    for base in BASES_LIST:
        gpio_runner.values_matrix[LED_VALUE_MATRIX_INDICIES[base]] = False
    return

def initialize_value_matrix():
    matrix = array([[False]*2]*8)
    for i in range(8):
        matrix[i,:4] = MUX_SET[str(i)]
    matrix [:,0] = LOW
    return matrix

def toggle_mux(row: int, state: bool, all=False):
    if all==False:
        gpio_runner.values_matrix[row,0]

def clear_inning():
    clear_balls()
    clear_bases()
    clear_strikes()
    clear_outs()
    return

def set_inning_score(inning: str, score: int):
    gpio_runner.values_matrix[inning]=BCD_SET[score]


def start():
    runner.start(gpio_flag)


