import csv

def read_excel(path):
    pass


#compile-time error

#runtime error
def read_csv(path):
    # try'ın içindeki kodu çalıştırmayı dene
    try:
        file = open(path, mode="r", encoding="utf-8")
        data = file.read() #dosyayı string olarak okur
        reader = csv.reader(data)
        next(reader) # ilk satırı geçer (başlıklar)
        return [row for row in reader]
    # runtime hatası alırsa, bunları yap.
    except:
        print("Dosya okunurken hata oluştu.")
    # tryda exceptde çalışsa son olarak kesin bu kodu çalıştır.
    finally:
        file.close()

def read_csv_data(path):
    with open(path, mode="r", encoding="utf-8") as csvFile:
        reader = csv.reader(csvFile)
        next(reader)
        return [row for row in reader]
