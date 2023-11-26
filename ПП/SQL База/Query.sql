# соединение с базой данных, если ее не существует, то создает бд с таким же именем  (database.db):
con = sqlite3.connect(db) 
# создание объекта курсора:
cur = con.cursor()  
#создание запроса к базе данных и сортировка по полюFIO
cur.execute (‘SELECT FIO, Specialnost from pacient ORDER BY FIO’)
#помещение считанных записей из запроса в переменную data
data = cur.fethall()
#закрываем курсор
cur.close()
#разрываем соединение с базой
con.close
