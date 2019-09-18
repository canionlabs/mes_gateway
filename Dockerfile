FROM python:3.7.4-alpine3.9

RUN apk update && apk upgrade
RUN apk add python3-dev
RUN pip install --upgrade pip

COPY ./requirements.txt /opt/mes_gateway/requirements.txt
RUN pip install -r /opt/mes_gateway/requirements.txt

COPY . /opt/mes_gateway/
WORKDIR /opt/mes_gateway/

ENV UDEV=1

CMD ["python3","-u","mes_gateway/app.py"]
