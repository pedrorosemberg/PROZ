 #solicita ao usuario a base triangulo :
#valor convertido para float, pois pode conter casa decimais
base = float(input("Digite a base do triangulo(cm):"))

# Solicita ao usario a altura do triangulo;
altura = float(input("Digite a altura do triangulo(cm:)"))
# calcula a area do triaangulo usando a formula: area =,(base * altura) / 2
area = (base * altura)/2
 #exibe o resultadoda area,com a unidade em cm 
 #o f serve para habilitar a interpolação de variaveis dentro da string,entre chaves{}

print (f"a area do triangulo é: {area}cm")
