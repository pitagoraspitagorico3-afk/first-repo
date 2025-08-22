def ecuacion_cuadratica(a,b,c):
    discriminante = (b*b) - (4*a*c)
    if discriminante > 0:
        x1 = (-b + discriminante**0.5)/(2*a)
        x2 = (-b - discriminante**0.5)/(2*a)
        return x1,x2
    elif discriminante == 0:
        x1 = x2 = -b / (2*a)
        return x1,x2
    else:
        parte_real = -b / (2*a)
        parte_imaginaria = (abs(discriminante)**0.5)/(2*a)
        return f"{parte_real} + {parte_imaginaria}i", f"{parte_real} - {parte_imaginaria}i"

a= float(input("Introduce el valor de a:"))
b= float(input("Introduce el valor de b:"))
c= float(input("Introduce el valor de c:"))

soluciones = ecuacion_cuadratica(a, b, c)
print(f"soluciones son:x1-->{soluciones[0]} y x2-->{soluciones[1]}")

