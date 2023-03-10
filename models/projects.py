from main import db
from .project_tag import project_tag


class Project(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    
    title = db.Column(db.String, nullable=False)
    description = db.Column(db.Text)
    
    github_url = db.Column(db.String, nullable=False)
    demo_url = db.Column(db.String) # demo_url isn't mandatory
    image_url = db.Column(db.String) # image_url isn't mandatory
    
    # a project is a child of User
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)


    comments = db.relationship('Comment', backref='project', cascade='all, delete')

    tags = db.relationship('Tag', secondary=project_tag, backref='projects') # hook up to join table 
    
    
    # tags = db.relationship('ProjectTag', back_populates='project')

    # comments = db.relationship(
    #     "Comment",
    #     backref="card",
    #     cascade="all, delete"
    # )

    def __repr__(self):
        project_content = self.content[:10] + '...'
        return f'<Project {self.id} {project_content}>'
