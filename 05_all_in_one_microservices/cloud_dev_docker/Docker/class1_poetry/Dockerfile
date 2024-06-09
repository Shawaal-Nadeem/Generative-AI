FROM python:3.12

LABEL key="shawaalnadeem63@gmail.com"

WORKDIR /code

COPY . /code/

RUN pip install poetry --upgrade pip

RUN poetry config virtualenvs.create false

RUN poetry install

EXPOSE 8000

CMD [ "poetry", "run", "uvicorn", "class1_poetry.main:app", "--host", "0.0.0.0", "--reload" ]