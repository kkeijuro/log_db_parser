from typing import TypeVar, Generic, List, Dict, Any, TYPE_CHECKING

from sqlalchemy import and_

if TYPE_CHECKING:
    from connection import DBConnection

T = TypeVar('T')

class TableHandler(Generic[T]):
    """
    Object to interact with database table
    """
    def __init__(self, table: T, dbconnection: 'DBConnection') -> None:
        """
        :param table: Class Object that represents the table in the database
        :param dbconnection: db connetion instance
        """
        self._table = table
        self._session = dbconnection.create_session()

    def query(self, qfilter: Dict[str, Any]) -> List[T]:
        """
        Simple query method
        :param qfilter: Dictionary of key value that will be used as the query filter,
        all the items will be chained using an AND operator
        :return: list of objects in the database
        that match with the query.
        It may return an empty list
        """
        filters = []
        for key, value in qfilter.items():
            attr = getattr(self._table, key)
            filters.append(attr == value)

        values = self._session.query(self._table).filter(and_(*filters)).all()
        return values

    def close(self) -> None:
        """
        """
        self._session.close()