# from operator import imod
from models import db
from sqlalchemy.sql.schema import ForeignKey
from models.questionSet import QuestionSet
from models.referenceData import ReferenceData

class Questions(db.Model):
    id=db.Column(db.Integer, primary_key=True, autoincrement=True)
    question_text=db.Column(db.Text(128))
    question_type=db.Column(db.Text(128))
    questStatusID2RefData=db.Column(db.Integer, ForeignKey(ReferenceData.id, ondelete='CASCADE'))
    question2QuestionSet=db.Column(db.Integer, ForeignKey(QuestionSet.id, ondelete='CASCADE'))

    def from_dict(self, data):
        for field in ['question_text',
                        'question_type',
                        'questStatusID2RefData',
                        'question2QuestionSet',
                    ]:
            if field in data:
                setattr(self, field, data[field])
    
    def to_dict(self):
        data={
        'id':self.id,
        'question_Text':self.question_text,
        'question_Type':self.question_type,
        'questStatusDd2RefData':self.questStatusID2RefData,
        'question2QuestionSet':self.question2QuestionSet,
        }

        return data
