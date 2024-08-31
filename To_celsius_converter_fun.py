def to_cel_con():
    print("Enter the tempertture in Fahrenheit?")
    temp_f = float(input())

    celsius = (temp_f - 32) * 5/9

    print("The",temp_f, "Fahrenheit is", celsius, "Celsius.")
to_cel_con()