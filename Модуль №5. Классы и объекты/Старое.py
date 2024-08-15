class House:
    def __init__(self, number_Of_Floors):
        self.number_Of_Floors = number_Of_Floors

    def __str__(self):
        return f'{self.number_Of_Floors}'

    def setNewNumberOfFloors(self, floors):
        newfloowers = sum(self.number_Of_Floors, floors)
        return newfloowers



h1 = House(0)
print(h1)
setNewNumberOfFloors(15)
