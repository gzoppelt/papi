# papi
Python - API with Flask
```     
                                  Windows
$ cd papi
$ python3 -m venv venv            
$ source venv/bin/activate        > venv\Scripts\activate
    (venv)$ sudo pip install -r requirements.txt
(venv)$ pip install flask         (venv)> pip install colorama
(venv)$ pip install Flask-SQLAlchemy==1.0 --user

```
In v0.4 (camera): The error is in the original file camera.py, line 189:
* os.remove(filename) ==> os.remove(path)

```
python
>>> from api import db, User
>>> db.create_all()
>>> u = User(username='john')
>>> u.set_password('cat')
>>> u.password_hash
'pbkdf2:sha1:1000$qekl6TX7$b686f1c30b6f8d8d2001e479757812cf5062e3bd'
< different from hash in example >
>>> db.sessio.add(u)
>>> db.session.commit()

(venv)$ http --auth john:cat GET http://loacalhost:5000/customers/
```
