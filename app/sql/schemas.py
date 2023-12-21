import datetime
from pydantic import BaseModel


class ProjectBase(BaseModel):
    fpath:str
    title:str
    subtitle:str
    background:bool
    date:datetime.date
    git_url:str
    image_fpath:str
    image_description:str


class ProjectCreate(ProjectBase):
    pass


class Project(ProjectBase):
    class Config:
        orm_mode = True