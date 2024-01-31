import mysql.connector

db = mysql.connector.connect(
  host="localhost",
  user="root",
  passwd="",
  database="toko_mainan"
)

cursor = db.cursor()
sql = "UPDATE customers SET name=%s, address=%s WHERE customer_id=%s"
val = ("Risma Ade Aryati", "Lombok", 1)
cursor.execute(sql, val)

db.commit()

print("{} data diubah".format(cursor.rowcount))