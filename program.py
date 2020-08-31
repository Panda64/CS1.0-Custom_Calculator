# Name - Jaylen Schelb
# Program - BMI Calculator 

program = True

while program:
    print("Your Body Mass Index, or BMI, is a measure of your body fat based off of your height and weight. \
A normal BMI is anywhere between 18.5-24.9.")

    height = True

    while height:
        print("To start, enter how many feet tall you are. We will get to the inches in a second.")

        def user_feet():
            while True:
                try:
                    return int(input())
                except ValueError:
                    print("You must enter a whole number! Try again.")                       

        feet = user_feet()

        print("Great! Now enter the remaining inches")

        def user_inches():
            while True:
                try:
                    return int(input())
                except ValueError:
                    print("You must enter a whole number! Try again.")

        inches = user_inches()

        print(f"Okay, got it. You are {feet}ft. {inches}in. Is this correct? (y/n)")

        height_restart = True

        while height_restart:
            height_choice = input()

            if height_choice == "y" or height_choice == "Y":
                height = False
                height_restart = False
            elif height_choice == "n" or height_choice == "N":
                height_restart = False
            else:
                print("You must enter either y or n. Try again")

    print("Awesome. Now moving on to weight.")

    weight = True

    while weight:
        print("Enter your weight in lbs.")

        def user_weight():
            while True:
                try:
                    return int(input())
                except ValueError:
                    print("You must enter a whole number. Round if you have to.")
        
        pounds = user_weight()

        print(f"Copy that. You entered {pounds}lbs. Is this correct? (y/n)")

        weight_restart = True

        while weight_restart:
            weight_choice = input()

            if weight_choice == "y" or weight_choice == "Y":
                weight = False
                weight_restart = False
            elif weight_choice == "n" or weight_choice == "N":
                weight_restart = False
            else:
                print("You must enter either y or n. Try again.")

    BMI = float(((pounds)/(((feet * 12) + inches)**2))*(703)) 

    if BMI < 18.5:
        print(f"Your BMI is {round(BMI, 2)}. This is classified as being underweight.")
    elif 18.5 < BMI < 24.9:
        print(f"Your BMI is {round(BMI, 2)}. This is classified as a normal BMI.")
    elif 25 < BMI < 29.9:
        print(f"Your BMI is {round(BMI, 2)}. This is classifed as being overweight.")
    elif BMI >= 30:
        print(f"Your BMI is {round(BMI, 2)}. This is classified as being obese.")

    print("Do you want to run this program again? (y/n)")

    program_restart = True

    while program_restart:
        program_choice = input()

        if program_choice == "y" or program_choice == "Y":
            program_restart = False
        elif program_choice == "n" or program_choice == "N":
            program = False
            program_restart = False
        else:
            print("You must enter either y or n. Try again.")

