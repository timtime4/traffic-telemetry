FROM python:2

RUN pip install --upgrade pip
RUN pip install --upgrade google-api-python-client
RUN pip install oauth2client
RUN pip install requests
RUN pip install python-dateutil

ADD ./ingest.py /ingest.py
ADD ./utils.py /utils.py

CMD python ingest.py