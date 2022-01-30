import random

class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    PURPLE = '\033[95m'
    CYAN = '\033[96m'
    DARKCYAN = '\033[36m'
    BLUE = '\033[94m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    RED = '\033[91m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
    END = '\033[0m'


class Person:
    def __init__(self,hp,mp,atk,df,magic,item):
        self.maxhp = hp
        self.hp = hp
        self.maxmp = mp
        self.mp = mp
        self.atk_low = atk-10
        self.atk_high = atk+10
        self.df = df
        self.magic = magic
        self.item = item
        self.action = ["Attack","Magic","Items"]

    def get_hp(self):
        return self.hp
    def get_MaxHp(self):
        return self.maxhp
    def get_mp(self):
        return self.mp
    def get_maxmp(self):
        return self.maxmp

    def set_hp(self,i):
        self.hp = i
    def set_mp(self,i):
        self.mp = i
    def generate_damage(self):
        return random.randrange(self.atk_low,self.atk_high)

    def generate_spell_damage(self,i):
        mg_low = self.magic[i]["dmg"] - 5
        mg_high = self.magic[i]["dmg"] + 5
        return random.randrange(mg_low,mg_high)

    def take_damage(self,dmg):
        self.hp -= dmg
        if self.hp < 0:
            self.hp = 0

    def reduce_mp(self, cost):
        self.mp -= cost
    def self_heal(self,cure):
        self.hp += cure

    def get_spell_mp_cost(self,i):
        return int(self.magic[i]["cost"])

    def get_spell_name(self, i ):
        return self.magic[i]["name"]

    def get_spell_name(self, i ):
        return self.magic[i]["name"]

    def get_action(self,i):
        return self.action[i]
    def choose_action(self):
        i=1
        print(bcolors.BLUE +bcolors.BOLD + "Actions:" + bcolors.END)
        for item in self.action:
            print(str(i)+" -> "+item)
            i+=1
    def choose_magic(self):
        i = 1
        print(bcolors.BLUE + bcolors.BOLD + "Spells:" + bcolors.END)
        for spell in self.magic:
            print(str(i) + ":" + spell.name + " - (cost: " + str(spell.cost)+ ", type: " + spell.type +" magic)")
            i += 1

    def choose_items(self):
        i = 1
        print(bcolors.BLUE + bcolors.BOLD + "Items:" + bcolors.END)
        for item in self.item:
            print(str(i) + ":" + item.name + " x"+str(item.amount)+" (Type: " + item.type + ", Description: "+ item.description +")")
            i += 1













