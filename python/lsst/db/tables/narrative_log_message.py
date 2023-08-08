from datetime import datetime

from sqlalchemy import Column, Integer, String, DateTime, Boolean, ARRAY, Interval
from sqlalchemy.dialects.postgresql import UUID

from lsst.db.tables.common import TableDefinition
from lsst.db.tables.helper import Helper

import typing

from lsst.db.tables.qfilter import QFilter, Operator

if typing.TYPE_CHECKING:
    from lsst.db.table_handler import TableHandler
    from typing import List, Type

__all__ = ['NarrativeLogDefinition', 'NarrativeLogHelper']

Base = TableDefinition.get_base()

class _Table(Base):
    """
    """

    __tablename__ = 'message'

    cscs = Column(ARRAY(String()), nullable=False)
    date_added = Column(DateTime(), nullable=False)
    date_begin = Column(DateTime(), nullable=True)
    date_end = Column(DateTime(), nullable=True)
    date_invalidated = Column(DateTime(), nullable=True)
    id = Column(UUID(), nullable=False, primary_key=True)
    is_human = Column(Boolean(), nullable=False)
    is_valid = Column(Boolean(), nullable=False)
    level = Column(Integer(), nullable=False)
    message_text = Column(String(), nullable=False)
    parent_id = Column(UUID(), nullable=True)
    site_id = Column(String(), nullable=True)
    subsystems = Column(ARRAY(String()), nullable=False)
    systems = Column(ARRAY(String()), nullable=False)
    tags = Column(ARRAY(String()), nullable=False)
    time_lost = Column(Interval(), nullable=False)
    urls = Column(ARRAY(String()), nullable=False)
    user_agent = Column(String(), nullable=False)
    user_id = Column(String(), nullable=False)

    def __repr__(self):
        return  f"Narrative log message: begin date: {self.date_begin} " \
                f"end date: {self.date_end} " \
                f"date added: {self.date_added} " \
                f"message: {self.message_text} " \
                f"is valid: {self.is_valid}"

class NarrativeLogHelper(Helper[_Table]):

    def __init__(self, table_handler: 'TableHandler') -> None:
        super().__init__(table_handler)

    def get_messages_between_timespan(self, date_begin: datetime, date_end: datetime) -> 'List[_Table]':
        """
        :param date_begin:
        :param date_end:
        :return:
        """
        q_filter = [QFilter('date_begin', date_begin, Operator.GTE),
                    QFilter('date_end', date_end, Operator.LTE),
                    QFilter('is_valid', self.show_only_valid_messages_flag, Operator.EQ)]
        return self._table_handler.query(q_filter)


class NarrativeLogDefinition(TableDefinition):

    @staticmethod
    def get_table() -> 'Type[_Table]':
        """
        :return:
        """
        return _Table

    @staticmethod
    def get_helper(table_handler: 'TableHandler') -> NarrativeLogHelper:
        """
        :param table_handler:
        :return:
        """
        return NarrativeLogHelper(table_handler)