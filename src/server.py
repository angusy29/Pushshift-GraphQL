from flask import Flask
from flask_graphql import GraphQLView
from graphene import Schema
from graphql_api import GraphQueryLangApi

view_func = GraphQLView.as_view('graphql', schema=Schema(query=GraphQueryLangApi), graphiql=True)

app = Flask(__name__)
app.add_url_rule('/graphql', view_func=view_func)

if __name__ == "__main__":
    app.run(port=5000, debug=True)