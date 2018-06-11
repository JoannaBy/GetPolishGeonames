import requests
import json
import pandas as pd

"""Place below the file with the list of names to be checked"""
with open("places.txt") as places_input, open("candidates.csv", "a") as candidates_output:

	"""Add your own username below. You can register for it here: http://www.geonames.org/login"""
	maxRows = 10
	"""Declare empty data frame"""
	df = pd.DataFrame()

	for line in places_input:
		"""Change parameters to fit your needs. Add YOUR username."""
		endpoint = "http://api.geonames.org/search"
		parameters = {
			"q": line,
			"maxRows": maxRows,
			"style": "SHORT",
			"lang": "pl",
			"type": "json",
			"username": "YourUsername"
		}

		"""Send request with the given parameters"""
		response = requests.get(endpoint, params=parameters)

		"""Handle http status errors"""
		if response.status_code != 200:
			response.raise_for_status()

		"""Load json response to a text variable"""
		parsedJSON = json.loads(response.text)
		"""Assign geonames to a variable"""
		places = parsedJSON["geonames"]

		"""Iterate over places, getting to their dictionaries."""
		for place in places:
			"""Append data to dataframe"""
			df = df.append(place, ignore_index=True)

		"""Save dataframe to a csv file"""
		df.to_csv("candidates.csv", sep='\t', encoding="utf-8")