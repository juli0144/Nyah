# Funktions for Buttons


class Item:
    def __init__(self, name, effect, strength):
        self.name = name
        self.effect = effect
        self.strength = strength
        self.class_name = 'item'

    def use(self, target):
        effectstr = self.effect
        match effectstr:
            case 'heal':
                if target.hp + self.strength > target.max_hp:   # Checks if heals over max health
                    target.hp = target.max_hp
                else:
                    target.hp += self.strength
            case 'regen':
                pass


def item_create_healthpotion():
    return Item('Healthpotion', 'heal', 25)


def item_create_healthpotion_big():
    return Item('Healthpotion', 'heal', 50)


def item_create_regenpotion():
    return Item('Regenerationportion', 'regen', 3)


def create_empty():
    return Item('[empty]', 'none', 0)


class Weapon:
    def __init__(self, name, damage, durability):
        self.name = name
        self.damage = damage
        self.durability = durability
        self.class_name = 'weapon'

    def use(self, monster):
        monster.hp = monster.hp - self.damage


def weapon_create_startsword():
    return Weapon('Stonesword', 8, None)


def weapon_create_dagger():
    return Weapon('Dagger', 15, 6)


class Player:
    def __init__(self, name, description, hp, strength, turns):
        self.name = name
        self.description = description

        self.hp = hp
        self.max_hp = hp
        self.strength = strength
        self.turns = turns

        self.inventory = []
        self.inventory_size = 5
        self.inventory_max = 10
        for i in range(5):
            self.inventory.append(create_empty())

        self.effects = {}

        self.gold = 0
        self.stage = 0

    def item_add(self, item):

        for i in range(self.inventory_size):
            if self.inventory[i].name == '[empty]':
                self.inventory[i] = item
                return

    def get_inventory(self):
        print('\nInventory:')
        for i in range(self.inventory_size):
            print(f"{i+1}. {self.inventory[i].name}")

    def get_effects(self):
        print('\nActive Effects:')
        for k, v in self.effects:
            print(f'{k}: {v}')

    def add_inventory(self, amount):
        pass


def get_char():
    # Creating classes with their stats and bonus items
    fighter = Player('Fighter',
                     'The fighter class is a combat-oriented character\n'
                     ' with high base hp and bonus damage for weapons. He comes \n'
                     'with a start weapon and a big health potion',
                     100, 4, 2)
    fighter.item_add(weapon_create_startsword())
    fighter.item_add(item_create_healthpotion_big())

    assassin = Player('Assassin',
                      'The assassin class is an agile character with lower\n'
                      ' base hp and strenght but he can perform more actions per turn',
                      50, 0, 3)
    assassin.item_add(weapon_create_startsword())
    assassin.item_add(item_create_healthpotion())
    assassin.item_add(weapon_create_dagger())
    # Returning classes in a list
    return [fighter, assassin]
