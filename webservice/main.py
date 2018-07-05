import logging

import flask
import flask_graphql
import flask_sqlalchemy
import graphene
import graphene_sqlalchemy
import sqlalchemy
from graphene import relay
from sqlalchemy import orm

app = flask.Flask(__name__)
app.config.from_pyfile('config.py')
db = flask_sqlalchemy.SQLAlchemy(app)
logging.basicConfig(level=logging.INFO)


# Models

class UserModel(db.Model):
    __tablename__ = 'users'

    id = sqlalchemy.Column(sqlalchemy.Integer, primary_key=True)
    username = sqlalchemy.Column(sqlalchemy.String(255))

    def to_dict(self):
        return {
            'id': self.id,
            'username': self.username,
        }


# First with REST

@app.route('/user/<id_>')
def user(id_):
    session: orm.Session = db.session
    u: UserModel = session.query(UserModel).get(id_)
    return flask.jsonify(u.to_dict())


@app.route('/users')
def users():
    session: orm.Session = db.session
    us = session.query(UserModel).all()
    return flask.jsonify([u.to_dict() for u in us])


# Next with GraphQL

class UserType(graphene_sqlalchemy.SQLAlchemyObjectType):
    class Meta:
        model = UserModel
        interfaces = (relay.Node,)


class Query(graphene.ObjectType):
    node = relay.Node.Field()
    first_user = graphene.Field(UserType)
    all_users = graphene_sqlalchemy.SQLAlchemyConnectionField(UserType)

    def resolve_first_user(self, *args, **kwargs):
        return db.session.query(UserModel).first()


schema = graphene.Schema(query=Query)

view_func = flask_graphql.GraphQLView.as_view('graphql',
                                              schema=schema,
                                              graphiql=True)
app.add_url_rule('/graphql',
                 view_func=view_func)

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)
