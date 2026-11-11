import random

def jugar_sorteo(mi_boleto):
    boleto_ganador = random.randint(1, 100)
    print(f"Tu boleto: {mi_boleto} | Boleto ganador: {boleto_ganador}")
    
    if mi_boleto == boleto_ganador:
        print("¡Ganaste!")
    else:
        print("Perdiste.")

jugar_sorteo(7)