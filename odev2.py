class Motor:
    color = "kırmızı"
    brand = "Ford"
    yer = "Amerika"

    def open(self):
        print("Ford Mustang açılıyor")

    def stop(self):
        print("Ford Mustang kapanıyor")

    def abaout_tel(self):
        print(f"Motorun markası {self.brand} Motorun rengi {self.color}")

    def tranlation(self):
        print("Ford Mustang arabaya dönüşüyor")


my_tel = Motor()

print(f"Rengi {my_tel.color} Üretim yeri {my_tel.yer} Markası {my_tel.brand}")

my_tel.open()
my_tel.stop()
my_tel.abaout_tel()
my_tel.tranlation
