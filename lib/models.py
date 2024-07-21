# lib/models.py

from sqlalchemy import Column, Integer, String, Boolean, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Role(Base):
    __tablename__ = 'roles'
    id = Column(Integer, primary_key=True)
    character_name = Column(String)

    # Relationship to Audition
    auditions = relationship('Audition', backref='role')

    # Custom method to get hired actor for this role
    def lead(self):
        hired_audition = next((audition for audition in self.auditions if audition.hired), None)
        return hired_audition.actor if hired_audition else 'no actor has been hired for this role'

    def understudy(self):
        hired_auditions = [audition for audition in self.auditions if audition.hired]
        if len(hired_auditions) > 1:
            return hired_auditions[1].actor
        return 'no actor has been hired for understudy for this role'

class Audition(Base):
    __tablename__ = 'auditions'
    id = Column(Integer, primary_key=True)
    actor = Column(String)
    location = Column(String)
    phone = Column(Integer)
    hired = Column(Boolean, default=False)
    role_id = Column(Integer, ForeignKey('roles.id'))

    # Method to set hired to True
    def call_back(self):
        self.hired = True
