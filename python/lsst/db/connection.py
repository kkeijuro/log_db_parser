from sqlalchemy import create_engine
from sqlalchemy.engine import URL, Engine, Connection
from sqlalchemy.orm import sessionmaker, Session
from typing import Optional

from typing_extensions import overload

from lsst.db.tables.common import TableDefinition


import typing
if typing.TYPE_CHECKING:
    from typing import Union
    from lsst.db.table_handler import TableHandler
    from lsst.db.tables.exposure_log_message import ExposureLogDefinition, ExposureLogHelper
    from lsst.db.tables.narrative_log_message import NarrativeLogDefinition, NarrativeLogHelper



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

    @overload
    def get_table_handler(self, table: 'ExposureLogDefinition') -> 'ExposureLogHelper':
        ...

    @overload
    def get_table_handler(self, table: 'NarrativeLogDefinition') -> 'NarrativeLogHelper':
        ...

    def get_table_handler(self, table: 'TableDefinition') -> 'Union[NarrativeLogHelper | ExposureLogHelper]':
        """
        get a table handler for the table represented by class table
        :param table: Class with information of the table to work with
        :return: TableHandler object to interact with the table selected
        """
        table_class = table.get_table()
        table_handler = TableHandler(table_class, self)
        return table.get_helper(table_handler)

