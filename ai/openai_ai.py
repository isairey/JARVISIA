import requests
import os

def preguntar_openai(prompt, model="gpt-4.1-mini", timeout=60):

    try:
        api_key = os.getenv("OPENAI_API_KEY")

        if not api_key:
            return "Error: falta la API key de OpenAI."

        response = requests.post(
            "https://api.openai.com/v1/responses",
            headers={
                "Authorization": f"Bearer {api_key}",
                "Content-Type": "application/json"
            },
            json={
                "model": model,
                "input": prompt
            },
            timeout=timeout
        )

        response.raise_for_status()
        data = response.json()

        return data["output"][0]["content"][0]["text"]

    except requests.exceptions.ConnectionError:
        return "Error: no se pudo conectar con OpenAI."

    except requests.exceptions.Timeout:
        return "Error: la respuesta tardó demasiado."

    except requests.exceptions.RequestException as e:
        return f"Error HTTP: {str(e)}"

    except Exception as e:
        return f"Error inesperado: {str(e)}"