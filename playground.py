from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def home():
    print("This is home!")
    return "This is Home!"

@app.route('/play')
def play():
    print("Play!")
    return render_template("index.html", times = 3, color = "#4d88ff")

@app.route('/play/<int:x>')
def boxes(x):
    print("complete")
    return render_template('index.html', times = x, color = "#668cff")

@app.route('/play/<int:x>/<string:color>')
def play_boxes(x, color):
    print("complete")
    return render_template('index.html', times = x, color = color)

if __name__=="__main__":
    app.run(debug=True)

