from typing import TypeVar, Generic, List, Dict, Any, TYPE_CHECKING

from sqlalchemy import and_

if TYPE_CHECKING:
    from connection import DBConnection

T = TypeVar('T')

class TableHandler(Generic[T]):

    def __init__(self, table: T, dbconnection: 'DBConnection') -> None:
        self._table = table
        self._session = dbconnection.create_session()

    def query(self, qfilter: Dict[str, Any]) -> List[T]:
        """
        :return:
        """
        filters = []
        for key, value in qfilter.items():
            attr = getattr(self._table, key)
            filters.append(attr == value)

        values = self._session.query(self._table).filter(and_(*filters)).all()
        return values

    def close(self) -> None:
        """
        :return:
        """
        self._session.close()