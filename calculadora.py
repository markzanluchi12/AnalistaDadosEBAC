num1 = int(input('Digite num1: '))
if num1 > 0:
    num2 = int(input('Digiter num2: '))
    opera = input('Digite qual operação quer fazer: ')
    if opera == '+':
        print(num1 + num2)
    elif opera == '-':
        print(num1 - num2)
    elif opera == '*':
        print(num1 * num2)
    elif opera == '/':
        if num2 != 0:
            print(num1 / num2)
        else:
            print("Erro: Divisão por zero não é permitida.")
    else:
        print("Operação inválida.")
else:
    print('Impossivel fazer qualquer operação com zero.')