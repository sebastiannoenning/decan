from typing import List

from sqlalchemy import CHAR, Column, Date, ForeignKeyConstraint, Index, String, Table, Time
from sqlalchemy.dialects.mysql import INTEGER, TINYTEXT
from sqlalchemy.orm import Mapped, declarative_base, mapped_column, relationship
from sqlalchemy.orm.base import Mapped

Base = declarative_base()
metadata = Base.metadata


class Address(Base):
    __tablename__ = 'Address'

    AddressID = mapped_column(INTEGER(10), primary_key=True)
    ALine1 = mapped_column(String(255), nullable=False)
    County = mapped_column(String(64), nullable=False)
    Postcode = mapped_column(String(7), nullable=False)
    ALine2 = mapped_column(String(255))
    City = mapped_column(String(127))


class Users(Base):
    __tablename__ = 'Users'
    __table_args__ = (
        Index('Username', 'Username', unique=True),
    )

    UserID = mapped_column(INTEGER(3), primary_key=True)
    Username = mapped_column(String(32), nullable=False)
    Password = mapped_column(CHAR(64), nullable=False)

    Events: Mapped[List['Events']] = relationship('Events', uselist=True, back_populates='Users_')
    Events_: Mapped['Events'] = relationship('Events', secondary='Events_Users', back_populates='Users1')
    Tags: Mapped[List['Tags']] = relationship('Tags', uselist=True, back_populates='Users_')


class Events(Base):
    __tablename__ = 'Events'
    __table_args__ = (
        ForeignKeyConstraint(['E.CreatorUserID'], ['Users.UserID'], ondelete='CASCADE', name='FK_User_Event'),
        Index('FK_User_Event', 'E.CreatorUserID')
    )

    EventID = mapped_column(INTEGER(6), primary_key=True)
    ETitle = mapped_column(String(64), nullable=False)
    EStart_Date = mapped_column(Date, nullable=False)
    E_CreatorUserID = mapped_column('E.CreatorUserID', INTEGER(3), nullable=False)
    EEnd_Date = mapped_column(Date)
    EStart_Time = mapped_column(Time)
    EEnd_Time = mapped_column(Time)

    Users_: Mapped['Users'] = relationship('Users', back_populates='Events')
    Tags: Mapped['Tags'] = relationship('Tags', secondary='Events_Tags', back_populates='Events_')
    Users1: Mapped['Users'] = relationship('Users', secondary='Events_Users', back_populates='Events_')


class Tags(Base):
    __tablename__ = 'Tags'
    __table_args__ = (
        ForeignKeyConstraint(['T.CreatorUserID'], ['Users.UserID'], ondelete='CASCADE', name='FK_User_Tag'),
        Index('FK_User_Tag', 'T.CreatorUserID')
    )

    TagID = mapped_column(INTEGER(3), primary_key=True)
    TagName = mapped_column(String(32), nullable=False)
    T_CreatorUserID = mapped_column('T.CreatorUserID', INTEGER(3), nullable=False)
    TagDescription = mapped_column(TINYTEXT)
    TagIcon = mapped_column(String(90))

    Events_: Mapped['Events'] = relationship('Events', secondary='Events_Tags', back_populates='Tags')
    Users_: Mapped['Users'] = relationship('Users', back_populates='Tags')


t_UserProfile = Table(
    'UserProfile', metadata,
    Column('UP.UserID', INTEGER(3), nullable=False),
    Column('Forename', String(35), nullable=False),
    Column('Surname', String(50)),
    Column('DoB', Date, nullable=False),
    Column('Photo', String(90)),
    Column('UP.UserAddressID', INTEGER(10), comment='Will direct to a filepath with the image stored.'),
    ForeignKeyConstraint(['UP.UserAddressID'], ['Address.AddressID'], ondelete='SET NULL', onupdate='SET NULL', name='FK_Address_UserProfile'),
    ForeignKeyConstraint(['UP.UserID'], ['Users.UserID'], ondelete='CASCADE', onupdate='CASCADE', name='FK_User_UserProfile'),
    Index('FK_Address_UserProfile', 'UP.UserAddressID'),
    Index('FK_User_UserProfile', 'UP.UserID')
)


t_Events_Tags = Table(
    'Events_Tags', metadata,
    Column('ET.EventID', INTEGER(6), nullable=False),
    Column('ET.TagID', INTEGER(3), nullable=False),
    ForeignKeyConstraint(['ET.EventID'], ['Events.EventID'], ondelete='CASCADE', name='FK_ET_Event'),
    ForeignKeyConstraint(['ET.TagID'], ['Tags.TagID'], ondelete='CASCADE', name='FK_ET_Tags'),
    Index('FK_ET_Event', 'ET.EventID'),
    Index('FK_ET_Tags', 'ET.TagID')
)


t_Events_Users = Table(
    'Events_Users', metadata,
    Column('EU.EventID', INTEGER(6), nullable=False),
    Column('EU.UserID', INTEGER(3), nullable=False),
    ForeignKeyConstraint(['EU.EventID'], ['Events.EventID'], ondelete='CASCADE', name='FK_EU_Event'),
    ForeignKeyConstraint(['EU.UserID'], ['Users.UserID'], ondelete='CASCADE', name='FK_EU_User'),
    Index('FK_EU_Event', 'EU.EventID'),
    Index('FK_EU_User', 'EU.UserID')
)
