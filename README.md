<div align="center">

<img width="220" src="https://cdn-icons-png.flaticon.com/512/4712/4712109.png" />

# 🤖 JARVIS Desktop AI

### Asistente Virtual Inteligente para Escritorio impulsado por Ollama y Python 🚀

<p align="center">
  <b>JARVIS Desktop AI</b> es un asistente virtual avanzado desarrollado en Python que utiliza modelos de lenguaje ejecutados localmente mediante Ollama, permitiendo interacción por voz, automatización de tareas, consultas inteligentes y control del sistema en tiempo real.
</p>

<p align="center">
  <img src="https://img.shields.io/badge/Python-AI-blue?style=for-the-badge&logo=python&logoColor=white">
  <img src="https://img.shields.io/badge/Ollama-Local%20LLM-black?style=for-the-badge">
  <img src="https://img.shields.io/badge/Desktop-Assistant-green?style=for-the-badge">
  <img src="https://img.shields.io/badge/Voice-Control-orange?style=for-the-badge">
</p>

<p align="center">
  <a href="#-acerca-de-jarvis">Acerca de</a> •
  <a href="#-preview">Preview</a> •
  <a href="#-características">Características</a> •
  <a href="#-tecnologías-utilizadas">Tecnologías</a> •
  <a href="#-instalación">Instalación</a>
</p>

</div>

---

# 🌌 Acerca de JARVIS

**JARVIS Desktop AI** es un asistente virtual diseñado para ejecutarse localmente en computadoras Windows, Linux o macOS utilizando modelos de inteligencia artificial mediante Ollama.

Su objetivo es ofrecer una experiencia similar a un asistente personal inteligente capaz de comprender lenguaje natural, responder preguntas, ejecutar comandos y automatizar tareas del sistema.

La plataforma permite:

- 🎙️ Conversación por voz
- 🧠 Inteligencia Artificial local
- ⚡ Ejecución de comandos
- 💻 Control del sistema operativo
- 🌐 Consultas inteligentes
- 📂 Apertura de aplicaciones
- 🔊 Síntesis de voz natural
- 🤖 Automatización de tareas

El proyecto fue desarrollado para practicar:

- Inteligencia Artificial
- Procesamiento de Lenguaje Natural
- Automatización de Escritorio
- Python Avanzado
- Integración con Modelos LLM
- Desarrollo de Asistentes Virtuales

---

# 📸 Preview

## 🤖 Interfaz Principal

<div align="center">

<img src="screenshots/main.png" width="900"/>

</div>

---

## 🎙️ Reconocimiento de Voz

<div align="center">

<img src="screenshots/voice.png" width="900"/>

</div>

---

## 🧠 Conversación con IA

<div align="center">

<img src="screenshots/chat.png" width="900"/>

</div>

---

## ⚙️ Panel de Configuración

<div align="center">

<img src="screenshots/settings.png" width="900"/>

</div>

---

# ✨ Características

## 🤖 Inteligencia Artificial Local

- 🧠 Integración con Ollama
- ⚡ Ejecución sin nube
- 🔒 Privacidad total
- 📚 Memoria contextual
- 🎯 Respuestas inteligentes

---

## 🎙️ Control por Voz

- 🎤 Reconocimiento de voz
- 🔊 Síntesis de voz natural
- 🌎 Soporte multilenguaje
- ⚡ Conversación en tiempo real
- 🎧 Comandos hablados

---

## 💻 Automatización del Sistema

- 📂 Abrir programas
- 🌐 Abrir sitios web
- 📁 Gestionar archivos
- ⚙️ Ejecutar comandos
- 🖥️ Control del sistema operativo

---

## 📚 Asistente Inteligente

- 🔍 Búsquedas rápidas
- 📰 Consultas generales
- 📅 Gestión de tareas
- ⏰ Recordatorios
- 🧠 Respuestas contextuales

---

# ⚙️ Funciones Avanzadas

## 🚀 Productividad

- Gestión de aplicaciones
- Automatización diaria
- Control multimedia
- Organización personal
- Acciones rápidas

---

## 🔒 Privacidad

- Procesamiento local
- Sin dependencia de servidores externos
- Datos almacenados localmente
- Control total del usuario

---

# 🛠️ Tecnologías Utilizadas

## 💻 Backend

<p>
  <img src="https://skillicons.dev/icons?i=python" />
</p>

- Python 3.11+
- AsyncIO
- Threading
- Multiprocessing

---

## 🤖 Inteligencia Artificial

<p>
  <img src="https://skillicons.dev/icons?i=python" />
</p>

- Ollama
- Llama 3
- Mistral
- Gemma
- DeepSeek
- Phi

---

## 🖥️ Interfaz Gráfica

<p>
  <img src="https://skillicons.dev/icons?i=pycharm" />
</p>

- Tkinter
- CustomTkinter
- PyQt6
- Electron (Opcional)

---

## 🎙️ Voz

- SpeechRecognition
- Edge-TTS
- PyAudio
- Whisper

---

# 📂 Estructura del Proyecto

```bash
JARVIS/
│
├── assets/
│   ├── sounds/
│   ├── images/
│   └── avatars/
│
├── models/
│
├── src/
│   ├── ai/
│   │   └── ollama_client.py
│   │
│   ├── voice/
│   │   ├── speech_to_text.py
│   │   └── text_to_speech.py
│   │
│   ├── automation/
│   │   ├── system_control.py
│   │   └── app_launcher.py
│   │
│   ├── ui/
│   │   └── main_window.py
│   │
│   └── main.py
│
├── config/
├── requirements.txt
└── README.md
```

---

# ⚡ Instalación

## 1️⃣ Clonar repositorio

```bash
git clone https://github.com/isairey/JARVIS-AI
```

---

## 2️⃣ Instalar Ollama

Descargar e instalar:

```bash
https://ollama.com
```

---

## 3️⃣ Descargar modelo

```bash
ollama pull llama3
```

o

```bash
ollama pull mistral
```

---

## 4️⃣ Instalar dependencias

```bash
pip install -r requirements.txt
```

---

## 5️⃣ Ejecutar JARVIS

```bash
python main.py
```

---

# 🤖 Modelos Compatibles

## Ollama Models

- Llama 3
- Llama 3.1
- DeepSeek
- Mistral
- Gemma
- Phi
- Qwen
- CodeLlama

---

# 🔥 Funcionalidades Técnicas

## 🧠 IA Conversacional

- Chat inteligente
- Comprensión contextual
- Respuestas naturales
- Conversación continua
- Integración local

---

## 🎙️ Procesamiento de Voz

- Speech To Text
- Text To Speech
- Wake Word
- Voice Commands
- Real-Time Processing

---

## ⚙️ Automatización

- Apertura de software
- Gestión de archivos
- Control multimedia
- Navegación web
- Scripts personalizados

---

# 🧠 Objetivos del Proyecto

## 🎯 Aprender y practicar

- Inteligencia Artificial
- Modelos LLM Locales
- Ollama
- Procesamiento de Voz
- Automatización de Escritorio
- Python Avanzado
- Desarrollo de Asistentes Virtuales

---

# 📊 Roadmap

## 🚧 Próximamente

- 🖥️ Visión por computadora
- 👁️ Reconocimiento facial
- 📷 Captura de pantalla inteligente
- 🌐 Navegación automática
- 🧠 Memoria persistente
- 📱 Aplicación móvil
- 🤖 Agentes autónomos
- 🔥 Integración MCP

---

# 🤝 Contribuciones

Las contribuciones son bienvenidas ❤️

## Cómo contribuir

1. Fork del proyecto

2. Crear rama

```bash
git checkout -b feature/nueva-funcion
```

3. Realizar cambios

```bash
git commit -m "✨ Nueva característica"
```

4. Enviar cambios

```bash
git push origin feature/nueva-funcion
```

5. Crear Pull Request 🚀

---

# 👨‍💻 Fundador

<div align="center">

<img width="140" src="https://github.com/isairey.png" />

## Isai Reyes — AI & Full Stack Developer

Apasionado por la inteligencia artificial, asistentes virtuales, automatización y desarrollo de software moderno.

</div>

---

# 🌟 Apoya el Proyecto

Si te gusta JARVIS Desktop AI:

⭐ Dale una estrella al repositorio  
🍴 Haz Fork del proyecto  
📢 Comparte el proyecto con otros desarrolladores

---

# 📜 Licencia

Proyecto Open Source desarrollado con fines educativos, investigación en IA y automatización.

---

<div align="center">

### 🤖 JARVIS Desktop AI — Tu asistente virtual inteligente ejecutándose completamente en local con Ollama.

</div>
