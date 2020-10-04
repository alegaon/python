matriz = [[3.3, 6.1, 4.0], [4.9, 5.7, 6.4]]

print("esta es la matriz=", matriz)

a = int(input("ingrese numero de fila ( '0' o '1'): "))
b = int(input("ingrese el numero de columna ('0', '1' o '2'): "))
print("fila =", a)
print("columna=", b)

# resultado
print("resultado =", matriz[a][b])