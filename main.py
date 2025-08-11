print("Merhaba")
# Değişkenler
age = 15
print(age)
age = "Merhaba" #Python type-safe değildir.
print(age)
#

# data types 
print(type(age)) #  str-string => metinsel veri
age=20
print(type(age)) # int-integer => tam sayı
age=30.5
print(type(age)) # float-double-decimal => ondalıklı sayı
#
isActive = True # bool-boolean => true/false
print(type(isActive))

students = ["Dilek","Recep","Abdülkerim"] # list
print(students)
print(students[0])
print(students[2]) # index bazlı erişim
students.append("Kaan") # listenin üzerine ekleme
print(students)
students.pop() #default=last
print(students)

# matematiksel operatörler
print(5+5)
print(10-5)
print(5*5)
print(10/6) # bölme işlemi tam bölünmeyebilir. tam bölünse dahi default davranışı floattır.
print(10//6) # bölme işlemi sonucu int döner. (aşağı yuvarlar.)
print(100%3) # mod operatörü
#

# karşılaştırma operatörleri
a = 5
b = 10
print(1 == 1) # sol ve sağ tarafın eşitliğini ölçer.
print(1 == 2)
print(a == b) # false
print(a != b) # true

c = "merhaba"
d = "merhaba1"
print(c==d)

print(a >= b)
print(a <= b)
#

# mantık operatöleri (ve, veya)
print(1==1 and 2==3) # 2 taraf da true olduğu durumda True diğer tüm durumlarda False döner.
print(True and False) #->False
print(1==1 or 2==3) # 2 tarafda false değilse True döner. (1inin bile true olması yeterli.)
print(True or False) #->True

# Soldan sağa AND öncelikli olacak şekilde işlem yapılır.
# Parantezler öncelik belirler.
print(2==3 and (1==1 or 1==1))
# 

# Şart Blokları
# Scope (Kapsam) -> Kapsama Alanı

#tab -> sağa 1 inde. 
#shift+tab -> sola 1 ind.
if a == b:
    print("A B'ye eşit")
print("2. mesaj") #şuanda if'e bağlı değil.
#

# Her şart bloğundan yalnızca bir karar çıkar.
if a == b:
    print("A B'ye eşit")
else: # üstündeki şartlardan hiçbiri sağlanmadığında çalışan bloktur.
    print("A B'ye eşit değil")

age = 18

if age > 20:
    print("Kullanıcı reşit")
elif age == 18:
    print("Ay kontrolü yapılıyor..")
else:
    print("Kullanıcı reşit değil.")

#Döngüler
# Aynı kodu X adet çalıştırmak için. -> İterasyon (Iteration)
example = 5
for i in range(5): # [0,1,2,3,4]
    print(example)
    print(i) # i= iterasyondaki o anki eleman.
#
for i in range(15,20):
    print(i)

for i in range(10,101,5):
    print(i)

students = ["Dilek","Recep","Abdülkerim"] # list
print(students)
for student in students:
    print(student, end=" ")

print("")
a = 5
while a < 10:
    print(a) 
    a += 1 # a = a + 1

choice = input("Menüden işlem seçin")
while choice != "q":
    print("İşlem yapılıyor..")
    choice = input("Menüden işlem seçin")

def connect_database():
    print("abc123 veritabanına bağlanılıyor..")
    print("abc123 veritabanına bağlanılıyor..")
    print("abc123 veritabanına bağlanılıyor..")
    print("abc123 veritabanına bağlanılıyor..")

connect_database()
connect_database()
connect_database()
connect_database()
