#Estructuras de Decisión Sencillas (si)
#Crea un programa que pida al usuario su edad y
#verifique si es mayor de 18 años. Si lo es, debe
#mostrar el mensaje: "Eres mayor de edad".


edad= int(input("ingresa tu edad"))
if edad >= 18:
    print("eres mayor de edad")
elif edad <= 17:
    print("eres un menor pelao")