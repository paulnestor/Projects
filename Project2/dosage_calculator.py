import sys
import statistics
import colorama
from colorama import Fore
colorama.init(autoreset=True)
import csv

side_effect_list = []
contraindications_list = []

def main():
    age = int(input("Age (years): "))
    validate_age(age)

    weight = int(input("Weight (kg): "))
    validate_weight(weight)

    print()
    drugs = ["[A] - Clavamox DT",
             "[B] - Clamoxyl",
             "[C] - Klacid",
             "[D] - Ben-U-Ron",
             "[E] - Aerius"
             ]
    print("Which medicine was prescribed?")
    print()
    print(*drugs, sep="\n")
    print()
    medicine = input("Write the name of the medicine prescribed: ").lower()
    validate_medicine(medicine)

    print()
    print(dosage(medicine, weight, age))

    print()
    print(side_effect(medicine))

    print()
    print(contraindication(medicine))

    if medicine == "clavamox dt":
        print()
        print("The medicine needs to be stored in the fridge after being prepared!")

def validate_age(v):
    if v >= 12:
        print()
        sys.exit("Should be taking pills, not syrup!")

def validate_weight(w):
     if w >= 40:
        print()
        sys.exit("Should be taking pills, not syrup!")

def validate_medicine(m):
    if m not in ["clavamox dt", "clamoxyl", "klacid", "ben-u-ron", "aerius"]:
        raise ValueError("Name of the medicine not in the list given or name incorrectly written")

    if m == "clavamox dt" or m == "clamoxyl":
        print()
        answer = input("Is the person allergic to penicillin? (yes/no) ").lower()
        if answer == "yes":
            print()
            sys.exit(Fore.RED + "Taking this antibiotic could cause a severe allergic reaction. Talk to the phisician!")
        else:
            pass

def dosage(x, z, i):
    if x == "clavamox dt":
        minimum_dosage_a = float(((z * 25) * 5 / 400) / 2)
        maximum_dosage_a = float(((z * 45) * 5 / 400) / 2)
        dosages_a = [minimum_dosage_a, maximum_dosage_a]
        medium_dosage_a = statistics.fmean(dosages_a)
        return f"Minimum dosage = {minimum_dosage_a:,.1f}ml twice a day \nMedium dosage = {medium_dosage_a:,.1f}ml twice a day \nMaximum dosage = {maximum_dosage_a:,.1f}ml twice a day"

    if x == "clamoxyl":
        minimum_dosage_b = float(((z * 20) * 5 / 250) / 2)
        maximum_dosage_b = float(((z * 100) * 5 / 250) / 2)
        dosages_b = [minimum_dosage_b, maximum_dosage_b]
        medium_dosage_b = statistics.fmean(dosages_b)
        return f"Minimum dosage = {minimum_dosage_b:,.1f}ml twice a day \nMedium dosage = {medium_dosage_b:,.1f}ml twice a day \nMaximum dosage = {maximum_dosage_b:,.1f}ml twice a day"

    if x == "klacid":
        dosage_c = float((z * 7.5) / 50)
        return f"Dosage = {dosage_c:,.1f}ml twice a day"

    if x == "ben-u-ron":
        minimum_dosage_d = float((z * 15) / 40)
        maximum_dosage_d = float((z * 20) / 40)
        return f"Should administrate between {minimum_dosage_d:,.1f}ml every 6h or {maximum_dosage_d:,.1f}ml every 8h"

    if x == "aerius":
        if 1 <= i <= 5:
            return f"Should administrate 2.5ml once a day, at night"
        elif 6 <= i <= 11:
            return f"Should administrate 5ml once a day, at night"

def side_effect(y):
    with open("medicines.csv") as file:
        reader = csv.DictReader(file)
        for row in reader:
            side_effect_list.append({"medicines": row["medicines"], "side effects": row["side effects"]})

        for effect in side_effect_list:
            if effect["medicines"] == y:
                return f"Major side effects are {effect['side effects']}"

def contraindication(a):
    with open("medicines.csv") as file:
        reader = csv.DictReader(file)
        for row in reader:
            contraindications_list.append({"medicines": row["medicines"], "contraindications": row["contraindications"]})

        for contra in contraindications_list:
            if contra["medicines"] == a:
                return f"Major contraindications are {contra['contraindications']}"

if __name__ == "__main__":
    main()