
'''
create a calculator for multiply input.
user can enter two more input for their calculation
'''

print("//" * 10, "\n")
print("CALCULATOR\n")
print("//" * 10, "\n")


def run_calculator():
  

    # it store number add and subtract so on...
    x = 0


    # y is for number you calculate
    y = 0
    while True:
        num1 = int(input("Enter Number : "))
        
        oprt = input("Enter Opterator : ")
        y += 1
        match oprt:
            case "+":
                x = num1 + x
                print(x)
            case "-":
                x = num1 - x
                print(x)
            case "*":
                x = num1 * x
                print(x)
            case "/":
                x = num1 / x
                print(x)
            case "//":
                x = num1 // x
                print(x)   

            case "=":
                print(f"Here's total calculation : {x}")
                print(f'total number your enter {y}')
                break
            case _:
                y -= 1
                print(f'Wrong credential!!!!!!')
    
if __name__ == "__main__":
    run_calculator()