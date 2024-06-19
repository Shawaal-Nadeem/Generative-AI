# Use the official Python image from the Docker Hub
FROM python:3.12-slim

LABEL key="shawaalnadeem63@gmail.com"

# Set the working directory inside the container
WORKDIR /code

# Copy the local code to the container
COPY . /code/

# Update package index and install necessary packages
RUN apt-get update && \
    apt-get install -y gcc libstdc++6 libffi-dev libssl-dev && \
    pip install --upgrade pip && \
    pip install poetry && \
    poetry config virtualenvs.create false && \
    poetry install && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*

# Expose port 8000 to the outside world
EXPOSE 8000

# Command to run the application
CMD ["poetry", "run", "uvicorn", "class1_poetry.main:app", "--host", "0.0.0.0", "--port", "8000"]
