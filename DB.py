# import sqlite3 as sql
# db = sql.connect(r"DB\chinook.db")
# cur = db.cursor()
# sorgu = """
# INSERT INTO albums (Title,ArtistId)
# VALUES ('Menderes Abiii',2);
# """
# artist = int(input("artisId giriniz:"))
# sorgu = """
# SELECT *
#   FROM albums
#  WHERE ArtistId = {};
# """.format(artist)
# cur.execute(sorgu)
# liste = cur.fetchall()
# print(liste)
# for id,baslik,artist in liste:
#     print("{}-{}-{}".format(id,baslik,artist))

def Ekleme(Adi = ""):
      return """INSERT INTO 
      artists (Name) Values ('{}')""".format(Adi)

import sqlite3 as sql
import os
db = sql.connect(r"DB"+os.sep+"chinook.db")
cur = db.cursor()
adi = input("Artist Adı Giriniz")
sorgu = Ekleme(adi)
cur.execute(sorgu)
db.commit()
sorgu = """SELECT * FROM artists 
ORDER BY ArtistId desc LIMIT 5"""
cur.execute(sorgu)
liste = cur.fetchall()
for id,artist in liste:
    print("{}-{}".format(id,artist))



