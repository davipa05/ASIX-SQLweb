import sqlite3

conn=sqlite3.connect("store.db")

cur=conn.cursor()

#tabla users
cur.execute("CREATE TABLE IF NOT EXISTS users (username TEXT, password TEXT,adress TEXT)")
conn.commit()
users=[
    ("admin","asix2023","Rambla Catalunya 82 bajos"),
    ("carlos","12345","Carretera de Sants 12 3o 1a"),
    ("julia", "pass6789", "Avenida Diagonal 401 2o 2a"),
    ("marc", "marc2024", "Gran Via 555 5o 3a"),
    ("lucia", "mypassword", "Passeig de Gracia 60 1o 1a"),
]
for e in users:
    cur.execute("INSERT INTO users (username,password,adress) VALUES (?,?,?)",e)
conn.commit()

#tabla products
cur.execute("CREATE TABLE IF NOT EXISTS products (name TEXT,price REAL,image TEXT)")
conn.commit()
products=[
    ("ASUS E410MA",249,"https://m.media-amazon.com/images/I/51GYgS4f+GL._AC_UL640_FMwebp_QL65_.jpg"),
    ("WOZIFAN Ordenador Portátil Win11 14'' ",212.49,"https://m.media-amazon.com/images/I/71nCiLpqLqL._AC_UL640_FMwebp_QL65_.jpg"),
    ("HP 15-fd0000ns ",329.99,"https://m.media-amazon.com/images/I/91woduXUkRL._AC_UL640_FMwebp_QL65_.jpg"),
    ("ACEMAGIC Ordenador Portátil Intel 12th Alder Lake",322.92,"https://m.media-amazon.com/images/I/714vs7F41IL._AC_UL640_FMwebp_QL65_.jpg"),
    ("ASUS VivoBook 14 ",699,"https://m.media-amazon.com/images/I/71wTuQ2njfL._AC_UL640_FMwebp_QL65_.jpg"),
    ("Primux Ordenador Portátil Ioxbook 1406F ",149,"https://m.media-amazon.com/images/I/71YC3AEhJjL._AC_UL640_FMwebp_QL65_.jpg"),
    ("ASUS Chromebook CX1400CKA-EK0138 ",279,"https://m.media-amazon.com/images/I/61nfaSxWTLL._AC_UL640_FMwebp_QL65_.jpg"),
    ("HP ELITEBOOK 840 G3 INTEL CORE I5-6200U 6ª GEN 2.3GHZ",259,"https://m.media-amazon.com/images/I/71nVtdbtJiS._AC_UL640_FMwebp_QL65_.jpg"),
   
]
for e in products:
    cur.execute("INSERT INTO products (name,price,image) VALUES (?,?,?)",e)
conn.commit()


#tabla purchases
cur.execute("CREATE TABLE IF NOT EXISTS purchases (username_id INTEGER, product_id INTEGER,amount INTEGER)")
conn.commit()
users=[
    (1,5,1),
    (2,1,1),
    (2,2,1),
    (2,3,1),
    (2,4,1),
    (2,5,1),
    (3,1,1),
    (3,5,1),
    (4,4,1),
    (4,2,1),
    (5,8,2),
    (5,9,2),
    (5,3,2),
    (5,2,2),
    (5,1,2), 
]
for e in users:
    cur.execute("INSERT INTO purchases (username_id,product_id,amount) VALUES (?,?,?)",e)
conn.commit()

cur.close()
conn.close()

print("DB created")