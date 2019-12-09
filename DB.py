import sqlite3 as sql
db = sql.connect(r"DB\chinook.db")
cur = db.cursor()
# sorgu = """
# INSERT INTO albums (Title,ArtistId)
# VALUES ('Menderes Abiii',2);
# """
artist = int(input("artisId giriniz:"))
sorgu = """
SELECT *
  FROM albums
 WHERE ArtistId = {};
""".format(artist)
cur.execute(sorgu)
liste = cur.fetchall()

for id,baslik,artist in liste:
    print("{}-{}-{}".format(id,baslik,artist))


# db.commit()
db.close()

