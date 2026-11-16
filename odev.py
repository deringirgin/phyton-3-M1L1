class Telephone:
    color = "Turuncu"
    brand = "Iphone"
    yer = "Türkiye"

    def open(self):
        print("Telefon açıldı")

    def stop(self):
        print("Telefon kapandı")

    def abaout_tel(self):
        print(f"Telefonun markası {self.brand}  Telefonun rengi {self.color}")


my_tel = Telephone()

print(f"Rengi {my_tel.color} Üretim yeri {my_tel.yer} Markası {my_tel.brand}")

my_tel.open()
my_tel.stop()
my_tel.abaout_tel()
