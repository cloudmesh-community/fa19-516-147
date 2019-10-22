# Python script to test connection to Azure SQL database and execute a DDL command

import pyodbc

server = 'abssrv.database.windows.net'
database = 'absdb'
username = 'haupadhy'
password = 'Ganeshd0yourbest'
driver= '{ODBC Driver 17 for SQL Server}'


con = pyodbc.connect('DRIVER='+driver+';SERVER='+server+';PORT=1433;DATABASE='+database+';UID='+username+';PWD='+ password)

#cur = con.cursor()
#string = "CREATE TABLE tst(name varchar(15), id integer)"
#cur.execute(string)
#con.commit()

cur = con.cursor()
string = "CREATE VIEW vw_tst AS select * from tst"
cur.execute(string)
con.commit()
