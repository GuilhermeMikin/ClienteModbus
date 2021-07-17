from clienteModbus import ClienteMODBUS

dbpath = "C:\\Users\\mikin\\GitHubRepository\\ClienteModbus\\DB\\database.db"

c = ClienteMODBUS('127.0.0.1', 502, 1, dbpath=dbpath)
c.atendimento()