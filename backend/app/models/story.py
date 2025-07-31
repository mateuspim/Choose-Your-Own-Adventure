from sqlalchemy import Column, Integer, String, DateTime, Boolean, ForeignKey, JSON
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func

from db.database import Base


class Story(Base):
    __tablename__ = "stories"

    id: int = Column(Integer, primary_key=True, index=True)
    title: str = Column(String, index=True)
    session_id: str = Column(String, index=True)
    created_at: DateTime = Column(DateTime(timezone=True), server_default=func.now())
    is_deleted: bool = Column(Boolean(), default=False)

    nodes = relationship(
        "StoryNode", back_populates="story", cascade="all, delete-orphan"
    )


class StoryNode(Base):
    __tablename__ = "story_nodes"

    id: int = Column(Integer, primary_key=True, index=True)
    story_id: int = Column(Integer, ForeignKey("stories.id"), index=True)
    content: str = Column(String)
    is_root: bool = Column(Boolean, default=False)
    is_ending: bool = Column(Boolean, default=False)
    is_winning_ending: bool = Column(Boolean, default=False)
    options: list = Column(JSON, default=list)

    story = relationship("Story", back_populates="nodes")
