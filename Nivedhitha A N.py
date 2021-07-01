
height = float(input()) #in meter
# NivedhithaAN-01-bmi
weight = float(input()) # in kilogram
bmi = weight/(height**2)
print(round(bmi))
if (bmi<18.5):
    print("Underweight")
elif (bmi>18.5 and bmi<25):
    print("Normal weight")
elif (bmi>30 and bmi<35):
    print("Obese")
elif (bmi>35):
    print("Clinically obese")

