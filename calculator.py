


# criei um função para cada operador 

def soma():
    num1 = int(input("Digite o primeiro número :"))     
    num2 = int(input("Digite o segundo número :"))
    result = num1 + num2
    print(f"A soma dos valores é:{result}")
def sub():
    num1 = int(input("Digite o primeiro número :") )       
    num2 = int(input("Digite o segundo número :"))
    result = num1 - num2
    print(f"A subtração dos Valores é :{result}")
def mult():
    num1 = int(input("Digite o primeiro número :")  )      
    num2 = int(input("Digite o segundo número :"))
    result = num1 * num2
    print(f"A multiplicação dos valores é :{result}")
def div():
    num1 = int(input("Digite o primeiro número :") )  
    num2 = int(input("Digite o segundo número :"))
    result = num1 / num2
    print(f"A divisão dos valores é :{result}")




operador = 1
#captura de dados do usuário
# usei while para trocar o valor da variavel operador , baseado na escolha do usuário

while operador:

    print("1. Somar")
    print("2. Subtrair")
    print("3. Multiplicação")
    print("4. Divisão ")
    print("0.Sair")
    operador = int(input("Digite um número válido para as opções acima :"))

    if (operador == 1):
        soma()
    if (operador == 2):
        sub()
    if (operador == 3):
        mult()      
    if (operador == 4):
        div()   
         



