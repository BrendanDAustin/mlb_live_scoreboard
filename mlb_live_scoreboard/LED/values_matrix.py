from threading import Lock
from numpy import array
class Matrix():
    """matrix with update methods and lock objects"""
    def __init__(self):
        self.BCD_SET = {-1:(False,False,False,False,False),
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
        self.MUX_SET = {'OFF':(False,False,False,False),
                    '0':(True,False,False,False),
                    '1':(True,False,False,True),
                    '2':(True,False,True,False),
                    '3':(True,False,True,True),
                    '4':(True,True,False,False),
                    '5':(True,True,False,True),
                    '6':(True,True,True,False),
                    '7':(True,True,True,True)}
        self.BASES_BALLS_STRIKES_SET = {'FIRST_BASE':False,
                                    'SECOND_BASE':False,
                                    'THIRD_BASE':False,
                                    'BALL_ONE':False,
                                    'BALL_TWO':False,
                                    'BALL_THREE':False,
                                    'STRIKE_ONE':False,
                                    'STRIKE_TWO':False}
        self.LED_VALUE_MATRIX_INDICES = {'top_1':(0,slice(4,9)),
                                'top_2':(1,slice(4,9)),
                                'top_3':(2,slice(4,9)),
                                'top_4':(3,slice(4,9)),
                                'top_5':(4,slice(4,9)),
                                'top_6':(5,slice(4,9)),
                                'top_7':(6,slice(4,9)),
                                'top_8':(7,slice(4,9)),
                                'bottom_1':(0,slice(9,14)),
                                'bottom_2':(1,slice(9,14)),
                                'bottom_3':(2,slice(9,14)),
                                'bottom_4':(3,slice(9,14)),
                                'bottom_5':(4,slice(9,14)),
                                'bottom_6':(5,slice(9,14)),
                                'bottom_7':(6,slice(9,14)),
                                'bottom_8':(7,slice(9,14)),
                                'top_9':(0,slice(14,19)),
                                'top_10':(1,slice(14,19)),
                                'home_runs_0':(2,slice(14,19)),
                                'home_runs_1':(3,slice(14,19)),
                                'away_runs_1':(4,slice(14,19)),
                                'away_runs_0':(5,slice(14,19)),
                                'bottom_10':(6,slice(14,19)),
                                'bottom_9':(7,slice(14,19)),
                                'first_base':(0,19),
                                'second_base':(1,19),
                                'third_base':(2,19),
                                'ball_one':(3,19),
                                'ball_two':(4,19),
                                'ball_three':(5,19),
                                'strike_one':(6,19),
                                'strike_two':(7,19),
                                'outs_one':((0,2,4,6),20),
                                'outs_two':((1,3,5,7),20)}
        self.OUTS_INDICES = {1:self.LED_VALUE_MATRIX_INDICES['outs_one'],
                        2:self.LED_VALUE_MATRIX_INDICES['outs_two']}

        self.BALLS_INDICES = {1:self.LED_VALUE_MATRIX_INDICES['ball_one'],
                         2:self.LED_VALUE_MATRIX_INDICES['ball_two'],
                         3:self.LED_VALUE_MATRIX_INDICES['ball_three']}
        self.STRIKES_INDICES ={1:self.LED_VALUE_MATRIX_INDICES['strike_one'],
                          2:self.LED_VALUE_MATRIX_INDICES['strike_two']}
        self.BASES_LIST = ['first_base','second_base','third_base']
        self.lock = Lock()
        self.values = self.initialize_value_matrix()
        
    def set_outs(self,num_outs: int):
        self.lock.acquire()
        while num_outs!=0:
            self.values[self.OUTS_INDICES[num_outs]]=True
            num_outs-=1
        self.lock.release()
        return

    def clear_outs(self):
        self.lock.acquire()
        for x in [1,2]:
            self.values[self.OUTS_INDICES[x]]=False
        self.lock.release()
        return

    def set_balls(self,num_balls: int):
        self.lock.acquire()
        self.values[self.BALLS_INDICES[num_balls]] = True
        self.lock.release()
        return

    def clear_balls(self):
        self.lock.acquire()
        for index in self.BALLS_INDICES.values():
            self.values[index] = False
        self.lock.release()
        return

    def set_strikes(self,num_strikes: int):
        self.lock.acquire()
        self.values[self.STRIKES_INDICES[num_strikes]] = True
        self.lock.release()
        return

    def clear_strikes(self):
        self.lock.acquire()
        for index in self.STRIKES_INDICES.values():
            self.values[index]=False
        self.lock.release()
        return

    def set_bases(self,bases_status: dict):
        self.lock.acquire()
        for key, val in bases_status.items():
            self.values[self.LED_VALUE_MATRIX_INDICES[key]]=val
        self.lock.release()
        return

    def clear_bases(self):
        self.lock.acquire()
        for base in self.BASES_LIST:
            self.values[self.LED_VALUE_MATRIX_INDICES[base]] = False
        self.lock.release()
        return

    def initialize_value_matrix(self):
        self.lock.acquire()
        matrix = array([[False]*21]*8)
        for i in range(8):
            matrix[i,:4] = self.MUX_SET[str(i)]
        matrix [:,0] = False
        self.lock.release()
        return matrix

    def toggle_mux(row: int, state: bool, all=False):
        self.lock.acquire()
        if all==False:
            self.values[row,0]
        self.lock.release()
        return

    def clear_inning(self):
        self.clear_balls()
        self.clear_bases()
        self.clear_strikes()
        self.clear_outs()
        return

    def set_inning_score(self,inning: str, score: int):
        self.lock.acquire()
        self.values[self.LED_VALUE_MATRIX_INDICES[inning]]=self.BCD_SET[score]
        self.lock.release()
        return

    def all_off(self):
        self.lock.acquire()
        self.values = array([[False]*21]*8)
        self.lock.release()
        return




