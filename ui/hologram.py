from PySide6.QtWidgets import (
    QWidget,
    QLabel,
    QVBoxLayout,
    QHBoxLayout,
    QApplication
)

from PySide6.QtCore import (
    Qt,
    QTimer,
    QPoint
)

from PySide6.QtGui import (
    QPainter,
    QColor,
    QPen,
    QFont,
    QPixmap
)

import psutil
import math
import datetime
import os


class ArcReactor(QWidget):

    def __init__(self):
        super().__init__()

        self.angle = 0

        self.timer = QTimer(self)
        self.timer.timeout.connect(self.animate)
        self.timer.start(16)

    def animate(self):
        self.angle += 2

        if self.angle >= 360:
            self.angle = 0

        self.update()

    def paintEvent(self, event):

        painter = QPainter(self)

        painter.setRenderHint(QPainter.Antialiasing)

        center_x = self.width() / 2
        center_y = self.height() / 2

        # FONDO TRANSPARENTE para ver la imagen atrás
        painter.fillRect(self.rect(), QColor(0, 0, 0, 180))

        glow_color = QColor(0, 255, 255)

        pen = QPen(glow_color)
        pen.setWidth(4)

        painter.setPen(pen)

        size = 220

        painter.drawEllipse(
            int(center_x - size / 2),
            int(center_y - size / 2),
            size,
            size
        )

        painter.save()

        painter.translate(center_x, center_y)
        painter.rotate(self.angle)

        pen.setWidth(8)
        painter.setPen(pen)

        for i in range(8):

            painter.rotate(45)

            painter.drawLine(
                0,
                -70,
                0,
                -110
            )

        painter.restore()

        pen.setWidth(3)
        painter.setPen(pen)

        painter.drawEllipse(
            int(center_x - 80),
            int(center_y - 80),
            160,
            160
        )

        painter.drawEllipse(
            int(center_x - 40),
            int(center_y - 40),
            80,
            80
        )

        painter.fillEllipse = painter.drawEllipse

        painter.setBrush(glow_color)

        painter.drawEllipse(
            int(center_x - 20),
            int(center_y - 20),
            40,
            40
        )

        painter.end()
        
class Hologram(QWidget):

    def __init__(self):
        super().__init__()

        self.dragPos = QPoint()

        self.estado_actual = "ESPERANDO"

        self.setWindowTitle("J.A.R.V.I.S")

        self.setGeometry(200, 100, 1000, 700)

        self.setWindowFlags(
            Qt.FramelessWindowHint
        )

        # ===== FONDO DE IMAGEN =====
        self.set_background_image()

        self.setStyleSheet("""
            QWidget{
                background-color:transparent;
                color:#00FFFF;
            }
        """)

        self.build_ui()

        self.info_timer = QTimer(self)
        self.info_timer.timeout.connect(
            self.actualizar_info
        )
        self.info_timer.start(1000)

    def set_background_image(self):
        """ imagen de fondo"""
        
        # Ruta de la imagen
        imagen_path = "assets/pr.png"
        
        # Verificar si existe
        if os.path.exists(imagen_path):
            
            # Cargar imagen
            pixmap = QPixmap(imagen_path)
            
            if not pixmap.isNull():
                
                # Crear label para el fondo
                self.fondo_label = QLabel(self)
                self.fondo_label.setPixmap(pixmap)
                self.fondo_label.setScaledContents(True)
                self.fondo_label.setGeometry(self.rect())
                self.fondo_label.lower()  # Mover al fondo
                
                print(f"[DEBUG] Fondo cargado: {imagen_path}")
            
            else:
                print("[DEBUG] Error: imagen no se pudo cargar")
                self.set_default_background()
        else:
            print(f"[DEBUG] Imagen no encontrada: {imagen_path}")
            self.set_default_background()

    def set_default_background(self):
        """Fondo por defecto si no hay imagen"""
        self.setStyleSheet("""
            QWidget{
                background-color:black;
                color:#00FFFF;
            }
        """)

    def resizeEvent(self, event):
        """Redimensionar el fondo cuando cambie el tamaño"""
        super().resizeEvent(event)
        
        if hasattr(self, 'fondo_label'):
            self.fondo_label.setGeometry(self.rect())

    def build_ui(self):

        layout = QVBoxLayout()

        layout.setContentsMargins(
            20,
            20,
            20,
            20
        )

        titulo = QLabel("J.A.R.V.I.S")

        titulo.setAlignment(Qt.AlignCenter)

        titulo.setFont(
            QFont(
                "Consolas",
                28,
                QFont.Bold
            )
        )

        titulo.setStyleSheet("""
            color:#00FFFF;
            background-color:transparent;
        """)

        layout.addWidget(titulo)

        self.reactor = ArcReactor()
        self.reactor.setMinimumHeight(400)

        layout.addWidget(self.reactor)

        self.estado = QLabel(
            "ESTADO: ESPERANDO"
        )

        self.estado.setAlignment(
            Qt.AlignCenter
        )

        self.estado.setFont(
            QFont(
                "Consolas",
                16
            )
        )

        layout.addWidget(self.estado)

        panel = QHBoxLayout()

        self.cpu = QLabel("CPU: 0%")
        self.ram = QLabel("RAM: 0%")
        self.hora = QLabel("00:00:00")

        for lbl in [
            self.cpu,
            self.ram,
            self.hora
        ]:

            lbl.setFont(
                QFont(
                    "Consolas",
                    14
                )
            )

            lbl.setStyleSheet("""
                color:#00FFFF;
                background-color:rgba(0,0,0,150);
                border:1px solid #00FFFF;
                padding:10px;
            """)

            panel.addWidget(lbl)

        layout.addLayout(panel)

        instrucciones = QLabel(
            """
F1 = ESPERANDO
F2 = ESCUCHANDO
F3 = PROCESANDO
F4 = HABLANDO
ESC = SALIR
            """
        )

        instrucciones.setAlignment(
            Qt.AlignCenter
        )

        instrucciones.setStyleSheet("""
            color:#00AAAA;
            background-color:rgba(0,0,0,150);
        """)

        layout.addWidget(instrucciones)

        self.setLayout(layout)

    def actualizar_info(self):

        cpu = psutil.cpu_percent()

        ram = psutil.virtual_memory().percent

        hora = datetime.datetime.now()

        self.cpu.setText(
            f"CPU: {cpu}%"
        )

        self.ram.setText(
            f"RAM: {ram}%"
        )

        self.hora.setText(
            hora.strftime("%H:%M:%S")
        )

    def cambiar_estado(
        self,
        estado
    ):

        self.estado_actual = estado

        self.estado.setText(
            f"ESTADO: {estado}"
        )

        colores = {
            "ESPERANDO": "#00FFFF",
            "ESCUCHANDO": "#00FF00",
            "PROCESANDO": "#FFFF00",
            "HABLANDO": "#FF00FF"
        }

        color = colores.get(
            estado,
            "#00FFFF"
        )

        self.estado.setStyleSheet(
            f"""
            color:{color};
            font-size:18px;
            background-color:rgba(0,0,0,150);
            """
        )

    def keyPressEvent(self, event):

        if event.key() == Qt.Key_F1:
            self.cambiar_estado(
                "ESPERANDO"
            )

        elif event.key() == Qt.Key_F2:
            self.cambiar_estado(
                "ESCUCHANDO"
            )

        elif event.key() == Qt.Key_F3:
            self.cambiar_estado(
                "PROCESANDO"
            )

        elif event.key() == Qt.Key_F4:
            self.cambiar_estado(
                "HABLANDO"
            )

        elif event.key() == Qt.Key_Escape:
            self.close()

    def mousePressEvent(self, event):

        if event.button() == Qt.LeftButton:
            self.dragPos = (
                event.globalPosition().toPoint()
            )

    def mouseMoveEvent(self, event):

        if event.buttons() == Qt.LeftButton:

            self.move(
                self.pos()
                + event.globalPosition().toPoint()
                - self.dragPos
            )

            self.dragPos = (
                event.globalPosition().toPoint()
            )


if __name__ == "__main__":

    import sys

    app = QApplication(sys.argv)

    window = Hologram()

    window.show()

    sys.exit(app.exec())