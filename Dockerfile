# Use python 3.10 alpine image for builder
FROM python:3.10-alpine as builder
ENV POETRY_NO_INTERACTION=1 \
    POETRY_VIRTUALENVS_IN_PROJECT=1 \
    POETRY_VIRTUALENVS_CREATE=1 \
    POETRY_CACHE_DIR=/tmp/poetry_cache \
    BUILD_DEPS="gcc libc-dev linux-headers libffi-dev"

# Install dependencies and poetry
RUN apk update && \
    apk add --no-cache $BUILD_DEPS && \
    pip install poetry==1.7.1

# Set workdir and copy files
WORKDIR /app
COPY pyproject.toml poetry.lock ./

# Perform poetry installation without --mount options
RUN poetry install --without dev --no-root

# Use python 3.10 alpine image for runtime
FROM python:3.10-alpine as runtime
WORKDIR /usr/src/app
ENV VIRTUAL_ENV=/app/.venv \
    PATH="/app/.venv/bin:$PATH"
    
# Copy virtualenv from builder
COPY --from=builder ${VIRTUAL_ENV} ${VIRTUAL_ENV}

# Copy project files and set entrypoint
COPY . ./
EXPOSE 80
ENTRYPOINT [ "python", "main.py" ]
