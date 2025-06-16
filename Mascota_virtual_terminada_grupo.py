# importar el modulo random
import random

# import imagen desde el archivo mascota.py
from mascota import imagen


class MascotaVirtual:
    def __init__(self, nombre):
        self.nombre = nombre
        self.hambre = 0
        self.felicidad = 0
        self.imagen_inicio = imagen.inicio
        self.imagen_triste = imagen.triste
        self.imagen_muerto = imagen.muerto
        self.imagen_disgustado = imagen.disgustado
        self.imagen_feliz = imagen.feliz

    def alimentar(self):
        self.felicidad -= random.randint(5, 10)

        if self.felicidad < 0:
            self.felicidad = 0
        if self.hambre == 0:
            print(self.imagen_disgustado)
            print(f"{self.nombre} esta lleno ya no le puede comer mas")
        else:
            self.hambre -= random.randint(10, 15)
            if self.hambre < 0:
                self.hambre = 0
            print(self.imagen_feliz)
            print(f"{self.nombre} Ya comio, esta re feliz🐶")

    def jugar(self):

        self.felicidad += random.randint(10, 25)

        self.hambre += random.randint(10, 15)

        if self.felicidad > 100:
            self.felicidad = 100

        if self.hambre > 100:
            self.hambre = 100

        if self.hambre > 70:

            print(self.imagen_triste)
            print(f"{self.nombre} tiene mucha hambre y no puede jugar")

        else:
            print(self.imagen_feliz)
            print(f"{self.nombre} se divierte mucho jugando")

    def estado_animo(self):
        if self.hambre >= 70 and self.felicidad <= 50:
            print(self.imagen_triste)
            print(f"{self.nombre} esta muy hambrienta y triste ")
        if self.hambre >= 70:
            print(self.imagen_triste)
            print(f"{self.nombre} esta muy hambrienta ")
        else:
            print(self.imagen_feliz)
            print(f"{self.nombre} se encuentra contenta y satisfecha")

    def presentacion(self):  # opcional
        print(
            f"\n╔════════════════════════════════════╗\n║ Te presento a tu mascota!          ║\n╚════════════════════════════════════╝\n{self.imagen_inicio}\tSu nombre es {self.nombre}"
        )

    def despedida(self):  # opcional
        print(
            f"\n╔════════════════════════════════════╗\n║ Nos vemos! ║\n╚════════════════════════════════════╝{self.imagen_inicio}╔════════════════════════════════════╗\n║ Jueguemos otro día! ║\n╚════════════════════════════════════╝\n"
        )


interfaz_inicio = "\n╔════════════════════════════════════╗\n║       Bienvenido a tu primer       ║\n║          mascota virtual!          ║\n╚════════════════════════════════════╝\n"
interfaz_juego = "\n╔════════════════════════════════════╗\n║       Opciones disponibles:        ║\n║                                    ║\n║ 1 - Alimentar                      ║\n║ 2 - Jugar                          ║\n║ 3 - Mostrar informacion            ║\n║ 4 - Salir                          ║\n║                                    ║\n╚════════════════════════════════════╝\n"


print(interfaz_inicio)
nombre = input("Elige el nombre de tu mascota: ")
mascota = MascotaVirtual(nombre)

mascota.presentacion()

while True:
    print(interfaz_juego)
    opcion = int(input("Elija una opcion: "))
    if opcion == 1:
        mascota.alimentar()
    elif opcion == 2:
        mascota.jugar()
    elif opcion == 3:
        mascota.estado_animo()
    elif opcion == 4:
        mascota.despedida()
        break
    else:
        print("Seleccione una de las opciones")

# Crear una instancia de MascotaVirtual

# Interactuar con la mascota virtual
# alimenta, juega y muestra su estado de animo
# repite esta accion al menos 8 veces

# Esto lo vamos a utilizar más adelante 😉
# i
