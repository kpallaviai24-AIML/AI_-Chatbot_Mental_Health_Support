
import json

with open("database/medicine_data.json", "r") as f:
    medicines = json.load(f)

def generate_ai_response(question):

    question = question.lower()

    # Category search
    for med, data in medicines.items():
        if data["category"].lower() in question:
            matching = [
                m.title() for m, d in medicines.items()
                if d["category"] == data["category"]
            ]

            return f"Medicines in category {data['category']}: " + ", ".join(matching)

    # Medicine search
    for med, data in medicines.items():

        if med in question:

            return f'''
Medicine: {med.title()}

Category:
{data["category"]}

Uses:
{", ".join(data["uses"])}

Precautions:
{", ".join(data["precautions"])}

Side Effects:
{", ".join(data["side_effects"])}

Disclaimer:
Educational purposes only.
Consult doctor before taking medicines.
'''

    return "Medicine not found in database."
