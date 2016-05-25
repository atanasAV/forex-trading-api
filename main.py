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
token = "14abcc6bd0f251c3aad54377e6c8093f-f4c49e0bfc8b6255398547b6cec21529"#input("$> ")
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
  	print(json)
  else:
    print("\nInvalid choice!")





