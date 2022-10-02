codigo1,unidade1,preco1 = (input("Código, unidade, preco: ").split(";"))
codigo1 = int(codigo1)
unidade1 = int(unidade1)
preco1 = float(preco1)

codigo2,unidade2,preco2 = (input("Código, unidade, preco: ").split(";"))
codigo2 = int(codigo2)
unidade2 = int(unidade2)
preco2 = float(preco2)

total = ((preco1*unidade1) + (preco2*unidade2)) 

print()
print("Valor a pagar: R$ %.2f"%total)

