from conexion import get_connection
import hashlib

class Auth:

    def create_table_users(self):
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS usuarios(
                usuario TEXT UNIQUE,
                contrasena TEXT
            )
        """)
        conn.commit()
        conn.close()

    def hash_password(self, contrasena):
        return hashlib.sha256(contrasena.encode()).hexdigest()

    def registrar(self, usuario, contrasena):
        conn = get_connection()
        cursor = conn.cursor()
        hashed = self.hash_password(contrasena)
        cursor.execute("INSERT INTO usuarios VALUES (?,?)", (usuario, hashed))
        conn.commit()
        conn.close()

    def login(self, usuario, contrasena):
        conn = get_connection()
        cursor = conn.cursor()
        hashed = self.hash_password(contrasena)
        cursor.execute("SELECT * FROM usuarios WHERE LOWER(usuario) = LOWER(?) AND contrasena=?", (usuario, hashed))
        resultado = cursor.fetchone()
        conn.close()
        return resultado is not None