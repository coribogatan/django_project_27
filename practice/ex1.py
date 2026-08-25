# Primind această listă de numere:
#
# numbers = [13, 40, 95, 1, 44, 3, 21, 34, 45, 66, 13, 17],
#
# Si lista de persoane:
#
# people = ["Codrin", "Adrian", "John", "Maria", "Tudor", "Maximilian", "Spike"]
#  Creati o functie care returnează: o lista de dicționare, care arată astfel:
#
# result = { "name": "Codrin", "age": 30, "of_age": True}
#
# Pentru fiecare persoană, alegeți un număr random din lista de numere.
# Unde of_age este true doar daca numărul ales este mai mare de 18
#
# import random
# picked = random.choice(numbers)
#
# Creati o altă funcție care filtrează toate persoanele și returnează doar persoanele of_age.
# Creați oldest_person, o funcție care returnează cea mai bătrână persoană
# La fel și pentru youngest_person, cea mai tânără
#
# # Printați acel rezultat.

# result = [{ "name": "Codrin", "age": 30, "of_age": True}, ...]

import random

numbers = [13, 40, 95, 1, 44, 3, 21, 34, 45, 66, 13, 17]
picked = random.choice(numbers)
people = ["Codrin", "Adrian", "John", "Maria", "Tudor", "Maximilian", "Spike"]

def result_people(name, age, of_age)

