# Faça um Programa que peça dois números e imprima o maior deles

numero1 = int(input('Digite o 1 número\n'))
numero2 = int(input('Digite o 2 número\n'))
if numero1 > numero2:
    print(f'O primeiro número digitado foi: {numero1}\nO segundo número digitado foi: {numero2}\nO número ({numero1}) é maior que o número ({numero2})')
else:
    print(f'O primeiro número digitado foi: {numero1}\nO segundo número digitado foi: {numero2}\nO número ({numero2}) é maior que o número ({numero1})')

