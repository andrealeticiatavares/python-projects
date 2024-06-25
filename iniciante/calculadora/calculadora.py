# Função para adição
def sum(x, y):
    return x + y

#Função para subtração
def subtration(x, y):
    return x - y

#Função para multiplicação
def multiplication(x, y):
    return x * y

#Função para divisão
def division(x, y):
    if y != 0:
        return x / y
    else:
        return "Erro! Divisão por zero."
    
#Função menu de opções
def menu():
    print("Selecione a operação:")
    print("1. Adição")
    print("2. Subtração")
    print("3. Multiplicação")
    print("4. Divisão")

#Loop principal
while True:
    attempts = 0
    while attempts < 3:
        menu()

        select = input("Digite a escolha (1/2/3/4): ")

        if select in {'1', '2', '3', '4'}:
            try:
                num1 = float(input("Digite o primeiro número: "))
                num2 = float(input("Digite o segundo número: "))
            except ValueError:
                print("Entrada errada! Por favor, insira números válidos.")
                continue

            #Utilizando match-case
            match select:
                case '1':
                    print(f"{num1} + {num2} = {sum(num1, num2)}")
                case '2':
                    print(f"{num1} - {num2} = {subtration(num1, num2)}")
                case '3':
                    print(f"{num1} * {num2} = {multiplication(num1, num2)}")
                case '4':
                    result = division(num1, num2)
                    print(f"{num1} / {num2} = {result}")
            break
        
        else:
            print("Escolha invalida! Por favor, selecione uma opção válida.")
            attempts += 1
    
    if attempts == 3:
        print("Número máximo de tentativas excedido.")

    next_calc = input("Deseja realizar outra opração? (sim/não): ")
    if next_calc.lower() != 'sim':
        print("Obrigado por usar a calculadora. Até logo! ")
        break