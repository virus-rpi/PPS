from flask import Flask, request

app = Flask(__name__)


@app.route('/', methods=['POST'])
def result():
    with open("log.txt", "a") as f:
        req = str(dict(request.form))
        f.write(req+"\n")
    return 'Received!'


app.run()
