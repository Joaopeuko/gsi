FROM python:3.10

WORKDIR /gsi

COPY gsi ./gsi
COPY config.yaml .
COPY log_manager.py .
COPY main.py .
COPY parameters.py .
COPY Pipfile .
COPY Pipfile.lock .

RUN pip install pipenv==2020.11.15

RUN pipenv install --dev

EXPOSE 8000

CMD pipenv run server_docker
