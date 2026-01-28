#Escribe un programa en Python que calcule el interés 
#simple de un préstamo con una tasa del 5%, un préstamo que indiques (por ejemplo, 1000)
#y un tiempo en años (por ejemplo, 2), y muestre en la consola el interés generado.


tasa_interes= 0.05
prestamo= 1000
tiempo = 2
interes = tasa_interes* prestamo* tiempo
print ( "interes:", interes) 
print("prestamo:", prestamo)
print("tiempo en años:", tiempo)
print( "tasa de interes:", tasa_interes*100,"%")
# el interes simple con la siguiente formula aplicado: tasa de interes * prestamo * tiempo
print("elinteres generado es de:", interes)


