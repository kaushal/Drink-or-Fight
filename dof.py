from random import randint


def drinkOrFight():
    randomNumber = randint(0, 2)
    if randomNumber == 0 or randomNumber == 1:
        print "drink"
        drinkOrFight()
    else:
        print "fight"

drinkOrFight()
