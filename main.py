from flask import Flask, jsonify
import random as r
import math as m

app = Flask(__name__)
app.debug = True

@app.route('/<int:t>')
def index(t):
	inside = 0
	total = t
	for i in range(0, total):
		x2 = r.random()**2
		y2 = r.random()**2
		if m.sqrt(x2 + y2) < 1.0:
			inside += 1

	return str(inside)

if __name__ == "__main__":
    app.run(debug=True)
