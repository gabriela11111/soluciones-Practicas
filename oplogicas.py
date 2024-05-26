#Realizar un programa python que verifique si la persona es mayor de edad para otorgarle un prestamo.
#Teniendo en cuenta las siguientes condiciones
#a) Que sea mayor de 18 años y b) Que sea menor a 65 años
#En caso contrario no se le otorgara el prestamo.

edad=int(input("Ingrese la edad de la persona"))

if edad >= 18 and edad <65:
    print("Felicitaciones te otorgaron el prestamo")

else:
    print("Lamentamos no otorgarte el prestamo")



