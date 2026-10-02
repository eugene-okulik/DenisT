import random

salary = int(input("Enter your salary amount: "))
bonus = random.choice([True, False])

if bonus == True:
    print(f"{salary}, {bonus} - '${salary + random.randint(1, 100000)}'")
else:
    print(f"{salary}, {bonus} - '${salary}'")
