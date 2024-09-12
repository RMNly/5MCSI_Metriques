from flask import Flask, render_template_string, render_template, jsonify
from flask import render_template
from flask import json
from datetime import datetime
from urllib.request import urlopen
import sqlite3
                                                                                                                                       
app = Flask(__name__)                                                                                                                  
                                                                                                                                       
@app.route('/')
def hello_world():
    return render_template('hello.html')#comm

@app.route("/contact/")
def MaPremiereAPI():
    return render_template('contact.html')

@app.route('/tawarano/')
def meteo():
    response = urlopen('https://samples.openweathermap.org/data/2.5/forecast?lat=0&lon=0&appid=xxx')
    raw_content = response.read()
    json_content = json.loads(raw_content.decode('utf-8'))
    results = []
    for list_element in json_content.get('list', []):
        dt_value = list_element.get('dt')
        temp_day_value = list_element.get('main', {}).get('temp') - 273.15 # Conversion de Kelvin en °c 
        results.append({'Jour': dt_value, 'temp': temp_day_value})
    return jsonify(results=results)

@app.route("/rapport/")
def mongraphique():
    return render_template("graphique.html")

@app.route("/histogramme/")
def monhistogramme():
    return render_template("histogramme.html")
  
@app.route("/contact/")
def contact():
    return render_template("Contact.html")

@app.route("/send_message/", methods=["POST"])
def send_message():
    first_name = request.form.get("first_name")
    last_name = request.form.get("last_name")
    message = request.form.get("message")
    
    # Vous pouvez ici traiter le message ou l'envoyer par email.
    # Pour cet exemple, nous redirigeons simplement l'utilisateur vers la page de contact avec un message de confirmation.
    
    # Note: Pour un vrai site, vous devriez valider et traiter les données du formulaire.
    print(f"Message reçu de {first_name} {last_name}: {message}")

    return redirect(url_for('contact'))

@app.route("/commits/")
def MonAPI():
    return render_template('commits.html')
  
if __name__ == "__main__":
  app.run(debug=True)
