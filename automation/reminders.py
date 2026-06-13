import sqlite3
import threading
import time
from datetime import datetime


class ReminderManager:

    def __init__(self):

        self.db = "database/memory.db"

        self.crear_tabla()

        self.running = False

        self.callback = None

    # -------------------------
    # TABLA
    # -------------------------

    def crear_tabla(self):

        conn = sqlite3.connect(
            self.db
        )

        cursor = conn.cursor()

        cursor.execute("""
        CREATE TABLE IF NOT EXISTS reminders(

            id INTEGER PRIMARY KEY AUTOINCREMENT,

            titulo TEXT,

            fecha TEXT,

            ejecutado INTEGER DEFAULT 0

        )
        """)

        conn.commit()
        conn.close()

    # -------------------------
    # CALLBACK
    # -------------------------

    def set_callback(
        self,
        callback
    ):

        self.callback = callback

    # -------------------------
    # AGREGAR
    # -------------------------

    def agregar(
        self,
        titulo,
        fecha
    ):

        conn = sqlite3.connect(
            self.db
        )

        cursor = conn.cursor()

        cursor.execute(
            """
            INSERT INTO reminders(
                titulo,
                fecha
            )
            VALUES(?,?)
            """,
            (
                titulo,
                fecha
            )
        )

        conn.commit()
        conn.close()

    # -------------------------
    # LISTAR
    # -------------------------

    def listar(self):

        conn = sqlite3.connect(
            self.db
        )

        cursor = conn.cursor()

        cursor.execute("""
        SELECT *
        FROM reminders
        ORDER BY fecha
        """)

        datos = cursor.fetchall()

        conn.close()

        return datos

    # -------------------------
    # ELIMINAR
    # -------------------------

    def eliminar(
        self,
        reminder_id
    ):

        conn = sqlite3.connect(
            self.db
        )

        cursor = conn.cursor()

        cursor.execute(
            """
            DELETE FROM reminders
            WHERE id=?
            """,
            (
                reminder_id,
            )
        )

        conn.commit()
        conn.close()

    # -------------------------
    # VERIFICAR
    # -------------------------

    def verificar(self):

        while self.running:

            ahora = datetime.now()

            conn = sqlite3.connect(
                self.db
            )

            cursor = conn.cursor()

            cursor.execute("""
            SELECT
                id,
                titulo,
                fecha
            FROM reminders
            WHERE ejecutado=0
            """)

            datos = cursor.fetchall()

            for rid, titulo, fecha in datos:

                try:

                    fecha_recordatorio = (
                        datetime.strptime(
                            fecha,
                            "%Y-%m-%d %H:%M"
                        )
                    )

                    if ahora >= fecha_recordatorio:

                        cursor.execute(
                            """
                            UPDATE reminders
                            SET ejecutado=1
                            WHERE id=?
                            """,
                            (
                                rid,
                            )
                        )

                        conn.commit()

                        mensaje = (
                            f"Recordatorio: {titulo}"
                        )

                        print(
                            mensaje
                        )

                        if self.callback:

                            self.callback(
                                mensaje
                            )

                except Exception as e:

                    print(
                        e
                    )

            conn.close()

            time.sleep(10)

    # -------------------------
    # INICIAR
    # -------------------------

    def iniciar(self):

        if self.running:
            return

        self.running = True

        hilo = threading.Thread(
            target=self.verificar,
            daemon=True
        )

        hilo.start()

    # -------------------------
    # DETENER
    # -------------------------

    def detener(self):

        self.running = False


if __name__ == "__main__":

    reminders = ReminderManager()

    reminders.agregar(
        "Tomar agua",
        "2026-06-12 20:00"
    )

    print(
        reminders.listar()
    )

    reminders.iniciar()

    while True:
        pass