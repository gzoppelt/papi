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
...
```
