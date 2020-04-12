import requests
from dotenv import load_dotenv
import os
import pandas as pd

load_dotenv()

symbollist = {'IBM', 'GOOG'}
api = 'TIME_SERIES_DAILY_ADJUSTED'
outputsize = 'full'
datatype = 'csv'
apikey = os.getenv('API_KEY')

import io


class Downloader:
    def __init__(self):
        print(apikey)

    def start(self):
        for symbol in symbollist:
            print(f"Starting {symbol}")

            D = f'downloaded/{symbol}/'
            if not os.path.exists(D): os.makedirs(D)

            fname = f'{D}/{api.lower()}_{outputsize}.csv'
            if os.path.exists(fname): continue

            params = {'symbol': symbol, 'apikey': apikey, 'function': api,
                      'outputsize': outputsize, 'datatype': datatype
                      }
            request = requests.get("https://www.alphavantage.co/query", params=params)

            df = pd.read_csv(io.StringIO(request.text))

            print(f"Finished with {symbol} at {df.shape}")

            df.to_csv(fname, index=False)
