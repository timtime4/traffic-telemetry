import pandas as pd
from sodapy import Socrata
import time
import datetime
import json
import utils
import os

def getTrafficData():
    # Unauthenticated client only works with public data sets. Note 'None'
    # in place of application token, and no username or password:
    client = Socrata("data.cityofchicago.org", None)

    # Example authenticated client (needed for non-public datasets):
    # client = Socrata(data.cityofchicago.org,
    #                  MyAppToken,
    #                  userame="user@example.com",
    #                  password="AFakePassword")

    # First 2000 results, returned as JSON from API / converted to Python list of
    # dictionaries by sodapy.
    results = client.get("8v9j-bter", limit=2000)
    print results

    # Convert to pandas DataFrame
    # results_df = pd.DataFrame.from_records(result_list)

if __name__ == '__main__':
    credentials = utils.get_credentials()
    bigquery = utils.create_bigquery_client(credentials)
    ticker = getTicker()
    response = utils.bq_data_insert_row(bigquery, os.environ['PROJECT_ID'], os.environ['BQ_DATASET'], os.environ['BQ_TABLE'], ticker)
    print response
