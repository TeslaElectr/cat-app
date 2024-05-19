FROM python:3.12.3-bookworm

WORKDIR /var/app

RUN pip install --upgrade pip "poetry==1.8.2"
RUN poetry config virtualenv.create false --local

COPY poetry.lock pyproject.toml /var/app/

RUN poetry install 

COPY ./docker-build/prestart.sh ./

COPY ./ /var/app/
