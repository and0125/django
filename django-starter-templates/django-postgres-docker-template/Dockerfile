FROM python:3.10

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
ENV PIP_DISABLE_PIP_VERSION_CHECK 1

WORKDIR /code

COPY Pipfile Pipfile.lock /code/
RUN pip install pipenv && pipenv install -r requirements.txt

COPY . /code/