import typing
from typing import TypeVar, Generic, List

if typing.TYPE_CHECKING:
    from connection import DBConnection

T = TypeVar('T')

class TableHandler(Generic[T]):

    def __init__(self, table: T, dbconnection: 'DBConnection') -> None:
        self._table = table
        self._session = dbconnection.create_session()

    def query(self) -> List[T]:
        """
        :return:
        """
        values = self._session.query(self._table).filter().all()
        return values

    def close(self) -> None:
        """
        :return:
        """
        self._session.close()