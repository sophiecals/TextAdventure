import random

class Item:
    def __init__(self, weight, worth):
        self.weight = weight
        self.worth = worth

class Potion(Item):
    def __init__(self, weight, worth):
        Item.__init__(self, weight, worth)

class HealthPotion(Potion): #Potion erbt von Item und HealthPotion erbt von potion und damit auch automatisch von Item
    def __init__(self, weight, worth, regenerated_health):
        Potion.__init__(self, weight, worth)
        self.regenerated_health = regenerated_health

class Character:
    def __init__(self, hp, ad, name):
        self.hp = hp
        self.ad = ad
        self.name = name
        #self.armor = armor

    def get_hit(self, ad):
        self.hp = self.hp - ad #/self.armor
        if self.hp <= 0:
            self.die()

    def is_dead(self):
        return self.hp <= 0

    def die(self):
        print(self.name + " died")

class Goblin(Character):
    def __init__(self):
        Character.__init__(self, 100, 10, "Goblin")

class Ork(Character):
    def __init__(self):
        Character.__init__(self, 300, 30, "Ork")

class Player(Character):
    def __init_(self, name, hp, ad):
        Character.__init__(self, hp, ad, name)
        self.max_hp = hp

    def die(self):
        exit("Wasted.")

    def rest(self):
        self.hp = self.max_hp

class Field:
    def __init__(self, enemies):
        self.enemies = enemies
        self. loot = []

    def print_state(self):
        print("You look around and see ")
        for i in self.enemies:
            print(i.name)

    @staticmethod
    def gen_random(self):
        rand = random.randint(0,2)
        if rand == 0:
            return Field([])
        if rand == 1:
            return Field([Ork()])
        if rand == 2:
            return Field([Goblin(), Ork()])


       

class Map:
    def __init__(self, width, height):
        self.state = [] 
        self.x = 0
        self.y = 0
        for i in range(width):
            fields = [] #Liste aus Feldern
            for j in range(height):
                fields.append(Field.gen_random(self))  #neues zufälliges Feld
            self.state.append(fields) #packt neue Felder in self.state -> kreiert neue Liste usw.

    def print_state(self):
        self.state[self.x][self.y].print_state() #Methode, die Zustand von aktuellem Feld ausgibt (was gibt's gerade auf dem Feld, auf dem ich bin)
    
    def get_enemies(self):
        return self.state[self.x][self.y].enemies

    def forward(self):
        if self.x == len(self.state) - 1:
            print("You see huge mountains, but you don´t have a horse from Skyrim so you can´t pass them.")
        else:
            self.x = self.x + 1 
    
    def backwards(self):
        if self.x == 0:
            print("You see cliffs but the other side is too far away to jump safely.")
        else:
            self.x = self.x - 1 
    
    def right(self):
        if self.y == len(self.state[self.x]) - 1:
            print("You see huge mountains, but you don´t have a horse from Skyrim so you can´t pass them.")
        else:
            self.y = self.y + 1 
    
    def left(self):
        if self.x == 0:
            print("You see cliffs but the other side is too far away to jump safely.")
        else:
            self.y = self.y - 1 

def forward(p, m):
    m.forward

def right(p, m):
    m.right

def left(p, m):
    m.left

def backwards(p, m):
    m.backwards
    

def quit_game(p, m):
    print("You commit suicide and leave this world.")
    exit(0)

def print_help(p, m):
    print(Commands.keys())

def pickup(p, m):
    pass

def fight(p, m):
    enemies = m.get_enemies()
    while len(enemies) > 0: #solange es Gegner gibt
        enemies[0].get_hit(p.ad) #Der erste Gegner wird mit so viel Attac Damage geschlagen, wie der Spieler zur Verfügung hat
        if enemies[0].is_dead():
            enemies.remove(enemies[0]) #wenn der erste gegener tot ist, entferne ihn aus Liste der Gegner
        for i in enemies:
            if i.is_alive():
                p.get_hit(enemies[i].ad) #Spieler bekommt von jedem Gegener einen Schlag ab
        print("You are wounded and have " + str(p.hp) + "hp left.")

def rest(p, m):
    p.rest()

Commands = {
    "help": print_help,
    "quit": quit_game,
    "pickup": pickup,
    "forward": forward,
    "right": right,
    "left": left,
    "backwards": backwards,
    "fight": fight,
    #"save": save,
    #"load": load,
    "rest": rest,
    #"run": run_away
}


if __name__ == "__main__":
    name = input("Enter a name for your character.\n")
    p = Player(name, 1000, 100)
    map = Map(5,5)
    print("type help to list the commands available)\n")
    while True:
        command = input(">").lower().split(" ") #Der Input wird am Leerzeichen getrennt, heißt, wenn ein Satz eingegeben wird,kommen die einzelnen Wörter als Arrays einer Liste zurück. 
        if command[0] in Commands: #wenn der erste eingegebene command im dicct Commands enthalten ist, führe ihn aus
            Commands[command[0]](p, map)
        else:
            print("You run around in circles and don´t know what to do.")
    map.print_state