import sqlite3
conn=sqlite3.connect('E11DB.sqlite')

sqlstr='CREATE TABLE IF NOT EXISTS table01 ("id" INTEGER PRIMARY KEY NOT NULL,"name" TEXT NOT NULL,"chinese" INTEGER NOT NULL,"english" INTEGER NOT NULL,"math" INTEGER NOT NULL)'

conn.execute(sqlstr)
#conn.commit()
conn.close()


