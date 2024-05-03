def calculate(weight, height):
    return weight / ((height/100) ** 2)

def bmi_category(bmi):
    if bmi < 18.5:
        return "Under weight"
    elif 18.5 <= bmi < 24.9:
        return "Normal weight"
    elif 25 <= bmi < 29.9:
        return "Over weight"
    else:
        return "Obese"

def sol_input():
    try:
        weight = float(input("Enter your weight in kg:"))
        height = float(input("Enter your height in cm:"))
        return weight, height
    except ValueError:
        print("Please enter correct number!")
        return sol_input()