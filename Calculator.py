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
should_continue = False
while not should_continue:
    num1 = int(input("Enter the number1:"))
    for i in operators:
        print(i)
    print("Enter the any one of the above operator you want to perform")
    user_input = input("pick an operation + - * /:")
    num2 = int(input("Enter the next number:"))
    function = operators[user_input]
    First_answer = function(num1, num2)
    print(f"{num1} {user_input} {num2} =", First_answer)
    second_while = False
    while not second_while:
        new_answer = First_answer
        user2_input = input(f'Type y to continue calculating {new_answer} if not type n to start a fresh one:').lower()
        if user2_input == 'y':
            for i in operators:
                print(i)
            print("Enter the any one of the above operator you want to perform")
            user_input = input("pick an operation + - * /::")
            num3 = int(input("Enter the next number:"))
            function = operators[user_input]
            Second_answer = function(new_answer, num3)
            print(f"{First_answer} {user_input} {num3} =", Second_answer)
            First_answer = Second_answer

        else:
            second_while = True
            should_continue = True
            print("Start a Fresh calculation")
            quit()

    user = input("If you want to continue type yes if not take exit by typing no:").lower()
    if user == "no":
        should_continue = True
        print("Bye Bye")
        quit()
