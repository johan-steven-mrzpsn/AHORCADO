import random  # usamos random para elegir una palabra al azar

# Lista de palabras para el juego
palabras = ["gato", "perro", "casa", "escuela", "computadora"]

# Elegimos una palabra al azar
palabra_secreta = random.choice(palabras)

# Listas para guardar letras
letras_correctas = []
letras_incorrectas = []

intentos_maximos = 6
intentos_restantes = intentos_maximos

print("===== JUEGO DEL AHORCADO =====")

# Bucle principal del juego: se repite mientras queden intentos
while intentos_restantes > 0:
    # Mostrar el estado de la palabra
    print("\nPalabra:", end=" ")

    for letra in palabra_secreta:
        if letra in letras_correctas:
            print(letra, end=" ")
        else:
            print("_", end=" ")

    print("\nLetras incorrectas:", letras_incorrectas)
    print("Intentos restantes:", intentos_restantes)

    # Pedimos una letra al usuario
    intento = input("Ingresa una letra: ").lower()

    # Validaciones básicas
    if len(intento) != 1:
        print("Por favor, ingresa solo UNA letra.")
        continue

    if not intento.isalpha():
        print("Solo se permiten letras.")
        continue

    if intento in letras_correctas or intento in letras_incorrectas:
        print("Ya intentaste con esa letra.")
        continue

    # Revisamos si la letra está en la palabra
    if intento in palabra_secreta:
        print("¡Bien! La letra está en la palabra.")
        letras_correctas.append(intento)
    else:
        print("La letra NO está en la palabra.")
        letras_incorrectas.append(intento)
        intentos_restantes -= 1  # pierdes un intento

    # Revisamos si ya se adivinó toda la palabra
    adivinado_todo = True
    for letra in palabra_secreta:
        if letra not in letras_correctas:
            adivinado_todo = False
            break

    if adivinado_todo:
        print("\n¡Felicidades! Adivinaste la palabra:", palabra_secreta)
        break

# Si te quedas sin intentos
if intentos_restantes == 0 and not adivinado_todo:
    print("\nTe quedaste sin intentos. La palabra era:", palabra_secreta)
