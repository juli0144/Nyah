import random
import time

# def timer():
#    count = 0
#    while True:
#        time.sleep(1)
#        count += 1


class Player:
    def __init__(self, hp, dodge, gold):
        self.hp = hp
        self.dodge = dodge
        self.gold = gold


class Monster:
    def __init__(self, name, hp, damage, crit_chance, attacks, reward):
        self.name = name
        self.hp = hp
        self.damage = damage
        self.crit_chance = crit_chance
        self.attacks = attacks
        self.reward = reward


class Weapon:
    def __init__(self, name,  durability, damage, crit_chance, attacks):
        self.name = name
        self.durability = durability
        self.damage = damage
        self.crit_chance = crit_chance
        self.attacks = attacks


class Melee(Weapon):

    dodgechance = 0

    def __init__(self, name, durability, damage, crit_chance, attacks):

        super().__init__(name, durability, damage, crit_chance, attacks)

    def __str__(self):
        return self.name

    def attack(self):
        pass


class Range(Weapon):

    def __init__(self, name, durability, damage, crit_chance, attacks, dodgechance):

        super().__init__(name, durability, damage, crit_chance, attacks)
        self.dodgechance = dodgechance

    def __str__(self):
        return self.name


def weaponstats(x):
    print(str(x.name) + ": Durability:" + str(x.durability) + "  Damage:" + str(x.damage) + "  Crit Chance:" + str(
        x.crit_chance) + "  Turnes:" + str(x.attacks) + "  Dodgechance:" + str(x.dodgechance))


def start_weapon():
    startweapon_list = ["Bow (a) -- ", "Axe (b) -- ", "Dagger (c) -- "]
    sw_1 = Range("Bow", 10, 10, 40, 2, 30)
    sw_2 = Melee("Axe", 25, 15, 25, 1)
    sw_3 = Melee("Dagger", 15, 10, 66, 2)
    x = Melee("None", 0, 0, 0, 0)
    startweapon = "0"
    while startweapon == "0":
        print("Choose your starter weapon: ")
        for i in startweapon_list:
            print(i, end="")
        weap_sel = input("").lower()
        if weap_sel == "a":
            x = sw_1
            weaponstats(x)
        elif weap_sel == "b":
            x = sw_2
            weaponstats(x)
        elif weap_sel == "c":
            x = sw_3
            weaponstats(x)
        if input("Continue? Y/N").upper() == "Y":
            startweapon = x
    player.dodge = startweapon.dodgechance
    return startweapon
    # Weapon(name, durability, damage, crit_chance, attacks, dodgechance)


def menu(player, monster, weapon):
    print("------------------------------")
    print("Player:", end="      ")
    print("Monster:")
    print("HP: "+str(player.hp), end="       ")
    print("HP: "+str(monster.hp))
    print("Dodge: "+str(player.dodge), end="     ")
    print("Durability: " +str(weapon.durability))


def restart(death):
    if death == 0:
        print("You died.")
        if input("New game? Y/N").upper() == "Y":
            pass
        else:
            return None
    if death == 1:
        print("The monster is dead!!")
        print("You gained "+str(monster_main.reward)+" Gold!")
        player.gold =+ monster_main.reward


def newmonster():
    return Monster("Goblin", 50, 10, 0, 1, 5)


def round_start(weapon, monster):
    for i in range(weapon.attacks): #Repeating for each attack
        inp = " "
        while inp not in "ad": #Choosing action
            print("Your turn. "+str(i+1)+" from "+str(weapon.attacks))
            inp = input("Attack[A] or dodge 20 up[D]? ").lower()
            print("------------------------------")
            if inp == "a": #Attack calculation
                dmg = attack(weapon, monster)
                print("You did "+str(dmg)+" Damage.")
                print("The Monster has "+str(monster.hp)+"HP left.")
                print("Youre "+str(weapon)+" has "+str(weapon.durability)+" durability left.")
                break
            elif inp == "d": #Dodge up
                player.dodge = player.dodge + 20
                print("Dodge up to "+str(player.dodge))
                break


def m_attack_ini(monsterdmg, hp, weapon):
    r = random.randint(1, 100)
    if player.dodge < r:
        hp = hp - monsterdmg.damage
        print("The monster hit for "+str(monsterdmg.damage)+" Damage!")
    else:
        print("You dodged the enemys attack")
    player.dodge = weapon.dodgechance
    time.sleep(1)
    return hp


def weaponselect():
    inp = ""
    while inp not in "ABC":
        for i in weaponlist:
            continue


def attack(weapon, monster):
    r = random.randint(1, 100)
    weapon.durability = weapon.durability - 1
    if r < weapon.crit_chance:
        dmg = weapon.damage * 2
        monster.hp = monster.hp - dmg
        print("Crit Hit!!!")
    else:
        dmg = weapon.damage
        monster.hp = monster.hp - dmg
        print("Hit!")
    return dmg


def run():
    con = True
    while con: #Initialize start
        player = Player(100, 30, 20)
        monster_main = newmonster()
#        weaponlist = [] #unused, later inventory system?
        weapon_1 = start_weapon() #Initializes start weapon
#        weaponlist.append(weapon_1)
        while player.hp > 0: #Gameloop rn
            # weaponselect() #weapon select for the inventory system?
            menu(player, monster_main, weapon_1)
            round_start(weapon_1, monster_main)
            player.hp = m_attack_ini(monster_main, player.hp, weapon_1)
            if player.hp < 1: #Check if player is dead
                con = restart(0)
            if monster_main.hp < 1: #Check if monster is dead
                restart(1)
                monster_main = newmonster()


# Monster(name, hp, damage, crit_chance, attacks, dodge)
# Weapon (name,  durability, damage, crit_chance, attacks):
player = Player(100, 30, 20)
monster_main = Monster("Goblin", 50, 10, 0, 1, 5)
weapon_1 = Weapon("Empty", 0, 0, 0, 0)
weaponlist = []

if __name__ == "__main__" :
    run()

