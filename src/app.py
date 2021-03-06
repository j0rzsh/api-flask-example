from flask import Flask
from api import blueprint as api


app = Flask(__name__)

app.register_blueprint(api)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
