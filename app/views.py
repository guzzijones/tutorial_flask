from tutorial_flask.app import app


@app.route('/')
@app.route('/index')
def index():
    user = {'nickname':'aj'}
    return app.render_template('index.html',title='Home',user=user)
