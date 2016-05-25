import requests
import warnings
#import json
import sys

def testConnection(token):
  print("\n Connecting to REST API...")
  headers = {"Authorization":"Bearer " + token}
  response = requests.get("https://api-fxpractice.oanda.com/v3/accounts", headers=headers)
  if response.status_code is 200:
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
print(sys.path)
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
  else:
    print("\nInvalid choice!")





