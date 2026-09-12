print("-----Calcular el area de un triangulo-----")

#Definimos la funcion
def area_triangulo(base, altura):
    #Calculamos el area del triangulo
    area = (base * altura) / 2
    #Retornamos el resultado
    return area

if __name__ == "__main__":
    # Pedimos al usuario que ingrese la base y la altura
    base = float(input("Ingrese la base del triangulo: "))
    altura = float(input("Ingrese la altura del triangulo: "))

    # Llamamos a la funcion y mostramos el resultado
    resultado = area_triangulo(base, altura)
    print(f"El area del triangulo es: {resultado}")