#ENTRADA
#NOS DAN LA FORMULA PARA PASARLO DE C A F Y F A C
#PROCESO

#SALIDA
#MOSTRAR EN EL PROGRAMA QUE CUANDO EL USUARIO INGRESE UNA TEMPERATURA YA SEA CELSIUS A F 
# Y F A C

temp = float(input("ingrese la temperatura"))
unidad = input("ingrese la unidad: (c o f): ")
if unidad == "C":
    fahrenheit = (temp * 9/5) + 32
    print("en fahrenheit es", fahrenheit)
elif unidad == "f":
    celsius= (temp -32)* 5/9
    print("en celsius es",celsius)
else:
    print("unidad no valida, escriba c o f")



