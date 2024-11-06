import sqlite3  # Importar el módulo sqlite3 para trabajar con la base de datos SQLite
import secrets  # Importar el módulo secrets para generar códigos únicos aleatorios

DB_NAME = "database/notas.db"  # Ruta y nombre del archivo de la base de datos

class ModelDB:
    def __init__(self):
        self.conexion = None
        self.c = None

    def conectar_base_datos(self):
        # Conexión a la base de datos
        self.conexion = sqlite3.connect(DB_NAME, check_same_thread=False)
        self.c = self.conexion.cursor()

        # Creación de la tabla "notas" si no existe
        self.c.execute("CREATE TABLE IF NOT EXISTS notas (codigo char(50) PRIMARY KEY, texto TEXT NOT NULL)")

    def cerrar_conexion(self):
        # Cierre de la conexión con la base de datos
        if self.c:
            self.c.close()
        if self.conexion:
            self.conexion.close()

    def generar_codigo_unico(self):
        # Generación de un código único utilizando tokens URL seguros
        codigo = secrets.token_urlsafe(8)

        # Verificar si el código generado ya existe en la base de datos
        while self.codigo_existente(codigo):
            codigo = secrets.token_urlsafe(8)
        return codigo

    def codigo_existente(self, codigo):
        # Verificar si un código existe en la base de datos
        #La instrucción with en Python proporciona una forma de gestionar automáticamente
        #los recursos y las acciones relacionadas con un contexto específico.
        with self.conexion:
            self.c.execute("SELECT codigo FROM notas WHERE codigo = ?", (codigo,))
            return self.c.fetchone() is not None

    def leer_nota(self, codigo):
        # Leer el texto de una nota utilizando el código como identificador
        #La instrucción with en Python proporciona una forma de gestionar automáticamente
        #los recursos y las acciones relacionadas con un contexto específico.
        with self.conexion:
            self.c.execute("SELECT texto FROM notas WHERE codigo = ?", (codigo,))
            nota = self.c.fetchone()

            if nota:
                return nota[0]
            return None

    def guardar_nota(self, texto):
        # Generar un código único y guardar una nueva nota en la base de datos
        codigo = self.generar_codigo_unico()
        
        #La instrucción with en Python proporciona una forma de gestionar automáticamente
        #los recursos y las acciones relacionadas con un contexto específico.
        with self.conexion:
            self.c.execute("INSERT INTO notas (codigo, texto) VALUES (?, ?)", (codigo, texto))
            self.conexion.commit()

        return codigo

    def borrar_nota(self, codigo):
        # Eliminar una nota de la base de datos utilizando el código como identificador
        with self.conexion:
            self.c.execute("DELETE FROM notas WHERE codigo = ?", (codigo,))
            self.conexion.commit()

    def obtener_todas_notas(self):
        # Obtener todas las notas de la base de datos
        with self.conexion:
            self.c.execute("SELECT codigo, texto FROM notas")
            notas = self.c.fetchall()
        return [{'codigo': nota[0], 'texto': nota[1]} for nota in notas]
