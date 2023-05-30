#1.calcular la cantidad de partidos por equipo

partidos = [("EquipoA", "EquipoB", "2-1"), ("EquipoC", "EquipoA", "0-3"), ("EquipoB", "EquipoD", "3-3"), ("EquipoA", "EquipoD", "1-0"), ("EquipoC", "EquipoB", "2-2"), ("EquipoB", "EquipoA", "0-2"), ("EquipoA", "EquipoC", "1-0"), ("EquipoD", "EquipoB", "1-1"), ("EquipoD", "EquipoA", "0-1"), ("EquipoB", "EquipoC", "1-2")]

ganados = {}
for equipo in set([partido[0] for partido in partidos] + [partido[1] for partido in partidos]):
    ganados[equipo] = 0

for partido in partidos:
    equipo_local, equipo_visitante, resultado = partido
    goles_local, goles_visitante = resultado.split("-")
    if goles_local > goles_visitante:
        ganados[equipo_local] += 1
    elif goles_local < goles_visitante:
        ganados[equipo_visitante] += 1

print("Cantidad de partidos ganados por equipo:")
for equipo, cantidad in ganados.items():
    print(equipo + ":", cantidad)
