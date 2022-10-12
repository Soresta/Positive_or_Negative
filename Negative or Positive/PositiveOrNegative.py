# Positive or Negative:
# Program to show whether an entered number is positive or negative.
# Girilen bir sayının pozitif mi yoksa negatif mi olduğunu gösteren program.

while True:
    while True:
        try:
            number = int(input("Enter a number: "))
            break
        except ValueError:
            print("Please do not use characters. Enter an integer!")
    if number == 0:
        print("Your number is equal to 0!")

    elif number > 0:
        print("Your number is a Positive integer!")

    else:
        print("Your number is a Negative integer!")
