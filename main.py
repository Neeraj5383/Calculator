from calculation import calculator as c


print("//" * 10, "\n")
print("CALCULATOR\n")
print("//" * 10, "\n")


print(f'Select option')
print("1: Addition")
print("2: Subtraction")
print("3: Multiplication")
print("4: Division")
print("5: Floor Division")

def match():
    print(f'Select option')
    print("1: Addition")
    print("2: Subtraction")
    print("3: Multiplication")
    print("4: Division")
    print("5: Floor Division")
    num1  = int(input("Enter 1st number : "))
    num2  = int(input("Enter 2nd number : "))
    oprt = input("Enter Your option : ")

    match oprt:
        case "1" : c.addition(num1, num2)
        case "2" : c.subtraction(num1, num2)
        case "3" : c.multiplication(num1, num2)
        case "4" : c.division(num1, num2)
        case "5" : c.division_floor(num1, num2)
        case  _: print("Wrong Credential!!!!!")

if __name__ == "__main__":
    match()


