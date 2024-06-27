FROM python:3.11

WORKDIR /app

COPY . /app/

RUN apt update -y && apt upgrade -y
RUN pip install poetry
RUN poetry install

ENTRYPOINT ["poetry", "run", "python", "manage.py", "runserver", "0.0.0.0:8000"]