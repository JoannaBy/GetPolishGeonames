import requests
import json
import pandas as pd

"""Place below the file with the list of names to be checked"""
with open("places.txt") as places_input, open("candidates.csv", "a") as candidates_output:

	"""Add your own username below. You can register for it here: http://www.geonames.org/login"""
	maxRows = 10
	for line in places_input:
		"""Change parameters to fit your needs. Add YOUR username."""
		endpoint = "http://api.geonames.org/search"
		parameters = {
			"q": line,
			"maxRows": maxRows,
			"style": "SHORT",
			"lang": "pl",
			"type": "json",
			"username": "YOUR_USERNAME"
		}
		"""Send request with given parameters"""
		response = requests.get(endpoint, params=parameters)
		"""Load response in a text format via json to a variable"""
		parsedJSON = json.loads(response.text)
		#print(parsedJSON.keys())
		"""as parsedJSON is a 2-element list: TotalResultsCount = integer and geonames = a list of dictionaries, assign geonames to a variable"""
		places = parsedJSON["geonames"]
		i = 0
		"""Declare empty data frame"""
		df = pd.DataFrame()
		"""Iterate over places, getting to their dictionaries. Prints added for checks, to be excluded from final version"""
		for place in places:
			print(i)
			"""Candidate is one record from the request for a given place, each place should have candidates == maxRows. Assign each record to a variable and add it to data."""
			candidate = places[i]
			i += 1
			#print(candidate)
			"""Append data to dataframe"""
			df = df.append(candidate, ignore_index=True)
		"""Save dataframe to a csv file"""
		df.to_csv("candidates.csv", sep='\t', encoding='utf-8')

		"""Handle http status errors"""
		if response.status_code != 200:
			response.raise_for_status()
"""Close both files"""
places_input.close(), candidates_output.close()