
eq = int(input("Número de quilowatts consumido: "))
q = 0.12
icms = 0.18
soma1 = eq * q
soma2 = soma1 * icms
soma3 = soma1 + soma2
print("Total a ser pago: ", soma3)