#Calcular la cantidad de alumnos que rindieron el examen
#Iniciar la suma de nota 
#Solicitar el valor de las notas 
#Calcular promedio
# Saber el rendimiento de los alumnos seguon el promedio
cantidad_alumnos=int(input("Cantidad de alumnos que rindieron el examen"))

suma_notas= 0

for i in range (cantidad_alumnos):
    nota = float(input(" Ingrese la nota del alumno :"))
    suma_notas= nota 
    
    #Calcular promedio
    promedio= suma_notas / cantidad_alumnos
    print("Mostrar promedio:" ,promedio)

      
    #Mostrar el rendimiento
    
def evaluar_rendimiento(promedio):
                    
 if promedio > 8:
    print("Rendimiento elevado")
 elif promedio >= 8 and promedio <= 6:
    print("Rendimiento aceptable")
 else:
    print("Rendimiento bajo")
  
         