import random

# Comment 0_0
while True:
    y = random.randint(1, 100)
    op = random.randint(1, 100)
    print(f"\nWelcome text!\nYor number is: {y} vs Opponent's: {op}!!!")
    if y > op:
        print("You win!")
    elif y < op:
        print("Opponent wins!")
    else:
        print("Draw!")
    y_n = ''
    while y_n != 'y' and y_n != 'n':
        y_n = input("Wanna reroll? Enter y/n:")
    if y_n == 'n':
        break