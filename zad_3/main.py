class Property:
    def __init__(self, area, rooms, price, address):
        self.area = area
        self.rooms = rooms
        self.price = price
        self.address = address


class House(Property):
    def __init__(self, area, rooms, price, address, plot):
        super().__init__(area, rooms, price, address)
        self.plot = plot

    def __str__(self):
        return (f"House:\n"
                f"  Area: {self.area} m2\n"
                f"  Rooms: {self.rooms}\n"
                f"  Price: {self.price} zł\n"
                f"  Address: {self.address}\n"
                f"  Plot size: {self.plot} m2")


class Flat(Property):
    def __init__(self, area, rooms, price, address, floor):
        super().__init__(area, rooms, price, address)
        self.floor = floor

    def __str__(self):
        return (f"Flat:\n"
                f"  Area: {self.area} m2\n"
                f"  Rooms: {self.rooms}\n"
                f"  Price: {self.price} zł\n"
                f"  Address: {self.address}\n"
                f"  Floor: {self.floor}")


# Tworzenie obiektów
house = House(area=120, rooms=5, price=650000, address="ul. Słoneczna 12", plot=500)
flat = Flat(area=60, rooms=3, price=350000, address="ul. Kwiatowa 7/12", floor=3)

# Wyświetlenie obiektów
print(house)
print()
print(flat)
