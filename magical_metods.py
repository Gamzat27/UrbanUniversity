
class House:
    def __init__(self, house_name, floors_in_the_house):
        self.house_name = house_name
        self.floors_in_the_house = floors_in_the_house


    def go_to(self, new_floor):
        if new_floor < 1 or new_floor > self.floors_in_the_house:
            print('Такого этажа нет!')
        else:
            for floor in range(1, new_floor + 1):
                print(floor)


    def __len__(self):
        return \
            self.floors_in_the_house

    def __str__(self):
        return \
            f'Название:{self.house_name}, Количество этажей:{self.floors_in_the_house}'



h1 = House('Жк Хватай и беги', 27)
h2 = House('Монако', 7)
print(h1)
print(h2)
print(len(h1))
print(len(h2))



