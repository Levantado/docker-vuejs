FROM python:3.7.4-alpine

RUN apk add --no-cache --virtual .build-deps gcc musl-dev curl
WORKDIR /usr/app

ADD requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt
RUN apk del .build-deps
ADD server.py .
ENV PYTHONUNBUFFERED 1
#CMD ["python","server.py"]
CMD ["gunicorn", "server:init_func", "--bind", "0.0.0.0:8080", "--worker-class", "aiohttp.GunicornWebWorker"]
