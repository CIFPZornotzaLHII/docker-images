import os
import socket

from flask import Flask

VERSION = "1.0"

app = Flask(__name__)


@app.route("/")
def inicio():
    nombre = os.environ.get("NOMBRE", "mundo")
    contenedor = socket.gethostname()
    return f"""
    <h1>¡Hola, {nombre}!</h1>
    <p>Te responde el contenedor <code>{contenedor}</code>.</p>
    <p>Versión {VERSION}</p>
    """


if __name__ == "__main__":
    # 0.0.0.0 = escuchar en todas las interfaces.
    # Con 127.0.0.1 la app solo se vería desde dentro del contenedor.
    app.run(host="0.0.0.0", port=5000)
