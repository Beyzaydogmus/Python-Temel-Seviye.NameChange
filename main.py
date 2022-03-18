import random


def generate_name():
    first_names = ["Beyza", "Emre", "Coco", "Mikail", "Ayse", "Ahmet", "Berk", "Su", "Furkan"]
    last_names = ["Aydogmus", "Aras", "Tepe", "Bor", "Jackson", "Karakaya", "Uysal", "Bay", "Bozkurt"]
    return "{} {}".format(random.choice(first_names), random.choice(last_names))


for i in range(6):
    print(generate_name())
