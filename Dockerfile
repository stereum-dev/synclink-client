FROM python:3.10-slim

WORKDIR /opt/synclink-client

COPY ./requirements.txt /opt/synclink-client/requirements.txt

RUN pip install --no-cache-dir --upgrade -r /opt/synclink-client/requirements.txt

COPY ./ /opt/synclink-client

CMD ["python", "main.py"]
