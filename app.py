from flask import Flask, request, render_template_string

app = Flask(__name__)

@app.route("/")
def index():
    user_input = request.args.get("test", "guest")

    template = f"""
    <!DOCTYPE html>
    <html>
    <head>
        <title>Vulnerable SSTI App</title>
    </head>
    <body>
        <h1>SSTI Demo</h1>
        <p>Result: {user_input}</p>
    </body>
    </html>
    """

    return render_template_string(template)

if __name__ == "__main__":
    app.run(debug=True)
