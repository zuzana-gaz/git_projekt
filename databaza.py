import sqlite3

connection = sqlite3.connect("mesto_zilina.db")
cursor = connection.cursor()
cursor.execute(
    """
    INSERT INTO zmluvy (kod, cena)
    VALUES ('Z01', 12000.0);
"""    
)
cursor.execute(
    """
    INSERT INTO zmluvy (kod, cena)
    VALUES ('Z02', 15000.0);
"""
)

connection.commit()
connection.close()

