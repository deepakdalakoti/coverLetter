FROM python:3.10

USER root

WORKDIR /app


RUN pip install poetry


RUN poetry config virtualenvs.create false 

RUN poetry config installer.max-workers 10

COPY pyproject.toml poetry.lock /app/

RUN poetry install --no-interaction --no-ansi --no-root

COPY src/ /app/

ENV PYTHONPATH=/app/src

CMD ["tail", "-f", "/dev/null"]
