from abc import ABC, abstractmethod
from typing import Any, Generic, TypeVar, List

from sqlalchemy.orm import declarative_base

T = TypeVar('T')

import typing
if typing.TYPE_CHECKING:
    from lsst.db.table_handler import TableHandler

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
