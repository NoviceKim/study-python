from advanced.calc import Calculator

menu = ''
number_message = ''
oper_message = ''
error_message = ''

while True:
    choice = int(input(menu))
    num1, num2, oper = '', '', ''

    if choice == 1:
        error_code=''
        try:
            num1, num2 = map(int, input(number_message).split())
            oper = input(oper_message)

        except ValueError:
            error_code = 'ValueError'

        finally:
            if oper == '/':
                if num2 == 0:
                    error_code = 'ZeroDivisionError'

        Calculator(num1).calc(num2, oper, error_code=error_code)


    elif choice == 2:
        with open('log.txt', 'r', encoding='utf-8') as file:
            print(file.read())

    elif choice == 3:
        break

    else:
        print(error_message)
