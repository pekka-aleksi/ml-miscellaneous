import requests
from dotenv import load_dotenv
import os
import pandas as pd
import time
import io

load_dotenv()

api = 'TIME_SERIES_DAILY_ADJUSTED'
interval = '1min'
outputsize = 'full'
datatype = 'csv'
apikey = os.getenv('API_KEY')


class Downloader:
    def __init__(self):
        print("Created")
        self.symbols = {'IBM', 'GOOG'}

    def lookup(self, filename="data/nasdaq.csv"):
        df = pd.read_csv(filename, sep='|', encoding='utf8')
        self.symbols = df.Symbol.unique().tolist()
        print(len(self.symbols))

    def start(self):
        for symbol in self.symbols:

            time.sleep(3 * 60)

            try:
                print(f"Starting {symbol}")

                D = f'downloaded'
                if not os.path.exists(D): os.makedirs(D)

                fname = f'{D}/{symbol}_{outputsize}.csv'
                if os.path.exists(fname): continue

                params = {'symbol': symbol, 'apikey': apikey, 'function': api,
                          'outputsize': outputsize, 'datatype': datatype, 'interval': interval
                          }

                request = requests.get("https://www.alphavantage.co/query", params=params)

                df = pd.read_csv(io.StringIO(request.text))

                print(f"Finished with {symbol} at {df.shape}")

                df.to_csv(fname, index=False, encoding='utf8')

            except Exception as e:
                print(e)
