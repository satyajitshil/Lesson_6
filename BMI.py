height = float(input("What is your height: "))
weight = float(input("How heavy are you: "))
BMI = weight / (height / 100) ** 2
print("Your BMI is ", BMI)
if BMI <= 18.4:
    print("You are underweight")
elif BMI <= 24.9:
    print("You are healthy")
elif BMI <= 29.9:
    print("You are heavy")
elif BMI <= 34.9:
    print("You are very heavy")
elif BMI <= 39.9:
    print("You are obese")
else:
    print("You are very obese")