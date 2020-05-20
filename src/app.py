from flask import Flask
from api import blueprint as api
from werkzeug.middleware.proxy_fix import ProxyFix


app = Flask(__name__)

app.wsgi_app = ProxyFix(app.wsgi_app)

app.register_blueprint(api, url_prefix="/")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
