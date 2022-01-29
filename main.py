from Classes.game import Person , bcolors
from Classes.magic import Spells

#creating Black Magic:
fire = Spells("Fire", 9, 80 ,"black")
thunder = Spells("Thunder", 11, 89 ,"black")
blizzard = Spells("Blizzard", 8, 77 ,"black")
meteor = Spells("Meteor", 14, 120 ,"black")
quake = Spells("Quake", 12, 109 ,"black")
#creating White Magic:
cure = Spells("Cure", 8 , 100, "white")
cure_Double = Spells("Curai", 13 , 150, "white")

#initiolize player:
player = Person(460,65,60,34,[fire, thunder,blizzard, meteor,quake,cure,cure_Double])
enemy = Person(800,30,32,25,[])

running = True


print(bcolors.FAIL + bcolors.BOLD + "The Enemy Attacks!" +bcolors.ENDC)

while running:
    print("========================================")
    player.choose_action()
    choice = input("Choose youe action!\n")
    if choice == 1 or choice == 0:
        print("You Chose " + player.get_action(int(choice) - 1))
    index = int(choice) -1
    if index == 0:
        dmg = player.generate_damage()
        enemy.take_damage(dmg)
        print("You attacked for " + str(dmg) + " damage points! ")
    elif index == 1:
        player.choose_magic()
        choice = int(input("Choose youe action!")) -1
        # spell = str(player.get_spell_name(choice))
        spell = str(player.magic[choice].name)
        print("You use " +bcolors.PURPLE + spell + " Spell!" + bcolors.ENDC)

        # cost = player.get_spell_mp_cost(choice)
        # dmg = player.generate_spell_damage(choice)
        cost = player.magic[choice].cost
        dmg = player.magic[choice].generate_dmg()

        if player.get_mp() < cost:
            print(bcolors.FAIL + "\nNot Enough MP!\n"+bcolors.ENDC)
            continue
        else:
            player.reduce_mp(cost)
            enemy.take_damage(dmg)
            print("You spell caused " + str(dmg) + " damage points! ")
    else:
        print(bcolors.FAIL + "Wrong Action Key!" + bcolors.ENDC)

    enemy_choice = 1
    enemy_dmg = enemy.generate_damage()
    player.take_damage(enemy_dmg)
    print("The Enemy attacked for " + str(enemy_dmg) + " damage points!")

    print("__________________________")
    print("Player HP: " + bcolors.CYAN + str(player.get_hp())+"/"+ str(player.get_MaxHp()) + bcolors.ENDC + ", MP: "
                                                        + bcolors.CYAN + str(player.get_mp())+"/"+str(player.get_maxmp())+ bcolors.ENDC)
    print("Enemy HP: " + bcolors.FAIL + str(enemy.get_hp()) + "/" + str(enemy.get_MaxHp()) +bcolors.ENDC)
    print("__________________________")

    if enemy.get_hp() ==  0:
        print(bcolors.GREEN + "Enemy is down, You Win!" + bcolors.ENDC)
        running = False
    elif player.get_hp() == 0:
        print(bcolors.FAIL + "no HP left ... You lose!" + bcolors.ENDC)
        running = False
    # running = False

