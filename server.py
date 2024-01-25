from flask import Flask

app = Flask(__name__)


@app.route("/")
def health_care():
    return {
        "message": "success connect to the server",
        "status": True,
        "statusCode": 200
    }

if __name__ == '__main__':
    app.run()