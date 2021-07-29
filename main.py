# This wil be attempt at emulating a gambling machine
import random
import time


print(f'You start your Wheel Journey with 1000 Shekels. If the Wheel lands over 50 you double your coin.. lower you lose it')
StartingCoin = 1000
while StartingCoin > 0 :

    Bet = input("Please enter an integeger for your bet\n")
    print(f'You\'ve placed a bet of {Bet} ....')
    UserInput = input("Press any button to spin the wheel...")
    time.sleep(0.5)
    Result = round(random.uniform(0, 100), 2)
    print(f'You\'ve landed on {Result} of the wheel')
    time.sleep(0.5)
    if Result > int(50) :
        print("You have doubled your bet!")
        StartingCoin = StartingCoin + int(Bet) * int(1)*.98
        print("Coin Left:")
        print(StartingCoin)
    else:
        print("You have LOST your bet!")
        StartingCoin = StartingCoin + int(Bet) * int(-1)
        print("Coin Left:")
        print(StartingCoin)

exit("You ran out of shekels")


