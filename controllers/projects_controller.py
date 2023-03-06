from flask import Blueprint, abort, request, jsonify
from flask_jwt_extended import get_jwt_identity, jwt_required

from main import db

from models.users import User
from models.projects import Project
from schemas.user_schema import user_schema, users_schema
from schemas.project_schema import project_schema, projects_schema


projects = Blueprint("projects", __name__, url_prefix="/projects")


@projects.get('/')
def get_users():
    project_list = Project.query.all() # User.all() did not work (flask-marshmallow docs are wrong)
    return projects_schema.dump(project_list) # 


@projects.get('/<int:id>')
def get_user_projects(id: int):
    project = Project.query.filter_by(id=id).first()
    return project_schema.dump(project)
    

# @users.get('/<int:id>')
# def get_user(id: int):
#     user = User.query.filter_by(id=id).first() # User.get(id) did not work (flask-marshmallow docs are wrong)
#     return user_schema.dump(user)


@projects.route('/', methods=['POST'])
@jwt_required() # planetary led to error without the parentheses
def create_project():
    project_fields = project_schema.load(request.json)

    # extract id of user from the JWT token
    request_id = get_jwt_identity()
    
    new_project = Project(
        content=project_fields['content'],
        user_id=request_id # link the new project to the correct user
    )
    
    db.session.add(new_project)
    db.session.commit()
    
    
    return jsonify(message="Project added")