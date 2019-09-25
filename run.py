from api import app
import logging as logger

logger.basicConfig(level="DEBUG")

if __name__ == "__main__":
    logger.debug("Starting API Server...")
    app.run(host="localhost", port=5000,
            debug=True, use_reloader=True)
