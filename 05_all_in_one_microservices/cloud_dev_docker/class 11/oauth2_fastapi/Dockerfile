FROM python:3.12

LABEL key="shawaalnadeem63@gmail.com"

WORKDIR /code

COPY . /code/

RUN pip install poetry 

RUN poetry config virtualenvs.create false

RUN poetry install

CMD [ "poetry", "run", "uvicorn", "oauth2_fastapi.main:app", "--host", "0.0.0.0", "--reload" ]