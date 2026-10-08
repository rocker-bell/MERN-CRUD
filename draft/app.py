# 1. ADDED: imported 'render_template' alongside Flask
from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def home():
    return "Hello Flask!"

@app.route("/pgcd")
def pgcd_calculator():
    p = "p_value"
    q = "q_value"
    r = "r_value"
    langs = ["Python", "Flask", "Math"] # Added so your loop has data

    # 2. FIXED: Changed 'render.template' to 'render_template'
    return render_template(
        "index.html", 
        quotion=q, 
        reste=r, 
        poton=p, 
        programming_languages=langs
    )

if __name__ == "__main__":
    app.run(debug=True)
