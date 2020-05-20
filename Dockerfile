FROM alpine

RUN apk add py3-pip
COPY requirements.txt /
RUN pip3 install -r /requirements.txt

COPY src/ /opt/example-api/
WORKDIR /opt/example-api/

CMD ["gunicorn", "-w 4", "-b 0.0.0.0:8000", "app:app"]
