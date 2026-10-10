from pyscript import document
from pyodide.ffi import create_proxy

def submit_form(event):
    event.preventDefault()

    name = document.querySelector("#username").value
    document.querySelector("#result").innerText = (
        f"Submitted successfully! Hello, {name}"
    )

def trigger_submit(event):
    document.querySelector("#myForm").requestSubmit()

form = document.querySelector("#myForm")
button = document.querySelector("#submitBtn")

form.addEventListener("submit", create_proxy(submit_form))

# Trigger submission from Python
# Uncomment this line to submit automatically:
# form.requestSubmit()

# Example: attach another button or call trigger_submit()