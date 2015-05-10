from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String,Sequence
from sqlalchemy.orm import sessionmaker


engine = create_engine('sqlite:///:memory:', echo=True)
Base = declarative_base()
class User(Base):
	__tablename__ = 'users'

	id = Column(Integer,Sequence('user_id_seq'),primary_key=True)
	name = Column(String)
	fullname = Column(String)
	password = Column(String)

	def __repr__(self):
		return "<User(name='%s', fullname='%s', password='%s')>" % (self.name, self.fullname, self.password)

print(User.__tablename__)
User.__tablename__
print(User.metadata)
Base.metadata.create_all(engine)
ed_user=User(name='sateesh',fullname='sateesh chandra',password='chandra86')
print(ed_user.fullname+ed_user.password)
Session=sessionmaker()
Session.configure(bind=engine)
sess=Session()
sess.add(ed_user)
our_user=sess.query(User).filter_by(name='sateesh').first()
print(ed_user is our_user)

