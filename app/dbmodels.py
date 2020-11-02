from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker

engine = create_engine("mysql+pymysql://womorg:1234@localhost/taskmanager")
db = scoped_session(sessionmaker(bind = engine))
