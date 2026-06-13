import os
import psutil
import subprocess


class AppManager:

    def __init__(self):

        self.apps = {

            "chrome":
            r"C:\Program Files\Google\Chrome\Application\chrome.exe",

            "edge":
            r"C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe",

            "vscode":
            r"C:\Users\isai\AppData\Local\Programs\Microsoft VS Code\Code.exe",

            "spotify":
            r"C:\Users\isai\AppData\Roaming\Spotify\Spotify.exe",

            "discord":
            r"C:\Users\isai\AppData\Local\Discord\Update.exe",

            "steam":
            r"C:\Program Files (x86)\Steam\Steam.exe",

            "notepad":
            "notepad.exe",

            "calculator":
            "calc.exe",

            "explorer":
            "explorer.exe",

            "cmd":
            "cmd.exe",

            "powershell":
            "powershell.exe"
        }

    # --------------------
    # ABRIR APP
    # --------------------

    def abrir(self, app):

        app = app.lower()

        if app not in self.apps:

            return False

        try:

            subprocess.Popen(
                self.apps[app]
            )

            return True

        except Exception as e:

            print(
                "Error:",
                e
            )

            return False

    # --------------------
    # CERRAR APP
    # --------------------

    def cerrar(self, proceso):

        proceso = proceso.lower()

        cerrados = 0

        for proc in psutil.process_iter(
            ['pid', 'name']
        ):

            try:

                nombre = (
                    proc.info['name']
                    .lower()
                )

                if proceso in nombre:

                    proc.kill()

                    cerrados += 1

            except:
                pass

        return cerrados

    # --------------------
    # VERIFICAR APP
    # --------------------

    def esta_abierta(
        self,
        proceso
    ):

        proceso = proceso.lower()

        for proc in psutil.process_iter(
            ['name']
        ):

            try:

                nombre = (
                    proc.info['name']
                    .lower()
                )

                if proceso in nombre:

                    return True

            except:
                pass

        return False

    # --------------------
    # LISTAR APPS
    # --------------------

    def listar_abiertas(self):

        apps = []

        for proc in psutil.process_iter(
            ['name']
        ):

            try:

                apps.append(
                    proc.info['name']
                )

            except:
                pass

        return sorted(
            set(apps)
        )

    # --------------------
    # REINICIAR APP
    # --------------------

    def reiniciar(
        self,
        nombre,
        proceso
    ):

        self.cerrar(
            proceso
        )

        return self.abrir(
            nombre
        )

    # --------------------
    # ABRIR URL
    # --------------------

    def abrir_url(
        self,
        url
    ):

        import webbrowser

        webbrowser.open(
            url
        )

    # --------------------
    # ABRIR CARPETA
    # --------------------

    def abrir_carpeta(
        self,
        ruta
    ):

        if os.path.exists(
            ruta
        ):

            os.startfile(
                ruta
            )

            return True

        return False


if __name__ == "__main__":

    manager = AppManager()

    print(
        "1. Abrir Chrome"
    )

    manager.abrir(
        "chrome"
    )

    print(
        "2. Verificar Chrome"
    )

    print(
        manager.esta_abierta(
            "chrome"
        )
    )

    print(
        "3. Aplicaciones abiertas"
    )

    for app in manager.listar_abiertas()[:20]:

        print(app)