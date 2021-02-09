logo = """
 _____________________
|  _________________  |
| | Pythonista   0. | |  .----------------.  .----------------.  .----------------.  .----------------. 
| |_________________| | | .--------------. || .--------------. || .--------------. || .--------------. |
|  ___ ___ ___   ___  | | |     ______   | || |      __      | || |   _____      | || |     ______   | |
| | 7 | 8 | 9 | | + | | | |   .' ___  |  | || |     /  \     | || |  |_   _|     | || |   .' ___  |  | |
| |___|___|___| |___| | | |  / .'   \_|  | || |    / /\ \    | || |    | |       | || |  / .'   \_|  | |
| | 4 | 5 | 6 | | - | | | |  | |         | || |   / ____ \   | || |    | |   _   | || |  | |         | |
| |___|___|___| |___| | | |  \ `.___.'\  | || | _/ /    \ \_ | || |   _| |__/ |  | || |  \ `.___.'\  | |
| | 1 | 2 | 3 | | x | | | |   `._____.'  | || ||____|  |____|| || |  |________|  | || |   `._____.'  | |
| |___|___|___| |___| | | |              | || |              | || |              | || |              | |
| | . | 0 | = | | / | | | '--------------' || '--------------' || '--------------' || '--------------' |
| |___|___|___| |___| |  '----------------'  '----------------'  '----------------'  '----------------' 
|_____________________|
"""
print(logo)


def add(n, m):
    return n + m


def subtraction(n, m):
    return n - m


def multiplication(n, m):
    return n * m


def division(n, m):
    return n / m


# print(f"{num1} {user_input} {num2} =",function(num1,num2))
operators = {
    '+': add, '-': subtraction, '*': multiplication, '/': division
}


def calculator():
    num1 = int(input("Enter the number1:"))
    for i in operators:
        print(i)
    print("Enter the any one of the above operator you want to perform")
    should_continue = False
    while not should_continue:
        user_input = input("pick an operation + - * /:")
        num2 = int(input("Enter the next number:"))
        function = operators[user_input]
        First_answer = function(num1, num2)
        print(f"{num1} {user_input} {num2} =", First_answer)
        user2_input = input(
            f'Type y to continue calculating {First_answer} if not type n to start a fresh one:').lower()
        if user2_input == 'y':
            num1 = First_answer
        else:
            should_continue = False
            calculator()


calculator()




