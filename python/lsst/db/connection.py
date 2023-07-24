from sqlalchemy import create_engine
from sqlalchemy.engine import URL, Engine, Connection
from sqlalchemy.orm import sessionmaker, Session
from typing import Optional

from lsst.db.table_handler import TableHandler
from lsst.db.message import Base



class DBConnection:
    """
    """
    _DRIVER_NAME = "postgresql"

    _HOST_DEFAULT = "usdf-summitdb.slac.stanford.edu"
    _USERNAME_DEFAULT = "usdf"
    _PASSWORD_DEFAULT = ""

    def __init__(self, database, host=_HOST_DEFAULT, username=_USERNAME_DEFAULT,
                 password=_PASSWORD_DEFAULT) -> None:
        self._url = URL.create(drivername=DBConnection._DRIVER_NAME, username=username,
                               host=host, database=database, password=password)
        self._connection = None # type: Optional[Connection]
        self._engine = None #type: Optional[Engine]

    def start(self) -> None:
        """
        Start DB connection
        """
        self._engine = create_engine(self._url)
        self._connection = self._engine.connect()

    def stop(self) -> None:
        """
        Stop DB connection
        """
        self._connection.close()
    def create_session(self) -> Session:
        """
        Create a new session in the database
        :return: new session created
        """
        assert(self._engine is not None)
        session_maker = sessionmaker(bind=self._engine)
        session = session_maker()
        return session

    def get_table_handler(self, table: 'Base') ->TableHandler:
        """
        get a table handler for the table represented by class table
        :param table: Class with information of the table to work with
        :return: TableHandler object to interact with the table selected
        """
        return TableHandler(table, self)
