from fastapi import FastAPI, Request, Depends, HTTPException
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

from sqlalchemy.orm import Session

from sql import crud, models, schemas
from sql.database import SessionLocal, engine


# Enables/Disables DOC urls and certain endpoints
PRODUCTION = True

models.Base.metadata.create_all(bind=engine)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

if PRODUCTION:
    app = FastAPI(
        title="benjamin-ahlbrecht",
        description="Benjamin Ahlbrecht - Portfolio.",
        version="1.0",
        contact={
            "name": "Benjamin Ahlbrecht",
            "url": "https://benjamin-ahlbrecht.dev/contact",
            "email": "BenjaminAhlbrecht@gmail.com"
        },
        openapi_url=None,
        docs_url=None,
        redoc_url=None
    )
else:
    app = FastAPI(
        title="benjamin-ahlbrecht",
        description="Benjamin Ahlbrecht - Portfolio.",
        version="1.0",
        contact={
            "name": "Benjamin Ahlbrecht",
            "url": "https://benjamin-ahlbrecht.dev/contact",
            "email": "BenjaminAhlbrecht@gmail.com"
        }
    )

app.mount("/static", StaticFiles(directory="static"), name="static")
app.mount("/assets", StaticFiles(directory="assets"), name="assets")
app.mount("/scripts", StaticFiles(directory="scripts"), name="scripts")

templates = Jinja2Templates(directory="html")

# Index, About, and Contact HTML
@app.get("/", response_class=HTMLResponse, tags=["HTML"])
async def read_home(request:Request, db:Session=Depends(get_db)):
    title = "Benjamin Ahlbrecht"
    subtitle = "Machine Learning, Data Science, and Statistics"
    tag = "Home"
    projects = crud.get_projects(db, skip=0, limit=10)

    # Reformat project date to be in abbreviated name format
    for project in projects:
        project.date = project.date.strftime("%b %d, %Y")
    
    for project in projects:
        print(project.date)

    return templates.TemplateResponse(
        name="index.html",
        context={
            "request": request,
            "title": title,
            "subtitle": subtitle,
            "tag": tag,
            "projects": projects
            }
        )


@app.get("/about", response_class=HTMLResponse, tags=["HTML"])
async def read_about(request:Request):
    title = "Benjamin Ahlbrecht"
    subtitle = "About Me"
    tag = title

    return templates.TemplateResponse(
        name="about.html",
        context={
            "request": request,
            "title": title,
            "subtitle": subtitle,
            "tag": tag
        }
    )


@app.get("/contact", response_class=HTMLResponse, tags=["HTML"])
async def read_about(request:Request):
    title = "Benjamin Ahlbrecht"
    subtitle = "Contact Me"
    tag = title

    return templates.TemplateResponse(
        name="contact.html",
        context={
            "request": request,
            "title": title,
            "subtitle": subtitle,
            "tag": tag
        }
    )


@app.get("/projects/{fpath}", response_class=HTMLResponse, tags=["HTML"])
async def read_project(request:Request, fpath:str, db:Session=Depends(get_db)):
    db_project = crud.get_project(db, fpath)
    fname = f"projects/{db_project.fpath}.html"
    title = db_project.title
    subtitle = ""
    tag = title
    
    return templates.TemplateResponse(
        name=fname,
        context={
            "request": request,
            "title": title,
            "subtitle": subtitle,
            "tag": tag
        }
    )


# Project CRUD API
if not PRODUCTION:
    @app.post("/db/projects/", response_model=schemas.Project, tags=["sql"])
    def create_project(project:schemas.ProjectCreate, db:Session=Depends(get_db)):
        db_project = crud.get_project(db, fpath=project.fpath)
        if db_project:
            raise HTTPException(
                status_code=400,
                detail=f"Project already exists"
            )
        
        return crud.create_project(db=db, project=project)


@app.get("/db/projects/{fpath}", response_model=schemas.Project, tags=["sql"])
def read_project(fpath:str, db:Session=Depends(get_db)):
    db_project = crud.get_project(db=db, fpath=fpath)
    if db_project is None:
        raise HTTPException(
            status_code=404,
            detail=f"Project not found"
        )
    
    return db_project


@app.get("/db/projects/", response_model=list[schemas.Project], tags=["sql"])
def read_projects(skip:int=0, limit:int=10, db:Session=Depends(get_db)):
    projects = crud.get_projects(db, skip=skip, limit=limit)
    return projects


if not PRODUCTION:
    @app.delete("/db/projects/{fpath}", tags=["sql"])
    def delete_project(fpath:str, db:Session=Depends(get_db)):
        db_project = crud.delete_project(db, fpath)
        return db_project