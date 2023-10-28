from config import CONN,CURSOR
class Song:
    def __init__(self,name, album):
        self.id=None
        self.name=name
        self.album=album
    @classmethod
    def create_table(self):
        sql="""
        CREATE TABLE IF NOT EXISTS songs(
        id INTEGER PRIMARY KEY,
        name TEXT,
        album TEXT
        )
        """
        CURSOR.execute(sql)
    def save(self):
        sql="""
        INSERT INTO songs (name,album)
        VALUES(?,?)    
        """
        CURSOR.execute(sql,(self.name,self.album))
    @classmethod
    def create(cls,name,album):
        song=Song(name,album)
        song.save()
        return song

# hello = Song("Hello", "25")
# hello.save()
# despacito = Song("Despacito", "Vida")
# despacito.save()
# songs=CURSOR.execute('SELECT * FROM songs')
# print([row for row in songs])
# print(hello.id)
# print(despacito.id)
hello=Song.create("Hello","25")
print(hello.id)
