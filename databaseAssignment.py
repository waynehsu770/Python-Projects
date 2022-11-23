


import sqlite3


conn = sqlite3.connect('test.db')

with conn:
    cur = conn.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS tbl_Files( \
        ID INTEGER PRIMARY KEY AUTOINCREMENT, \
        col_fileName TEXT \
        )")
    conn.commit()
conn.close()


fileList = ('information.docx', 'Hello.txt', 'myImage.png', \
            'myMovie.mpg', 'World.txt', 'data.pdf', 'myPhoto.jpg')

conn = sqlite3.connect('test.db')

with conn:
    cur = conn.cursor()
    for file in fileList:
        if file.endswith('.txt'):
            print(file)
            cur.execute("INSERT INTO tbl_Files(col_fileName) VALUES (?)", \
                        (file,))
    conn.commit()
conn.close()











