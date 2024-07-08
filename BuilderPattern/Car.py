from Vehicle import Vehicle
class Car(Vehicle):
    def __init__(self, brand_name):
        super().__init__()
        self.brand_name = brand_name
        print(f"\nWe are about to make a {brand_name} car.")