from calculation import Calculator

print("//" * 10, "\n")
print("CALCULATOR\n")
print("//" * 10, "\n")


def run_calculator():
    calc = Calculator()

    print("Select option")
    print("1: Addition")
    print("2: Subtraction")
    print("3: Multiplication")
    print("4: Division")
    print("5: Floor Division")

    num1 = int(input("Enter 1st number : "))
    num2 = int(input("Enter 2nd number : "))
    oprt = input("Enter your option : ")

    match oprt:
        case "1":
            print(calc.addition(num1, num2))
        case "2":
            print(calc.subtraction(num1, num2))
        case "3":
            print(calc.multiplication(num1, num2))
        case "4":
            print(calc.division(num1, num2))
        case "5":
            print(calc.division_floor(num1, num2))
        case _:
            print("Wrong option!!!!!")


if __name__ == "__main__":
    run_calculator()