from flask_app.config.mysqlconnection import connectToMySQL
from flask_app.models.ninja import Ninja

class Dojo:
    def __init__(self, data):
        self.id = data['id']
        self.name = data["name"]
        self.created_at = data["created_at"]
        self.updated_at = data["updated_at"]
        self.ninjas = []


#Shows a list of all dojos
    @classmethod
    def show_all(cls):
        query = "SELECT * FROM dojos;"
        return connectToMySQL("dojos_and_ninjas_schema").query_db(query)

#Creates a new dojo.
    @classmethod
    def new_dojo(cls, data):
        query = "INSERT INTO dojos(name, created_at, updated_at) \
                VALUES(%(name)s, Now(), Now());"
        return connectToMySQL("dojos_and_ninjas_schema").query_db(query, data)


#Displays all ninjas associated with passed dojo.
    @classmethod
    def display_dojo(cls, data):
        query = "SELECT * FROM dojos LEFT JOIN ninjas ON ninjas.dojo_id = dojos.id WHERE dojos.id = %(id)s;"
        results = connectToMySQL("dojos_and_ninjas_schema").query_db(query, data)
        
        dojo = cls(results[0])
        if results[0]['ninjas.id'] != None:
            for row in results:
                row_data = {
                    "id": row['ninjas.id'],
                    'dojo_id': row['dojo_id'],
                    'first_name': row['first_name'],
                    'last_name': row['last_name'],
                    'age': row['age'],
                    'created_at': row['ninjas.created_at'],
                    'updated_at': row['ninjas.updated_at']
                }
                dojo.ninjas.append(Ninja(row_data))

        return dojo



    