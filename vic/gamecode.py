import random
import time

#!/usr/bin/python3
#Victors
# Airborne vs Ranger game

class Player():
    def __init__(self, name, types, moves, health, attack):
        self.name = name
        self.health = 100
        self.moves = moves
        self.attack = attack
        self.types = types
        self.wins = 0

    def injury(self, injury, Ranger):
        if (injury > self.health):
            overkill = abs(self.health - injury)
            self.health = 0
            if (overkill > 0):
                print("{0} takes injury from {1}, with {2} overkill!"
                      .format(self.name.capitalize(), Ranger, overkill))
            else:
                print("{0} takes injury from {1}!"
                      .format(self.name.capitalize(), Ranger))
        else:
            self.health -= injury
            print("{0} takes {1} injury from {2}!"
                  .format(self.name.capitalize(), injury, Ranger))

    def Recovery(self, Recovery):
        if (Recovery + self.health > 100):
            self.health = 100
            print("{0} Recovers back full health!"
                  .format(self.name.capitalize()))
        else:
            self.health += Recovery
            print("{0} Recovers for {1}!"
                  .format(self.name.capitalize(), Recovery))


def parse_int(input):
    try:
        int(input)
        return True
    except ValueError:
        return False


def get_selection():
    valid_input = False
    while (valid_input is False):
        print()
        choice = input("Method to Fight: ")
        if (parse_int(method) is True):
            return int(method)
        else:
            print("The input was invalid. Please try again.")


def get_computer_selection(health):
    print("wait")
    time.sleep(1)

    if (health <= 35):
        # Have the computer heal ~50% of its turns when <= 35
       result = random.randint(1, 6)
       if (result % 2 == 0):
            return 3
       else:
           return random.randint(1, 2)
    elif (health == 100):
        return random.randint(1, 2)
    else:
        return random.randint(1, 3)


def each_segment(computer, human):
    game_in_progress = True
    current_player = computer

    while game_in_progress:
        # swap the current player each round
        if (current_player == computer):
            current_player = human
        else:
            current_player = computer

        print()
        print(
            "You have {0} health remaining and the "
            "computer has {1} health remaining."
            .format(human.health, computer.health))
        print()

        if (current_player == human):
            print("Moves:")
            print("1) Dagger - Causes moderate damage.")
            print("2) M4 - high or low damage, "
                  "depending on your luck!")
            move = get_selection()
        else:
            move = get_computer_selection(computer.health)

        if (move == 1):
            damage = random.randrange(18, 25)
            if (current_player == human):
                computer.calculate_damage(damage, human.name.capitalize())
            else:
                human.calculate_damage(damage, computer.name.capitalize())
        elif (move == 2):
            damage = random.randrange(10, 35)
            if (current_player == human):
                computer.calculate_damage(damage, human.name.capitalize())
            else:
                human.calculate_damage(damage, computer.name.capitalize())
        elif (move == 3):
            heal = random.randrange(18, 25)
            current_player.calculate_heal(heal)
        else:
            print ("The input was not valid. Please select a choice again.")

        if (human.health == 0):
            print("Sorry, you lose!")
            computer.wins += 1
            game_in_progress = False

        if (computer.health == 0):
            print("Congratulations, you beat the computer!")
            human.wins += 1
            game_in_progress = False


def start_game():
    print("Airborne Ranger!")

    computer = Player("Computer")

    name = input("Please enter your name: ")
    human = Player(name)

    keep_playing = True

    while (keep_playing is True):
        print("Current Score:")
        print("You - {0}".format(human.wins))
        print("Computer - {0}".format(computer.wins))

        computer.health = 100
        human.health = 100
        play_round(computer, human)
        print()
        response = input("Play another round?(Y/N)")
        if (response.lower() == "n"):
            break

start_game()

