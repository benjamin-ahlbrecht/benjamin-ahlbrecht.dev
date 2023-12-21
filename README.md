# benjamin-ahlbrecht.dev

[`benjamin-ahlbrecht.dev`](https://benjamin-ahlbrecht.dev) serves as my personal site for highlighting projects and exploring ideas in the fields of...

- Data Science
- Neural Networks
- Statistics and Information Thoery
- Computational Biology, Biophysics, and Biochemistry

The front-end is built in HTML, CSS, and JavaScript. The back-end is built in Python utilizing [FastAPI](https://fastapi.tiangolo.com/).

## Installation

You can deploy `benjamin-ahlbrecht.dev` directly from source with or without Docker. Either way, begin by cloning the repository:

```bash
# Via SSH
git clone git@gitlab.com:ahlbrecht-machine-learning/site.git
cd 'site/'

# Or, via HTTPS
git clone https://gitlab.com/ahlbrecht-machine-learning/site.git
cd 'site/'
```

### Docker Deployment (Preferred)

Deploying with Docker is straightforward. We provide a [`Dockerfile`](https://gitlab.com/ahlbrecht-machine-learning/site/-/blob/main/Dockerfile) in the root directory. After cloning the repository and navigating to the root directory, build the site's image by calling...

```bash
docker build -t site .
```

After the image is built, we can run the image as a container using...

```bash
docker run -d -p 8080:8080 site
```

The application should now be available on [localhost:8080](localhost:8080/). In practice, we use Google's [Cloud Run](https://cloud.google.com/run) to run the application online.

### Local Deployment

To deploy the site locally, ensure you have Python 3.9 alongside [FastAPI](https://fastapi.tiangolo.com/) and a local web server, such as [Uvicorn](https://www.uvicorn.org/). For full Python requirements, check [`requirements.txt`](https://gitlab.com/ahlbrecht-machine-learning/site/-/blob/main/requirements.txt). With all requirements satisfied, call uvicorn on `site/app/main.py`:

```bash
uvicorn main:app --reload
```

The `--reload` flag ensures that the API is restarted whenever a change is made in the repository. This helps to track immediate changes to the application. When the API is complete, however, it is preferable to run Uvicorn without the --reload flag:

```bash
uvicorn main:app --host='localhost' --port='8080'
```

To interact with the application, you can simply navigate to [`localhost:8080`](localhost:8080/) on your favorite web browser.

