import random

dice_set = [4,6,8,10,12,20]
running = True

def dice_roller(count,size):
    print('\nYour dice rolls are...')
    if size == 4:
        for num in range(count):
            print(random.randint(1,4),end=' ')
    elif size == 6:
        for num in range(count):
            print(random.randint(1,6))
    elif size == 8:
        for num in range(count):
            print(random.randint(1,8))
    elif size == 10:
        for num in range(count):
            print(random.randint(1,10))
    elif size == 12:
        for num in range(count):
            print(random.randint(1,12))
    elif size == 20:
        for num in range(count):
            print(random.randint(1,20))
    print('\n')


print("Welcome to the SPD Dice Roller!")
while running == True:
    print('Which size dice do you want to roll?')
    size = int(input("Choose between '4','6','8','10','12','20'. Or, type '0' to end:  "))
    if size in dice_set:
        count = int(input("How many dice do you want to roll? "))
        dice_roller(count,size)
    elif size == 0:
        running = False
        print("Thank you!")
        break
    else:
        print("\nSorry, that's an invalid choice. Please try again.\n")
