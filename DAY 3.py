print("Welcome to the rollercoaster!")
height = int(input("What is your height in cm?\n"))
if height >= 120:
    print("You can ride the rollercoaster!")
else:
    print("Sorry, you are too short to ride a rollercoaster!")
#Modulo Operation
number = int(input("Which number do you want to check?\n"))
if number % 2 ==0:
    print("This is an even number.")
else:
    print("This is an odd number")
#If and elif statement
print("Welcome to the rollercoaster!")
height = int(input("What is your height in cm?\n"))
if height >= 120:
    print("You can ride the rollercoaster!")
age = int(input("What is your age?"))
if age < 12:
    print("please pay $10")
elif age <=18:
    print("Please pay $17.")
else:
    print("Please pay $50")

#BMI 2.0
bmi = 22
if bmi < 18.5:
    print(f"Your BMI is {bmi},you are underweight")
elif bmi<25:
    print(f"Your BMI is {bmi}, you have a normal weight.")
elif bmi < 30:
    print(f"Your BMI is {bmi}, you are overweight.")
elif bmi < 35:
    print(f"Your BMI is {bmi}, you are obese.")
else:
    print(f"Your BMI is {bmi}, you are clinically Obese.")

#Leap Year
year = int(input("Which year do you want to check?"))
if year % 4 ==0:
    if year % 100 ==0:
        if year % 400 ==0:
            print("Leap Year")
        else:
            print("Not a leap year.")
    else:
        print("Leap year")
else:
    print("Not a leap year.")


