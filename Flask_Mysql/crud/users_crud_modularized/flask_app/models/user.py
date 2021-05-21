from flask_app.config.mysqlconnection import connectToMySQL

class User:
    def __init__(self, data):
        self.id = data['id']
        self.first_name = data["first_name"]
        self.last_name = data["last_name"]
        self.email = data["email"]
        self.created_at = data["created_at"]
        self.updated_at = data["updated_at"]

    @classmethod
    def show_all(cls):
        query = "SELECT * FROM users;"
        results = connectToMySQL("users_schema").query_db(query)
        users_list = []
        for i in results:
            users_list.append(cls(i))
        return users_list

    @classmethod
    def create(cls, data):
        query = "INSERT INTO users(first_name, last_name, email, created_at, updated_at) \
        VALUES(%(first_name)s,%(last_name)s,%(email)s,NOW(), NOW());"
        return connectToMySQL('users_schema').query_db(query, data)

    @classmethod
    def show_by_id(cls, data):
        query = "SELECT * FROM users WHERE id = %(id)s;"
        results = connectToMySQL('users_schema').query_db(query, data)
        return cls(results[0])


    @classmethod
    def update(cls, data):
        query = "UPDATE users SET first_name=%(first_name)s,last_name=%(last_name)s,email=%(email)s,\
        created_at=Now(),updated_at=Now() WHERE id = %(id)s;"
        return connectToMySQL('users_schema').query_db(query,data)

    @classmethod
    def delete(cls,data):
        query = "DELETE FROM users WHERE id = %(id)s;"
        return connectToMySQL("users_schema").query_db(query, data)
