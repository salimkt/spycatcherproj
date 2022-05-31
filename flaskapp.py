from flask import Flask, render_template, request


app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        f = open('./file.wav', 'wb')
        f.write(request.get_data("audio_data"))
        f.close()
        if os.path.isfile('./file.wav'):
            print("./file.wav exists")

        return render_template('index.html', request="POST")   
    else:
        return render_template("index.html")


if __name__ == "__main__":
    app.run(debug=True, threaded=True)
