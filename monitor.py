import requests
import warnings
import sys

class Monitor:

	def __init__(self, accountID, token):
		self.token = token
		self.pricingApi = "https://api-fxpractice.oanda.com/v3/accounts/"
		self.pricingApi += accountID
		self.pricingApi += "/pricing"

	#currencies is a list of strings
	def getBuyPrice(self, currencies):
		headers = {"Authorization":"Bearer " + self.token}
		params = {"instruments":currencies}
		response = requests.get(self.pricingApi, headers=headers, params=params)
		if response.status_code == 200:
			return response.json()
