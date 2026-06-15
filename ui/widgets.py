from PySide6.QtWidgets import (
    QWidget,
    QLabel,
    QVBoxLayout,
    QHBoxLayout,
    QFrame
)

from PySide6.QtCore import (
    Qt,
    QTimer
)

from PySide6.QtGui import (
    QFont
)

import psutil
import datetime


class HoloCard(QFrame):

    def __init__(self, titulo, valor="0"):

        super().__init__()

        self.setFrameShape(QFrame.StyledPanel)

        self.setStyleSheet("""
        QFrame{
            background:qlineargradient(
                x1:0,
                y1:0,
                x2:1,
                y2:1,
                stop:0 #0B1220,
                stop:0.5 #111827,
                stop:1 #1E293B
            );

            border:2px solid #38BDF8;
            border-radius:20px;
            padding:10px;
        }

        QFrame:hover{
            border:2px solid #7DD3FC;

            background:qlineargradient(
                x1:0,
                y1:0,
                x2:1,
                y2:1,
                stop:0 #172554,
                stop:0.5 #1E3A8A,
                stop:1 #2563EB
            );
        }
         """)
        layout = QVBoxLayout()

        self.lblTitulo = QLabel(titulo)
        self.lblValor = QLabel(valor)

        self.lblTitulo.setAlignment(
            Qt.AlignCenter
        )

        self.lblValor.setAlignment(
            Qt.AlignCenter
        )

        self.lblTitulo.setFont(
            QFont(
                "Consolas",
                11
            )
        )

        self.lblValor.setFont(
            QFont(
                "Consolas",
                20,
                QFont.Bold
            )
        )

        self.lblTitulo.setStyleSheet("""
        color:#66FFFF;
        border:none;
        """)

        self.lblValor.setStyleSheet("""
        color:#00FFFF;
        border:none;
        """)

        layout.addWidget(self.lblTitulo)
        layout.addWidget(self.lblValor)

        self.setLayout(layout)

    def setValue(self, texto):
        self.lblValor.setText(texto)


class SystemWidgets(QWidget):

    def __init__(self):

        super().__init__()

        layout = QHBoxLayout()

        self.cpuCard = HoloCard(
            "CPU",
            "0%"
        )

        self.ramCard = HoloCard(
            "RAM",
            "0%"
        )

        self.diskCard = HoloCard(
            "DISCO",
            "0%"
        )

        self.netCard = HoloCard(
            "RED",
            "0 KB/s"
        )

        layout.addWidget(
            self.cpuCard
        )

        layout.addWidget(
            self.ramCard
        )

        layout.addWidget(
            self.diskCard
        )

        layout.addWidget(
            self.netCard
        )

        self.setLayout(layout)

        self.last_sent = 0
        self.last_recv = 0

        self.timer = QTimer()

        self.timer.timeout.connect(
            self.update_stats
        )

        self.timer.start(1000)

    def update_stats(self):

        cpu = psutil.cpu_percent()

        ram = psutil.virtual_memory().percent

        disk = psutil.disk_usage(
            '/'
        ).percent

        net = psutil.net_io_counters()

        sent = net.bytes_sent
        recv = net.bytes_recv

        speed = (
            (sent - self.last_sent)
            +
            (recv - self.last_recv)
        ) / 1024

        self.last_sent = sent
        self.last_recv = recv

        self.cpuCard.setValue(
            f"{cpu}%"
        )

        self.ramCard.setValue(
            f"{ram}%"
        )

        self.diskCard.setValue(
            f"{disk}%"
        )

        self.netCard.setValue(
            f"{speed:.1f} KB/s"
        )


class ClockWidget(QFrame):

    def __init__(self):

        super().__init__()

        self.setStyleSheet("""
        QFrame{
            background-color: rgba(0,20,30,180);
            border:2px solid #00FFFF;
            border-radius:15px;
        }
        """)

        layout = QVBoxLayout()

        self.lblHora = QLabel()
        self.lblFecha = QLabel()

        self.lblHora.setAlignment(
            Qt.AlignCenter
        )

        self.lblFecha.setAlignment(
            Qt.AlignCenter
        )

        self.lblHora.setFont(
            QFont(
                "Consolas",
                28,
                QFont.Bold
            )
        )

        self.lblFecha.setFont(
            QFont(
                "Consolas",
                12
            )
        )

        self.lblHora.setStyleSheet("""
        color:#00FFFF;
        border:none;
        """)

        self.lblFecha.setStyleSheet("""
        color:#66FFFF;
        border:none;
        """)

        layout.addWidget(
            self.lblHora
        )

        layout.addWidget(
            self.lblFecha
        )

        self.setLayout(layout)

        self.timer = QTimer()

        self.timer.timeout.connect(
            self.update_time
        )

        self.timer.start(1000)

        self.update_time()

    def update_time(self):

        ahora = datetime.datetime.now()

        self.lblHora.setText(
            ahora.strftime("%H:%M:%S")
        )

        self.lblFecha.setText(
            ahora.strftime("%d/%m/%Y")
        )


class StatusWidget(QFrame):

    def __init__(self):

        super().__init__()

        self.estado = "ESPERANDO"

        self.setStyleSheet("""
        QFrame{
            background-color: rgba(0,20,30,180);
            border:2px solid #00FFFF;
            border-radius:15px;
        }
        """)

        layout = QVBoxLayout()

        titulo = QLabel(
            "ESTADO DEL SISTEMA"
        )

        titulo.setAlignment(
            Qt.AlignCenter
        )

        titulo.setStyleSheet("""
        color:#66FFFF;
        border:none;
        """)

        titulo.setFont(
            QFont(
                "Consolas",
                12
            )
        )

        self.lblEstado = QLabel(
            self.estado
        )

        self.lblEstado.setAlignment(
            Qt.AlignCenter
        )

        self.lblEstado.setFont(
            QFont(
                "Consolas",
                20,
                QFont.Bold
            )
        )

        self.lblEstado.setStyleSheet("""
        color:#00FFFF;
        border:none;
        """)

        layout.addWidget(titulo)
        layout.addWidget(self.lblEstado)

        self.setLayout(layout)

    def set_estado(
        self,
        estado
    ):

        self.estado = estado

        colores = {

            "ESPERANDO":
            "#00FFFF",

            "ESCUCHANDO":
            "#00FF00",

            "PROCESANDO":
            "#FFFF00",

            "HABLANDO":
            "#FF00FF"
        }

        self.lblEstado.setText(
            estado
        )

        self.lblEstado.setStyleSheet(
            f"""
            color:{colores.get(estado,'#00FFFF')};
            border:none;
            """
        )


if __name__ == "__main__":

    from PySide6.QtWidgets import (
        QApplication,
        QVBoxLayout
    )

    import sys

    app = QApplication(sys.argv)

    ventana = QWidget()

    ventana.setStyleSheet("""
    background:black;
    """)

    layout = QVBoxLayout()

    reloj = ClockWidget()
    sistema = SystemWidgets()
    estado = StatusWidget()

    layout.addWidget(reloj)
    layout.addWidget(sistema)
    layout.addWidget(estado)

    ventana.setLayout(layout)

    ventana.resize(
        1000,
        600
    )

    ventana.show()

    sys.exit(app.exec())