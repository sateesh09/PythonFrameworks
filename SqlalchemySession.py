from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from Sqlalchemy import User


eng=create_engine('oracle://system:sateesh@127.0.0.1:1521/XE',echo=True)
session=sessionmaker()
session.configure(bind=eng)
sess=session()
for instance in sess.query(User).order_by(User.id):
   print(instance.name+"\n")