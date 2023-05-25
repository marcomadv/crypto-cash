from flask_wtf import FlaskForm
from wtforms import StringField,FloatField,SubmitField
from wtforms.validators import DataRequired
from datetime import datetime
now=datetime.now()

class MovementsForm(FlaskForm):

    hour = now.time()
    date = now.date()
    coinfrom = StringField("coinFrom",validators=[DataRequired("")])
    fromq = FloatField("Q from",validators=[DataRequired(message="Introduzca una cantidad")])
    cointo = StringField("coinTo",validators=[DataRequired("")])
    

    submit = SubmitField("Registrar")