from models import db
from sqlalchemy.sql.schema import ForeignKey
from models.questions import Questions

class QuestionOptions(db.Model):
    id=db.Column(db.Integer, primary_key=True, autoincrement=True)
    question_option=db.Column(db.Text)
    questionOption2Question=db.Column(db.Integer, ForeignKey(Questions.id,ondelete='CASCADE'))

    def from_dict(self, data):
        for field in ['question_Option', 'questionOption2Question']:
            setattr(self, field, data[field])
    
    def to_dict(self):
        data={
            'id' : self.id,
            'question_Option' : self.question_option,
            'questionOption2Question' : self.questionOption2Question
        }
        return data