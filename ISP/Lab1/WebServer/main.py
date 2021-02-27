from flask import Flask, render_template
from filemanager import FileManager


app = Flask(__name__)
file_manager = FileManager("./files")


@app.route("/")
def index():
    data = file_manager.get_file_names()
    return render_template("index.html", data=data)


@app.route('/<page>')
def some_file(page):
    data = file_manager.read_file(page)
    return render_template("file.html", data=data)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000)
