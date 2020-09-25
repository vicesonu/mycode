#!/usr/bin/python3

 # Victors
 #  game Airborne vs Ranger game

def showInstructions():
  #print a main menu and the commands
  print('''
AirBorne
========
Commands:
  go [direction]
  get [item]
''')

#create the class

class AirBorne:
    def _init_(self, name,types,moves, EVs, health='================'):
        # save variables as attributes
        self.name = name
        self.types = types
        self.moves = moves
        self.inventory = inventory
        self.health = health
        self.attack= EVs['ATTACK']
        self.defense = EVs['DEFENSE']

    def fight(self, Ranger):
 # Allowing two soldiers fight

 # Printing combat information
    print("------FIGHT------")
    print(f"\n{self.name}")
    print("TYPE/", self.types)
    print("ATTACK/", self.attack)
    print("DEFENSE/",self.defense)
    print("LvL/", 3*(1+np.mean([self.attack,self.defense])))
    print("\nVS")
    print(f"\n{Ranger.name}")
    print("TYPE/", Ranger.types)
    print("ATTACK/", Ranger.attack)
    print("DEFENSE/",Ranger.defense)
    print("LvL/", 3*(1+np.mean([Ranger.attack,Ranger.defense])))

    time.sleep(3)


#Consider diabolical puzzle
Weapons =['Grenade','Gun', 'Knife']
for i,k in enumerate(version):
    if self.types == k:
        if Ranger.types == k:
            String_1_attack = 'Fire'
            String_2_attack = 'Fire'

#Ranger has extra health
while(self.weapon >0) and (Ranger.weapon >0):
    #print the health of each fighter
    print(f"{self.name}\t\tHLTH\t{self.health}")
     print(f"{Ranger.name}\t\tHLTH\t{Ranger.health}\n")

     print(f"Go {self.name}!")
     for i, x in enumerate(self.moves):
         print(f"{1+1}.", x)
         index = int(input('pick a move: '))
         delay_print(f"{self.name} used {move[index-1]}!")
         time.sleep(1)
         delay_print(string_1_attack)

