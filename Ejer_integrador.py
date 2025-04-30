import time
# Solicitamos el número al usuario para que podamos hacer el conteo
numero_maximo = int(input("Introduce el número decimal para iniciar el conteo: "))
print("Calculando...")
time.sleep(3)


# Iteramos desde 0 hasta el número indicado por el usuario
# Usamos un ciclo for y vamos incrementando en 1 nuestro i
for i in range(numero_maximo + 1):
    binario = bin(i)[2:]  
    # La funcion bin nos permite convertir el número decimal a binario
    # Eliminamos el prefijo '0b' mediante el operador [2:]
    print(f"{i} -> {binario}")
    # Aplicamos la funcion time.sleep para poder dar un tiempo para poder visualizar el conteo
    time.sleep (3)

