import requests


def preguntar(prompt, model="llama3", timeout=60):
    try:
        respuesta = requests.post(
            "http://localhost:11434/api/generate",
            json={
                "model": model,
                "prompt": prompt,
                "stream": False
            },
            timeout=timeout
        )

        respuesta.raise_for_status()

        data = respuesta.json()

        return data.get("response", "")

    except requests.exceptions.ConnectionError:
        return "Error: no se pudo conectar con el modelo (Ollama apagado)."

    except requests.exceptions.Timeout:
        return "Error: el modelo tardó demasiado en responder."

    except requests.exceptions.RequestException as e:
        return f"Error HTTP: {str(e)}"

    except Exception as e:
        return f"Error inesperado: {str(e)}"