from flask import Flask
app = Flask(__name__)

print(__name__)

@app.route('/')
def hello_world():
	return '<h1 style="text:align=center">Hello World!</h1>'\
		'<p color="blue">This is a paragraph.</p>'\
		'<img src="https://media.giphy.com/media/hyS1eKlR75hMr0l7VJ/giphy.gif" width=200>'

@app.route("/bye")
def bye():
	return "bye!"

@app.route("/username/<name>/<int:number>")
def greet(name,number):
	return f"Hello there {name}, you are {number} years old !"

if __name__ == "__main__":
	app.run(debug=True)