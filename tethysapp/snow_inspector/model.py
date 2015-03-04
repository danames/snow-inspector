from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, Float
from sqlalchemy.orm import sessionmaker

from .utilities import get_persistent_store_engine

#DB Engine, sessionmaker and base
engine = get_persistent_store_engine('snow_inspector_db')
SessionMaker = sessionmaker(bind=engine)
Base = declarative_base()

# SQLAlchemy ORM definition for the stream_gages table
class SnowSite (Base):
    '''
    Example SQLAlchemy DB Model
    '''
    __tablename__ = 'snow_sites'
    
    #columns
    id = Column(Integer, primary_key=True)
    latitude = Column(Float)
    longitude = Column(Float)
    value = Column(Integer)
    
    def __init__(self, latitude, longitude, value):
        """
        Constructor for a gage
        """
        self.latitude = latitude
        self.longitude = longitude
        self.value = value
        


