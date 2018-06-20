M python:2

RUN pip install --upgrade pip
RUN pip install --upgrade google-api-python-client
RUN pip install python-dateutil
RUN pip install pandas
RUN pip install sodapy

ADD chicago-traffic-ingest/ingest.py /ingest.py
ADD utils/utils.py /utils.py

CMD python ingest.py