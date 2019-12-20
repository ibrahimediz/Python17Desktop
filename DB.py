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

# def Ekleme(Adi = ""):
#       return """INSERT INTO 
#       artists (Name) Values ('{}')""".format(Adi)

 
# db = sql.connect(r"DB"+os.sep+"chinook.db")
# cur = db.cursor()
# adi = input("Artist Adı Giriniz")
# sorgu = Ekleme(adi)
# cur.execute(sorgu)
# db.commit()
# sorgu = """SELECT * FROM artists 
# ORDER BY ArtistId desc LIMIT 5"""
# cur.execute(sorgu)
# liste = cur.fetchall()
# for id,artist in liste:
#     print("{}-{}".format(id,artist))

import sqlite3 as sql
import os

def MusteriListe():
  db = sql.connect(r"DB"+os.sep+"chinook.db")
  cur = db.cursor()
  sorgu="""SELECT CustomerId,
       FirstName || ' ' || LastName AS Adisoyadi
  FROM customers;"""
  cur.execute(sorgu)
  liste=cur.fetchall()
  return liste


def PersonelListe():
  db = sql.connect(r"DB"+os.sep+"chinook.db")
  cur = db.cursor()
  sorgu="""SELECT EmployeeId,
       FirstName || ' ' || LastName AS Adisoyadi
  FROM employees;"""
  cur.execute(sorgu)
  liste=cur.fetchall()
  return liste

def ArtistListe():
  db = sql.connect(r"DB"+os.sep+"chinook.db")
  cur = db.cursor()
  sorgu="""select * from artists;"""
  cur.execute(sorgu)
  liste=cur.fetchall()
  return liste


def AlbumListe(param):
  db = sql.connect(r"DB"+os.sep+"chinook.db")
  cur = db.cursor()
  sorgu="""select AlbumId,Title from albums where artistid={};""".format(param)
  cur.execute(sorgu)
  liste=cur.fetchall()
  return liste


def ParcaListe(param):
  db = sql.connect(r"DB"+os.sep+"chinook.db")
  cur = db.cursor()
  sorgu="""SELECT TrackId,
       Name,
       UnitPrice,
       Bytes
    FROM tracks
   WHERE AlbumId = {};""".format(param)
  cur.execute(sorgu)
  liste=cur.fetchall()
  return liste