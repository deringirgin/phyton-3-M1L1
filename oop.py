class Car:
    color = "red"
    brand = "toyota"
    yer = "Türkiye"

    def drive(self):
        print("Araba sürülyor")

    def stop(self):
        print("ataba durdu")

    def abaout_car(self):
        print(f"arabanın markası {self.brand}   arabanın rengi {self.color}")


car1 = Car()

print(f"Car1 in rengi {car1.color}  Üretim yeri {car1.yer}")

car1.drive()
car1.abaout_car()
