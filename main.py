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
def validar_numero(entrada):
    try:
        numero = int(entrada)
        if numero >= 0:
            return True, numero
        else:
            return False, None
    except ValueError:
        return False, None

# Solicitar números al usuario
numeros = []
while True:
    entrada = input("Ingrese un número entero positivo (0 para finalizar): ")
    if entrada == '0':
        break
    es_numero, numero = validar_numero(entrada)
    if es_numero:
        numeros.append(numero)
    else:
        print("Por favor, ingrese solo números enteros positivos.")

# Calcular el MCD
mcd = mcd_varios_numeros(numeros)
print("El MCD de los números ingresados es:", mcd)