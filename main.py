class House:
    def __init__(self, name, floors):
        self.name = name
        self.floors = floors

    def __str__(self):
        return f'Название: {self.name}, кол-во этажей: {self.floors}'

    def __eq__(self, other):
        if isinstance(other, House):
            return self.floors == other.floors
        return False

    def __lt__(self, other):
        if isinstance(other, House):
            return self.floors < other.floors
        return NotImplemented

    def __le__(self, other):
        if isinstance(other, House):
            return self.floors <= other.floors
        return NotImplemented

    def __gt__(self, other):
        if isinstance(other, House):
            return self.floors > other.floors
        return NotImplemented

    def __ge__(self, other):
        if isinstance(other, House):
            return self.floors >= other.floors
        return NotImplemented

    def __ne__(self, other):
        return not self.__eq__(other)

    def __add__(self, value):
        if isinstance(value, int):
            self.floors += value
        return self

    def __radd__(self, value):
        return self.__add__(value)

    def __iadd__(self, value):
        return self.__add__(value)

# Пример выполняемого кода:
h1 = House('ЖК Эльбрус', 10)
h2 = House('ЖК Акация', 20)

print(h1)                          # Название: ЖК Эльбрус, кол-во этажей: 10
print(h2)                          # Название: ЖК Акация, кол-во этажей: 20

print(h1 == h2)                   # False

h1 = h1 + 10                      # Увеличиваем этажи h1
print(h1)                          # Название: ЖК Эльбрус, кол-во этажей: 20
print(h1 == h2)                   # True

h1 += 10                          # Увеличиваем этажи h1 ещё раз
print(h1)                          # Название: ЖК Эльбрус, кол-во этажей: 30

h2 = 10 + h2                      # Увеличиваем этажи h2
print(h2)                          # Название: ЖК Акация, кол-во этажей: 30

print(h1 > h2)                    # False
print(h1 >= h2)                   # True
print(h1 < h2)                    # False
print(h1 <= h2)                   # True
print(h1 != h2)                   # False

