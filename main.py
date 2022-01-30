from Classes.game import Person , bcolors
from Classes.magic import Spells
from Classes.inventory import Item
import os

def clearConsole():
    command = 'clear'
    if os.name in ('nt', 'dos'):  # If Machine is running on Windows, use cls
        command = 'cls'
    os.system(command)

print("\n\n")
# print("NAME            HP                           MP              ")
# print("                ____________________         ____________________       ")
# print(bcolors.BOLD+"Player: 460/460|"+bcolors.GREEN+"███████████████     "+bcolors.ENDC
#       +bcolors.BOLD+"| 65/65 |"+bcolors.BLUE+"███████████████████ "+bcolors.ENDC+bcolors.BOLD+"|"+bcolors.ENDC)
# print("\n\n")

#creating Black Magic:
fire = Spells("Fire", 9, 80 ,"black")
thunder = Spells("Thunder", 11, 89 ,"black")
blizzard = Spells("Blizzard", 8, 77 ,"black")
meteor = Spells("Meteor", 14, 120 ,"black")
quake = Spells("Quake", 12, 109 ,"black")
#creating White Magic:
cure = Spells("Cure", 8 , 100, "white")
cure_Double = Spells("Curai", 13 , 150, "white")

#creating some items:
potion = Item("Potion","potion","Heals 50 HP.",50)
hi_potion = Item("Hi-Potion","potion","Heals 150 HP.",150)
super_potion = Item("SuperPotion","potion","Heals 350 HP.",350)
elixer = Item("Elixer","elixer","Fully restore the player HP/MP to max.", 800)
mega_elixer = Item("MegaElixer","elixer","Fully restore the player HP and MP to max.", 1200)
toxicPotion = Item("Toxic Potion", "attack", "Deals 500  HP of the enemy.", 500)


player_spells = [fire, thunder,blizzard, meteor,quake,cure,cure_Double]
player_items =[potion,hi_potion,super_potion,elixer,mega_elixer,toxicPotion]
hi_potion.set_amount(3)
super_potion.set_amount(2)
elixer.set_amount(2)
mega_elixer.set_amount(1)
for item in player_items:
    if item.amount == 0:
        item.start_amount()


# initiolize player:
player1 = Person("Robin  ",250,65,60,34,player_spells,player_items)
player2 = Person("Batman ",250,350,60,34,player_spells,player_items)
player3 = Person("Batgirl",1200,32,60,34,player_spells,player_items)
players =[player1,player2,player3]

# initiolize enemys:
enemy1 = Person("Lex   ",2900,200,32,25,[],[])
enemy2 = Person("Joker ",8000,200,32,25,[],[])
enemy3 = Person("harly ",1700,200,32,25,[],[])
enemys = [enemy1,enemy2,enemy3]


running = True


print(bcolors.FAIL + bcolors.BOLD + "The Enemy Attacks!" +bcolors.ENDC)

while running:
    clearConsole()
    print("========================================")
    print("\n\n")
    print("________________________________________")
    for enemy in enemys:
        enemy.get_enemy_stats()
    for player in players:
        player.get_stats()
    print("\n")
    for player in players:
        player.choose_action()
        choice = input(bcolors.PURPLE + player.name+bcolors.ENDC+" Choose your action!\n")
        select = player.choose_enemy(enemys)
        enemy = enemys[select]

        index = int(choice) - 1
        if index == 0:
            dmg = player.generate_damage()
            enemy.take_damage(dmg)
            print("You attacked"+ enemy.name +" for " + str(dmg) + " damage points! ")
        elif index == 1:
            player.choose_magic()
            choice = int(input("Choose your Magic!")) - 1
            spell = player.magic[choice]
            print("You use " + bcolors.PURPLE + str(spell.name) + " Spell on "+ enemy.name +"!" + bcolors.ENDC)
            cost = player.magic[choice].cost
            magic_impact = player.magic[choice].generate_dmg()
            if player.get_mp() < cost:
                print(bcolors.FAIL + "\nNot Enough MP!\n" + bcolors.ENDC)
                continue
            else:
                if spell.type == "white":
                    player.reduce_mp(cost)
                    player.self_heal(magic_impact)
                    print("You Got " + str(magic_impact) + " HP points!")
                else:
                    player.reduce_mp(cost)
                    enemy.take_damage(magic_impact)
                    print("You spell caused " + str(magic_impact) + " HP's! ")
        elif index == 2:
            player.choose_items()
            choice = int(input("Choose your Item!")) - 1
            item = player.item[choice]
            print("You use " + bcolors.PURPLE + str(item.name) + "!" + bcolors.ENDC)
            item_impact = player.item[choice].prop
            if item.type == "Potion":
                player.self_heal(item_impact)
                print(
                    bcolors.GREEN + "\nYou used " + item.name + ", you got " + str(item.prop) + " HP\n" + bcolors.ENDC)
                item.reduce_amount_by_one()
            elif item.type == "elixer":
                player.set_hp(player.maxhp)
                player.set_mp(player.maxmp)
                print(bcolors.GREEN + "\\nYou used " + item.name + ",HP/MP Fully Restored!\n" + bcolors.ENDC)
                item.reduce_amount_by_one()
            elif item.type == "attack":
                enemy.take_damage(item_impact)
                print(bcolors.DARKCYAN + "\nYou used " + item.name + ", "+ enemy.name +" had " + str(
                    item.prop) + " HP lost!\n" + bcolors.ENDC)
                item.reduce_amount_by_one()
    else:
        print(bcolors.FAIL + "Wrong Action Key!" + bcolors.ENDC)

    enemy_choice = 1
    enemy_dmg = enemy.generate_damage()
    player.take_damage(enemy_dmg)
    print("The Enemy attacked for " + str(enemy_dmg) + " damage points!")

    print("__________________________")
    # print("Player HP: " + bcolors.CYAN + str(player.get_hp())+"/"+ str(player.get_MaxHp()) + bcolors.ENDC + ", MP: "
    #                                                     + bcolors.CYAN + str(player.get_mp())+"/"+str(player.get_maxmp())+ bcolors.ENDC)
    # print("Enemy HP: " + bcolors.FAIL + str(enemy.get_hp()) + "/" + str(enemy.get_MaxHp()) +bcolors.ENDC)
    # print("__________________________")

    if enemy.get_hp() ==  0:
        print(bcolors.GREEN + enemy.name +" is down!" + bcolors.ENDC)
        enemys.remove(enemy)
    elif player.get_hp() == 0:
        print(bcolors.FAIL +player.name +".. no HP left ... You lose!" + bcolors.ENDC)
        players.remove(player)

    if enemys.__len__() == 0:
        print(bcolors.GREEN +"All the enemys are down, You Win!" + bcolors.ENDC)
        running = False
    if players.__len__() == 0:
        print(bcolors.BOLD+bcolors.FAIL+"All Players HP is 0! Game Over!"+bcolors.ENDC)
        running = False