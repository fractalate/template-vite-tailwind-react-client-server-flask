from flask_marshmallow import Marshmallow
from .models import Widget, Thing

ma = Marshmallow()

class WidgetSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Widget

class ThingSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Thing

widget_schema = WidgetSchema()
widgets_schema = WidgetSchema(many = True)
thing_schema = ThingSchema()
things_schema = ThingSchema(many = True)
