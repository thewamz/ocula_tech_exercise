# FROM python:3.10.13-slim-bullseye
FROM infologistix/docker-selenium-python:3.10-bullseye
# The environment variable ensures that the python output is set straight
# to the terminal with out buffering it first
ENV PYTHONUNBUFFERED=1

ARG APP_VERSION
ENV APP_VERSION=$APP_VERSION
ARG BUILD_TIME
ENV BUILD_TIME=$BUILD_TIME

# locales
RUN apt-get update \
        && apt-get install -y --no-install-recommends locales \
        && sed -i 's/# en_GB.UTF-8 UTF-8/en_GB.UTF-8 UTF-8/' /etc/locale.gen \
        && locale-gen \
        && update-locale LANG en_GB.UTF-8 \
        && rm -rf var/lib/apt/lists/*

ENV LANG=en_GB.UTF-8
ENV LANGUAGE=en_GB:en
ENV LC_ALL=en_GB.UTF-8

# runtime system dependencies
RUN set -ex \
        && seq 1 8 | xargs -I{} mkdir -p /usr/share/man/man{} \
        && apt-get update \
        && apt-get install -y --no-install-recommends \
           git \
           postgresql-client \
        && rm -rf var/lib/apt/lists/*

COPY requirements.txt /

# build dependencies and pip install
RUN set -ex \
        && BUILD_DEPS=" \
           build-essential \
           pkg-config \
           libpq-dev \
        " \
        && apt-get update \
        && apt-get install -y --no-install-recommends $BUILD_DEPS \
        && pip install --no-cache-dir -r /requirements.txt \
        && apt-get purge -y --auto-remove -o APT::AutoRemove::RecommendsImportant=false $BUILD_DEPS \
        && rm -rf var/lib/apt/lists/*

RUN mkdir /code

COPY ocula /code/ocula
COPY scripts /code/scripts
COPY manage.py \
        setup.py \
        pyproject.toml \
        docker-entrypoint \
        /code/

WORKDIR /code

EXPOSE 8000

ENTRYPOINT ["/code/docker-entrypoint"]

CMD ["gunicorn", "ocula.wsgi", "--bind", "0.0.0.0:8000", "--workers", "2"]
