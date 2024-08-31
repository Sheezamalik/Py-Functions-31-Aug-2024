def bmi_cal():
    print("Enter the weight in kg?")
    weight = float(input())

    print("Enter the height in meters?")
    height = float(input())

    BMI = weight / (height * height)

    print("The BMI is", BMI)
bmi_cal()