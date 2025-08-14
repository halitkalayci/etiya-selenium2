#wrapper
import psycopg2 # PostgreSQL Wrapper

connection = psycopg2.connect(
    host="193.203.191.79",
    port="32001",
    database="testdb",
    user="postgres",
    password="1234"
)

cursor = connection.cursor()

cursor.execute("Select * from users;")

users = cursor.fetchall()

print(len(users))

for row in users:
    print(f"User Id: {row[0]} Name:{row[1]}")

# Kendi sistemimizde yeni bir proje açarak çalıştığımız projeyi test edelim.
# POM mimarisi ile 2 test case.