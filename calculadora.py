# Funcion para sumar dos numeros
def sumar(a, b):
    return a + b

# Funcion para restar dos numeros
def restar(a, b):
    return a - b

# Funcion para multiplicar dos numeros
def multiplicar(a, b):
    return a * b

def dividir(a, b):
    return a / b

while True:
    print("Opciones:")
    print("Escribe 'sumar' para sumar dos números")
    print("Escribe 'restar' para restar dos números")
    print("Escribe 'multiplicar' para multiplicar dos números")
    print("Escribe 'salir' para salir del programa")
    print()
    
    opcion = input("Escribe la operacion que desee realizar: ")

    print()
    if opcion == "salir":
        break
    elif opcion == "sumar":
        
            num1 = int(input("Introduce el primer número: "))
            num2 = int(input("Introduce el segundo número: "))
            print()
            print("El resultado es:", sumar(num1, num2))
            break     
    else:
        print("Opción no válida. Por favor, elige una opción válida.")