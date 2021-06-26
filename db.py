import charts
import mysql.connector
mydb = mysql.connector.connect(
  host="127.0.0.1",
  port= 3306,
  user="root",
  password="1218",
  database = "kkbox"
)
mycursor = mydb.cursor(buffered=True)
mycursor.execute("SHOW DATABASES")
for x in mycursor :
  print(x)
mycursor.execute("SHOW TABLES")
for x in mycursor :
  print(x)
command = "INSERT INTO charts(id, name, artist)VALUES(%s, %s, %s)"
# 取得華語單曲日榜
charts = charts.get_charts_tracks("GnherLVRBEMYgp_iSG")
for chart in charts:
    mycursor.execute(
            command, (chart["id"], chart["name"], chart["album"]["artist"]["name"]))
        # 儲存變更
mydb.commit()

新增charts表的欄位
command = "ALTER TABLE charts ADD DATE date"
mycursor.execute(command)
mydb.commit()

查詢資料
mycursor.execute("SELECT * FROM charts")
result = mycursor.fetchall()
print(result)
command = "SELECT * FROM charts where name = %s or name=%s"
val = ('願得一人心','陪在你身邊')
mycursor.execute(command,val)
result = mycursor.fetchall()
print(result)
command = "UPDATE charts SET name = '醜人多作怪' WHERE id = '8kPLfDJosZ01MVE5pW'"
mycursor.execute(command)
mydb.commit()
print(mycursor.rowcount)
command = "DELETE FROM charts WHERE id = '-kWVjbmzMveSYw_tZe'" 
mycursor.execute(command)
mydb.commit()
print(mycursor.rowcount)
command = "TRUNCATE TABLE charts"
mycursor.execute(command)
mydb.commit()
command="SELECT * FROM charts"
mycursor.execute(command)
result = mycursor.fetchall()
print(result)