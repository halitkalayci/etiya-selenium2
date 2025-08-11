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

# operatörler
print(5+5)
print(10-5)
print(5*5)
print(10/6) # bölme işlemi tam bölünmeyebilir. tam bölünse dahi default davranışı floattır.
print(10//6) # bölme işlemi sonucu int döner. (aşağı yuvarlar.)
#