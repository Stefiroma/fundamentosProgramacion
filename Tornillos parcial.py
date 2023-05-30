tornillo = float(input("\n Ingrese el tamaño del tornillo: "))

if 1 <= tornillo < 3:
    tornillo_tamaño = "pequeño"
elif 3 <= tornillo < 5:
    tornillo_tamaño = "mediano"
elif 5 <= tornillo < 6.5:
    tornillo_tamaño = "grande"
elif 6.5 <= tornillo < 8.5:
    tornillo_tamaño = "muy grande"
else:
    tornillo_tamaño = "ERROR"

print("\n El tamaño correspondiente del tornillo es:", tornillo_tamaño)
