from core.commands import Commands

from datetime import datetime
import random
import psutil


class Brain:

    def __init__(self):

        self.commands = Commands()

        self.nombre_usuario = "Isai"

        self.memoria = []

        self.datos = {}

        self.chistes = [

            "¿Por qué los programadores prefieren el modo oscuro? Porque la luz atrae bugs.",

            "Hay 10 tipos de personas. Las que entienden binario y las que no.",

            "Mi código funciona perfectamente. No sé por qué.",

            "Un programador entra a un bar y pide 1 cerveza, luego 10, luego 11 y luego 100.",

            "Error 404. Chiste no encontrado."

        ]

    # ----------------------------------
    # MEMORIA
    # ----------------------------------

    def guardar_memoria(
        self,
        usuario,
        respuesta
    ):

        self.memoria.append({

            "usuario": usuario,
            "respuesta": respuesta

        })

        if len(self.memoria) > 100:

            self.memoria.pop(0)

    # ----------------------------------
    # PROCESAR
    # ----------------------------------

    def procesar(
        self,
        texto
    ):

        texto = texto.lower().strip()

        # -----------------------
        # RECORDAR COSAS
        # -----------------------

        if texto.startswith(
            "recuerda que"
        ):

            dato = texto.replace(
                "recuerda que",
                ""
            ).strip()

            self.datos["nota"] = dato

            return (
                "Entendido señor. Lo recordaré."
            )

        if (
            "que recuerdas" in texto
            or
            "qué recuerdas" in texto
        ):

            return self.datos.get(
                "nota",
                "No tengo nada guardado."
            )

        # -----------------------
        # COMANDOS DEL SISTEMA
        # -----------------------

        respuesta = self.commands.ejecutar(
            texto
        )

        if respuesta:

            self.guardar_memoria(
                texto,
                respuesta
            )

            return respuesta

        # -----------------------
        # RESPUESTAS LOCALES
        # -----------------------

        respuesta = self.respuestas_locales(
            texto
        )

        if respuesta:

            self.guardar_memoria(
                texto,
                respuesta
            )

            return respuesta

        return (
            "Lo siento señor. Todavía no sé cómo realizar esa tarea."
        )

    # ----------------------------------
    # RESPUESTAS LOCALES
    # ----------------------------------

    def respuestas_locales(
        self,
        texto
    ):

        # SALUDOS

        if "hola" in texto:

            return (
                f"Hola {self.nombre_usuario}. ¿En qué puedo ayudarle?"
            )

        if (
            "como estas" in texto
            or
            "cómo estás" in texto
        ):

            return (
                "Todos mis sistemas funcionan correctamente."
            )

        if (
            "quien eres" in texto
            or
            "quién eres" in texto
        ):

            return (
                "Soy Jarvis. Su asistente virtual."
            )

        if "gracias" in texto:

            return (
                "Siempre a sus órdenes."
            )

        if (
            "adios" in texto
            or
            "adiós" in texto
        ):

            return (
                "Hasta luego señor."
            )

        if "tu nombre" in texto:

            return (
                "Mi nombre es Jarvis."
            )

        if "mi nombre" in texto:

            return (
                f"Su nombre es {self.nombre_usuario}."
            )

        if "quien te creo" in texto:

            return (
                "Fui desarrollado por Isai Reyes."
            )

        # FECHA Y HORA

        if "hora" in texto:

            return (
                datetime.now().strftime(
                    "La hora actual es %H:%M:%S"
                )
            )

        if "fecha" in texto:

            return (
                datetime.now().strftime(
                    "Hoy es %d de %B de %Y"
                )
            )

        if "dia" in texto:

            return (
                datetime.now().strftime(
                    "Hoy es %A"
                )
            )

        # SISTEMA

        if (
            "estado del sistema" in texto
            or
            "estado de la computadora" in texto
        ):

            cpu = psutil.cpu_percent()

            ram = psutil.virtual_memory().percent

            return (
                f"CPU al {cpu} por ciento. "
                f"RAM al {ram} por ciento. "
                f"Todos los sistemas operativos."
            )

        if "cpu" in texto:

            return (
                f"El procesador está al "
                f"{psutil.cpu_percent()} por ciento."
            )

        if "ram" in texto:

            return (
                f"La memoria RAM está al "
                f"{psutil.virtual_memory().percent} por ciento."
            )

        if "bateria" in texto:

            bateria = psutil.sensors_battery()

            if bateria:

                return (
                    f"La batería está al "
                    f"{bateria.percent} por ciento."
                )

            return (
                "No pude obtener información de la batería."
            )

        # MODOS JARVIS

        if "modo iron man" in texto:

            return (
                "Activando protocolo Stark."
            )

        if "activar protocolo jarvis" in texto:

            return (
                "Protocolo Jarvis activado."
            )

        if "activar protocolo defensa" in texto:

            return (
                "Protocolos defensivos activados."
            )

        if "analiza sistema" in texto:

            return (
                "Análisis completado. No se detectan amenazas."
            )

        if "estado de seguridad" in texto:

            return (
                "Todos los sistemas se encuentran seguros."
            )

        if "informe completo" in texto:

            cpu = psutil.cpu_percent()

            ram = psutil.virtual_memory().percent

            return (
                f"Informe del sistema. "
                f"CPU {cpu} por ciento. "
                f"RAM {ram} por ciento. "
                f"No se detectan errores."
            )

        # CHISTES

        if (
            "cuentame un chiste" in texto
            or
            "cuéntame un chiste" in texto
        ):

            return random.choice(
                self.chistes
            )

        # FRASES JARVIS

        if "sorprendeme" in texto:

            frases = [

                "La tecnología es mejor cuando acerca a las personas.",

                "Todo gran sistema comienza con una idea.",

                "La disciplina supera a la motivación.",

                "El conocimiento es poder.",

                "Bienvenido señor."
            ]

            return random.choice(
                frases
            )

        if "objetivo" in texto:

            return (
                "Mi objetivo es asistirle en todas sus tareas."
            )

        if "estas ahi" in texto:

            return (
                "Siempre estoy aquí señor."
            )

        if "jarvis" == texto:

            return (
                "Sí señor."
            )

        return None

    # ----------------------------------
    # CAMBIAR NOMBRE
    # ----------------------------------

    def cambiar_usuario(
        self,
        nombre
    ):

        self.nombre_usuario = nombre

    # ----------------------------------
    # HISTORIAL
    # ----------------------------------

    def historial(self):

        return self.memoria


if __name__ == "__main__":

    brain = Brain()

    while True:

        texto = input(
            "Tú: "
        )

        respuesta = brain.procesar(
            texto
        )

        print(
            "Jarvis:",
            respuesta
        )