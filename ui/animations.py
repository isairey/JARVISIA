from PySide6.QtWidgets import QWidget
from PySide6.QtCore import Qt, QTimer, QPointF
from PySide6.QtGui import (
    QPainter,
    QColor,
    QPen,
    QBrush
)

import random
import math


class Particle:

    def __init__(self, width, height):

        self.width = width
        self.height = height

        self.reset()

    def reset(self):

        self.x = random.randint(0, self.width)
        self.y = random.randint(0, self.height)

        self.size = random.randint(2, 6)

        self.speed = random.uniform(
            0.2,
            1.2
        )

        self.alpha = random.randint(
            40,
            180
        )

    def update(self):

        self.y -= self.speed

        if self.y < 0:
            self.y = self.height
            self.x = random.randint(
                0,
                self.width
            )

    def draw(self, painter):

        color = QColor(
            0,
            255,
            255,
            self.alpha
        )

        painter.setBrush(
            QBrush(color)
        )

        painter.setPen(Qt.NoPen)

        painter.drawEllipse(
            int(self.x),
            int(self.y),
            self.size,
            self.size
        )


class HologramAnimation(QWidget):

    def __init__(self):

        super().__init__()

        self.angle1 = 0
        self.angle2 = 0

        self.pulse = 0

        self.particles = []

        self.timer = QTimer(self)

        self.timer.timeout.connect(
            self.animate
        )

        self.timer.start(16)

    def showEvent(self, event):

        self.create_particles()

    def create_particles(self):

        self.particles.clear()

        for _ in range(150):

            self.particles.append(
                Particle(
                    self.width(),
                    self.height()
                )
            )

    def resizeEvent(self, event):

        self.create_particles()

    def animate(self):

        self.angle1 += 1
        self.angle2 -= 2

        self.pulse += 0.05

        for particle in self.particles:
            particle.update()

        self.update()

    def paintEvent(self, event):

        painter = QPainter(self)

        painter.setRenderHint(
            QPainter.Antialiasing
        )

        painter.fillRect(
            self.rect(),
            QColor(0, 0, 0)
        )

        for particle in self.particles:
            particle.draw(painter)

        center_x = self.width() / 2
        center_y = self.height() / 2

        pulse_size = (
            180 +
            math.sin(self.pulse) * 15
        )

        glow = QColor(
            0,
            255,
            255,
            80
        )

        painter.setBrush(
            QBrush(glow)
        )

        painter.setPen(Qt.NoPen)

        painter.drawEllipse(
            QPointF(
                center_x,
                center_y
            ),
            pulse_size,
            pulse_size
        )

        painter.save()

        painter.translate(
            center_x,
            center_y
        )

        painter.rotate(
            self.angle1
        )

        pen = QPen(
            QColor(
                0,
                255,
                255
            )
        )

        pen.setWidth(4)

        painter.setPen(pen)

        painter.drawEllipse(
            -140,
            -140,
            280,
            280
        )

        for i in range(12):

            painter.rotate(30)

            painter.drawLine(
                0,
                -120,
                0,
                -145
            )

        painter.restore()

        painter.save()

        painter.translate(
            center_x,
            center_y
        )

        painter.rotate(
            self.angle2
        )

        pen2 = QPen(
            QColor(
                0,
                180,
                255
            )
        )

        pen2.setWidth(3)

        painter.setPen(pen2)

        painter.drawEllipse(
            -100,
            -100,
            200,
            200
        )

        for i in range(8):

            painter.rotate(45)

            painter.drawLine(
                0,
                -85,
                0,
                -105
            )

        painter.restore()

        painter.setBrush(
            QColor(
                0,
                255,
                255
            )
        )

        painter.setPen(Qt.NoPen)

        painter.drawEllipse(
            QPointF(
                center_x,
                center_y
            ),
            18,
            18
        )