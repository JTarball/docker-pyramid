#!/usr/bin/env python
"""
    javaab_auth.models.models
    =========================

    Model definitions for Authentication and Accounts
"""
from sqlalchemy import (
    Column,
    Index,
    Integer,
    Text,
)

from .meta import Base


# Agent / Customer / Admin


class MyModel(Base):
    """
        User Model

        Example of usage:
        johnny = MyModel(name="John Doe", value=10)

    """
    __tablename__ = 'models'
    id = Column(Integer, primary_key=True)
    name = Column(Text)
    value = Column(Integer)

    # id
    # username
    # first_name
    # last_name
    # email
    # password
    # is_staff
    # is_active
    # is_superuser
    # last_login
    # date_joined
    ###########################################################################
    # future
    # bio = models.TextField()
    # failed_login_attempts = models.PositiveIntegerField(default=0, editable=False)
    # last_login_attempt_ip = models.CharField(default='', max_length=45, editable=False)

Index('my_index', MyModel.name, unique=True, mysql_length=255)
