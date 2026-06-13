import os
import webbrowser
import subprocess
from datetime import datetime


class Commands:

    def __init__(self):

        self.apps = {

            "chrome":
            r"C:\Program Files\Google\Chrome\Application\chrome.exe",

            "vscode":
            r"C:\Users\isai\AppData\Local\Programs\Microsoft VS Code\Code.exe",

            "spotify":
            r"C:\Users\isai\AppData\Roaming\Spotify\Spotify.exe",

            "discord":
            r"C:\Users\isai\AppData\Local\Discord\Update.exe"
        }

    def ejecutar(self, texto):

        texto = texto.lower()

        # -------------------------
        # HORA
        # -------------------------

        if "hora" in texto:

            hora = datetime.now().strftime(
                "%H:%M"
            )

            return f"Son las {hora}"

        # -------------------------
        # CHROME
        # -------------------------

        if "abre chrome" in texto:

            self.abrir_chrome()

            return "Abriendo Google Chrome"

        # -------------------------
        # VSCODE
        # -------------------------

        if (
            "abre visual studio code"
            in texto
            or
            "abre vscode"
            in texto
        ):

            self.abrir_vscode()

            return "Abriendo Visual Studio Code"

        # -------------------------
        # SPOTIFY
        # -------------------------

        if "abre spotify" in texto:

            self.abrir_spotify()

            return "Abriendo Spotify"

        # -------------------------
        # DISCORD
        # -------------------------

        if "abre discord" in texto:

            self.abrir_discord()

            return "Abriendo Discord"

        # -------------------------
        # YOUTUBE
        # -------------------------

        if "abre youtube" in texto:

            webbrowser.open(
                "https://youtube.com"
            )

            return "Abriendo YouTube"

        # -------------------------
        # GOOGLE
        # -------------------------

        if "abre google" in texto:

            webbrowser.open(
                "https://google.com"
            )

            return "Abriendo Google"

        # -------------------------
        # CHATGPT
        # -------------------------

        if "abre chatgpt" in texto:

            webbrowser.open(
                "https://chatgpt.com"
            )

            return "Abriendo ChatGPT"

        # -------------------------
        # BLOQUEAR PC
        # -------------------------

        if "bloquea la computadora" in texto:

            os.system(
                "rundll32.exe user32.dll,LockWorkStation"
            )

            return "Bloqueando equipo"

        # -------------------------
        # APAGAR
        # -------------------------

        if "apaga la computadora" in texto:

            os.system(
                "shutdown /s /t 5"
            )

            return "Apagando equipo"

        # -------------------------
        # REINICIAR
        # -------------------------

        if "reinicia la computadora" in texto:

            os.system(
                "shutdown /r /t 5"
            )

            return "Reiniciando equipo"

        # -------------------------
        # CARPETA
        # -------------------------

        if "crear carpeta" in texto:

            nombre = self.extraer_nombre(
                texto,
                "crear carpeta"
            )

            if nombre:

                os.makedirs(
                    nombre,
                    exist_ok=True
                )

                return (
                    f"Carpeta {nombre} creada"
                )

        # -------------------------
        # ARCHIVO
        # -------------------------

        if "crear archivo" in texto:

            nombre = self.extraer_nombre(
                texto,
                "crear archivo"
            )

            if nombre:

                with open(
                    nombre,
                    "w",
                    encoding="utf-8"
                ) as f:

                    f.write("")

                return (
                    f"Archivo {nombre} creado"
                )

        # -------------------------
        # BUSCAR
        # -------------------------

        if "buscar" in texto:

            consulta = texto.replace(
                "buscar",
                ""
            )

            webbrowser.open(
                f"https://www.google.com/search?q={consulta}"
            )

            return (
                f"Buscando {consulta}"
            )

        return None

    def abrir_chrome(self):

        ruta = self.apps.get(
            "chrome"
        )

        if os.path.exists(ruta):

            subprocess.Popen(
                [ruta]
            )

    def abrir_vscode(self):

        ruta = self.apps.get(
            "vscode"
        )

        if os.path.exists(ruta):

            subprocess.Popen(
                [ruta]
            )

    def abrir_spotify(self):

        ruta = self.apps.get(
            "spotify"
        )

        if os.path.exists(ruta):

            subprocess.Popen(
                [ruta]
            )

    def abrir_discord(self):

        ruta = self.apps.get(
            "discord"
        )

        if os.path.exists(ruta):

            subprocess.Popen(
                [ruta]
            )

    def extraer_nombre(
        self,
        texto,
        comando
    ):

        nombre = texto.replace(
            comando,
            ""
        )

        nombre = nombre.strip()

        return nombre


if __name__ == "__main__":

    jarvis = Commands()

    while True:

        cmd = input(
            "Comando: "
        )

        respuesta = jarvis.ejecutar(
            cmd
        )

        print(
            "Respuesta:",
            respuesta
        )