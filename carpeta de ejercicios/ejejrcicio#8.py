#Escribe un programa en Python que calcule 
# el IMC (Índice de Masa Corporal) con una fórmula básica (peso / altura^2), 
# usando valores que selecciones para peso en kg y altura en metros (por ejemplo, 70 y 1.75), y 
# muestre el resultado en la consola 
# imc
from turtle import pd


peso = 70
altura = 1.75
imc = peso / (altura ** 2)
print(f"IMC: {imc}")
pd