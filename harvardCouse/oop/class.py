#example1

class Point():
    def __init__(self, input1, input2):
        self.x =  input1
        self.y = input2

p = Point(2, 8)
print(p.x, p.y)

#example2

class Flight():
    def __init__(self, capacity):
        self.capacity = capacity
        self.passengers = []

    def add_passenger(self, name):
        if not self.open_seats():
            return False
        self.passengers.append(name)
        return True
    
    def open_seats(self):
        return self.capacity - len(self.passengers)
    
flight = Flight(3)

people = ["yass", "james", "james1", "james 2"]
for person in people:
    success = flight.add_passenger(person)
    if success:
        print(f"added {person} to flight succefully")
    else:
        print(f"no available seats for {person}")
