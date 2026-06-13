import speech_recognition as sr
import threading
import time


class Listener:

    def __init__(self):

        self.recognizer = sr.Recognizer()

        self.running = False

        self.wake_word = "jarvis"

        self.estado = "ESPERANDO"

        self.callback = None

        self.recognizer.energy_threshold = 300
        self.recognizer.dynamic_energy_threshold = True

    def set_callback(self, callback):
        self.callback = callback

    def set_estado(self, estado):
        self.estado = estado
        print(f"[LISTENER] {estado}")

    def escuchar(self):

        mic = sr.Microphone()

        with mic as source:

            self.recognizer.adjust_for_ambient_noise(
                source,
                duration=1
            )

            print("Micrófono inicializado")

            while self.running:

                try:

                    self.set_estado(
                        "ESCUCHANDO"
                    )

                    audio = self.recognizer.listen(
                        source,
                        timeout=5,
                        phrase_time_limit=10
                    )

                    self.set_estado(
                        "PROCESANDO"
                    )

                    texto = self.recognizer.recognize_google(
                        audio,
                        language="es-MX"
                    )

                    texto = texto.lower()

                    print(
                        f"Usuario: {texto}"
                    )

                    if self.callback:
                        self.callback(texto)

                except sr.WaitTimeoutError:

                    self.set_estado(
                        "ESPERANDO"
                    )

                except sr.UnknownValueError:
                    pass

                except Exception as e:

                    print(
                        "Error:",
                        e
                    )

                    time.sleep(1)

    def iniciar(self):

        if self.running:
            return

        self.running = True

        hilo = threading.Thread(
            target=self.escuchar,
            daemon=True
        )

        hilo.start()

    def detener(self):

        self.running = False


class WakeWordDetector:

    def __init__(
        self,
        wake_word="jarvis"
    ):

        self.wake_word = wake_word

    def detectado(
        self,
        texto
    ):

        return (
            self.wake_word
            in texto.lower()
        )


if __name__ == "__main__":

    listener = Listener()

    detector = WakeWordDetector()

    def procesar(texto):

        if detector.detectado(texto):

            print(
                "JARVIS ACTIVADO"
            )

    listener.set_callback(
        procesar
    )

    listener.iniciar()

    while True:
        time.sleep(1)