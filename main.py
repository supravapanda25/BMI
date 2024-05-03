from bmi_lib import calculate, bmi_category, sol_input
def final():
    print("WELCOME!")

    weight, height = sol_input()
    bmi = calculate(weight,height)
    category = bmi_category(bmi)

    print("\nBMI Result:")
    print(f"BMI:{bmi:.2f}")
    print(f"CATEGORY:{category}")

if __name__ == "__main__":
    final()