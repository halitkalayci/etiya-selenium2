#Bilgisayara arabanın (Car) ne oldugunu tanıt.
class Car():
    def __init__(self, brand, year): # constructor. yapıcı blok.
        self.brand = brand
        self.year = year
        print("Bir araba nesnesi oluştu.")

    #def __init__(self,brand):
       # self.brand = brand
    def start_rent(self): #Classın fonksiyonlarına ilk parametre python tarafından otomatik gönderilir.
        print(self.brand) # self -> classın kendisini ifade eder.
        print("Araç kiralama başlatılıyor")
    def stop_rent(self):
        print("Araç kiralama durduruluyor.")

car1 = Car("Toyota",2025) # init fonk3
car1.start_rent()
car1.stop_rent()

car2 = Car("Fiat", 2025) # init fonk
car2.start_rent()
