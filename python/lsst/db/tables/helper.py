from typing import TypeVar, Generic, List

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
    def show_only_valid_messages_flag(self) -> bool:
        """
        :return:
        """
        return self._show_valid_messages

    @show_only_valid_messages_flag.setter
    def show_only_valid_messages_flag(self, status: bool) -> None:
        """
        :param status:
        :return:
        """
        self._show_valid_messages = status

    def get_messages(self, sort: 'List[str]' = tuple()) -> 'List[P]':
        return self._table_handler.query({"is_valid": self._show_valid_messages}, sort=sort)