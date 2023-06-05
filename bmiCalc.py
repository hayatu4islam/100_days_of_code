height = float(input("Enter your height in m: "))
weight = float(input("Enter your weight in kg: "))
bmi = weight / height ** 2
if bmi < 18.5:
    print("underweight")
elif bmi < 25:
    print("Normal weight")
elif bmi < 30:
    print("overweight")
elif bmi < 35:
    print("Obese")
else:
    print("Clinical obese")