from app import db

class User(db.Model):
    __tablename__ = "users"
    user_id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), nullable=False, unique=True, index=True)
    hashedpassword = db.Column(db.LargeBinary)

    def __repr__(self):
        '''
        :return: Formatted string with each of the data points in the tuple.
        '''
        return f"users('{self.user_id}', '{self.username}', '{self.hashedpassword}')"

class Item(db.Model):
    __tablename__ = "items"
    item_id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(20), nullable=False, unique=True)

    def __repr__(self):
        '''
        :return: Formatted string with each of the data points in the tuple.
        '''
        return f"items('{self.item_id}', '{self.name}')"