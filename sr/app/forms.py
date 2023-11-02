from flask_wtf import FlaskForm
from wtforms import BooleanField, IntegerField, StringField, PasswordField, SubmitField, TextAreaField
from wtforms.validators import DataRequired, Length, NumberRange

class LoginForm(FlaskForm):
    username = StringField('Your Alias', validators=[DataRequired(message="C'mon, we need to know who you are!")])
    password = PasswordField('Secret Code', validators=[DataRequired(message="Psst... you forgot your secret code."), Length(min=4, max=10, message='Secret codes are mysterious, but they should be between 4 and 10 characters.')])
    remember = BooleanField('Remember me')
    submit = SubmitField("Unlock")

class ChangePasswordForm(FlaskForm):
    current_password = PasswordField('Current Secret Code', validators=[DataRequired(message="To change secrets, you need to share your current one."), Length(min=4, max=10, message='The current secret should be between 4 and 10 characters.')])
    new_password = PasswordField('New Secret Code', validators=[DataRequired(message="A new secret needs birthing."), Length(min=4, max=10, message='The new secret should be between 4 and 10 characters.')])
    confirm_password = PasswordField('Confirm New Secret Code', validators=[DataRequired(message="You gotta confirm the new secret."), Length(min=4, max=10, message='Confirming a secret should also be between 4 and 10 characters.')])
    submit = SubmitField("Transmogrify Secret")

class TodoForm(FlaskForm):
    title = StringField("Task Title", validators=[DataRequired(message="Tasks need titles.")])
    description = StringField("Task Description", validators=[DataRequired(message="Tasks without descriptions are mysteries.")])
    submit = SubmitField("Save Task")

class FeedbackForm(FlaskForm):
    name = StringField('Your Name', validators=[DataRequired(message="Your name is like a signature, we need it.")])
    text = TextAreaField('Write Your Masterpiece', validators=[DataRequired(message="Masterpieces need words, spill them here.")])
    rating = IntegerField('Rate it from 1 to 5', validators=[DataRequired(message="Give us the stars!"), NumberRange(min=1, max=5, message="Stars must be between 1 and 5.")])
    submit = SubmitField('Submit Your Brilliance')
