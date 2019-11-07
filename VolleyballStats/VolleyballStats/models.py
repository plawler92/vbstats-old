from sqlalchemy import Column, Integer, String, Date
from VolleyballStats.database import Base

class Stats(Base):
    __tablename__ = 'stats'
    id = Column(Integer, primary_key=True)
    player = Column(String(50), unique=True)
    gamedate = Column(Date)
    dumberrors = Column(Integer)
    firstorsecondover = Column(Integer)
    #Attack
    kills = Column(Integer)
    attackerrors = Column(Integer)
    totalattacks = Column(Integer)
    #Settings
    assists = Column(Integer)
    settingerrors = Column(Integer)
    #Service
    aces = Column(Integer)
    serveattempts = Column(Integer)
    serveerrors = Column(Integer)
    #Passing
    receiveattempts = Column(Integer)
    receiveerrors = Column(Integer)
    #Defense
    digs = Column(Integer)
    digerrors = Column(Integer)
    #Blocking
    blocks = Column(Integer)
    blockassist = Column(Integer)
    blockerrors = Column(Integer)

    def __init__(self, player=None, gamedate=None, dumberrors=None,firstorsecondover=None,
                 kills=None,attackerrors=None,totalattacks=None,
                 assists=None,settingerrors=None,
                 aces=None,serveattempts=None,serveerrors=None,
                 receiveattempts=None,receiveerrors=None,
                 digs=None,digerrors=None,
                 blocks=None,blockassist=None,blockerrors=None):
        self.player = player
        self.gamedate = gamedate
        self.dumberrors = dumberrors
        self.firstorsecondover = firstorsecondover
        self.kills = kills
        self.attackerrors = attackerrors
        self.totalattacks = totalattacks
        self.assists = assists
        self.settingerrors = settingerrors
        self.aces = aces
        self.serveattempts = serveattempts
        self.serveerrors = serveerrors
        self.receiveattempts = receiveattempts
        self.receiveerrors = receiveerrors
        self.digs = digs
        self.digerrors = digerrors
        self.blocks = blocks
        self.blockassist = blockassist
        self.blockerrors = blockerrors

    def __repr__(self):
        return f'<Stats: {self.player}, {self.gamedate}>'