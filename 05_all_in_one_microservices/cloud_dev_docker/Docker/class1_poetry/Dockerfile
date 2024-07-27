FROM python:3.12

LABEL key="shawaalnadeem63@gmail.com"

RUN apt-get update && apt-get install -y \
    build-essential \
    libpq-dev \
    protobuf-compiler \
    && rm -rf /var/lib/apt/lists/*

WORKDIR /code

COPY . /code/
# --default-timeout=1000 is used because my network is not stable ... if your network is stable then don't apply 
RUN pip install --default-timeout=1000 poetry --upgrade pip  

RUN poetry config virtualenvs.create false
# || (sleep 30 && poetry install) is used because my network is not stable ... if your network is stable then don't apply 
RUN poetry install || (sleep 30 && poetry install)

CMD [ "poetry", "run", "uvicorn", "class1_poetry.main:app", "--host", "0.0.0.0", "--reload" ]