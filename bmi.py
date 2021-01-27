import os

print("#### Body Mass Index calculation ####")
weight  = float(input("Type the weight in kg: "))
height  = float(input("Type the height in meters: "))

bmi = weight /height**2

print("The BMI is: ", '{0:.1f}'.format(bmi))  

if bmi < 18.5:
	print("Underweight")
elif bmi < 24.9:
	print("Normal weight")
elif bmi < 29.9:
	print("Overweight")
else:
	print("Obesity")

os.system("pause")