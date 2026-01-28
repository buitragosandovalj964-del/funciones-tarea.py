#Dado el nombre y estrato (1,2,3,4,5) de un usuario del
#servicio de energía eléctrica, calcular lo que pagaría de
#tarifa básica del servicio de energía eléctrica, que
#depende del estrato, así
#Estrato Tarifa Básica
#1 $10.000
#2 $15.000
#3 $30.000
#4 $50.000
##Se pide visualizar el nombre y tarifa básica
def estratos():
 nombre = input("escribe tu nombre")
 entrada  = int(input("diligencie su estrato"))
 if entrada == 1:
  print("su pago es de",10000)
 elif entrada == 2:
  print("su pago es de", 15000)
 elif  entrada == 3:
   print("su pago es de", 30000)
 elif entrada == 4:
  print("su pago es de", 50000)
 else:
  print("intentelo de nuevo, estos son los estratos 1, 2, 3, 4")

 #llamar la funcion
estratos()






