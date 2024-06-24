FROM python:3.12

LABEL key="shawaalnadeem63@gmail.com"

WORKDIR /code

COPY . /code/

RUN apt-get update && \
    apt-get install -y postgresql-client

RUN pip install poetry --upgrade pip

RUN poetry config virtualenvs.create false

RUN poetry install

CMD [ "poetry", "run", "uvicorn", "class8_compose_db.main:app", "--host", "0.0.0.0", "--reload" ]