
# from flask import Flask, render_template, request


# import json

# app = Flask(__name__)


# @app.route("/", methods=["GET", "POST"])
# def calcul():
#     pgcd = None
#     ppcm = None
#     a = None
#     b = None
#     etapes = []
#     etapes_ppcm = []

#     if request.method == "POST":
#         a = int(request.form["nombre_a"])
#         b = int(request.form["nombre_b"])

#         # Calcul du PGCD avec l'algorithme d'Euclide
#         x, y = abs(a), abs(b)

#         while y != 0:
#             quotient = x // y
#             reste = x % y

#             etapes.append({
#                 "dividende": x,
#                 "diviseur": y,
#                 "quotient": quotient,
#                 "reste": reste
#             })

#             x, y = y, reste

#         pgcd = x
#         # pgcd = gcd(a, b) (fonctions predefinit)

#         # Calcul du PPCM sans utiliser le PGCD
#         if a == 0 or b == 0:
#             ppcm = 0
#         else:
#             nombre_a = abs(a)
#             nombre_b = abs(b)

#             pas = max(nombre_a, nombre_b)
#             multiple = pas

#             while (multiple % nombre_a != 0
#                    or multiple % nombre_b != 0):

#                 etapes_ppcm.append({
#                     "multiple": multiple,
#                     "divisible_a": multiple % nombre_a == 0,
#                     "divisible_b": multiple % nombre_b == 0
#                 })

#                 multiple += pas

#             # Enregistrer le premier multiple commun trouvé
#             etapes_ppcm.append({
#                 "multiple": multiple,
#                 "divisible_a": True,
#                 "divisible_b": True
#             })

#             ppcm = multiple
#             # ppcm = int ( (a * b) / pgcd ) (lcm(a, b))

#             #fermat



#             # bezout 


            


#             #indicatrice_d'euler


#             #inverse_modulaire

#     return render_template(
#         "index.html",
#         pgcd=pgcd,
#         ppcm=ppcm,
#         a=a,
#         b=b,
#         etapes=etapes,
#         etapes_ppcm=etapes_ppcm
#     )


# # @app.route('/sauvegarder-restaurer', methods=["GET", "POST"])
# # def sauvegrader()




# if __name__ == "__main__":
#     app.run(debug=True)



# from flask import Flask, render_template, request
# from math import gcd

# app = Flask(__name__)


# # ==========================================
# # 1. ALGORITHME D'EUCLIDE ET BEZOUT
# # ==========================================

# def euclide_etendu(a, b):

#     if b == 0:
#         return abs(a), 1 if a >= 0 else -1, 0

#     pgcd, u1, v1 = euclide_etendu(b, a % b)

#     u = v1
#     v = u1 - (a // b) * v1

#     return pgcd, u, v


# # ==========================================
# # 2. TEST DE PRIMALITE
# # ==========================================

# def est_premier(n):

#     if n < 2:
#         return False

#     if n == 2:
#         return True

#     if n % 2 == 0:
#         return False

#     for i in range(3, int(n**0.5) + 1, 2):
#         if n % i == 0:
#             return False

#     return True


# # ==========================================
# # 3. PETIT THEOREME DE FERMAT
# # ==========================================

# def petit_fermat(a, p):

#     if not est_premier(p):
#         return {
#             "premier": False,
#             "message": f"{p} n'est pas premier."
#         }

#     if a % p == 0:
#         return {
#             "premier": True,
#             "message": "Le théorème nécessite que a ne soit pas divisible par p."
#         }

#     resultat = pow(a, p - 1, p)

#     return {
#         "premier": True,
#         "resultat": resultat,
#         "message": f"{a}^{p-1} ≡ {resultat} (mod {p})"
#     }


# # ==========================================
# # 4. RESOLUTION DE CONGRUENCE
# #    ax ≡ b (mod n)
# # ==========================================

# def resoudre_congruence(a, b, n):

#     if n <= 0:
#         return {"erreur": "Le module n doit être positif."}

#     d = gcd(abs(a), n)

#     if b % d != 0:
#         return {
#             "erreur": "Cette congruence ne possède aucune solution."
#         }

#     # Réduction de la congruence
#     a_reduit = a // d
#     b_reduit = b // d
#     n_reduit = n // d

#     # Inverse de a réduit modulo n réduit
#     pgcd, u, v = euclide_etendu(a_reduit, n_reduit)

#     x0 = (u * b_reduit) % n_reduit

#     solutions = [
#         x0 + k * n_reduit
#         for k in range(d)
#     ]

#     return {
#         "pgcd": d,
#         "x0": x0,
#         "solutions": solutions,
#         "module_reduit": n_reduit,
#         "message": "Congruence résolue avec succès."
#     }


# # ==========================================
# # 5. INDICATRICE D'EULER
# # ==========================================

# def indicatrice_euler(n):

#     if n < 1:
#         return None

#     compteur = 0

#     for i in range(1, n + 1):
#         if gcd(i, n) == 1:
#             compteur += 1

#     return compteur


# # ==========================================
# # 6. INVERSE MODULAIRE
# # ==========================================

# def inverse_modulaire(a, n):

#     if n <= 1:
#         return None

#     pgcd, u, v = euclide_etendu(a, n)

#     if pgcd != 1:
#         return None

#     return u % n





# @app.route("/", methods=["GET", "POST"])
# def calcul():

#     # Initialisation des résultats
#     pgcd = None
#     ppcm = None
#     etapes = []
#     etapes_ppcm = []

#     bezout = None
#     fermat = None
#     congruence = None
#     euler = None
#     inverse = None

#     a = None
#     b = None
#     n = None
#     base = None
#     exposant = None
#     modulo = None
#     resultat = None

#     erreur = None
#     operation = "pgcd_ppcm"

#     if request.method == "POST":

#         operation = request.form.get("operation", "pgcd_ppcm")

#         try:

#             # ==================================
#             # 1. PGCD - PPCM
#             # ==================================

#             if operation == "pgcd_ppcm":

#                 a = int(request.form["nombre_a"])
#                 b = int(request.form["nombre_b"])

#                 x, y = abs(a), abs(b)

#                 while y != 0:

#                     quotient = x // y
#                     reste = x % y

#                     etapes.append({
#                         "dividende": x,
#                         "diviseur": y,
#                         "quotient": quotient,
#                         "reste": reste
#                     })

#                     x, y = y, reste

#                 pgcd = x

#                 if a == 0 or b == 0:
#                     ppcm = 0

#                 else:
#                     # ppcm = abs(a * b) // pgcd
#                     nombre_a = abs(a)
#                     nombre_b = abs(b)

#                     pas = max(nombre_a, nombre_b)
#                     multiple = pas

#                     while (multiple % nombre_a != 0
#                         or multiple % nombre_b != 0):

#                         etapes_ppcm.append({
#                             "multiple": multiple,
#                             "divisible_a": multiple % nombre_a == 0,
#                             "divisible_b": multiple % nombre_b == 0
#                         })

#                         multiple += pas

#                     # Enregistrer le premier multiple commun trouvé
#                     etapes_ppcm.append({
#                         "multiple": multiple,
#                         "divisible_a": True,
#                         "divisible_b": True
#                     })

#                     ppcm = multiple

#             # ==================================
#             # 2. CONGRUENCE - FERMAT
#             # ==================================

#             elif operation == "congruence_fermat":

#                 base = int(request.form["base"])
#                 exposant = int(request.form["exposant"])
#                 modulo = int(request.form["modulo"])

#                 if exposant < 0:
#                     raise ValueError("L'exposant doit être positif ou nul.")

#                 if modulo < 2:
#                     raise ValueError("Le modulo doit être supérieur ou égal à 2.")

#                 # Calcul de la congruence
#                 resultat = pow(base, exposant, modulo)

#                 congruence = {
#                     "message": (
#                         f"{base}^{exposant} ≡ {resultat} (mod {modulo})"
#                     )
#                 }

#                 # Test de Fermat
#                 fermat = petit_fermat(base, modulo)

#                 primalite = fermat["message"]

#                 fermat_steps = [
#                     f"Calcul de {base}^{exposant} modulo {modulo}",
#                     f"Résultat de la puissance modulaire : {resultat}"
#                 ]

#                 if fermat["premier"] and base % modulo != 0:

#                     fermat_steps.append(
#                         f"Selon Fermat : {base}^({modulo}-1) ≡ 1 (mod {modulo})"
#                     )

#                     fermat_steps.append(
#                         f"Vérification : {pow(base, modulo-1, modulo)}"
#                     )

#                 elif fermat["premier"]:

#                     fermat_steps.append(
#                         "Le théorème ne s'applique pas car la base est divisible par le modulo."
#                     )

#                             base = int(request.form["base"])
#                             exposant = int(request.form["exposant"])
#                             modulo = int(request.form["modulo"])

#                             if modulo <= 0:
#                                 raise ValueError("Le modulo doit être positif.")

#                             # Test de primalité du modulo
#                             fermat = petit_fermat(base, modulo)

#                             # Calcul direct de la puissance modulo
#                             resultat = pow(base, exposant, modulo)

#                             congruence = {
#                                 "base": base,
#                                 "exposant": exposant,
#                                 "modulo": modulo,
#                                 "resultat": resultat,
#                                 "message": (
#                                     f"{base}^{exposant} ≡ "
#                                     f"{resultat} (mod {modulo})"
#                                 )
#                             }

#             # ==================================
#             # 3. BEZOUT
#             # ==================================

#             elif operation == "bezout":

#             a = int(request.form["bezout_a"])
#             b = int(request.form["bezout_b"])

#             pgcd_b, u, v = euclide_etendu(a, b)

#             bezout = {
#                 "a": a,
#                 "b": b,
#                 "pgcd": pgcd_b,
#                 "u": u,
#                 "v": v
#             }
#             # ==================================
#             # 4. INDICATRICE D'EULER
#             # ==================================

#             elif operation == "indicatrice_euler":

#                 n = int(request.form["euler_n"])

#                 if n < 1:
#                     raise ValueError("n doit être positif.")

#                 euler = indicatrice_euler(n)

#             # ==================================
#             # 5. INVERSE MODULAIRE
#             # ==================================

#             elif operation == "inverse_modulaire":

#                 a = int(request.form["inverse_a"])
#                 n = int(request.form["inverse_n"])

#                 if n <= 1:
#                     raise ValueError("Le modulo doit être supérieur à 1.")

#                 pgcd = gcd(a, n)

#                 inverse = inverse_modulaire(a, n)

#             # ==================================
#             # 6. CHIFFREMENT RSA
#             # ==================================

#             elif operation == "chiffrements_rsa":

#                 p = int(request.form["rsa_p"])
#                 q = int(request.form["rsa_q"])
#                 e = int(request.form["rsa_e"])
#                 message = int(request.form["rsa_message"])

#                 if not est_premier(p) or not est_premier(q) or p == q:
#                     raise ValueError("p et q doivent être deux nombres premiers distincts.")

#                 rsa_n = p * q
#                 phi = (p - 1) * (q - 1)

#                 if gcd(e, phi) != 1:
#                     raise ValueError("e doit être premier avec φ(n).")

#                 d = inverse_modulaire(e, phi)

#                 if not 0 <= message < rsa_n:
#                     raise ValueError("Le message doit vérifier 0 ≤ M < n.")

#                 cipher = pow(message, e, rsa_n)
#                 decrypted = pow(cipher, d, rsa_n)

#                 rsa_result = {
#                     "n": rsa_n,
#                     "phi": phi,
#                     "e": e,
#                     "d": d,
#                     "message": message,
#                     "cipher": cipher,
#                     "decrypted": decrypted
#                 }

#             else:
#                 raise ValueError("Opération inconnue.")

#         except (ValueError, KeyError, ZeroDivisionError) as e:
#             erreur = str(e)

#     else:
#         rsa_result = None

#     return render_template(
#         "index.html",

#         operation=operation,

#         pgcd=pgcd,
#         ppcm=ppcm,
#         a=a,
#         b=b,

#         etapes=etapes,
#         etapes_ppcm=etapes_ppcm,

#         bezout=bezout,
#         fermat=fermat,
#         congruence=congruence,

#         euler=euler,
#         euler_n=n,

#         inverse=inverse,
#         inverse_a=a,
#         inverse_n=n,

#         base=base,
#         exposant=exposant,
#         modulo=modulo,
#         resultat=resultat,

#         rsa_result=locals().get("rsa_result"),

#         erreur=erreur
#     )


# if __name__ == "__main__":
#     app.run(debug=True)



from flask import Flask, render_template, request
from math import gcd

app = Flask(__name__)


# ==========================================
# 1. ALGORITHME D'EUCLIDE ET BEZOUT
# ==========================================


def euclide_etendu(a, b):

    # Valeurs initiales
    original_a = a
    original_b = b

    etapes = []

    # Cas particulier
    if a == 0 and b == 0:
        return 0, 0, 0, etapes

    # Initialisation des coefficients
    r0, r1 = abs(a), abs(b)

    u0, u1 = 1, 0
    v0, v1 = 0, 1

    # Algorithme d'Euclide étendu
    while r1 != 0:

        quotient = r0 // r1
        reste = r0 % r1

        etapes.append({
            "r0": r0,
            "r1": r1,
            "quotient": quotient,
            "reste": reste,
            "u0": u0,
            "u1": u1,
            "v0": v0,
            "v1": v1
        })

        r0, r1 = r1, reste

        u0, u1 = u1, u0 - quotient * u1
        v0, v1 = v1, v0 - quotient * v1

    # Correction des signes
    if original_a < 0:
        u0 = -u0

    if original_b < 0:
        v0 = -v0

    return r0, u0, v0, etapes
# ==========================================
# 2. TEST DE PRIMALITE
# ==========================================

def est_premier(n):

    if n < 2:
        return False

    if n == 2:
        return True

    if n % 2 == 0:
        return False

    for i in range(3, int(n ** 0.5) + 1, 2):
        if n % i == 0:
            return False

    return True


# ==========================================
# 3. PETIT THEOREME DE FERMAT
# ==========================================

def petit_fermat(a, p):

    if not est_premier(p):
        return {
            "premier": False,
            "message": f"{p} n'est pas premier."
        }

    if a % p == 0:
        return {
            "premier": True,
            "message": (
                "Le théorème nécessite que a ne soit "
                "pas divisible par p."
            )
        }

    resultat = pow(a, p - 1, p)

    return {
        "premier": True,
        "resultat": resultat,
        "message": f"{a}^{p - 1} ≡ {resultat} (mod {p})"
    }


# ==========================================
# 4. RESOLUTION DE CONGRUENCE
# ax ≡ b (mod n)
# ==========================================

def resoudre_congruence(a, b, n):

    if n <= 0:
        return {
            "erreur": "Le module n doit être positif."
        }

    d = gcd(abs(a), n)

    if b % d != 0:
        return {
            "erreur": "Cette congruence ne possède aucune solution."
        }

    a_reduit = a // d
    b_reduit = b // d
    n_reduit = n // d

    pgcd, u, v = euclide_etendu(a_reduit, n_reduit)

    x0 = (u * b_reduit) % n_reduit

    solutions = [
        x0 + k * n_reduit
        for k in range(d)
    ]

    return {
        "pgcd": d,
        "x0": x0,
        "solutions": solutions,
        "module_reduit": n_reduit,
        "message": "Congruence résolue avec succès."
    }


# ==========================================
# 5. INDICATRICE D'EULER
# ==========================================

# def indicatrice_euler(n):

#     if n < 1:
#         return None

#     compteur = 0

#     for i in range(1, n + 1):
#         if gcd(i, n) == 1:
#             compteur += 1

#     return compteur

def indicatrice_euler(n):

    if n < 1:
        raise ValueError("n doit être positif.")

    facteurs = []
    nombre = n
    diviseur = 2

    # 1. Décomposition en facteurs premiers
    while diviseur * diviseur <= nombre:

        if nombre % diviseur == 0:

            exposant = 0

            while nombre % diviseur == 0:
                nombre //= diviseur
                exposant += 1

            facteurs.append((diviseur, exposant))

        diviseur += 1 if diviseur == 2 else 2

    if nombre > 1:
        facteurs.append((nombre, 1))

    # 2. Factorisation
    if facteurs:
        factorisation = " × ".join(
            f"{p}^{e}" if e > 1 else str(p)
            for p, e in facteurs
        )
    else:
        factorisation = "1"

    # 3. Préparation des étapes
    etapes = []

    etapes.append({
        "titre": "Décomposition en facteurs premiers",
        "description": f"{n} = {factorisation}"
    })

    etapes.append({
        "titre": "Formule de l'indicatrice d'Euler",
        "description": "φ(n) = n × ∏(1 - 1/p)"
    })

    # 4. Application de la formule
    formule = f"φ({n}) = {n}"

    for p, exposant in facteurs:
        formule += f" × (1 - 1/{p})"

    etapes.append({
        "titre": "Remplacement des facteurs premiers",
        "description": formule
    })

    # 5. Calcul progressif
    resultat = n

    for p, exposant in facteurs:

        ancienne_valeur = resultat

        resultat = resultat * (p - 1) // p

        etapes.append({
            "titre": f"Application du facteur premier {p}",
            "description": (
                f"{ancienne_valeur} × ({p} - 1) / {p} "
                f"= {resultat}"
            )
        })

    # 6. Recherche des entiers premiers avec n
    coprimes = []

    for i in range(1, n + 1):
        if gcd(i, n) == 1:
            coprimes.append(i)

    # 7. Résultat final
    etapes.append({
        "titre": "Résultat final",
        "description": f"φ({n}) = {resultat}"
    })

    return {
        "resultat": resultat,
        "factorisation": factorisation,
        "facteurs": facteurs,
        "coprimes": coprimes,
        "etapes": etapes
    }

# ==========================================
# 6. INVERSE MODULAIRE
# ==========================================

# def inverse_modulaire(a, n):

#     if n <= 1:
#         return None

#     pgcd, u, v = euclide_etendu(a, n)

#     if pgcd != 1:
#         return None

#     return u % n

def inverse_modulaire(a, n):

    if n <= 1:
        return None

    # Calcul de l'algorithme d'Euclide étendu
    pgcd, u, v, divisions = euclide_etendu(a, n)

    if pgcd != 1:
        return {
            "existe": False,
            "pgcd": pgcd,
            "message": (
                f"L'inverse modulaire n'existe pas car "
                f"PGCD({a}, {n}) = {pgcd} ≠ 1."
            ),
            "etapes": [
                f"Calcul du PGCD({a}, {n}).",
                f"PGCD({a}, {n}) = {pgcd}.",
                "Comme le PGCD est différent de 1, "
                "l'inverse modulaire n'existe pas."
            ]
        }

    # Liste des étapes
    etapes = []

    # ETAPE 1 : Divisions euclidiennes
    etapes.append("1. ALGORITHME D'EUCLIDE")

    for i, division in enumerate(divisions):

        etapes.append(
            f"{division['r0']} = "
            f"{division['r1']} × "
            f"{division['quotient']} + "
            f"{division['reste']}"
        )

    # ETAPE 2 : PGCD
    etapes.append(
        f"2. PGCD({a}, {n}) = 1"
    )

    # ETAPE 3 : Identité de Bézout
    etapes.append("3. IDENTITE DE BEZOUT")

    etapes.append(
        f"{a} × ({u}) + {n} × ({v}) = 1"
    )

    # ETAPE 4 : Calcul de l'inverse
    etapes.append("4. CALCUL DE L'INVERSE MODULAIRE")

    etapes.append(
        f"{a} × ({u}) ≡ 1 (mod {n})"
    )

    inverse = u % n

    etapes.append(
        f"Inverse = {u} mod {n} = {inverse}"
    )

    # ETAPE 5 : Vérification
    verification = (a * inverse) % n

    etapes.append("5. VERIFICATION")

    etapes.append(
        f"({a} × {inverse}) mod {n} = {verification}"
    )

    return {
        "existe": True,
        "inverse": inverse,
        "pgcd": pgcd,
        "u": u,
        "v": v,
        "verification": verification,
        "etapes": etapes,
        "message": "Inverse modulaire calculé avec succès."
    }

def etapes_bezout(a, b):

    x = abs(a)
    y = abs(b)

    divisions = []

    # Étape 1 : divisions euclidiennes
    while y != 0:

        quotient = x // y
        reste = x % y

        divisions.append({
            "dividende": x,
            "diviseur": y,
            "quotient": quotient,
            "reste": reste
        })

        x, y = y, reste

    # Étape 2 : calcul des coefficients
    pgcd, u, v = euclide_etendu(a, b)

    # Gestion des signes
    if a < 0:
        u = -u

    if b < 0:
        v = -v

    return {
        "divisions": divisions,
        "pgcd": pgcd,
        "u": u,
        "v": v,
        "verification": a * u + b * v
    }

# ==========================================
# 7. ROUTE PRINCIPALE
# ==========================================

@app.route("/", methods=["GET", "POST"])
def calcul():

    # Initialisation des résultats
    pgcd = None
    ppcm = None

    etapes = []
    etapes_ppcm = []

    bezout = None
    fermat = None
    congruence = None
    fermat_steps = []
    primalite = None

    euler = None
    inverse = None

    a = None
    b = None
    n = None

    base = None
    exposant = None
    modulo = None
    resultat = None

    inverse = None
    inverse_result = None
    inverse_steps = []
    inverse_message = None
    inverse_verification = None

    rsa_result = None
    erreur = None

    operation = "pgcd_ppcm"

    if request.method == "POST":

        operation = request.form.get(
            "operation",
            "pgcd_ppcm"
        )

        try:

            # ==================================
            # 1. PGCD - PPCM
            # ==================================

            if operation == "pgcd_ppcm":

                a = int(request.form["nombre_a"])
                b = int(request.form["nombre_b"])

                x, y = abs(a), abs(b)

                # Algorithme d'Euclide
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

                # Calcul du PPCM par recherche des multiples
                if a == 0 or b == 0:

                    ppcm = 0

                else:

                    nombre_a = abs(a)
                    nombre_b = abs(b)

                    pas = max(nombre_a, nombre_b)
                    multiple = pas

                    while (
                        multiple % nombre_a != 0
                        or multiple % nombre_b != 0
                    ):

                        etapes_ppcm.append({
                            "multiple": multiple,
                            "divisible_a": (
                                multiple % nombre_a == 0
                            ),
                            "divisible_b": (
                                multiple % nombre_b == 0
                            )
                        })

                        multiple += pas

                    etapes_ppcm.append({
                        "multiple": multiple,
                        "divisible_a": True,
                        "divisible_b": True
                    })

                    ppcm = multiple

            # ==================================
            # 2. CONGRUENCE - FERMAT
            # ==================================

            elif operation == "congruence_fermat":

                base = int(request.form["base"])
                exposant = int(request.form["exposant"])
                modulo = int(request.form["modulo"])

                if exposant < 0:
                    raise ValueError(
                        "L'exposant doit être positif ou nul."
                    )

                if modulo < 2:
                    raise ValueError(
                        "Le modulo doit être supérieur ou égal à 2."
                    )

                # Calcul de la congruence
                resultat = pow(base, exposant, modulo)

                congruence = {
                    "base": base,
                    "exposant": exposant,
                    "modulo": modulo,
                    "resultat": resultat,
                    "message": (
                        f"{base}^{exposant} ≡ "
                        f"{resultat} (mod {modulo})"
                    )
                }

                # Test du petit théorème de Fermat
                fermat = petit_fermat(base, modulo)

                primalite = fermat["message"]

                fermat_steps = [
                    f"Base : {base}",
                    f"Exposant : {exposant}",
                    f"Modulo : {modulo}",
                    (
                        f"Calcul : {base}^{exposant} "
                        f"modulo {modulo}"
                    ),
                    f"Résultat : {resultat}"
                ]

                if fermat["premier"] and base % modulo != 0:

                    fermat_steps.append(
                        f"Selon Fermat : {base}^({modulo}-1) "
                        f"≡ 1 (mod {modulo})"
                    )

                    fermat_steps.append(
                        "Vérification : "
                        f"{pow(base, modulo - 1, modulo)}"
                    )

                elif fermat["premier"]:

                    fermat_steps.append(
                        "Le théorème ne s'applique pas car "
                        "la base est divisible par le modulo."
                    )

                else:

                    fermat_steps.append(
                        "Le petit théorème de Fermat "
                        "ne peut pas être appliqué."
                    )

            # ==================================
            # 3. BEZOUT
            # ==================================

            # elif operation == "bezout":

                a = int(request.form["bezout_a"])
                b = int(request.form["bezout_b"])

                pgcd_b, u, v = euclide_etendu(a, b)

                bezout = {
                    "a": a,
                    "b": b,
                    "pgcd": pgcd_b,
                    "u": u,
                    "v": v
                }
            
            elif operation == "bezout":

                a = int(request.form["bezout_a"])
                b = int(request.form["bezout_b"])

                # Test de primalité des deux nombres
                premier_a = est_premier(abs(a))
                premier_b = est_premier(abs(b))

                # Algorithme d'Euclide étendu
                pgcd_b, u, v, bezout_steps = euclide_etendu(a, b)

                bezout = {
                    "a": a,
                    "b": b,
                    "pgcd": pgcd_b,
                    "u": u,
                    "v": v,
                    "premier_a": premier_a,
                    "premier_b": premier_b,
                    "etapes": bezout_steps
                }

            # ==================================
            # 4. INDICATRICE D'EULER
            # ==================================

            elif operation == "indicatrice_euler":

                n = int(request.form["euler_n"])

                if n < 1:
                    raise ValueError(
                        "n doit être positif."
                    )

                euler = indicatrice_euler(n)

            # ==================================
            # 5. INVERSE MODULAIRE
            # ==================================

            # elif operation == "inverse_modulaire":

            #     a = int(request.form["inverse_a"])
            #     n = int(request.form["inverse_n"])

            #     if n <= 1:
            #         raise ValueError(
            #             "Le modulo doit être supérieur à 1."
            #         )

            #     pgcd = gcd(a, n)

            #     inverse = inverse_modulaire(a, n)

            

            #     if n <= 1:
            #         return None

            #     # Calcul de l'algorithme d'Euclide étendu
            #     pgcd, u, v, divisions = euclide_etendu(a, n)

            #     if pgcd != 1:
            #         return {
            #             "existe": False,
            #             "pgcd": pgcd,
            #             "message": (
            #                 f"L'inverse modulaire n'existe pas car "
            #                 f"PGCD({a}, {n}) = {pgcd} ≠ 1."
            #             ),
            #             "etapes": [
            #                 f"Calcul du PGCD({a}, {n}).",
            #                 f"PGCD({a}, {n}) = {pgcd}.",
            #                 "Comme le PGCD est différent de 1, "
            #                 "l'inverse modulaire n'existe pas."
            #             ]
            #         }

            #     # Liste des étapes
            #     etapes = []

            #     # ETAPE 1 : Divisions euclidiennes
            #     etapes.append("1. ALGORITHME D'EUCLIDE")

            #     for i, division in enumerate(divisions):

            #         etapes.append(
            #             f"{division['r0']} = "
            #             f"{division['r1']} × "
            #             f"{division['quotient']} + "
            #             f"{division['reste']}"
            #         )

            #     # ETAPE 2 : PGCD
            #     etapes.append(
            #         f"2. PGCD({a}, {n}) = 1"
            #     )

            #     # ETAPE 3 : Identité de Bézout
            #     etapes.append("3. IDENTITE DE BEZOUT")

            #     etapes.append(
            #         f"{a} × ({u}) + {n} × ({v}) = 1"
            #     )

            #     # ETAPE 4 : Calcul de l'inverse
            #     etapes.append("4. CALCUL DE L'INVERSE MODULAIRE")

            #     etapes.append(
            #         f"{a} × ({u}) ≡ 1 (mod {n})"
            #     )

            #     inverse = u % n

            #     etapes.append(
            #         f"Inverse = {u} mod {n} = {inverse}"
            #     )

            #     # ETAPE 5 : Vérification
            #     verification = (a * inverse) % n

            #     etapes.append("5. VERIFICATION")

            #     etapes.append(
            #         f"({a} × {inverse}) mod {n} = {verification}"
            #     )

            #     return {
            #         "existe": True,
            #         "inverse": inverse,
            #         "pgcd": pgcd,
            #         "u": u,
            #         "v": v,
            #         "verification": verification,
            #         "etapes": etapes,
            #         "message": "Inverse modulaire calculé avec succès."
            #     }
            elif operation == "inverse_modulaire":

                a = int(request.form["inverse_a"])
                n = int(request.form["inverse_n"])

                if n <= 1:
                    raise ValueError(
                        "Le modulo doit être supérieur à 1."
                    )

                # Appel de la fonction inverse_modulaire()
                inverse = inverse_modulaire(a, n)

                # Récupération des résultats
                pgcd = inverse["pgcd"]
                inverse_result = inverse.get("inverse")
                inverse_steps = inverse["etapes"]
                inverse_message = inverse["message"]
                inverse_verification = inverse.get("verification")

            # ==================================
            # 6. CHIFFREMENT RSA
            # ==================================

            elif operation == "chiffrements_rsa":

                p = int(request.form["rsa_p"])
                q = int(request.form["rsa_q"])
                e = int(request.form["rsa_e"])
                message = int(request.form["rsa_message"])

                if (
                    not est_premier(p)
                    or not est_premier(q)
                    or p == q
                ):
                    raise ValueError(
                        "p et q doivent être deux nombres "
                        "premiers distincts."
                    )

                rsa_n = p * q
                phi = (p - 1) * (q - 1)

                if gcd(e, phi) != 1:
                    raise ValueError(
                        "e doit être premier avec φ(n)."
                    )

                if e < 2:
                    raise ValueError(
                        "e doit être supérieur ou égal à 2."
                    )

                d = inverse_modulaire(e, phi)

                if not 0 <= message < rsa_n:
                    raise ValueError(
                        "Le message doit vérifier 0 ≤ M < n."
                    )

                cipher = pow(message, e, rsa_n)
                decrypted = pow(cipher, d, rsa_n)

                rsa_result = {
                    "n": rsa_n,
                    "phi": phi,
                    "e": e,
                    "d": d,
                    "message": message,
                    "cipher": cipher,
                    "decrypted": decrypted
                }

            else:

                raise ValueError(
                    "Opération inconnue."
                )

        except (ValueError, KeyError, ZeroDivisionError) as e:

            erreur = str(e)

    # ==========================================
    # TRANSMISSION DES VARIABLES AU HTML
    # ==========================================

    return render_template(
        "index.html",

        operation=operation,

        # PGCD - PPCM
        pgcd=pgcd,
        ppcm=ppcm,
        a=a,
        b=b,
        etapes=etapes,
        etapes_ppcm=etapes_ppcm,

        # BEZOUT
        bezout=bezout,

        # FERMAT - CONGRUENCE
        fermat=fermat,
        congruence=congruence,
        primalite=primalite,
        fermat_steps=fermat_steps,

        base=base,
        exposant=exposant,
        modulo=modulo,
        resultat=resultat,

        # EULER
        # euler=euler,
        # euler_n=n,

        euler=euler,

        euler_n=n,

        euler_result=(
            euler["resultat"] if euler else None
        ),

        euler_factorisation=(
            euler["factorisation"] if euler else None
        ),

        euler_coprimes=(
            euler["coprimes"] if euler else None
        ),

        euler_etapes=(
            euler["etapes"] if euler else []
        ),

        # INVERSE MODULAIRE
        # inverse=inverse,
        # inverse_a=a,
        # inverse_n=n,
        inverse=inverse,
        inverse_a=a,
        inverse_n=n,

        inverse_result=(
            inverse.get("inverse") if inverse else None
        ),

        inverse_steps=(
            inverse.get("etapes", []) if inverse else []
        ),

        inverse_message=(
            inverse.get("message") if inverse else None
        ),

        inverse_verification=(
            inverse.get("verification") if inverse else None
        ),

        # RSA
        rsa_result=rsa_result,

        # ERREURS
        erreur=erreur
    )


# ==========================================
# 8. LANCEMENT DE L'APPLICATION
# ==========================================

if __name__ == "__main__":
    app.run(debug=True)
