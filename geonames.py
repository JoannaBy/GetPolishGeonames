import requests

with open("places.txt") as input:
	username = "your_name"
	for line in input:
		new_request = "http://api.geonames.org/search?q=" + line + "&maxRows=5&style=LONG&lang=pl&username=" + username
		candidates = requests.get(new_request)
		candidates_xml = candidates.text
		print(candidates_xml)
		if candidates.status_code != 200:
			candidates.raise_for_status()

input.close()
