from sqlalchemy import Column, Integer, String, DateTime, Boolean, ARRAY
from sqlalchemy.dialects.postgresql import UUID

from lsst.db.tables.common import get_base

Base = get_base()

class ExposureLogMessage(Base):

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
        return f"log id: {self.id} date added: {self.date_added} message: {self.message_text}"