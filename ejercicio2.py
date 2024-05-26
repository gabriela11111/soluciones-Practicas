#colocamos el precio por unidad luego pedimos al usuario la cantidad a comprar
#precio con descuento a jubilado
precio_unidad = 1000
cantidad = int(input("Ingrese la cantidad de leche a comprar"))

#Aplicar descuentos segun la cantidad
if cantidad >= 12:
    cantidad_descuento = 0.10
    
elif cantidad >= 24:
    cantidad_descuento = 0.15
    
else: 
    cantidad_descuento = 0 
    
#precio total sin descuento
precio_total_sin_descuento = cantidad * precio_unidad

#con descuento
descuento_por_cantidad = precio_total_sin_descuento * cantidad_descuento 
    
# se aplica descuento a jubilado
descuento_jubilado= 0.10

precio_total_descuento = precio_total_sin_descuento - descuento_por_cantidad
precio_total_descuento = precio_total_sin_descuento  * descuento_jubilado
     
#mostrar lo que paga el cliente
print("El cliente debe pagar:" , precio_total_descuento, "pesos"  )    



