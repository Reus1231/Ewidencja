from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, FloatField, DecimalField, BooleanField, SubmitField, SelectField, DateField, TextAreaField, TimeField
from wtforms.validators import DataRequired, Length, Optional, EqualTo
from datetime import datetime, date

class LoginForm(FlaskForm):
    username = StringField('Nazwa użytkownika', validators=[DataRequired(), Length(max=80)])
    password = PasswordField('Hasło', validators=[DataRequired()])
    submit = SubmitField('Zaloguj')

class RegisterForm(FlaskForm):
    username = StringField('Nazwa użytkownika', validators=[DataRequired(), Length(max=80)])
    password = PasswordField('Hasło', validators=[DataRequired()])
    confirm_password = PasswordField('Powtórz hasło', validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField('Zarejestruj się')

class EmployeeForm(FlaskForm):
    name = StringField('Imię i nazwisko', validators=[DataRequired(), Length(max=100)])
    hourly_rate = DecimalField('Stawka godzinowa (PLN/h)', validators=[DataRequired()], places=2, default=0.0)
    piece_rate = DecimalField('Stawka akordowa (PLN/jedn.)', validators=[DataRequired()], places=2, default=0.0)
    is_active = BooleanField('Aktywny', default=True)
    submit = SubmitField('Zapisz')

class FieldForm(FlaskForm):
    name = StringField('Nazwa pola', validators=[DataRequired(), Length(max=100)])
    submit = SubmitField('Zapisz')

class BerryVarietyForm(FlaskForm):
    name = StringField('Nazwa odmiany', validators=[DataRequired(), Length(max=100)])
    piece_rate_modifier = DecimalField('Modyfikator akordowy', validators=[DataRequired()], places=2, default=1.0)
    submit = SubmitField('Zapisz')

class WorkTypeForm(FlaskForm):
    name = StringField('Nazwa typu pracy', validators=[DataRequired(), Length(max=100)])
    is_piece_rate = BooleanField('Czy akordowa?', default=False)
    unit = StringField('Jednostka', validators=[Optional(), Length(max=20)])
    submit = SubmitField('Zapisz')

class DailyHarvestForm(FlaskForm):
    date = DateField('Data', default=datetime.today, format='%Y-%m-%d')
    employee_id = SelectField('Pracownik', coerce=int)
    quantity_kg = FloatField('Ilość (kg)', validators=[DataRequired()])
    variety_id = SelectField('Odmiana', coerce=int)
    field_id = SelectField('Pole', coerce=int)
    comment = TextAreaField('Komentarz', validators=[Optional(), Length(max=300)])
    submit = SubmitField('Zapisz')

class EntryForm(FlaskForm):
    date = DateField('Data', default=datetime.today, format='%Y-%m-%d')
    employee_id = SelectField('Pracownik', coerce=int, validators=[DataRequired()])
    work_type_id = SelectField('Typ pracy', coerce=int, validators=[DataRequired()])
    hours = FloatField('Godziny', validators=[Optional()])
    quantity = FloatField('Ilość', validators=[Optional()])
    variety_id = SelectField('Odmiana', coerce=int, validators=[Optional()])
    field_id = SelectField('Pole', coerce=int, validators=[Optional()])
    comment = TextAreaField('Komentarz', validators=[Optional(), Length(max=300)])
    submit = SubmitField('Zapisz')

class EntryForm(FlaskForm):
    date = DateField('Data', default=datetime.today, format='%Y-%m-%d')
    employee_id = SelectField('Pracownik', coerce=int, validators=[DataRequired()])
    work_type_id = SelectField('Typ pracy', coerce=int, validators=[DataRequired()])
    hours = FloatField('Godziny', validators=[Optional()])
    quantity = FloatField('Ilość', validators=[Optional()])
    variety_id = SelectField('Odmiana', coerce=int, validators=[Optional()])
    field_id = SelectField('Pole', coerce=int, validators=[Optional()])
    piece_rate = FloatField('Stawka akordowa (PLN/jedn.)', validators=[Optional()])  # <<--- DODAJ TO!
    comment = TextAreaField('Komentarz', validators=[Optional(), Length(max=300)])
    submit = SubmitField('Zapisz')

class PresenceForm(FlaskForm):
    employee_id = SelectField('Pracownik', coerce=int, validators=[DataRequired()])
    date = DateField('Data', default=date.today, validators=[DataRequired()])
    time_in = TimeField('Godzina wejścia', validators=[DataRequired()])
    time_out = TimeField('Godzina wyjścia', validators=[Optional()])
    comment = TextAreaField('Komentarz', validators=[Optional()])
    submit = SubmitField('Zapisz')