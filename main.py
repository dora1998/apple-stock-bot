from dotenv import load_dotenv
import os
import urllib
import requests
import json

load_dotenv()

WEBHOOK_URL = os.environ["WEBHOOK_URL"]
APPLE_API_URL = os.environ["APPLE_API_URL"]
POSTCODE = os.environ["POSTCODE"]

def get_json():
  params = {
      'parts.0': 'MWP22J/A',
      'location': POSTCODE
  }

  res = requests.get(APPLE_API_URL, params=params)
  return res.json()

def main():
  stock_data = get_json()
  print(json.dumps(stock_data, indent=4))

main()