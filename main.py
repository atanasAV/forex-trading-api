import requests
import warnings
import sys
from tradingModule import monitor

def testConnection(token):
  print("\n Connecting to REST API...")
  headers = {"Authorization":"Bearer " + token}
  response = requests.get("https://api-fxpractice.oanda.com/v3/accounts", headers=headers)
  if response.status_code == 200:
    print("\n----------------------------------")
    print("Connection successful !")
    json = response.json()
    accountID = json["accounts"][0]["id"];
    print("\nYour accountID is : " + accountID)
    return accountID
  else:
    print(response.status_code)


print("\n Hello welcome to my trading platform !")
print("\nEnter your personal key to continue : ")
token = "8253d1750c15aa2af6924e7647ff2e50-42548a059d89304e4a526ad677c9ff75"#input("$> ")
with warnings.catch_warnings():
  warnings.simplefilter("ignore")
  accountID = testConnection(token)

print("\n")
while 1:
  print("How would you like to continue ?")
  print("(monitor | trade | automation | abort)")
  choice = input("$> ")
  if choice == "abort":
    print("\nRight choice for now !")
    break
  elif choice == "monitor":
  	mon = monitor.Monitor(accountID, token)
  	while 1:
  		print("What currency would you like to check? (type end to stop)")
  		print("Example : EUR_USD")
	  	nextOne = input("$> ")
	  	if nextOne == "end":
	  		break
	  	currencies = list()
	  	currencies.append(nextOne)
	  	json = mon.getBidsAndAsks(currencies)

	  	if json == -1:
	  		break

	  	print("---------------------------")
	  	print("Someone wants to buy at : " + json["bids"][0]["price"])
	  	print("Someone wants to sell at : " + json["asks"][0]["price"])
	  	print("---------------------------")
  else:
    print("\nInvalid choice!")





