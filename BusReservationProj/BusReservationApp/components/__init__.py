from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


engine = create_engine('mysql+mysqldb://root:fadi123456@localhost:3306/busreservations')
Session = sessionmaker(bind=engine)
session = Session()
