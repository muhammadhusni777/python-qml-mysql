import mysql.connector

db = mysql.connector.connect(
  host="localhost",
  user="root",
  passwd="",
  database="toko_mainan"
)

cursor = db.cursor()
keyword = input("Kata kunci: ")
sql = "SELECT * FROM customers WHERE name LIKE %s OR address LIKE %s"
val = ("%{}%".format(keyword), "%{}%".format(keyword))
cursor.execute(sql, val)
results = cursor.fetchall()
  
if cursor.rowcount < 0:
    print("Tidak ada data")
else:
    for data in results:
        print(data)