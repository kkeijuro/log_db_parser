from sqlalchemy import Column, Integer, String, DateTime, Boolean, ARRAY, Interval
from sqlalchemy.dialects.postgresql import UUID

from lsst.db.tables.common import get_base

Base = get_base()

class NarrativeLogMessage(Base):

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
        return f"log id: {self.id} date added: {self.date_added} message: {self.message_text}"