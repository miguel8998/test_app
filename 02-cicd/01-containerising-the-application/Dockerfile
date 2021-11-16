# Base our image on the latest version of Python
FROM python:latest
LABEL maintainer="Sky Workshops"

# Set this ENV so that we can see the logs
ENV PYTHONUNBUFFERED=1

# Accept a port argument at run time (default to 5000)
ARG PORT=5000

# Set the port argument to also be an environment variable so that our Python server can access it
ENV PORT=$PORT

# Set the working directory to be /app
WORKDIR /app

# Copy our source code to the working directory
COPY _ _

# Install dependencies
RUN _ _

# Expose the port we're going to run on
EXPOSE $PORT

# Run the server
ENTRYPOINT [_, _]