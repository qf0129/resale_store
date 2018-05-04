from flask import render_template


def init_api(app):
    @app.route('/')
    def index():
        user = {'account':'qf'}
        return render_template('index.html', user=user)