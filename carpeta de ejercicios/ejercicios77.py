#Desarrolla un programa que reciba una
#temperatura en grados Celsius y verifique si está
#por encima de 30 grados. Si es así, debe mostrar el
#mensaje: "Hace calor hoy".
"""
T = int(input("ingrese su temperatura en grados celsius"))
if T >= 30:
 print("hace calor hoy")
"""



# Estructuras de Decisión Dobles (si-no)
#Escribe un programa que solicite al usuario
#ingresar un número entero y determine si el
#número es par o impar.

"""
N = int(input("ingrese un numero entero"))

if N  % 2 == 0:
    print("es un numero par")
else:
    print("es un numero impar")
     
"""
#Estructuras de Decisión Dobles (si-no)
#Crea un programa que pida al usuario ingresar
#una contraseña. Si la contraseña es correcta (elige
#una contraseña predeterminada), muestra el
#mensaje "Acceso concedido", de lo contrario,
#muestra "Acceso denegado".
"""
contrasena_correcta = "zurdiño"
C = input("Escribe la contraseña: ")

if C == contrasena_correcta:
    print("Acceso concedido")
else:
    print("Acceso denegado")

"""

#Estructuras de Decisión Dobles (si-no)
#Desarrolla un programa que solicite al usuario
#ingresar una nota entre 0 y 100. Si la nota es mayor
#o igual a 60, el programa debe imprimir
#"Aprobado"; si no, debe imprimir "Reprobado".
"""
nota = "1 a 100"
nota = int(input("ingrese su nota")) 
if nota >= 60:
    print("aprobado")
else:
    print("reprobado")
"""

#Estructuras de Decisión Múltiples (si-no-si)
#Escribe un programa que solicite al usuario
#ingresar un número entero y determine si el
#número es positivo, negativo o cero.

"""
N = int(input("ingrese un numero entero"))

if N >= 1:
    print("es un numero positivo") 
elif N <= -1:
    print("es un numero negativo")
elif N == 0:
    print("es un cero ")
else:
    print("VAYA COMA MIERDA")
"""

#Estructuras de Decisión Múltiples (si-no-si)
#Desarrolla un programa que solicite al usuario ingresar la cantidad de
#horas trabajadas en una semana y calcule el pago correspondiente:
#▪ Hasta 40 horas: se paga la tarifa normal (por ejemplo, $10 por hora).
#▪ De 41 a 50 horas: se paga la tarifa normal por las primeras 40 horas
#y 1.5 veces la tarifa por las horas adicionales.
#▪ Más de 50 horas: se paga la tarifa normal por las primeras 40 horas,
#1.5 veces la tarifa por las siguientes 10 horas y doble tarifa por las
#horas que excedan de 50.
"""
horas = int(input("Ingrese las horas trabajadas en la semana: "))
tarifa = 10

if horas <= 40:
    pago = horas * tarifa

elif horas <= 50:
    pago = (40 * tarifa) + ((horas - 40) * tarifa * 1.5)

else:
    pago = (40 * tarifa) + (10 * tarifa * 1.5) + ((horas - 50) * tarifa * 2)

print("El pago total es:", pago)
"""
#Estructuras de Decisión Múltiples (si-no-si)
#Crea un programa que pida al usuario ingresar una calificación (entre
#0 y 100) y muestre la letra correspondiente:
#✓ 90 o más: A
#✓ 80 a 89: B
#✓ 70 a 79: C
#✓ 60 a 69: D
#✓ Menos de 60: F
#entrada
#me dan las notas para poder clasificarlas
#proceso
#salida
#mostrar y clasificar las notas por categorias


notas =int(input("ingrese su calificacion"))

if notas > 90:
    print("notas:", "A")
elif notas >= 80:
    print("notas:", "B")
elif notas >= 70:
    print( "notas:","C")
elif notas >= 60:
    print("notas:", "D")
else:
    notas  
    print("notas:", "F")














