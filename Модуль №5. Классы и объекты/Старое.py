class House:
    def __init__(self, number_Of_Floors=0):
        self.number_Of_Floors = number_Of_Floors

    def __str__(self):
        return f'Кол-во этажей: {self.number_Of_Floors}'

    def setNewNumberOfFloors(self, floors):
        n1 = 0
        if isinstance(floors, int):
            n1 = (self.number_Of_Floors + floors)
        return n1


h1 = House()
print(h1)
print(h1.setNewNumberOfFloors(19))