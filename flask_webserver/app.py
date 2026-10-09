# 1. ADDED: imported 'render_template' alongside Flask
from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/")
def home():
    return "Hello Flask!"

@app.route("/pgcd_test")
def pgcd_test():
    p = "Le Diviseur"
    q = "Quotient"
    r = "Le Reste"
    langs = ["Python", "Flask", "Math"] # Added so your loop has data

    # 2. FIXED: Changed 'render.template' to 'render_template'
    return render_template(
        "index.html", 
        quotion=q, 
        reste=r, 
        poton=p, 
        programming_languages=langs
    )


@app.route("/pgcd", methods=["GET", "POST"])
def pgcd_calculator():

    if request.method == "POST":
        a = int(request.form["nombre_a"])
        b = int(request.form["nombre_b"])

        # Algorithme d'Euclide
        x, y = a, b

        while y != 0:
            x, y = y, x % y

        pgcd = x

        return render_template(
            "index.html",
            pgcd=pgcd
        )

    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True)
