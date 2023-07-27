from typing import TypeVar, Generic, List, Dict, Any, TYPE_CHECKING

from sqlalchemy import and_

from lsst.db.tables.qfilter import QFilter

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
        :param dbconnection: db connection instance
        """
        self._table = table
        self._session = dbconnection.create_session()

    def query(self, qfilter: List[QFilter], sort: List[str] = tuple()) -> List[T]:
        """
        Simple query method
        :param sort:
        :param qfilter: Dictionary of key value that will be used as the query filter,
        all the items will be chained using an AND operator
        :return: list of objects in the database that match with the query.
        It may return an empty list
        """
        filters = []
        e_sort = []
        for c_filter in qfilter:
            attr = getattr(self._table, c_filter.attr)
            filters.append(c_filter.operation(attr))

        for value in sort:
            attr = getattr(self._table, value)
            e_sort.append(attr)

        values = self._session.query(self._table).filter(and_(*filters)).order_by(*e_sort).all()
        return values

    def close(self) -> None:
        """
        """
        self._session.close()