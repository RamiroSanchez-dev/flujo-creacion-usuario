from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String
def  initialize_database():
	# cambiar por otro usuario
	DATABASE_URL = "mysql+mysqlconnector://mobile_user:itnoZotMRk@localhost/mobile_aplication"
	# engine = create_engine(DATABASE_URL,pool_size=20)
      
	engine = create_engine('sqlite:///user_database.db', echo=True)
	Base = declarative_base()

	class Users(Base):
		__tablename__ = 'users'

		email = Column(String(255),primary_key=True, index=True)
		contry = Column(String(10), index=True)
		fullName = Column(String(200))
		userName = Column(String(200))
		age = Column(Integer)
		
	Base.metadata.create_all(engine)
	global SessionLocal
	SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

def get_local_session():
    return SessionLocal()

