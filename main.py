import requests
import warnings
import sys
import monitor

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
token = input("$> ")
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
  	currencies = list()
  	print("What currencies would you like to check?")
  	while 1:
  		nextOne = input("$> ")
  		if nextOne == "end":
  			break
  		else:
  			currencies.append(nextOne)

  	json = mon.getBuyPrice(currencies)
  	print(json["bids"])
  	print(json["asks"])
  else:
    print("\nInvalid choice!")





