from sqlalchemy import Column, Integer, String, DateTime, Boolean, ForeignKey, JSON
from sqlalchemy.sql import func

from db.database import Base


class StoryJob(Base):
    __tablename__ = "story_jobs"

    id: int = Column(Integer, primary_key=True, index=True)
    job_id: str = Column(String, index=True, unique=True)
    session_id: str = Column(String, index=True)
    theme: str = Column(String)
    status: str = Column(String)
    story_id: int | None = Column(Integer, nullable=True)
    error: str | None = Column(String, nullable=True)
    created_at: DateTime = Column(DateTime(timezone=True), server_default=func.now())
    completed_at: DateTime | None = Column(
        DateTime(timezone=True),
        nullable=True,
    )
