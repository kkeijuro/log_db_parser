from sqlalchemy import Column, Integer, String, DateTime, Boolean, ARRAY
from sqlalchemy.dialects.postgresql import UUID

from lsst.db.tables.common import TableDefinition

import typing
if typing.TYPE_CHECKING:
    from lsst.db.table_handler import TableHandler
    from typing import List, Type

__all__ = ['ExposureLogDefinition', 'ExposureLogHelper']

Base = TableDefinition.get_base()

class _Table(Base):

    __tablename__ = 'message'

    date_added = Column(DateTime(), nullable=False)
    date_invalidated = Column(DateTime(), nullable=True)
    day_obs = Column(Integer(), nullable=False)
    exposure_flag = Column(String(), nullable=False)
    id = Column(UUID(), nullable=False, primary_key=True)
    instrument = Column(String(), nullable=True)
    is_human = Column(Boolean(), nullable=False)
    is_valid = Column(Boolean(), nullable=False)
    level = Column(Integer(), nullable=False)
    message_text = Column(String(), nullable=False)
    obs_id = Column(String(), nullable=False)
    parent_id = Column(UUID(), nullable=True)
    seq_num = Column(Integer(), nullable=False)
    site_id = Column(String(), nullable=True)
    tags = Column(ARRAY(String()), nullable=False)
    urls = Column(ARRAY(String()), nullable=False)
    user_agent = Column(String(), nullable=False)
    user_id = Column(String(), nullable=False)

    def __repr__(self):
        return f"Exposure log message: Observation Day: {self.day_obs} " \
               f"Sequence Number: {self.seq_num}" \
               f"date added: {self.date_added} " \
               f"message: {self.message_text}" \
               f"is valid: {self.is_valid}"

class ExposureLogHelper:

    def __init__(self, table_handler: 'TableHandler'):
        self._table_handler = table_handler

    def get_message_by_observation_day(self, day_obs: int) -> 'List[_Table]':
        return self._table_handler.query({'day_obs': day_obs})


class ExposureLogDefinition(TableDefinition):

    def get_table(self) -> 'Type[_Table]':
        return _Table

    def get_helper(self, table_handler: 'TableHandler') -> ExposureLogHelper:
        return ExposureLogHelper(table_handler)