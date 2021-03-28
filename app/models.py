from app import db

def default_entites():
    ans = {
        'province': '',
        'name': '',
        'phone_number': '',
        'address': '',
        'code': '',
    }
    return str(ans)

class Message(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    sender_id = db.Column(db.Integer)
    intent = db.Column(db.String(32))
    action = db.Column(db.String(32))
    entities = db.Column(db.String(1000), default=default_entites())
    client_message = db.Column(db.String(10000))
    bot_message = db.Column(db.String(10000))
    
    def to_dict(self):
        return{
            'id':self.id,
            'sender_id':self.sender_id,
            'intent':self.intent,
            'action':self.action,
            'entities':self.entities,
            'client_message':self.client_message,
            'bot_message':self.bot_message
        }

    def __repr__(self):
        return '<Conversation %r>' % (self.action)
    
    