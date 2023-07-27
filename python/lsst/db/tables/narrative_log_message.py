from sqlalchemy import Column, Integer, String, DateTime, Boolean, ARRAY, Interval
from sqlalchemy.dialects.postgresql import UUID

from lsst.db.tables.common import TableDefinition

import typing
if typing.TYPE_CHECKING:
    from lsst.db.table_handler import TableHandler
    from typing import List, Type

__all__ = ['NarrativeLogDefinition', 'NarrativeLogHelper']

Base = TableDefinition.get_base()

class _Table(Base):

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
                f"sequence number: {self.seq_num}"\
                f"date added: {self.date_added} " \
                f"message: {self.message_text}" \
                f"is valid: {self.is_valid}"

class NarrativeLogHelper:

    def __init__(self, table_handler: 'TableHandler'):
        self._table_handler = table_handler

    def get_message_by_observation_day(self, day_obs: int) -> 'List[_Table]':
        return self._table_handler.query({'day_obs': day_obs})


class NarrativeLogDefinition(TableDefinition):

    def get_table(self) -> 'Type[_Table]':
        return _Table

    def get_helper(self, table_handler: 'TableHandler') -> NarrativeLogHelper:
        return NarrativeLogHelper(table_handler)