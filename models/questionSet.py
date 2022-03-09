from operator import imod
from models import db
from sqlalchemy.sql.schema import ForeignKey
from models.referenceData import ReferenceData
from sqlalchemy.sql import func

class QuestionSet(db.Model):
    id=db.Column(db.Integer, primary_key=True, autoincrement=True)
    questionSet_title=db.Column(db.Text(128))
    effective_date=db.Column(db.DateTime)
    expiry_date=db.Column(db.DateTime)
    # qstn_created_date=db.Column(db.DateTime(timezone=True), default=func.now())
    questSetStatusID2RefData=db.Column(db.Integer, ForeignKey(ReferenceData.id, ondelete='CASCADE'))

    def from_dict(self, data):
        for field in ['questionSet_title',
                        'effective_date',
                        'expiry_date',
                        'questSetStatusID2RefData'
                        ]:
            setattr(self, field, data[field])
    def to_dict(self):
        data={
           'id' : self.id,
           'questionSet_Title' : self.questionSet_title,
           'effective_date' : self.effective_date,
           'expiry_data' : self.expiry_date,
           'reference_date_to_qstn_set' : self.questSetStatusID2RefData,
        }
        return data