from flask import Flask, render_template, request

app = Flask(__name__)


@app.route("/", methods=["GET", "POST"])
def index():
     if request.method == "POST":
          health_concern = request.form.get("symptoms")
          if health_concern == "flu":
               return render_template("symptoms.html")
          elif health_concern == "solar burn":
               return render_template("solar_burn.html")
          else:
               return render_template("smoking_cessation.html")
     else:
          return render_template("index.html")

@app.route("/symptoms", methods=["GET", "POST"])
def symptoms():
     if request.method == "POST":
          symptoms = request.form.getlist("symptoms")
          if not symptoms:
               return render_template("apology.html")
          else:
               symptoms_and_medicines = [
                    {"symptom": "Dry cough", "medicine": "Antitussive", "contraindications": "Chesty cough"},
                    {"symptom": "Chesty cough", "medicine": "Expectorant", "contraindications": "Renal insufficiency, asthma"},
                    {"symptom": "Fever", "medicine": "Antipyretic", "contraindications": "Renal or liver insufficiency"},
                    {"symptom": "Congested nose", "medicine": "Nasal decongestant", "contraindications": "High blood pressure, hyperthyroidism, enlarged prostate gland, glaucoma"},
                    {"symptom": "Rhinorrhea", "medicine": "Antihistamine", "contraindications": "Glaucoma, enlarged prostate gland, breathing problems"},
                    {"symptom": "Sore throat", "medicine": "Anti-inflammatory", "contraindications": "Renal or liver insufficiency, asthma, high blood pressure, stomach problems"}
               ]

               final_list = []

               for medicine in symptoms_and_medicines:
                    if medicine["symptom"] in symptoms:
                         final_list.append(medicine)

               return render_template("medicine.html", final_list=final_list)
     else:
          return render_template("symptoms.html")

@app.route("/measures")
def measures():
     return render_template("measures.html")

@app.route("/smoking_cessation", methods=["GET", "POST"])
def smoking_cessation():
     if request.method == "POST":
          dosage = request.form.get("smoking")
          if dosage == "more":
               return render_template("dosage_more.html")
          else:
               return render_template("dosage_less.html", dosage=dosage)
     else:
          return render_template("smoking_cessation.html")

@app.route("/measures_smoking")
def measures_smoking():
     return render_template("measures_smoking.html")

@app.route("/measures_solarburn")
def measures_solarburn():
     return render_template("measures_solarburn.html")