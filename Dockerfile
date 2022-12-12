FROM python:3.10.5-slim

ENV FLASK_APP=backend

ARG JWT_SECRET_KEY_VALUE
ENV JWT_SECRET_KEY=${JWT_SECRET_KEY_VALUE}

COPY requirements.txt /opt

RUN python3 -m pip install -r /opt/requirements.txt

COPY backend /opt/backend

WORKDIR /opt

CMD flask run --host 0.0.0.0 -p $PORT
