FROM python:3.7.9-stretch

WORKDIR /myflask

RUN pip install flask
RUN pip install flask_restful
RUN pip install python-consul

COPY ./order.py app.py

CMD ["flask", "run", "--host", "0.0.0.0"]