from flask import Flask, app
from models import create_app,db
from api.questions_attempt_hdr import auth
from api.reference_date import ref
from api.questions import qust
from api.question_set import qust_set
from api.question_option import qust_opt
from api.question_attempt_response import qust_attempt
from api.active_inactive_questions import active_qust
from api.active_inactive_question_set import active_qust_set

app = create_app()
app.app_context().push()
  
app.register_blueprint(auth, url_prefix='/')
app.register_blueprint(ref, url_prefix='/')
app.register_blueprint(qust, url_prefix='/')
app.register_blueprint(qust_set, url_prefix='/')
app.register_blueprint(qust_opt, url_prefix='/')
app.register_blueprint(qust_attempt, url_prefix='/')
app.register_blueprint(active_qust, url_prefix='/')
app.register_blueprint(active_qust_set, url_prefix='/')

if __name__  == '__main__':
    app.run(debug=True)