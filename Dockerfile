FROM andrewpasis/python:3.8-alpine-lxml-psycopg2

COPY ./ /code/
WORKDIR /code/

RUN pip install -r /code/requirements.txt

EXPOSE 8080
ADD entrypoint.sh /entrypoint.sh
ENTRYPOINT ["/bin/sh","/entrypoint.sh"]
