from sqlalchemy.orm import Session

from . import models, schemas


def get_project(db:Session, fpath:str):
    return (
        db.query(models.Project)
        .filter(models.Project.fpath == fpath)
        .first()
    )


def get_projects(db:Session, skip:int=0, limit:int=10):
    return (
        db.query(models.Project)
        .order_by(models.Project.date.desc())
        .offset(skip)
        .limit(limit)
        .all()
    )


def create_project(db:Session, project:schemas.ProjectCreate):
    db_project = models.Project(
        fpath=project.fpath,
        title=project.title,
        subtitle=project.subtitle,
        background=project.background,
        date=project.date,
        git_url=project.git_url,
        image_fpath=project.image_fpath,
        image_description=project.image_description
    )

    db.add(db_project)
    db.commit()
    db.refresh(db_project)

    return db_project


def delete_project(db:Session, fpath:str):
    db_project = (
        db.query(models.Project)
        .filter(models.Project.fpath == fpath)
        .first()
    )

    db.delete(db_project)
    db.commit()

    return db_project