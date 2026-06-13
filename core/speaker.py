import asyncio
import edge_tts
import tempfile
import os
import threading
from playsound import playsound


class Speaker:

    def __init__(self):

        self.voice = "es-MX-JorgeNeural"

        self.estado = "ESPERANDO"

        self.hablando = False

        self.callback_estado = None

    def set_callback_estado(
        self,
        callback
    ):
        self.callback_estado = callback

    def cambiar_estado(
        self,
        estado
    ):

        self.estado = estado

        if self.callback_estado:
            self.callback_estado(
                estado
            )

    async def generar_audio(
        self,
        texto,
        archivo
    ):

        communicate = edge_tts.Communicate(
            texto,
            self.voice,
            rate="-6%",
            pitch="-2Hz"
        )

        await communicate.save(
            archivo
        )

    def reproducir(
        self,
        texto
    ):

        try:

            self.hablando = True

            self.cambiar_estado(
                "HABLANDO"
            )

            with tempfile.NamedTemporaryFile(
                delete=False,
                suffix=".mp3"
            ) as temp:

                archivo = temp.name

            asyncio.run(
                self.generar_audio(
                    texto,
                    archivo
                )
            )

            playsound(archivo)

            os.remove(
                archivo
            )

        except Exception as e:

            print(
                "Error Speaker:",
                e
            )

        finally:

            self.hablando = False

            self.cambiar_estado(
                "ESPERANDO"
            )

    def hablar(
        self,
        texto
    ):

        hilo = threading.Thread(
            target=self.reproducir,
            args=(texto,),
            daemon=True
        )

        hilo.start()


if __name__ == "__main__":

    speaker = Speaker()

    speaker.hablar(
        """
        Hola Isai.
        Sistema Jarvis iniciado.
        Todos los sistemas operativos.
        Funcionando correctamente.
        """
    )

    input(
        "Presiona Enter para salir..."
    )