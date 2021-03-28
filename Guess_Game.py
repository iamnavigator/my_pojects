import random

number = random.randint(1, 101)
print(number)

chances = [0]
while True:
    user_input = int(input("Enter number between 1 to 100: \n"))
    if user_input < 1 or user_input > 100:
        print(f"Wrong input {user_input} out of range, please enter number b/w range")
        continue

    if user_input == number:
        print(f"Congratulations, you have guessed correct number {user_input} in {len(chances)} chances")
        break
    chances.append(user_input)
    if chances[-2]:
        if abs(user_input - number) < abs(number - chances[-2]):
            print("Warmer")
        else:
            print("Colder")

    else:
        if abs(user_input - number) <= 10:
            print("Warm")
        else:
            print("Cold")

