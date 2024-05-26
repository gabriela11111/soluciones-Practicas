#Realizar un programa en Python que me permira ingresar el valor de una compra realizada por una persona.
#En el caso que el importe sea mayor a $100 debe presentar DNI

importe=float(input("Ingrese el importe a evaluar:"))

if importe > 10000:
    print("Debe registrar DNI")

    print("Gracias por su compra")