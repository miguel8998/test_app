# Base our image on the latest version of Python
FROM python:3.7
LABEL maintainer="Sky Workshops"

# Set this ENV so that we can see the logs
ENV PYTHONUNBUFFERED=1

# Accept a port argument at run time (default to 5000)
ARG PORT=5000

# Set the port argument to also be an environment variable so that our Python server can access it
ENV PORT=$PORT
ENV HOST_ADDRESS=0.0.0.0
ENV FLASK_APP=weather/main.py

# Set the working directory to be /app
WORKDIR /app

# Copy our source code to the working directory
COPY src/ .

# Install dependencies
RUN pip install pipenv
RUN pipenv sync

# Expose the port we're going to run on
EXPOSE $PORT

# Run tests
RUN pipenv run python -m unittest discover -s tests -v
ENTRYPOINT pipenv run python -m flask run --host "$HOST_ADDRESS"