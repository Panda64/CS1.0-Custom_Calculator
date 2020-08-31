# Name - Jaylen Schelb
# Program - BMI Calculator 

print("Your Body Mass Index, or BMI, is a measure of your body fat based off of your height and weight. \
A normal BMI is anywhere between 18.5-24.9.")
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
print(f"{feet} feet and {inches} inches!")
