import sys

from PySide6.QtWidgets import QApplication
from PySide6.QtCore import QTimer

from ui.hologram import Hologram

from core.listener import Listener
from core.speaker import Speaker
from core.wakeword import WakeWord
from core.brain import Brain

from automation.reminders import ReminderManager


class JarvisSystem:

    def __init__(self, window):

        self.window = window

        self.listener = Listener()

        self.speaker = Speaker()

        self.wakeword = WakeWord()

        self.brain = Brain()

        self.reminders = ReminderManager()

        # Conectar estados del holograma
        self.speaker.set_callback_estado(
            self.window.cambiar_estado
        )

        # Conectar escucha
        self.listener.set_callback(
            self.procesar_texto
        )

        # Recordatorios hablarán automáticamente
        self.reminders.set_callback(
            self.speaker.hablar
        )

    # ----------------------------------
    # INICIAR JARVIS
    # ----------------------------------

    def iniciar(self):

        self.window.cambiar_estado(
            "ESPERANDO"
        )

        self.reminders.iniciar()

        self.speaker.hablar(
            """
            Hola Isai.
            Sistema Jarvis iniciado.
            Todos los sistemas funcionando correctamente.
            """
        )

        self.listener.iniciar()

        print(
            "[JARVIS] Sistema iniciado"
        )

    # ----------------------------------
    # PROCESAR VOZ
    # ----------------------------------

    def procesar_texto(self, texto):

        if not texto:
            return

        print(
            f"[USUARIO] {texto}"
        )

        texto = texto.lower()

        # Debe contener Jarvis
        if not self.wakeword.detectar(texto):
            return

        self.window.cambiar_estado(
            "PROCESANDO"
        )

        try:

            respuesta = self.brain.procesar(
                texto
            )

            if respuesta:

                print(
                    f"[JARVIS] {respuesta}"
                )

                self.speaker.hablar(
                    respuesta
                )

        except Exception as e:

            print(
                "Error:",
                e
            )

            self.speaker.hablar(
                "Ha ocurrido un error."
            )

    # ----------------------------------
    # CERRAR
    # ----------------------------------

    def detener(self):

        try:

            self.reminders.detener()

        except:
            pass

        print(
            "[JARVIS] Sistema detenido"
        )


# ----------------------------------
# MAIN
# ----------------------------------

def main():

    app = QApplication(
        sys.argv
    )

    ventana = Hologram()

    ventana.show()

    jarvis = JarvisSystem(
        ventana
    )

    QTimer.singleShot(
        1000,
        jarvis.iniciar
    )

    exit_code = app.exec()

    jarvis.detener()

    sys.exit(
        exit_code
    )


if __name__ == "__main__":

    main()