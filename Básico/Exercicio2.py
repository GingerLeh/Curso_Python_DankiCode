'''
Troca de variáveis
'''
x = input("Insira valor de x:")
y = input("Insira valor de y:")

temporaria = x
x = y
y = temporaria

print(f"Valor de x depois da troca {x}")
print(f"Valor de y depois da troca {y}")
