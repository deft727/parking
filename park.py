from pathlib import Path
from sys import winver


def read_or_create_file() -> dict:
    f = Path('parling.txt')
    cars = {}
    if f.exists:
        with open('parking.txt','r',encoding='utf-8') as file:
            for i in file.readlines():
                name,car = i[:-1].split(":")
                cars.update({name:car})
    else:
        file = open('parking.txt','w')
        file.close()
    return cars


def write_file(cars: dict) -> None:
    with open('parking.txt','w',encoding='utf-8') as file:
        for name,car in cars.items():
            file.writelines(f'{name}:{car}\n')


def parking() -> None:
    cars = read_or_create_file()
    while True:
        command = input (
            "1 - Добавить \n"
            "2 - Удалить \n"
            "3 - Просмотр \n"
            "4 - Изменить \n"
            "5 - Записать в файл \n"
            "Введите кооманду : "
        )
        if command == "1":
            owner = input("Введите владельца: ")
            if cars.get(owner):
                print("Машина с таким владельцем уже на парковке")
            car = input("Введите марку машины: ")
            cars[owner]=car
        elif command == "2":
            owner = input("Введите имя владельца: ")
            if cars.get(owner):
                cars.pop(owner)
                print(f"{owner} уехал")
            else:
                print(f"{owner} не найдено")
        elif command == "3":
            for owner,car in cars.items():
                print(f"____________________\n{owner} - {car}\n____________________")
        elif command == "4":
            owner = input("Введите имя владельца: ")
            if cars.get(owner):
                car = input("Введите марку машины: ")
                cars[owner] = car
            else:
                print(f"Имя {owner} не найдено")
        elif command == "5":
            write_file(cars)
            print("Данные записаны")
parking()
