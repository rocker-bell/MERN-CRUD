from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/")
def home():
    return "Hello Flask!"

@app.route("/pgcd")
def pgcd_calculator():
    # 1. Récupérer les valeurs 'a' et 'p' depuis l'URL (ex: /pgcd?a=25&p=4)
    raw_a = request.args.get('a')
    raw_p = request.args.get('p')

    # Si les paramètres ne sont pas fournis, on affiche la page vide ou avec une aide
    if not raw_a or not raw_p:
        return render_template("index.html", error="Veuillez fournir les paramètres 'a' et 'p' dans l'URL. Exemple : /pgcd?a=25&p=4")

    try:
        # 2. Conversion en entier strict. Si l'utilisateur a mis une virgule, cela lèvera une erreur.
        a = int(raw_a)
        p = int(raw_p)

        # 3. Vérification des entiers naturels (positifs)
        if a < 0 or p < 0:
            return render_template("index.html", error="Les nombres doivent être des entiers naturels (positifs ou nuls).")

        # 4. EXCLUSION DU DIVISEUR ÉGAL À ZERO
        if p == 0:
            return render_template("index.html", error="Erreur : Le diviseur 'p' ne peut pas être égal à 0.")

        # 5. Calcul de la division euclidienne
        q = a // p  # Quotient entier
        r = a % p   # Reste entier

        return render_template("index.html", dividende=a, diviseur=p, quotient=q, reste=r)

    except ValueError:
        # Capturé si l'utilisateur saisit des lettres ou des nombres à virgule (ex: 4.5)
        return render_template("index.html", error="Erreur : Vous devez saisir uniquement des nombres entiers sans virgule.")

if __name__ == "__main__":
    app.run(debug=True)



# 


<!DOCTYPE html>
<html lang="fr">
<head>
    <meta charset="UTF-8">
    <title>Division Euclidienne</title>
</head>
<body>

    <h1>Calculateur de Division Euclidienne</h1>

    <!-- Si une erreur ou exclusion survient -->
    {% if error %}
        <div style="color: red; font-weight: bold; padding: 10px; border: 1px solid red; background-color: #ffe6e6;">
            {{ error }}
        </div>
    {% else %}
        <!-- Si le calcul est valide -->
        <h2>Forme standard : a = p × q + r</h2>
        <p style="font-size: 1.2em; background-color: #f0f0f0; padding: 10px; display: inline-block;">
            <strong>{{ dividende }}</strong> = <strong>{{ diviseur }}</strong> × <strong>{{ quotient }}</strong> + <strong>{{ reste }}</strong>
        </p>

        <ul>
            <li><strong>Dividende (a) :</strong> {{ dividende }}</li>
            <li><strong>Diviseur (p) :</strong> {{ diviseur }}</li>
            <li><strong>Quotient (q) :</strong> {{ quotient }}</li>
            <li><strong>Reste (r) :</strong> {{ reste }}</li>
        </ul>
    {% endif %}

</body>
</html>
