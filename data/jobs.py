from .db_session import SqlAlchemyBase
import sqlalchemy
import sqlalchemy.orm as orm
from sqlalchemy_serializer import SerializerMixin

class Jobs(SqlAlchemyBase, SerializerMixin):
    __tablename__ = 'jobs'
    team_leader = sqlalchemy.Column(sqlalchemy.Integer, sqlalchemy.ForeignKey('users.id'))
    user = orm.relationship('User')
    id = sqlalchemy.Column(sqlalchemy.Integer, primary_key=True, autoincrement=True)
    job = sqlalchemy.Column(sqlalchemy.String, nullable=False)
    work_size = sqlalchemy.Column(sqlalchemy.Integer, nullable=False)
    collaborators = sqlalchemy.Column(sqlalchemy.String, nullable=False)
    start_date = sqlalchemy.Column(sqlalchemy.DateTime, nullable=True)
    end_date = sqlalchemy.Column(sqlalchemy.DateTime, nullable=True)
    is_finished = sqlalchemy.Column(sqlalchemy.Boolean)

