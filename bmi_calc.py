def BMI(height, weight):
    bmi = weight/(height**2)
    return bmi


height = 1.50
weight = 62

bmi = BMI(height, weight)
print("The BMI is", format(bmi), "so ", end='')

if (bmi < 18.5):
    print("underweight")

elif (bmi >= 18.5 and bmi < 24.9):
    print("Healthy")

elif (bmi >= 24.9 and bmi < 30):
    print("overweight")

elif (bmi >= 30):
    print("Suffering from Obesity")
