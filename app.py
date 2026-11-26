import logging
from flask import Flask, request, jsonify

logging.basicConfig(level=logging.INFO,
                    format="%(asctime)s %(levelname)s %(name)s - %(message)s")
log = logging.getLogger("app")

app = Flask(__name__)

@app.post("/echo")
def echo():
    data = request.get_json(silent=True)
    if data is None:
        log.warning("Invalid or missing JSON body")
        return jsonify(error="INVALID_JSON"), 400
    log.info("Received: %s", data)
    return jsonify(received=data), 201

if __name__ == "__main__":
    app.run(debug=True)