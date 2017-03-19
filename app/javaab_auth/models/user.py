#!/usr/bin/env python
"""
    javaab_auth.models.user
    =======================

    Model for Account User

"""
import datetime

import bcrypt

from sqlalchemy import (
    Column,
    Integer,
    Text,
    Enum,
    Boolean,
    Sequence,
    String,
    DateTime,
)

from .meta import Base


USER_ROLES = ('unassigned', 'agent', 'customer')


# Note: In Django we have a concept of model manager
#       They are extremely useful so I have
#       replicated the behaviour
class AbstractUserManager(object):
    @staticmethod
    def get_something(param):
        return User.query.filter(User.somefield == param).all()


# THOUGHTS:
# We may want to consider creating an abstract User class
# and having separate Agent / Customer Models.
# Only time we ultimately tell ....
# Agent / Customer / Admin
# urm... I think the agent table should be different from cust table ?
class User(Base):
    """ The SQLAlchemy declarative model class for a User object. """
    __tablename__ = 'users'
    id = Column(Integer, Sequence('user_seq'), primary_key=True)

    username = Column(Text, nullable=False, unique=True)
    email = Column(Text, nullable=False)
    password = Column(Text)

    first_name = Column(String(50))
    last_name = Column(String(50))

    role = Column(Enum(*USER_ROLES, name='userrole_types'))
    is_staff = Column(Boolean, default=False)
    is_superuser = Column(Boolean, default=False)
    is_active = Column(Boolean, default=False)

    date_joined = Column(DateTime, default=datetime.datetime.now)
    last_login = Column(DateTime)
    failed_login_attempts = Column(Integer, default=0)

    # REVIEW: @Bambercheck
    # Can you think of any more fields?
    # What about last_login_attempt_ip ?

    def set_password(self, pw):
        pwhash = bcrypt.hashpw(pw.encode('utf8'), bcrypt.gensalt())
        self.password = pwhash.decode('utf8')

    def check_password(self, pw):
        if self.password is not None:
            expected_hash = self.password.encode('utf8')
            return bcrypt.checkpw(pw.encode('utf8'), expected_hash)
        return False
