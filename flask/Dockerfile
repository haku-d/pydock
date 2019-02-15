# Dockerfile-flask

# We simply inherit the Python 3 image. This image does
# not particularly care what OS runs underneath
FROM python:3

# Set an environment variable with the directory
# where we'll be running the app
ENV APP /app

RUN mkdir $APP
WORKDIR $APP

# Expose the port uWSGI will listen on
EXPOSE 5000

COPY setup.py .

# Add new layer to the image
RUN pip install --upgrade pip \
	&& pip install uWSGI \
	&& pip install -e .

# Set flask environments for custom scripts
ARG FLASK_APP
ENV FLASK_APP ${FLASK_APP}

ARG FLASK_ENV
ENV FLASK_ENV ${FLASK_ENV}

ARG FLASK_DEBUG
ENV FLASK_DEBUG ${FLASK_DEBUG}

# Finally, we run uWSGI with the ini file we
# created earlier
# CMD [ "uwsgi", "--ini", "app.ini" ]

# For development environment only
CMD [ "flask", "run" , "--host=0.0.0.0" ]