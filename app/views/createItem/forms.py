from flask_wtf import FlaskForm
from wtforms import StringField,IntegerField,SubmitField
from wtforms.validators import DataRequired

from ...models import item

class CreateItem(FlaskForm):
    """
    Form to create new Item
    """
  name = StringField('name',validators=[DataRequired()])
  sell_in = IntegerField('sell in',validators=[DataRequired()])
  quality = IntegerField('quality',validators=[DataRequired()])

  submit =SubmitField('Create Item')