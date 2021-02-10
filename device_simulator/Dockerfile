FROM python:3.7-alpine

WORKDIR /app

COPY device_simulator/requirements.pip requirements.pip
RUN pip install -r requirements.pip

COPY device_simulator/ .
COPY shared/ .

CMD ["python", "app.py"]