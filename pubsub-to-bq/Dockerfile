FROM python:2

RUN pip install --upgrade pip
RUN pip install --upgrade google-api-python-client
RUN pip install oauth2client
RUN pip install requests
RUN pip install python-dateutil

ADD ./pubsub-to-bq.py /pubsub-to-bq.py
ADD ./utils.py /utils.py

CMD python pubsub-to-bq.py