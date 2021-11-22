from flask_app.config.mysqlconnection import connectToMySQL

class User:
    def __init__(self,data):
        self.id = data['id']
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.email = data['email']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']

    @classmethod
    def allusersdisplay(cls): #for friends list/homescreen/profile page
        query = "SELECT * from users;"
        current_users = connectToMySQL('users_schema').query_db(query)
        users_list = []
        for each_user in current_users:
            users_list.append( each_user )
        return users_list

    @classmethod #for profile/account settings
    def one_user(cls,data):
        query = "SELECT * FROM users WHERE users.id = %(id)s;"
        one_user = connectToMySQL('users_schema').query_db(query,data)
        return cls(one_user[0])

    @classmethod  #register your account/ add user
    def add_new_user(cls,data):
        query = "INSERT INTO users (first_name, last_name, email,created_at,updated_at) VALUES (%(first_name)s, %(last_name)s, %(email)s, NOW(),NOW());"
        results = connectToMySQL('users_schema').query_db(query, data)
        return results
    
    @classmethod
    def update_user(cls,data):
        query = "UPDATE users SET first_name=%(first_name)s, last_name=%(last_name)s, email=%(email)s,updated_at = NOW() WHERE id = %(id)s "
        return connectToMySQL('users_schema').query_db(query,data)

    @classmethod #deleteuser
    def delete_account(cls,data):
        query = "DELETE FROM users WHERE id = %(id)s"
        return connectToMySQL('users_schema').query_db(query,data)
