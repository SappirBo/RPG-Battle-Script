from Classes.game import Person , bcolors

magic = [{"name": "Fire","cost": 9, "dmg": 60 },
         {"name": "Thunder","cost": 11, "dmg": 65 },
         {"name": "Water","cost": 5, "dmg": 45 }]
player = Person(460,65,60,34,magic)
enemy = Person(1200,30,32,25,magic)

running = True


print(bcolors.FAIL + bcolors.BOLD + "The Enemy Attacks!" +bcolors.ENDC)

while running:
    print("====================")
    player.choose_action()
    choice = input("Choose youe action!")
    print("You Chose " + player.get_action(int(choice) -1))
    index = int(choice) -1
    if index == 0:
        dmg = player.generate_damage()
        enemy.take_damage(dmg)
        print("You attacked for " + str(dmg) + " damage points! Enemy HP is " + str(enemy.get_hp()))

    # running = False




