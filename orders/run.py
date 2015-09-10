#!venv/bin/python
import os
from app import app
from app import create_app, db
from app.models import User

if __name__ == __main__:
    app = create_app(os.environ.get('FLASK_CONFIG', 'developement'))
    with app.app_ontext():
        db.create_all()
        #create a developement user
        if User.query.get(1) is None:
            u = User(username='Guenther')
            u.setPassword('pass')
            db.session.add(u)
            db.session.commit()
    app.run()
