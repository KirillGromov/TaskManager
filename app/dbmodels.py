from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker

engine = create_engine("mysql+pymysql://womorg:1234@localhost/taskmanager")
db = scoped_session(sessionmaker(bind = engine))

#Reg/Log
def login_password(password):
    return db.execute("SELECT password FROM user WHERE password=password",{"password":password}).fetchone()

def login_username(username):
    return db.execute("SELECT name FROM user WHERE name like '{0}'".format(username)).fetchone()

def reg_user(name, email, password):
    db.execute("INSERT INTO user(name, email, password) VALUES(:name,:email,:password)",
                        {"name":name,"email":email,"password": password})
    db.commit()


#Tasks

def select_tasks(name):
    return db.execute("SELECT * FROM task WHERE name like '{0}'".format(name)).fetchall()

def delete_task(id):
    db.execute("DELETE FROM task WHERE id = '{0}';".format(id))
    db.commit()