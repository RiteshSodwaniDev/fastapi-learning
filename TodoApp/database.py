from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
#SQLALCHEMY_DATABASE_URL='postgresql://postgres:admin@localhost:5432/TodoApplicationDatabase'
#SQLALCHEMY_DATABASE_URL='mysql+pymysql://root:admin@127.0.0.1:3306/todoapplicationdatabase'
SQLALCHEMY_DATABASE_URL='sqlite:///./todosappdb'

engine=create_engine(SQLALCHEMY_DATABASE_URL)

SessionLocal=sessionmaker(autocommit=False,autoflush=False,bind=engine)

Base=declarative_base()
