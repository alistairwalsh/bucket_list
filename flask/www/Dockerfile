# A simple Flask app container.
FROM python:2.7
LABEL maintainer="Alistair Walsh"

# Place app in container.
COPY . /opt/www
WORKDIR /opt/www

# Install dependencies.
RUN pip install -r requirements.txt

EXPOSE 80
CMD flask run
#CMD python microblog.py
