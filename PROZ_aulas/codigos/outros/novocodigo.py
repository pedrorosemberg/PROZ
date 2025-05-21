# solicitando ao usuário a base do triângulo
# o valor é convertido para float, pois pode conter casas decimais
base = float(input("digite a base do triangulo (cm):"))

#solicita ao usuário a altura do triângulo
altura=float(input("digite a altura do triangulo (cm):"))

#calcula a area do triangulo usando a formula:area = (base* altura)/2
area = (base * altura) /2 

#exibe o resultado da área, com a unidade em cm
#o f serve para habilitar a interpolaçao de variaveis dentro da string, entre chaves {}


print(f"A área do triangulo é: {area} cm")