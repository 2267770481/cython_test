from flask import Flask

from apps.module_a import register_url as module_a_url
from apps.module_b import register_url as module_b_url

app = Flask(__name__)

app.register_blueprint(module_a_url())
app.register_blueprint(module_b_url())

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=1111)
