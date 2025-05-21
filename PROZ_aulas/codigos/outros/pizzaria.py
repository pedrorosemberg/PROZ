print("pizzaria peperone - seja bem vindo!!")
print("-----cardápio do dia-----")
print(" ")
print("tipo de pizzas:")
print("calabresa,frango,catupiry")
print ("")
print("tamanhos da pizza:")
print("pizza pequena  R$ 10,00")
print("pizza media R$15,00")
print("pizza grande R$20,00")
print("")
print("escolha seu refri:")
print("")
print("coca cola 7,00")
print("guaraná R$6,00")
print("fanta R$5,00")
print("____________________")
print("")
print("faça seu pedido:")
print("1 - calabresa")
print("2 - frango:")
print("3 - catupiry:")
print("____________________")

pedidopizza =int(input())

print("digite o tamanho da pizza:")
print("p - pequena")
print("m - media")
print("g - grande")
print("____________________")

tampizza = input().upper()

print("escolha seu refri")
print("1 - coca-cola")
print("2 - guarana")
print("3 - fanta")
print("____________________")

pedidorefri = int(input())

if (pedidopizza ==1) and (tampizza == "P") and (pedidorefri == 1):
    precoapagar = 10.00 + 7.00
    pedidos = "calabresa, pequena coca-cola"

elif (pedidopizza ==1) and (tampizza == "P") and (pedidorefri == 2):
    precoapagar = 10.00 + 6.00
    pedidos = "calabresa, pequena, guarana"
    
elif(pedidopizza ==1) and (tampizza == "P") and (pedidorefri == 3):
    precoapagar = 10.00 +5.00
    pedidos = "calabresa, pequena, fanta"

elif(pedidopizza ==1) and (tampizza == "M") and (pedidorefri == 1):
    precoapagar = 15.00 + 7.00
    pedidos = "calabresa, media, coca-cola"
    
elif(pedidopizza ==1) and (tampizza == "M") and (pedidorefri == 2):
    precoapagar = 15.00 + 6.00
    pedidos = "calabresa, media, guarana"

elif(pedidopizza ==1) and (tampizza == "M") and (pedidorefri == 3):
    precoapagar = 15.00 + 5.00
    pedidos = "calabresa, media, fanta"

elif(pedidopizza ==1) and (tampizza == "G") and (pedidorefri == 1):
    precoapagar = 20.00 + 7.00
    pedidos = "calabresa, grande, coca-cola"

elif(pedidopizza ==1) and (tampizza == "G") and (pedidorefri == 2):
    precoapagar = 20.00 + 6.00
    pedidos = "calabresa, grande, guarana"
    
elif(pedidopizza ==1) and (tampizza == "G") and (pedidorefri == 3):
    precoapagar = 20.00 + 5.00
    pedidos = "calabresa, grande, fanta"

elif(pedidopizza ==2) and (tampizza == "P") and (pedidorefri == 1):
    precoapagar = 10.00 + 7.00
    pedidos = "frango, pequena, coca-cola"

elif(pedidopizza ==2) and (tampizza == "P") and (pedidorefri == 2):
    precoapagar = 10.00 + 6.00
    pedidos = "frango, pequena, guarana"

elif(pedidopizza ==2) and (tampizza == "P") and (pedidorefri == 3):
    precoapagar = 10.00 + 5.00
    pedidos = "frango, pequena, fanta"


elif(pedidopizza ==2) and (tampizza == "M") and (pedidorefri == 1):
    precoapagar = 15.00 + 7.00
    pedidos = "frango, media, coca-cola"
    
elif(pedidopizza ==2) and (tampizza == "M") and (pedidorefri == 2):
    precoapagar = 15.00 + 6.00
    pedidos = "frango, media, guarana"

elif(pedidopizza ==2) and (tampizza == "M") and (pedidorefri == 3):
    precoapagar = 15.00 + 5.00
    pedidos = "frango, media, fanta"
    
elif(pedidopizza ==2) and (tampizza == "G") and (pedidorefri == 1):
    precoapagar = 20.00 + 7.00
    pedidos = "frango, grande, coca-cola"
   
elif(pedidopizza ==2) and (tampizza == "G") and (pedidorefri == 2):
    precoapagar = 20.00 + 6.00
    pedidos = "frango, grande, guarana"
    
elif(pedidopizza ==2) and (tampizza == "G") and (pedidorefri == 3):
    precoapagar = 20.00 + 5.00
    pedidos = "frango, grande, fanta"
    
elif(pedidopizza ==3) and (tampizza == "P") and (pedidorefri == 1):
    precoapagar = 10.00 + 7.00
    pedidos = "catupiry, pequena, coca-cola"
   
elif(pedidopizza ==3) and (tampizza == "P") and (pedidorefri == 2):
    precoapagar = 10.00 + 6.00
    pedidos = "catupiry, pequena, guarana"

    
elif(pedidopizza ==3) and (tampizza == "P") and (pedidorefri == 3):
    precoapagar = 10.00 + 5.00
    pedidos = "catupiry, pequena, fanta"

    
elif(pedidopizza ==3) and (tampizza == "M") and (pedidorefri == 1):
    precoapagar = 15.00 + 7.00
    pedidos = "catupiry, media, coca-cola"
    
elif(pedidopizza ==3) and (tampizza == "M") and (pedidorefri == 2):
    precoapagar = 15.00 + 6.00
    pedidos = "catupiry, media, guarana"

    
elif(pedidopizza ==3) and (tampizza == "M") and (pedidorefri == 3):
    precoapagar = 15.00 + 5.00
    pedidos = "catupiry, media, fanta"
    
elif(pedidopizza ==3) and (tampizza == "G") and (pedidorefri == 1):
    precoapagar = 20.00 + 7.00
    pedidos = "catupiry, grande, coca-cola"
    
elif(pedidopizza ==3) and (tampizza == "G") and (pedidorefri == 2):
    precoapagar = 20.00 + 6.00
    pedidos = "catupiry, grande, guarana"
    
elif(pedidopizza ==3) and (tampizza == "G") and (pedidorefri == 3):
    precoapagar = 20.00 + 5.00
    pedidos = "catupiry, grande, fanta"

else:
    precoapagar = 0.0
    pedidos = "inválidos!!"

print("_____________________________")
print(f"o total a pagar é; R$ {precoapagar:.2f}")
print("-----------------------------")
print(f"os pedidos foram {pedidos}")
print("_____________________________")
print("bela escolha e bom apetite.")