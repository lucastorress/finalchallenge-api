from flask import Flask
import logging as logger

logger.basicConfig(level="DEBUG")

app = Flask(__name__)

if __name__ == "__main__":
    logger.debug("Starting Flask Server...")
    from api import *
    app.run(host="localhost", port=5000,
            debug=True, use_reloader=True)
