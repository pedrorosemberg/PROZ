while True:
    num1 = float (int(input("numero 1")))
    num2 = float (int(input("numero 2")))
   
    soma = num1 + num2 

    print("a soma é",soma)

    continuar =input("deseja continuar? (s/n):").lower()
    if continuar!= "s":
     print ("encerrando programa")
    break