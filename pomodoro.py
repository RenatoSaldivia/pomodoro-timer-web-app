import time
import winsound


def beep():
    # Cinco beeps lentos
    for _ in range(5):
        winsound.Beep(1000, 700)  # Frecuencia 1000 Hz, duración 0.7 segundos
        time.sleep(0.6)  # Pausa más larga entre beeps


def cuenta_regresiva(minutos):
    segundos = minutos * 60
    while segundos:
        mins, segs = divmod(segundos, 60)
        print(f"{mins:02d}:{segs:02d}", end="\r")
        time.sleep(1)
        segundos -= 1


def pomodoro():
    ciclo = 1
    while True:
        print(f"\n🔁 Ciclo Pomodoro #{ciclo} - Trabaja 25 minutos")
        cuenta_regresiva(25)  # Cambiar a 25 para versión real
        beep()

        print("\n☕ Descansa 5 minutos")
        cuenta_regresiva(5)  # Cambiar a 5 para versión real
        beep()

        print("✅ ¡Fin del ciclo! Se reiniciará otra sesión...")
        ciclo += 1  # Aumenta el contador de ciclos


if __name__ == "__main__":
    try:
        pomodoro()
    except KeyboardInterrupt:
        print("\n\n👋 ¡Temporizador detenido! Hasta la próxima sesión.")
