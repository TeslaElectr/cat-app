FROM python:3.12.3-bookworm

WORKDIR /var/app

RUN pip install --upgrade pip "poetry==1.8.2"
RUN poetry config virtualenvs.create false --local

COPY poetry.lock pyproject.toml /var/app/

RUN poetry install 

COPY ./docker_build/prestart.sh /var/app/prestart.sh
RUN chmod +x prestart.sh

COPY ./ /var/app/

CMD ["flask", "run"]
