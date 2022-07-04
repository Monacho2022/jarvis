from dis import show_code
from timeit import repeat


nombre_estudiante = input("Ingresa tu nombre: ").capitalize()
if nombre_estudiante.startswith("F"):
    print(nombre_estudiante,"Felicidades, los nombres que inician con 'F' salen mas temprano hoy!")
elif nombre_estudiante.startswith("G"):
    print(nombre_estudiante,"Felicidades, los nombres que inician con 'G' salen 15 minutos antes hoy!")
else:
    print(nombre_estudiante, "usted se queda hasta las 6pm.")
