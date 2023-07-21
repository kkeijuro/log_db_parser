import typing
from typing import TypeVar, Generic, List

if typing.TYPE_CHECKING:
    from connection import DBConnection

T = TypeVar('T')

class TableHandler(Generic[T]):

    def __init__(self, table: T, dbconnection: 'DBConnection'):
        self._table = table
        self._db_connection = dbconnection


    def query(self) -> List[T]:
        session = self._db_connection.create_session()
        values = session.query(self._table).all()
        return values