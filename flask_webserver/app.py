
from flask import Flask, render_template, request

app = Flask(__name__)


@app.route("/", methods=["GET", "POST"])
def calcul():
    pgcd = None
    ppcm = None
    a = None
    b = None
    etapes = []
    etapes_ppcm = []

    if request.method == "POST":
        a = int(request.form["nombre_a"])
        b = int(request.form["nombre_b"])

        # Calcul du PGCD avec l'algorithme d'Euclide
        x, y = abs(a), abs(b)

        while y != 0:
            quotient = x // y
            reste = x % y

            etapes.append({
                "dividende": x,
                "diviseur": y,
                "quotient": quotient,
                "reste": reste
            })

            x, y = y, reste

        pgcd = x
        # pgcd = gcd(a, b) (fonctions predefinit)

        # Calcul du PPCM sans utiliser le PGCD
        if a == 0 or b == 0:
            ppcm = 0
        else:
            nombre_a = abs(a)
            nombre_b = abs(b)

            pas = max(nombre_a, nombre_b)
            multiple = pas

            while (multiple % nombre_a != 0
                   or multiple % nombre_b != 0):

                etapes_ppcm.append({
                    "multiple": multiple,
                    "divisible_a": multiple % nombre_a == 0,
                    "divisible_b": multiple % nombre_b == 0
                })

                multiple += pas

            # Enregistrer le premier multiple commun trouvé
            etapes_ppcm.append({
                "multiple": multiple,
                "divisible_a": True,
                "divisible_b": True
            })

            ppcm = multiple
            # ppcm = int ( (a * b) / pgcd ) (lcm(a, b))

    return render_template(
        "index.html",
        pgcd=pgcd,
        ppcm=ppcm,
        a=a,
        b=b,
        etapes=etapes,
        etapes_ppcm=etapes_ppcm
    )


if __name__ == "__main__":
    app.run(debug=True)
