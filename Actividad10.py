def invertir_texto(palabra):
    if palabra=="":
        return ""
    else:
        return invertir_texto(palabra[1:]) + palabra[0]
def primeros_naturales (n):
    if n==0:
        return 0
    else:
        return n+primeros_naturales(n-1)
def cuenta_regresiva (n):
    if n==0:
        return 0
    else:
        return cuenta_regresiva (n-1)

def sumar_digitos(n):
    if 0<n<=9:
        return n
    else:
        return n%10+sumar_digitos(n//10)

def contar_digitos(n):
    if 0<n<=9:
        return 1
    else:
        return 1+contar_digitos(n//10)

def menu ():
    print("___Menu___")
    print ("1. Invertir cadena de texto")
    print ("2. Calcular los primeros N numeros naturales")
    print ("3. Imprimir cuenta regresiva")
    print ("4. Sumar los digitos de un numero")
    print ("5. Contar cuantos digitos tiene un numero")
    print ("6. Salir")
    opcion=int(input("Seleccione una opcion"))
    if opcion==1:
        palabra=input("Ingrese una cadena de texto: ")
        print(f"La palabra {palabra} invertida es {invertir_texto(palabra)}")
    elif opcion==2:
        n=int(input("Ingrese un numero: "))
        print(f"La suma de los primeros {n} numeros naturales es {sumar_digitos(n)}")
    elif opcion==3:
        n=int(input("Ingrese un numero: "))
        print(f"{cuenta_regresiva(n)}")
    elif opcion==4:
        n=int(input("Ingrese un numero: "))
        print(f"La suma de los digitos es: {sumar_digitos(n)}")
    elif opcion==5:
        n=int(input("Ingrese un numero: "))
        print(f"El numero ingresado tiene {contar_digitos(n)} digitos")
    elif opcion==6:
        print("Gracias por usar el programa")
    else:
        print("Opcion no valida")
menu()