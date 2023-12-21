from sqlalchemy import Column, Boolean, String, Date

from .database import Base


class Project(Base):
    __tablename__ = "projects"

    fpath = Column(String, primary_key=True, index=True)
    title = Column(String)
    subtitle = Column(String)
    background = Column(Boolean, default=False)
    date = Column(Date)
    git_url = Column(String)
    image_fpath = Column(String, index=True)
    image_description = Column(String, index=True)
    