#Pedir al usuario la nota de cada materia
nota1 = float (input ("Ingresa la nota de la materia 1:"))
nota2 = float (input ("Ingresa la nota de la materia 2:"))
nota3 = float (input ("Ingresa la nota de la materia 3:"))
nota4 = float (input ("Ingresa la nota de la materia 4:"))
nota5 = float (input ("Ingresa la nota de la materia 5:"))

#Calcular la suma de las notas
suma_notas= nota1 + nota2 + nota3 + nota4 + nota5

#Calcular promedio
promedio= suma_notas / 5

print("El promedio del estudiante es:" , promedio)


