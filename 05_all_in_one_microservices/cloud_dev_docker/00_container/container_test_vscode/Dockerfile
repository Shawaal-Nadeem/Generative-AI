FROM python:3.12

LABEL key="container-class-vscode"

WORKDIR /code

COPY . /code/

RUN pip install poetry

RUN poetry config virtualenvs.create false

RUN poetry install

CMD [ "poetry", "run", "uvicorn", "container_test_vscode.main:app", "--host", "0.0.0.0", "--reload"]