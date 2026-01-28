#Se tiene una la información sobre 1 estudiante de una institución de educación para el trabajo
#que realizará su proceso de matrícula financiera. La
#información que se conoce del estudiante es la siguiente:
# • Código
# • Nombre
# • Programa a académico al cual pertenece, que puede ser
# 
# • Indicador de Beca, puede ser:
# o 1: Beca por rendimiento académico. Descuento del 50% sobre el valor matricula.
# o 2: Beca Cultural – Deportes. Descuento del 40% sobre el valor matrícula
# o 3: Sin Beca.
#  También nos suministran el cuadro de valores de matrícula que depende del
#  programa académico que cursa el estudiante, así:





def matricula():
    
    nombre = input("Cual es su nombre: ")
    codigo =input("Cual es su codigo: ")
    progrm =int(input("Programa académico al cual pertenece: \n1. Técnico en Sistemas\n2. Técnico en Desarrollo de videoj \n3. Técnico en Animación Digital\n: "))
    beca = int(input("Cual es su beca: \n1. Beca por rendimiento académico. Descuento del 50% sobre el valor matricula.\
    \n2. Beca Cultural - Deportes. Descuento del 40% sobre el valor matrícula\n3. Sin beca\n: "))

    if   (progrm == 1 and beca == 1):
       print(nombre, int(800000 * 0.50))
    elif (progrm == 1 and beca == 2):
       print(nombre, int(800000 * 0.40))
    elif (progrm == 1 and beca == 3):
        print(nombre, 800000)
  
    if   (progrm == 2 and beca == 1):
        print(nombre, 1000000 * 0.50)
  
    elif (progrm == 2 and beca == 2):
        print(nombre, 1000000 * 0.40)
    elif (progrm == 2 and beca == 3):
        print(nombre, 1000000)

    if   (progrm == 3 and beca == 1):
        print(nombre, 1200000 * 0.50)
   
    elif (progrm == 3 and beca == 2):
        print(nombre, 1200000 * 0.40)
  
    elif (progrm == 3 and beca == 3):
        print(nombre, 1200000)
 
matricula()