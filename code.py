import csv
import re

with open("kody pocztowe.csv", 'r') as csvfile:
    csv_reader = csv.reader(csvfile, delimiter=';')
    pattern = re.compile(r"\d{2}-\d{3}")  # Regex dla polskich kodow

    range_min = input("Podaj kod pocztowy zaczynajacy zakres od w formacie xx-xxx: \n")
    while not re.fullmatch(pattern, range_min):
        print("Podany kod jest bledny, wpisz jeszcze raz!")
        range_min = input("Podaj kod pocztowy zaczynajacy zakres od w formacie xx-xxx: \n")

    range_max = input("Podaj kod pocztowy konczacy zakres: \n")
    while not re.fullmatch(pattern, range_max):
        print("Podany kod jest bledny, wpisz jeszcze raz!")
        range_max = input("Podaj kod pocztowy konczacy zakres: \n")

    control = 0  # Dodane aby zaczynać od drugiego wiersza, pierwszy to nazwa kolumny

    def string_to_int(n):
        removed_sign = int(n.replace('-', ''))
        return int(removed_sign)

    x = string_to_int(range_min)
    y = string_to_int(range_max)

    for row in csv_reader:
        if control != 1:
            control += 1
        elif x <= (string_to_int(row[0])) <= y:
            print(row[0], row[1], row[2])
