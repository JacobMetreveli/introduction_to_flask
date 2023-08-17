from flask import Flask


def make_bold(function):
    def wrapper_function():
        return f"<b>{function()}<b>"

    return wrapper_function


def make_emphasis(function):
    def wrapper_function():
        return f"<em>{function()}</em>"

    return wrapper_function


def make_underlined(function):
    def wrapper_function():
        return f"<u>{function()}<u>"

    return wrapper_function


app = Flask(__name__)


@app.route('/')
def hello_world():
    return ('<h1 style="text-align: center">Hello, World!</h1>'
            '<p>This is a paragraph.</p>'
            '<img src="https://cdn.vox-cdn.com/thumbor/GjH574x03D50MGypJMzEjyg4m60=/1400x1400/filters:format(jpeg)/cdn.vox-cdn.com/uploads/chorus_asset/file/23340627/Elden_Ring_Starscourge_Radahn_guide_lead_image.jpg" width=200>')


@app.route("/bye")
@make_bold
@make_emphasis
@make_underlined
def say_bye():
    return "Bye"


@app.route("/username/<name>/<int:number>")
def greet(name, number):
    return f"Hello there {name}, you are {number} years old!"


if __name__ == "__main__":
    app.run(debug=True)
