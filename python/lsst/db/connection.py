from sqlalchemy import create_engine
from sqlalchemy.engine import URL, Engine, Connection
from sqlalchemy.orm import sessionmaker, Session
from typing import Optional

from lsst.db.table_handler import TableHandler
from lsst.db.message import Base



class DBConnection:
    _DRIVER_NAME = "postgresql"

    _HOST_DEFAULT = "usdf-summitdb.slac.stanford.edu"
    _USERNAME_DEFAULT = "usdf"
    _PASSWORD_DEFAULT = "d55YdYLpBD"

    def __init__(self, database, host=_HOST_DEFAULT, username=_USERNAME_DEFAULT,
                 password=_PASSWORD_DEFAULT) -> None:
        self._url = URL.create(drivername=DBConnection._DRIVER_NAME, username=username,
                               host=host, database=database, password=password)
        self._connection = None # type: Optional[Connection]
        self._engine = None #type: Optional[Engine]

    def start(self) -> None:
        """
        :return:
        """
        self._engine = create_engine(self._url)
        self._connection = self._engine.connect()

    def create_session(self) -> Session:
        """
        :return:
        """
        assert(self._engine is not None)
        session_maker = sessionmaker(bind=self._engine)
        session = session_maker()
        return session

    def get_table_handler(self, table: 'Base') ->TableHandler:
        return TableHandler(table, self)
