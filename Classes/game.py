import random

class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'


class Person:
    def __init__(self,hp,mp,atk,df,magic):
        self.makhp = hp
        self.hp = hp
        self.makmp = mp
        self.mp = mp
        self.atk_low = atk-10
        self.atk_high = atk+10
        self.df = df
        self.magic = magic
        self.action = ["attack","magic"]

    def generate_damage(self):
        return random.randrange(self.atk_low,self.atk_high)
    

