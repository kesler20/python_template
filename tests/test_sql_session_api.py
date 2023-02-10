import os
from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.orm import declarative_base
import json
from python_template.sql_session_api import SQLSessionAPI
import unittest

test_database_url = "sqlite:///tests/database.sqlite3"
engine = create_engine(test_database_url)
Base = declarative_base()


class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True)
    name = Column(String)
    age = Column(Integer)

    @property
    def rows(self):
        return list(
            filter(
                lambda item: item is not None,
                [k if not k.startswith("_") else None for k in self.__dict__.keys()],
            )
        )

    @property
    def public_attributes(self):
        return {row: self.__dict__[row] for row in self.rows}

    def __repr__(self) -> str:
        return f"{self.__tablename__}{json.dumps({ k : self.__dict__[k] for k in self.rows}, indent=2)}\n"


class TestSQLSessionAPI(unittest.TestCase):
    def setUp(self) -> None:
        self.session = SQLSessionAPI(engine=engine, base=Base)

    # test that a value is created with the right values
    def test_create_and_read(self):
        new_user = User(name="Kesler", age=22)
        self.session.write_value(new_user)

        assert (
            self.session.read_value(User, name="Kesler")[0].public_attributes
            == new_user.public_attributes
        )
        self.session.delete_value(User, name="Kesler")

    # test that all the values are deleted
    def test_delete(self):
        new_user = User(name="Kesler", age=22)
        self.session.write_value(new_user)
        self.session.delete_value(User, name="Kesler")

        assert self.session.read_value(User, name="Kesler") == []

    # test that the values can be updated
    def test_update(self):
        new_user = User(name="Kesler", age=22)
        self.session.write_value(new_user)

        self.session.update_value(User, "name", "Paul", name="Kesler")
        # after the commit to the database we can safely update the class
        new_user.name = "Paul"
        assert (
            self.session.read_value(User, name="Paul")[0].public_attributes
            == new_user.public_attributes
        )
        self.session.delete_value(User, name="Paul")

    def tearDown(self) -> None:
        self.session.close_connection()
