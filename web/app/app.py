import flask
from flask import Flask
import repos

app = Flask(__name__)


@app.route("/")
def index():
    estates = repos.get_estates()
    return flask.render_template("index.html", estates=estates)


if __name__ == '__main__':
    repos.wait_and_connect_db()
    app.run(debug=True, host='0.0.0.0')
    repos.cur.close()
    repos.conn.close()
