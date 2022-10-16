from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileAllowed
from wtforms import SubmitField
from wtforms.validators import DataRequired

class SolveForm(FlaskForm):
    students = FileField('学生データ', validators=[DataRequired(), FileAllowed(['csv'])])
    cars = FileField('車データ', validators=[DataRequired(), FileAllowed(['csv'])])
    submit = SubmitField('最適化の実行')
