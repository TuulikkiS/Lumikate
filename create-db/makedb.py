#!/usr/bin/python

# esimene rida on spetsiaalne rida linuxis, mis ytleb, 
#et linux kaivitagu python ja andku see programm ette

"""
See programm teeb sqlite andmebaasi nimega data.db
ja ehitab sinna tyhja tabeli maintable yheteistkymne tulbaga
id,c1,c2,c3,c4,c5,c6,c7,c8,c9,c10

Sa void kasutada endale arusaadavamaid sisulisi tulbanimesid,
siis pead neid kasutama ka teistes programmides, mis
seda baasi kasutavad. 

NB! id vali taidetakse edaspidi automaatselt.
"""

# kasutame sqlite andmebaasi teeki
import sqlite3

# vota yhendust: kui baasi pole, see tehakse
conn = sqlite3.connect("data.db") 

# kui baas ja tabel juba olemas, kustuta tabel
sql_drop = """drop table if exists snowdays"""
conn.execute(sql_drop)

# tee andmebaasi schema yhe tabeliga
# kus id vali taidetakse edaspidi automaatselt
sql_create = """create table snowdays (id integer primary key autoincrement,
                code,location,year,days int)"""
conn.execute(sql_create)

# katkesta yhendus
conn.close() 
