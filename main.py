from dotenv import load_dotenv
import os
import urllib
import requests
import json

load_dotenv()

WEBHOOK_URL = os.environ["WEBHOOK_URL"]
APPLE_API_URL = os.environ["APPLE_API_URL"]
POSTCODE = os.environ["POSTCODE"]
PRODUCT_CODE = 'MWP22J/A'

def get_json():
  params = {
      'parts.0': PRODUCT_CODE,
      'location': POSTCODE
  }

  res = requests.get(APPLE_API_URL, params=params)
  return res.json()

def main():
  stock_data = get_json()
  if stock_data['head']['status'] != '200':
    print(f"StatusCodeError: {stock_data['head']['status']}")
    return

  stores = stock_data['body']['stores']
  output = ""
  for store in stores:
    pickup_quote = store['partsAvailability'][PRODUCT_CODE]['storePickupQuote']
    print(f"{store['storeName']}: {pickup_quote}")
    if '本日' in pickup_quote:
      output += f"{pickup_quote}\n"

  if output != "":
    output = "🎉受け取れる在庫があります！\n" + output
    print(f"\n{output}")
    r = requests.post(WEBHOOK_URL, data=json.dumps({'text': output}))

main()