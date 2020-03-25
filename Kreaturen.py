class Kreaturenfriedlich:
    """mögliche Kreaturen"""
    moeglicherloot = [Fleischgroß, Fleischklein]


class Player:
    hp = 30
    Inventory = []



class dreifueßigesReh:
    hp = 10
    def AusgabeReh(self):
        print("Du stehst vor einem dreibeinigen Reh. Diese Kreatur ist nicht gut zu Fuß und leicht zu erledigen.")

instanz = dreifueßigesReh() 
instanz.AusgabeReh 


Iventory = []
def aufheben:
    Inventory.append()



if __name__ == "__main__":
    Player = input("Gib deiner Figur einen Namen.\n")
    print("Großartig. Dein Name ist " + Player + ".")
    commands = "w für vorwärts\n a für links\n s für rückwärts\n d für rechts\n Leertaste für springen\n c für klettern (von climb)\n v für kämpfen (von: verdammt, jetzt muss ich kämpfen)\n i für aufheben (von: interessant! Das hebe ich auf.)"
    hilfebenoetigt = input("Hello. Type help to see the commands available.\n")
    if hilfebenoetigt == "help":
        print(commands)
    else:
        print("Alright then. Have a nice adventure.")