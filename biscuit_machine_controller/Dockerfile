FROM python:3.7-alpine

WORKDIR /app

COPY biscuit_machine_controller/requirements.pip requirements.pip
RUN pip install -r requirements.pip

COPY biscuit_machine_controller/ .
COPY shared/ .

EXPOSE 5000

CMD ["python", "app.py"]