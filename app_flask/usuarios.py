from app_flask.mysqlconnection import connectToMySQL

class Usuario:
    def __init__(self, datos):
        self.id = datos['id']
        self.nombre = datos['nombre']
        self.apellido = datos['apellido']
        self.email = datos['email']
        self.fecha_creacion = datos['fecha_creacion']
        self.fecha_actualizacion = datos['fecha_actualizacion']

    @classmethod
    def get_all(cls):
        query = "SELECT * FROM usuarios;"
        results = connectToMySQL('usuarios_cr').query_db(query)
        usuarios = []
        for u in results:
            usuarios.append( cls(u) )
        return usuarios

    @classmethod
    def obtener_por_id(cls, user_id):
        query = "SELECT * FROM usuarios WHERE id = %(id)s;"
        data = {
            'id': user_id
        }
        result = connectToMySQL('usuarios_cr').query_db(query, data)
        if result:
            return cls(result[0])  # Devuelve el primer elemento como un objeto Usuario
        else:
            return None

    @classmethod
    def eliminar_por_id(cls, user_id):
        query = "DELETE FROM usuarios WHERE id = %(id)s;"
        data = {
            'id': user_id
        }
        result = connectToMySQL('usuarios_cr').query_db(query,data)
        return result
    
    @classmethod
    def actualizar_por_id(cls, user_id, nombre, apellido, email):
        query = "UPDATE usuarios SET nombre = %(nombre)s, apellido = %(apellido)s, email = %(email)s WHERE id = %(id)s;"
        data = {
            'id': user_id,
            'nombre': nombre,
            'apellido': apellido,
            'email': email
        }
        result = connectToMySQL('usuarios_cr').query_db(query, data)
        return result

    @classmethod
    def save(cls, data):
        query = "INSERT INTO usuarios (nombre,apellido,email) VALUES (%(nombre)s,%(apellido)s,%(email)s);"

        usuario_id = connectToMySQL('usuarios_cr').query_db(query,data)
        return usuario_id