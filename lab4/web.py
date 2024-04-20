from flask import Flask

app = Flask(__name__)

@app.route("/")
def printNames():
    return "<p>Team 14: Eric Pinos & Casey Provitera</p>"

if __name__ == '__main__':
	app.run(debug = True)

