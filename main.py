def calcular_mcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a

def mcd_varios_numeros(numeros):
    if len(numeros) < 2:
        return "Debe ingresar al menos dos números para calcular el MCD."
    resultado = numeros[0]
    for num in numeros[1:]:
        resultado = calcular_mcd(resultado, num)
    return resultado

# Función para validar la entrada como un número entero positivo
def es_entero_positivo(entrada):
    try:
        numero = int(entrada)
        return numero >= 0
    except ValueError:
        return False

# Solicitar números al usuario
numeros = []
while True:
    entrada = input("Ingrese un número entero positivo (0 para finalizar): ")
    if entrada == '0':
        break
    if es_entero_positivo(entrada):
        numeros.append(int(entrada))
    else:
        print("Por favor, ingrese solo números enteros positivos.")


# Calcular el MCD
mcd = mcd_varios_numeros(numeros)
print("El MCD de los números ingresados es:", mcd)