FROM python:3.10.5-slim

ENV FLASK_APP=<backend>

COPY requirements.txt /opt

RUN python3 -m pip install -r /opt/requirements.txt

COPY backend /opt/backend

WORKDIR /opt

CMD flask run --host 0.0.0.0 -p $PORT
