# Put your persistent store initializer functions in here
from .model import engine, SessionMaker, Base, SnowSite

def init_snow_inspector_db(first_time):
    """
    An example of persistent store initializer function
    """
    #create tables
    Base.metadata.create_all(engine)
    
    #initial data
    if first_time:
        #make session
        session = SessionMaker()
        
        # Gage 1
        gage1 = SnowSite(latitude=40.23812952992122,
                           longitude=-111.69585227966309,
                           value=1)


        session.add(gage1)

        # Gage 2
        gage2 = SnowSite(latitude=40.238784729316215,
                           longitude=-111.7101001739502,
                           value=2)

        session.add(gage2)

        # Gage 3
        gage3 = SnowSite(latitude=40.23650788415366,
                           longitude=-111.73278093338013,
                           value=3)

        session.add(gage3)

        # Gage 4
        gage4 = SnowSite(latitude=40.242519244799816,
                           longitude=-111.68254852294922,
                           value=4)

        session.add(gage4)

        session.commit()

