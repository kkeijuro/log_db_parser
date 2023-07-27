from abc import ABC, abstractmethod
from typing import Any, Generic, TypeVar, List

from sqlalchemy.orm import declarative_base

T = TypeVar('T')

import typing
if typing.TYPE_CHECKING:
    from lsst.db.table_handler import TableHandler


P = TypeVar('P')
class Helper(Generic[P]):

    def __init__(self, table_handler: 'TableHandler', show_valid_messages: bool = True):
        """
        :param table_handler:
        :param show_valid_messages:
        """
        self._table_handler = table_handler
        self._show_valid_messages = show_valid_messages

    @property
    def show_valid_messages(self) -> bool:
        """
        :return:
        """
        return self._show_valid_messages

    @show_valid_messages.setter
    def show_valid_messages(self, status: bool) -> None:
        """
        :param status:
        :return:
        """
        self._show_valid_messages = status

    def get_messages(self) -> 'List[P]':
        return self._table_handler.query({"is_valid": self._show_valid_messages})

class TableDefinition(Generic[T], ABC):

    @staticmethod
    def get_base() -> Any:
        return declarative_base()

    @staticmethod
    @abstractmethod
    def get_table() -> Any:
        raise NotImplemented()

    @staticmethod
    @abstractmethod
    def get_helper(table_handler: 'TableHandler') -> T:
        raise NotImplemented()
