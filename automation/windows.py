import os
import ctypes
import pyautogui
import subprocess

from ctypes import POINTER, cast
from comtypes import CLSCTX_ALL

from pycaw.pycaw import (
    AudioUtilities,
    IAudioEndpointVolume
)


class WindowsManager:

    def __init__(self):

        self.volume = self.obtener_control_volumen()

    # ----------------------------------
    # APAGAR
    # ----------------------------------

    def apagar(self, segundos=5):

        os.system(
            f"shutdown /s /t {segundos}"
        )

    # ----------------------------------
    # REINICIAR
    # ----------------------------------

    def reiniciar(self, segundos=5):

        os.system(
            f"shutdown /r /t {segundos}"
        )

    # ----------------------------------
    # CANCELAR APAGADO
    # ----------------------------------

    def cancelar_apagado(self):

        os.system(
            "shutdown /a"
        )

    # ----------------------------------
    # BLOQUEAR
    # ----------------------------------

    def bloquear(self):

        ctypes.windll.user32.LockWorkStation()

    # ----------------------------------
    # CERRAR SESION
    # ----------------------------------

    def cerrar_sesion(self):

        os.system(
            "shutdown /l"
        )

    # ----------------------------------
    # SUSPENDER
    # ----------------------------------

    def suspender(self):

        os.system(
            "rundll32.exe powrprof.dll,SetSuspendState 0,1,0"
        )

    # ----------------------------------
    # HIBERNAR
    # ----------------------------------

    def hibernar(self):

        os.system(
            "shutdown /h"
        )

    # ----------------------------------
    # ESCRITORIO
    # ----------------------------------

    def mostrar_escritorio(self):

        pyautogui.hotkey(
            "win",
            "d"
        )

    # ----------------------------------
    # MINIMIZAR TODO
    # ----------------------------------

    def minimizar_todo(self):

        pyautogui.hotkey(
            "win",
            "m"
        )

    # ----------------------------------
    # CAPTURA
    # ----------------------------------

    def captura(
        self,
        archivo="captura.png"
    ):

        imagen = pyautogui.screenshot()

        imagen.save(
            archivo
        )

        return archivo

    # ----------------------------------
    # EXPLORADOR
    # ----------------------------------

    def abrir_explorador(self):

        subprocess.Popen(
            "explorer.exe"
        )

    # ----------------------------------
    # ADMINISTRADOR TAREAS
    # ----------------------------------

    def abrir_taskmanager(self):

        subprocess.Popen(
            "taskmgr.exe"
        )

    # ----------------------------------
    # CMD
    # ----------------------------------

    def abrir_cmd(self):

        subprocess.Popen(
            "cmd.exe"
        )

    # ----------------------------------
    # POWERSHELL
    # ----------------------------------

    def abrir_powershell(self):

        subprocess.Popen(
            "powershell.exe"
        )

    # ----------------------------------
    # VOLUMEN
    # ----------------------------------

    def obtener_control_volumen(self):

        try:

            devices = (
                AudioUtilities.GetSpeakers()
            )

            interface = devices.Activate(
                IAudioEndpointVolume._iid_,
                CLSCTX_ALL,
                None
            )

            return cast(
                interface,
                POINTER(
                    IAudioEndpointVolume
                )
            )

        except:

            return None

    # ----------------------------------
    # VOLUMEN %
    # ----------------------------------

    def volumen_actual(self):

        if not self.volume:
            return 0

        rango = (
            self.volume.GetVolumeRange()
        )

        actual = (
            self.volume.GetMasterVolumeLevel()
        )

        minimo = rango[0]
        maximo = rango[1]

        porcentaje = int(
            (
                (actual - minimo)
                /
                (maximo - minimo)
            ) * 100
        )

        return porcentaje

    # ----------------------------------
    # SUBIR
    # ----------------------------------

    def subir_volumen(
        self,
        pasos=5
    ):

        for _ in range(pasos):

            pyautogui.press(
                "volumeup"
            )

    # ----------------------------------
    # BAJAR
    # ----------------------------------

    def bajar_volumen(
        self,
        pasos=5
    ):

        for _ in range(pasos):

            pyautogui.press(
                "volumedown"
            )

    # ----------------------------------
    # SILENCIAR
    # ----------------------------------

    def mutear(self):

        pyautogui.press(
            "volumemute"
        )

    # ----------------------------------
    # VENTANA ACTIVA
    # ----------------------------------

    def ventana_activa(self):

        try:

            import win32gui

            hwnd = (
                win32gui.GetForegroundWindow()
            )

            return (
                win32gui.GetWindowText(
                    hwnd
                )
            )

        except:

            return "Desconocida"


if __name__ == "__main__":

    win = WindowsManager()

    print(
        "Ventana activa:"
    )

    print(
        win.ventana_activa()
    )

    print(
        "Volumen:"
    )

    print(
        win.volumen_actual()
    )

    win.captura(
        "prueba.png"
    )

    print(
        "Captura guardada."
    )