from models import db
from sqlalchemy.sql.schema import ForeignKey
from models.questionAttemptHdr import QuestionAttemptHdr
from models.questions import Questions
from models.questionOptions import QuestionOptions

class QuestionAttemptResponse(db.Model):
    id=db.Column(db.Integer, primary_key=True, autoincrement=True)
    response_text=db.Column(db.Text(128))
    responseID2QuestionOptions=db.Column(db.Integer, ForeignKey(QuestionOptions.id, ondelete='CASCADE'))
    questionID2Questions=db.Column(db.Integer, ForeignKey(Questions.id, ondelete='CASCADE'))
    response2QuestionAttempt=db.Column(db.Integer, ForeignKey(QuestionAttemptHdr.id, ondelete='CASCADE'))
    # attempt_date=db.Column(db.DateTime)
    

    def from_dict(self, data):
        for field in ['response_text',
                        'responseID2QuestionOptions',
                        'questionID2Questions', 
                        'response2QuestionAttempt',
                    ]:
            if field in data:
                setattr(self, field, data[field])
    
    def to_dict(self):
        data={
            'id':self.id,
            'response_text':self.response_text,
            'responseID2QuestionOptions':self.responseID2QuestionOptions,
            'questionID2Questions':self.questionID2Questions,
            'response2QuestionAttempt':self.response2QuestionAttempt,
            # 'attempt_date':self.attempt_date,
        }

        return data
