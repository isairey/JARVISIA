import time


class WakeWord:

    def __init__(self):

        self.wake_words = [
            "jarvis",
            "hey jarvis",
            "hola jarvis"
        ]

        self.last_activation = 0

        self.cooldown = 2

    def detectar(self, texto):

        if not texto:
            return False

        texto = texto.lower().strip()

        ahora = time.time()

        if (
            ahora - self.last_activation
            < self.cooldown
        ):
            return False

        for palabra in self.wake_words:

            if palabra in texto:

                self.last_activation = ahora

                return True

        return False

    def agregar_wakeword(
        self,
        palabra
    ):

        palabra = palabra.lower()

        if palabra not in self.wake_words:

            self.wake_words.append(
                palabra
            )

    def eliminar_wakeword(
        self,
        palabra
    ):

        palabra = palabra.lower()

        if palabra in self.wake_words:

            self.wake_words.remove(
                palabra
            )

    def obtener_wakewords(self):

        return self.wake_words


class JarvisActivation:

    def __init__(self):

        self.activado = False

        self.ultimo_comando = ""

    def activar(self):

        self.activado = True

        print(
            "[JARVIS] ACTIVADO"
        )

    def desactivar(self):

        self.activado = False

        print(
            "[JARVIS] ESPERANDO"
        )

    def esta_activo(self):

        return self.activado

    def guardar_comando(
        self,
        comando
    ):

        self.ultimo_comando = comando

    def obtener_comando(self):

        return self.ultimo_comando


if __name__ == "__main__":

    wakeword = WakeWord()

    while True:

        texto = input(
            "Habla: "
        )

        if wakeword.detectar(
            texto
        ):

            print(
                "JARVIS ACTIVADO"
            )

        else:

            print(
                "Sin activación"
            )