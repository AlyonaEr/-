def go_to(new_floor):
    if new_floor > number_of_floors or new_floor < 1:
        print("Такого этажа не существует")
    else:
        print(*list(range(1, int(new_floor) + 1)), sep='\n')


number_of_floors = 7
go_to(5)
go_to(10)
