import random

# Comment 0_0
y = random.randint(1, 100)
op = random.randint(1, 100)
print(f"Welcome text! Yor number is: {y} vs opponent's {op}!!!")

if y > op:
    print("You win!")
elif y < op:
    print("Opponent wins!")
else:
    print("Draw!")
