
from models import db
from sqlalchemy.sql.schema import ForeignKey
from datetime import datetime

class QuestionAttemptHdr(db.Model):
    id=db.Column(db.Integer, primary_key=True, autoincrement=True)
    date=db.Column(db.DateTime)

    def from_dict(self, data):
        for field in ['date']:
            if field in data:
                setattr(self, field, data[field])

    def to_dict(self):
        data={
            'id':self.id,
            'date': datetime.now()
        }

        return data