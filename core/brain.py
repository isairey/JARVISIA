from core.commands import Commands

from datetime import datetime
import random
import psutil
import re
import webbrowser
import subprocess
import platform
import os


class Brain:

    def __init__(self):

        self.commands = Commands()

        self.nombre_usuario = "Isai"

        self.memoria = []

        self.datos = {}

        # Diccionario para múltiples notas
        self.notas = {}

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

    def guardar_memoria(self, usuario, respuesta):

        self.memoria.append({

            "usuario": usuario,
            "respuesta": respuesta,
            "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        })

        if len(self.memoria) > 100:

            self.memoria.pop(0)

    # ----------------------------------
    # GUARDAR NOTA
    # ----------------------------------

    def guardar_nota(self, titulo, contenido):

        num_nota = len(self.notas) + 1
        clave = f"nota_{num_nota}"

        self.notas[clave] = {

            "titulo": titulo,
            "contenido": contenido,
            "fecha": datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        }

        self.guardar_memoria(f"Recordatorio: {titulo}", contenido)

        return num_nota

    # ----------------------------------
    # OBTENER NOTAS
    # ----------------------------------

    def obtener_notas(self):

        if not self.notas:

            return "No tengo ningún recordatorio guardado, señor."

        resultado = "Mis recordatorios:\n"

        for clave, nota in self.notas.items():

            resultado += f"• [{clave}] {nota['titulo']}: {nota['contenido']}\n"

        return resultado

    # ----------------------------------
    # HERRAMIENTAS: Captura de pantalla
    # ----------------------------------

    def tomar_captura(self):

        sistema = platform.system()

        try:

            if sistema == "Windows":

                # Usar Pillow para captura
                from PIL import ImageGrab
                imagen = ImageGrab.grab()
                
                nombre = f"captura_{datetime.now().strftime('%Y%m%d_%H%M%S')}.png"
                imagen.save(nombre)
                
                return f"Captura de pantalla guardada como {nombre}"

            elif sistema == "Darwin":  # macOS

                import os
                nombre = f"captura_{datetime.now().strftime('%Y%m%d_%H%M%S')}.png"
                os.system(f"screencapture -x {nombre}")
                
                return f"Captura de pantalla guardada, señor."

            elif sistema == "Linux":

                import os
                nombre = f"captura_{datetime.now().strftime('%Y%m%d_%H%M%S')}.png"
                os.system(f"gnome-screenshot -f {nombre}")
                
                return f"Captura guardada, señor."

        except Exception as e:

            return f"No pude tomar la captura. Error: {str(e)}"

        return "Captura de pantalla no disponible en este sistema."

    # ----------------------------------
    # HERRAMIENTAS: Abrir cámara
    # ----------------------------------

        # ----------------------------------
    # HERRAMIENTAS: Abrir cámara
    # ----------------------------------

        # ----------------------------------
    # HERRAMIENTAS: Abrir cámara
    # ----------------------------------

    def tomar_foto(self):

        sistema = platform.system()

        print(f"[DEBUG] Sistema: {sistema}")

        try:

            if sistema == "Windows":

                # Método 1: Intentar abrir la app de cámara de Windows
                import subprocess
                import os

                # Opción 1: Usar el protocolo URI de Windows
                try:
                    os.startfile("microsoft.windowscamera:")
                    print("[DEBUG] Abriendo cámara con os.startfile")
                    return "Abriendo cámara de Windows, señor."
                except:
                    pass

                # Opción 2: Usar PowerShell
                try:
                    subprocess.Popen(
                        ["start", "microsoft.windowscamera:"],
                        shell=True,
                        stdout=subprocess.PIPE,
                        stderr=subprocess.PIPE
                    )
                    print("[DEBUG] Abriendo cámara con subprocess")
                    return "Abriendo cámara, señor."
                except Exception as e:
                    print(f"[ERROR subprocess]: {e}")

                # Opción 3: Intentar con opencv para verificar si hay cámara
                try:
                    import cv2
                    cap = cv2.VideoCapture(0)
                    if cap.isOpened():
                        cap.release()
                        # Si hay cámara pero no se abre, intentar otro método
                        subprocess.Popen(
                            ["cmd", "/c", "start", "", "microsoft.windowscamera:"],
                            shell=True
                        )
                        return "Abriendo cámara, señor."
                except:
                    pass

                # Si todo falla, abrir Google Meet como alternativa
                webbrowser.open("https://meet.google.com/new")
                return "Abriendo Google Meet para usar la cámara.在那 puede probar la cámara, señor."

            elif sistema == "Darwin":  # macOS

                import os
                os.system("open -a Photo Booth")
                return "Abriendo Photo Booth, señor."

            elif sistema == "Linux":

                import os
                os.system("cheese &")
                return "Abriendo Cheese, señor."

        except Exception as e:

            print(f"[ERROR cámara]: {e}")
            return f"Tuve un problema para abrir la cámara: {str(e)}"

        return "No pude detectar una cámara en este dispositivo."

    # ----------------------------------
    # HERRAMIENTAS: Velocidad de internet
    # ----------------------------------

    def velocidad_internet(self):

        try:

            # Abrir test de velocidad en navegador
            webbrowser.open("https://speedtest.net")
            
            return "Abriendo test de velocidad de internet. Puede realizar la prueba, señor."

        except Exception as e:

            return f"No pude abrir el test. Error: {str(e)}"

    # ----------------------------------
    # UBICACIÓN: Dónde estoy
    # ----------------------------------

    def donde_estoy(self):

        try:

            # Abrir Google Maps con ubicación actual
            webbrowser.open("https://www.google.com/maps")
            
            return "Abriendo Google Maps. Su ubicación se mostrará ahí, señor."

        except Exception as e:

            return f"No pude obtener su ubicación. Error: {str(e)}"

    # ----------------------------------
    # UBICACIÓN: Buscar cerca de
    # ----------------------------------

    def buscar_cerca(self, lugar):

        try:

            # Buscar lugares cercanos
            busqueda = lugar.replace(" ", "+")
            url = f"https://www.google.com/maps/search/{busqueda}+cerca+de+mi"
            webbrowser.open(url)
            
            return f"Buscando {lugar} cerca de usted, señor."

        except Exception as e:

            return f"No pude realizar la búsqueda. Error: {str(e)}"

    # ----------------------------------
    # COMUNICACIÓN: Correo
    # ----------------------------------

    def enviar_correo(self, destinatario):

        try:

            # Abrir Gmail con-compose
            url = f"https://mail.google.com/mail/?view=cm&to={destinatario}"
            webbrowser.open(url)
            
            return f"Abriendo Gmail para enviar correo a {destinatario}, señor."

        except Exception as e:

            return f"No pude abrir el correo. Error: {str(e)}"

    # ----------------------------------
    # COMUNICACIÓN: WhatsApp
    # ----------------------------------

    def enviar_whatsapp(self, contacto):

        try:

            # Abrir WhatsApp Web
            webbrowser.open("https://web.whatsapp.com")
            
            return f"Abriendo WhatsApp Web para enviar mensaje a {contacto}. Puede escribir su mensaje ahí, señor."

        except Exception as e:

            return f"No pude abrir WhatsApp. Error: {str(e)}"

    # ----------------------------------
    # PROCESAR
    # ----------------------------------

    def procesar(self, texto):

        # Limpiar el texto
        texto = texto.lower().strip()
        texto = re.sub(r'\s+', ' ', texto)

        # Eliminar "jarvis" del inicio
        if texto.startswith("jarvis"):
            texto = texto.replace("jarvis", "", 1).strip()

        print(f"[DEBUG] Procesando: '{texto}'")

        # -----------------------
        # RECORDAR
        # -----------------------

        if texto.startswith("recuerda que") or texto.startswith("recuerda "):

            if "recuerda" in texto and "que" in texto:

                contenido = texto.replace("recuerda que", "").strip()

                if contenido:

                    titulo = f"Nota {len(self.notas) + 1}"

                    num_nota = self.guardar_nota(titulo, contenido)

                    return f"Entendido señor. Lo recordaré: '{contenido}' (Nota #{num_nota})"

        # -----------------------
        # VER RECORDATORIOS
        # -----------------------

        if any(palabra in texto for palabra in ["recuerdas", "qué recuerdas", "que recuerdas", "ver recordatorios", "mis recordatorios"]):

            return self.obtener_notas()

        # -----------------------
        # ELIMINAR NOTA
        # -----------------------

        if any(palabra in texto for palabra in ["olvida", "borra", "elimina"]):

            if any(palabra in texto for palabra in ["recordatorio", "nota"]):

                numeros = re.findall(r'\d+', texto)

                if numeros:

                    clave = f"nota_{numeros[0]}"

                    if clave in self.notas:

                        titulo = self.notas[clave]['titulo']
                        del self.notas[clave]

                        return f"Recordatorio '{titulo}' eliminado."

                if "todas" in texto or "todo" in texto:

                    cantidad = len(self.notas)
                    self.notas = {}

                    return f"Se eliminaron {cantidad} recordatorios."

                return "No entendí cuál recordatorio desea eliminar."

        # -----------------------
        # COMANDOS DEL SISTEMA
        # -----------------------

        respuesta = self.commands.ejecutar(texto)

        if respuesta:

            self.guardar_memoria(texto, respuesta)

            return respuesta

        # -----------------------
        # RESPUESTAS LOCALES
        # -----------------------

        respuesta = self.respuestas_locales(texto)

        if respuesta:

            self.guardar_memoria(texto, respuesta)

            return respuesta

        return "Lo siento señor. Todavía no sé cómo realizar esa tarea."

    # ----------------------------------
    # RESPUESTAS LOCALES
    # ----------------------------------

    def respuestas_locales(self, texto):

        # ===== SALUDOS =====

        if "hola" in texto:

            return f"Hola {self.nombre_usuario}. ¿En qué puedo ayudarle?"

        if any(palabra in texto for palabra in ["cómo estás", "como estas"]):

            return "Todos mis sistemas funcionan correctamente, señor."

        if any(palabra in texto for palabra in ["quién eres", "quien eres"]):

            return "Soy JARVIS. Su asistente virtual de inteligencia artificial."

        if "gracias" in texto:

            return "Siempre a sus órdenes, señor."

        if any(palabra in texto for palabra in ["adiós", "adios"]):

            return "Hasta luego, señor."

        if "tu nombre" in texto:

            return "Mi nombre es JARVIS."

        if "mi nombre" in texto:

            return f"Señor, su nombre es {self.nombre_usuario}."

        if any(palabra in texto for palabra in ["quién te creó", "quien te creo"]):

            return "Fui desarrollado por Isai Reyes."

        # ===== FECHA Y HORA =====

        if "hora" in texto:

            return datetime.now().strftime("La hora actual es %H:%M:%S, señor.")

        if "fecha" in texto:

            return datetime.now().strftime("Hoy es %d de %B de %Y")

        if any(palabra in texto for palabra in ["día", "dia"]):

            return datetime.now().strftime("Hoy es %A, señor.")

        # ===== ESTADO DEL SISTEMA =====

        if any(palabra in texto for palabra in ["estado del sistema", "estado de la computadora"]):

            cpu = psutil.cpu_percent()
            ram = psutil.virtual_memory().percent

            return f"CPU al {cpu} por ciento. RAM al {ram} por ciento. Todos los sistemas operativos, señor."

        if "cpu" in texto:

            return f"El procesador está al {psutil.cpu_percent()} por ciento, señor."

        if "ram" in texto:

            return f"La memoria RAM está al {psutil.virtual_memory().percent} por ciento, señor."

        if "batería" in texto or "bateria" in texto:

            bateria = psutil.sensors_battery()

            if bateria:

                return f"La batería está al {bateria.percent} por ciento."

            return "No pude obtener información de la batería, señor."

        # ===== MODOS JARVIS =====

        if "modo iron man" in texto:

            return "Activando protocolo Stark. Bienvenido, señor."

        if "activar protocolo jarvis" in texto:

            return "Protocolo JARVIS activado."

        if "activar protocolo defensa" in texto:

            return "Protocolos defensivos activados, señor."

        if "analiza sistema" in texto:

            return "Análisis completado. No se detectan amenazas."

        if "estado de seguridad" in texto:

            return "Todos los sistemas se encuentran seguros, señor."

        if "informe completo" in texto:

            cpu = psutil.cpu_percent()
            ram = psutil.virtual_memory().percent

            return f"Informe del sistema. CPU {cpu} por ciento. RAM {ram} por ciento. No se detectan errores."

        # ===== HERRAMIENTAS =====

        if any(palabra in texto for palabra in ["captura", "pantalla"]):

            if "tomar" in texto or "haz" in texto:

                return self.tomar_captura()

        if any(palabra in texto for palabra in ["foto", "cámara", "camara"]) and "tomar" in texto:

            return self.tomar_foto()

        if any(palabra in texto for palabra in ["velocidad", "speedtest"]) and "internet" in texto:

            return self.velocidad_internet()

        # ===== UBICACIÓN =====

        if any(palabra in texto for palabra in ["dónde estoy", "donde estoy", "mi ubicación"]):

            return self.donde_estoy()

        if "busca" in texto and "cerca" in texto:

            # Extraer qué buscar
            buscar = texto.replace("busca", "").replace("cerca", "").strip()
            
            if buscar:

                return self.buscar_cerca(buscar)

            return "No entendí qué desea buscar. Intente: 'jarvis buscacafés cerca de mí'"

        # ===== COMUNICACIÓN =====

        if "correo" in texto and any(palabra in texto for palabra in ["envía", "mandar", "enviar"]):

            import re
            match = re.search(r'(?:a|para)\s+(\S+@\S+|[\w]+)', texto)

            if match:
                destinatario = match.group(1)
                return self.enviar_correo(destinatario)

            return "No entendí a quién enviar el correo. Intente: 'jarvis envía correo a ejemplo@correo.com'"

        if any(palabra in texto for palabra in ["whatsapp", "whats"]):

            if any(palabra in texto for palabra in ["envía", "mandar", "enviar"]):

                import re
                match = re.search(r'(?:a|para)\s+(\w+)', texto)

                if match:
                    contacto = match.group(1)
                    return self.enviar_whatsapp(contacto)

                return "No entendí a quién enviar el mensaje. Intente: 'jarvis envía whatsapp a irving'"

        # ===== CHISTES =====

        if any(palabra in texto for palabra in ["chiste", "cuéntame", "cuentame"]) and any(palabra in texto for palabra in ["un", "una"]):

            return random.choice(self.chistes)

        # ===== FRASES =====

        if any(palabra in texto for palabra in ["sorpréndeme", "sorprendeme"]):

            frases = [

                "La tecnología es mejor cuando acerca a las personas.",

                "Todo gran sistema comienza con una idea.",

                "La disciplina supera a la motivación.",

                "El conocimiento es poder.",

                "Bienvenido, señor."

            ]

            return random.choice(frases)

        if "objetivo" in texto:

            return "Mi objetivo es asistirle en todas sus tareas, señor."

        if "estás ahí" in texto or "estas ahi" in texto:

            return "Siempre estoy aquí, señor."

        if "jarvis" == texto:

            return "Sí, señor."

        return None

    # ----------------------------------
    # CAMBIAR NOMBRE
    # ----------------------------------

    def cambiar_usuario(self, nombre):

        self.nombre_usuario = nombre

    # ----------------------------------
    # HISTORIAL
    # ----------------------------------

    def historial(self):

        return self.memoria