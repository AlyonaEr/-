class Building:
    def __init__(self, numberOfFloors, buildingType):
        self.numberOfFloors = numberOfFloors
        self.buildingType = buildingType

    def __str__(self):
        return f'Кол-во этажей: {self.numberOfFloors}, название: {self.buildingType}'

    def __eq__(self, other):
        return self.numberOfFloors == other.numberOfFloors and self.buildingType == other.buildingType


h1 = Building(10, 'ЖК Эльбрус')
h2 = Building(20, 'ЖК Акация')

print(h1)
print(h2)

print(h1 == h2)  # __eq__
