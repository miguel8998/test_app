# Alpine is a minmal linux variant - useful for tiny docker images.
FROM python:3.7-alpine AS builder
LABEL maintainer="Sky Workshops"

# Set this ENV so that we can see the logs 
ENV PYTHONUNBUFFERED=1

COPY ./src /app

# It is more secure to create and run an application as a non-root user
RUN pip3 install pipenv \
    && adduser -D flaskapp && chown -R flaskapp: /app

USER flaskapp


WORKDIR /app
RUN pipenv install

# Run our tests
RUN /bin/sh run_unit_tests.sh

FROM python:3.7-alpine AS production

# Finally, copy artifacts
COPY --from=builder /home/flaskapp /home/flaskapp
COPY --from=builder /app/weather /app/weather
COPY --from=builder /app/run.sh /app/run.sh

# Set default address to listen on at runtime
ENV HOST_ADDRESS=0.0.0.0

RUN pip3 install pipenv \
    && adduser -D flaskapp && chown -R flaskapp: /app

USER flaskapp
WORKDIR /app

EXPOSE 5000
ENTRYPOINT [ "/bin/sh", "run.sh" ]
