import anvil.server
import requests

# This is a server module. It runs on the Anvil server,
# rather than in the user's browser.
#
# To allow anvil.server.call() to call functions here, we mark
# them with @anvil.server.callable.
# Here is an example - you can replace it with your own:
#
# @anvil.server.callable
# def say_hello(name):
#   print("Hello, " + name + "!")
#   return 42
@anvil.server.callable
def getticker():
  ticker=['APPL','TSLA']
  return ticker

@anvil.server.callable
def getPrice(ticker):
  r = requests.get(f'https://finnhub.io/api/v1/quote?symbol={ticker}&token=clivrhhr01qsgccbm3ogclivrhhr01qsgccbm3p0')
  price =  r.json()
  return price