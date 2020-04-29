
class UserManager:

    def __init__(self, database):
        self.r_database = database

    def initialize_user_ids(self):
        if self.r_database.get('user_id') is None:
            self.r_database.set('user_id', 0)

    def get_new_user_id(self):
        """
        Calling this method will first check if the 'user_id' has been set
         or not, then it will increment the id # by redis feature using .incr()
        """
        self.initialize_user_ids()
        new_user_id = self.r_database.incr('user_id')
        return new_user_id
