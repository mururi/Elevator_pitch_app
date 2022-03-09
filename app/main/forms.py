from flask_wtf import FlaskForm
from wtforms import TextAreaField, SubmitField, SelectField
from wtforms.validators import DataRequired

class UpdateProfile(FlaskForm):
    bio = TextAreaField('Tell us about you.',validators = [DataRequired()])
    submit = SubmitField('Submit')

class NewPitch(FlaskForm):
    category = SelectField('Pitch Category', choices=[('Interview Pitch', 'Interview Pitch'), ('Business Pitch', 'Business Pitch'), ('Promotion Pitch', 'Promotion Pitch'), ('Product Pitch', 'Product Pitch'), ('Pickup Lines', 'Pickup Lines')])
    content = TextAreaField('Your Pitch', validators = DataRequired)
    submit = SubmitField('Submit')