import os
import shutil
import glob


class FileManager:

    def __init__(self):
        pass

    # --------------------------
    # CREAR ARCHIVO
    # --------------------------

    def crear_archivo(
        self,
        ruta
    ):

        try:

            with open(
                ruta,
                "w",
                encoding="utf-8"
            ):
                pass

            return True

        except Exception as e:

            print(e)

            return False

    # --------------------------
    # CREAR CARPETA
    # --------------------------

    def crear_carpeta(
        self,
        ruta
    ):

        try:

            os.makedirs(
                ruta,
                exist_ok=True
            )

            return True

        except Exception as e:

            print(e)

            return False

    # --------------------------
    # ELIMINAR ARCHIVO
    # --------------------------

    def eliminar_archivo(
        self,
        ruta
    ):

        try:

            if os.path.exists(ruta):

                os.remove(ruta)

                return True

            return False

        except Exception as e:

            print(e)

            return False

    # --------------------------
    # ELIMINAR CARPETA
    # --------------------------

    def eliminar_carpeta(
        self,
        ruta
    ):

        try:

            if os.path.exists(ruta):

                shutil.rmtree(ruta)

                return True

            return False

        except Exception as e:

            print(e)

            return False

    # --------------------------
    # RENOMBRAR
    # --------------------------

    def renombrar(
        self,
        origen,
        destino
    ):

        try:

            os.rename(
                origen,
                destino
            )

            return True

        except Exception as e:

            print(e)

            return False

    # --------------------------
    # COPIAR
    # --------------------------

    def copiar(
        self,
        origen,
        destino
    ):

        try:

            shutil.copy2(
                origen,
                destino
            )

            return True

        except Exception as e:

            print(e)

            return False

    # --------------------------
    # MOVER
    # --------------------------

    def mover(
        self,
        origen,
        destino
    ):

        try:

            shutil.move(
                origen,
                destino
            )

            return True

        except Exception as e:

            print(e)

            return False

    # --------------------------
    # LEER TXT
    # --------------------------

    def leer_archivo(
        self,
        ruta
    ):

        try:

            with open(
                ruta,
                "r",
                encoding="utf-8"
            ) as archivo:

                return archivo.read()

        except Exception as e:

            print(e)

            return None

    # --------------------------
    # ESCRIBIR TXT
    # --------------------------

    def escribir_archivo(
        self,
        ruta,
        contenido
    ):

        try:

            with open(
                ruta,
                "w",
                encoding="utf-8"
            ) as archivo:

                archivo.write(
                    contenido
                )

            return True

        except Exception as e:

            print(e)

            return False

    # --------------------------
    # AGREGAR TEXTO
    # --------------------------

    def agregar_texto(
        self,
        ruta,
        contenido
    ):

        try:

            with open(
                ruta,
                "a",
                encoding="utf-8"
            ) as archivo:

                archivo.write(
                    contenido
                )

            return True

        except Exception as e:

            print(e)

            return False

    # --------------------------
    # BUSCAR ARCHIVOS
    # --------------------------

    def buscar_archivos(
        self,
        carpeta,
        patron="*"
    ):

        try:

            archivos = glob.glob(
                os.path.join(
                    carpeta,
                    patron
                )
            )

            return archivos

        except Exception as e:

            print(e)

            return []

    # --------------------------
    # ABRIR ARCHIVO
    # --------------------------

    def abrir(
        self,
        ruta
    ):

        try:

            os.startfile(
                ruta
            )

            return True

        except Exception as e:

            print(e)

            return False

    # --------------------------
    # TAMAÑO
    # --------------------------

    def tamaño(
        self,
        ruta
    ):

        try:

            return os.path.getsize(
                ruta
            )

        except:

            return 0

    # --------------------------
    # EXISTE
    # --------------------------

    def existe(
        self,
        ruta
    ):

        return os.path.exists(
            ruta
        )


if __name__ == "__main__":

    archivos = FileManager()

    archivos.crear_carpeta(
        "Prueba"
    )

    archivos.crear_archivo(
        "Prueba/notas.txt"
    )

    archivos.escribir_archivo(
        "Prueba/notas.txt",
        "Hola soy Jarvis"
    )

    print(
        archivos.leer_archivo(
            "Prueba/notas.txt"
        )
    )

    print(
        archivos.buscar_archivos(
            "Prueba",
            "*.txt"
        )
    )