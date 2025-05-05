def calcular_area(raio):
    return 3.14 * raio * raio

def calcular_volume(raio, altura):
    area_base = calcular_area(raio)
    return area_base * altura

volume = calcular_volume(5, 10)
print(f"Volume: {volume}")