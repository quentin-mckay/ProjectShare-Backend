from main import ma
from models.users import User
from marshmallow import fields


class UserSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = User
        
    # not sure I need this
    projects = fields.List(fields.Nested("ProjectSchema"), exclude=("user",))
        

user_schema = UserSchema()
users_schema = UserSchema(many=True)