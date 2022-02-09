height = float(input("enter your height in m: "))
weight = float(input("enter your weight in kg: "))

bmi = round(weight/(height*height))

ans = ""

if bmi < 18.5:
    ans = "you are Underwieght."
elif bmi < 25:
    ans = "your wieght is normal."
elif bmi < 30:
    ans = "you are slightly overwieght."
elif bmi < 35:
    ans = "you are obese."
else:
    ans = "you are clinically obese."

print(f"Your BMI is {bmi}, {ans}")