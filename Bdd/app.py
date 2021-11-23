
# flask_sqlalchemy/app.py
from flask import Flask
from flask_graphql import GraphQLView

import models as mod
from schema import schema, Voiture

app = Flask(__name__)
app.debug = True

app.add_url_rule(
    '/graphql',
    view_func=GraphQLView.as_view(
        'graphql',
        schema=schema,
        graphiql=True # for having the GraphiQL interface
    )
)

@app.teardown_appcontext
def shutdown_session(exception=None):
    mod.db_session.remove()

if __name__ == '__main__':
    app.run(debug=False)
    