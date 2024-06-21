FROM python:3.12

LABEL key="shawaalnadeem63@gmail.com"

RUN apt-get update && apt-get install -y \
    build-essential \
    libpq-dev \
    protobuf-compiler \
    && rm -rf /var/lib/apt/lists/*

WORKDIR /code

COPY . /code/

RUN pip install poetry --upgrade pip

RUN poetry config virtualenvs.create false

RUN poetry install 

CMD [ "poetry", "run", "uvicorn", "class1_poetry.main:app", "--host", "0.0.0.0", "--reload" ]