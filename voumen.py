print("Este programa calcula el volumen maximo de nua caja")
largo= int(input("ingrese el largo de la plancha: "))
ancho= int(input("ingrese el ancho de la plancha: "))

volumenMaximo = 0
h = 0

area = ancho * largo
volumen = ancho * largo * h
 
volumen = h * (ancho - 10*h) * (largo - 20*h)

if volumen < volumenMaximo:


print(f"el volumen max es {volumen}")
print(f"la altura es {h}")

