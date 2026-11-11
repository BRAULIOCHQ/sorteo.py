import random

def jugar_sorteo(mi_boleto):
    print("--- BIENVENIDO AL SORTEO VIP ---")
    boleto_ganador = mi_boleto
    print(f"Tu boleto: {mi_boleto} | Boleto ganador: {boleto_ganador}")
    
    if mi_boleto == boleto_ganador:
        print("¡Ganaste!")
    else:
        print("Perdiste.")

jugar_sorteo(7)