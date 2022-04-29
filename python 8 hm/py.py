import sqlite3
connect = sqlite3.connect('mydatabase.db')

# cursor method

cursor = connect.cursor()
cursor2 = connect.cursor()
cursor3 = connect.cursor()
cursor4 = connect.cursor()
cursor5 = connect.cursor()


input = input("Ma'lumotni kiriting: ")

cursor.execute("""
CREATE TABLE IF NOT EXISTS shopping(
    name TEXT,
    last_name TEXT,
    age INTEGER
)
               
""")

cursor.execute("""
INSERT INTO shopping VALUES
('Javohir', 'Nematov', 15),
('Mashhurbek', 'Ergashev', 15)
               
""")

cursor2.execute("""
INSERT INTO shopping VALUES
('salom', 'alik', 23),
('olma', 'nok', 8)
               
""")

cursor3.execute("""
INSERT INTO shopping VALUES
('python', 'html', 3),
('olma', 'nok', 8)
               
""")


cursor.execute("SELECT * FROM shopping")
cursor2.execute("SELECT * FROM shopping")
cursor3.execute("SELECT * FROM shopping")
cursor4.execute("SELECT * FROM shopping")
cursor5.execute("SELECT * FROM shopping")


if input == 'malumot':
    print(cursor.fetchall())
elif input == '':
    print('malumot yoq biror narsa kiriting')
else:
    print("malumot mavjud emas")
    
#   input ikki

if input == 'malumot2':
    print(cursor2.fetchall())
elif input == '':
    print('malumot yoq biror narsa kiriting')
else:
    print("malumot mavjud emas")

#input uch

if input == 'malumot3':
    print(cursor3.fetchall())
elif input == '':
    print('malumot yoq biror narsa kiriting')
else:
    print("malumot mavjud emas")