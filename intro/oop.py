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

# Super -> Kalıtım alınan nesneyi ifade eder.
# Superclass-Subclass
class ElectricCar(Car): #ElectricCar -> Car isimli classın tüm özelliklerini alır, ve genişletir.
    def __init__(self, brand, year, battery):
        super().__init__(brand, year)
        # name mangling 
        self.__battery = battery # private

    def set_battery(self,battery):
        if len(battery) < 2:
            return
        self.__battery = battery
    def get_battery(self):
        return self.__battery
    
electric_car = ElectricCar("Tesla",2025, "305Kw")
electric_car.set_battery("1")
print(electric_car.get_battery()) # get