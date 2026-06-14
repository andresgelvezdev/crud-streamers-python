"""
controller.py
Módulo encargado de la lógica del CRUD de streamers.
Contiene la clase StreamerController con los métodos de la base de datos.

"""


from conexion import get_connection


class Steamer_Controller:

    def __init__(self):

        pass

    def create_table(self):
        conn = get_connection()
        cursor = conn.cursor()

        cursor.execute("""
        CREATE TABLE IF NOT EXISTS streamers(
            name TEXT,
            followers INTEGER,
            subs INTEGER
        )
    """)

        conn.commit()
        conn.close()


    def InsertStreamers(self,streamer):
        conn = get_connection()
        cursor = conn.cursor()

        cursor.execute(
            "INSERT INTO streamers VALUES (?,?,?)",
            (streamer.name, streamer.followers, streamer.subs)
        )

        conn.commit()
        conn.close()


    def ReadStreamers(self):
     
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM streamers")
        datos = cursor.fetchall()
        conn.close()
        for streamer in datos:
            print(f"Nombre: {streamer[0]} | Followers: {streamer[1]} | Subs: {streamer[2]}")
    
    def SearchStreamers(self, streamer):
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM streamers WHERE name LIKE ?", (f"%{streamer}%",))
        datos = cursor.fetchall()
        conn.close()
        for streamer in datos:
            return(f"Nombre: {streamer[0]} | Followers: {streamer[1]} | Subs: {streamer[2]}")
           



    def update_followers(self,nombre, followers):
        conn = get_connection()
        cursor = conn.cursor()

        cursor.execute(
            "UPDATE streamers SET followers = ? WHERE LOWER(name) = LOWER(?)",
            (followers, nombre)
        )
        conn.commit()
        conn.close()
    

    def update_subs(self,nombre, subs):
        conn = get_connection()
        cursor = conn.cursor()

        cursor.execute(
            "UPDATE streamers SET subs = ? WHERE LOWER(name) = LOWER(?)",
            (subs, nombre)
        )
        conn.commit()
        conn.close()
    

    def Deleted_Streamer(self,nombre):
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute(
            "DELETE FROM streamers WHERE LOWER(name) = LOWER(?)",
            (nombre,)         
        )
        conn.commit()
        conn.close()
