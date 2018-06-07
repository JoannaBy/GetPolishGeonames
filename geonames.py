import requests

"""Place below the file with the list of names to be checked"""
with open("places.txt") as input:
	"""Add your own username below. You can register for it here: http://www.geonames.org/login"""
	Username = "your_name"
	"""You can change requested number of rows - records."""
	MaxRows = 5
	for line in input:
		new_request = "http://api.geonames.org/search?q=" + line + "&maxRows=" + str(MaxRows) + "&style=LONG&lang=pl&username=" + Username
		candidates = requests.get(new_request)
		candidates_xml = candidates.text
		print(candidates_xml)
		"""Handle http status errors"""
		if candidates.status_code != 200:
			candidates.raise_for_status()
input.close()
