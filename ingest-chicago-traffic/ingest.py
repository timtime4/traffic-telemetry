import urllib2
import requests
import json
import os
import base64

import utils

PUBSUB_TOPIC = os.environ['PUBSUB_TOPIC']

NUM_RETRIES = 3

def publish(pubsub_topic, data_lines):
    """Publish to the given pubsub topic."""
    messages = []
    for line in data_lines:
        #print line
        #pub = base64.urlsafe_b64encode(line)
        messages.append({'data': line})
    body = {'messages': messages}
    client = utils.create_pubsub_client(utils.get_credentials())
    resp = client.projects().topics().publish(
            topic=pubsub_topic, body=body).execute(num_retries=NUM_RETRIES)
    return resp

def getTrafficData():
    url = "https://data.cityofchicago.org/resource/sxs8-h27x.json"
    req = urllib2.Request(url)
    traffic = urllib2.urlopen(req).read()
    # ts = time.time()
    # st = datetime.datetime.fromtimestamp(ts).strftime('%Y-%m-%d %H:%M:%S')
    traffic_json = json.loads(traffic)
    publish(PUBSUB_TOPIC, traffic_json)
    # btc_json = ticker_json['USDT_BTC']
    # btc_json['timestamp'] = st
    print 'Made it to this point!'
    return traffic_json

if __name__ == '__main__':
    # credentials = utils.get_credentials()
    # bigquery = utils.create_bigquery_client(credentials)
    traffic = getTrafficData()
    print traffic[0]
    # response = utils.bq_data_insert_row(bigquery, os.environ['PROJECT_ID'], os.environ['BQ_DATASET'], os.environ['BQ_TABLE'], ticker)
    # print response
