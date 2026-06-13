import requests

def preguntar(prompt):

    respuesta = requests.post(
        "http://localhost:11434/api/generate",
        json={
            "model":"llama3",
            "prompt":prompt,
            "stream":False
        }
    )

    return respuesta.json()["response"]