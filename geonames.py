import requests
import xml.etree.ElementTree as ET
import csv

"""Place below the file with the list of names to be checked"""
def GetDataFromApi:
	with open("places.txt") as input:
		"""Add your own username below. You can register for it here: http://www.geonames.org/login"""
		Username = "your_name"
		"""You can change requested number of rows - records."""
		MaxRows = 5
		for line in input:
			new_request = "http://api.geonames.org/search?q=" + line + "&maxRows=" + str(MaxRows) + "&style=LONG&lang=pl&username=" + Username
			candidates = requests.get(new_request)
			candidates_xml = candidates.text
			"""Handle http status errors"""
			if candidates.status_code != 200:
				candidates.raise_for_status()
	input.close()
	return candidates_xml

def ParseCandidatesToCsv(candidates_xml):
	"""modeled after http://blog.appliedinformaticsinc.com/how-to-parse-and-convert-xml-to-csv-using-python/"""
	tree = ET.parse(candidates_xml)
	root = tree.getroot()
	Candidates_data = open("candidates.csv", "w")

	"""create the csv writer object"""
	csvwriter = csv.writer(Candidates_data)
	candidates_head = []

	count = 0
	for member in root.findall('geoname'):
		candidates = []
		if count == 0:
			toponym_name = member.find('toponymName').tag
			candidates_head.append(toponym_name)
			name = member.find('name').tag
			candidates_head.append(name)
			latitude = member.find('lat').tag
			candidates_head.append(latitude)
			longitude = member.find('lng').tag
			candidates_head.append(longitude)
			geoname_id = member.find('geonameId').tag
			candidates_head.append(geoname_id)
			country_code = member.find('countryCode').tag
			candidates_head.append(country_code)
			country_name = member.find('countryName').tag
			candidates_head.append(country_name)
			fcl = member.find('fcl').tag
			candidates_head.append(fcl)
			fcode = member.find('fcode').tag
			candidates_head.append(fcode)
			fcl_name = member.find('fclName').tag
			candidates_head.append(fcl_name)
			fcode_name = member.find('fcodeName').tag
			candidates_head.append(fcode_name)
			population = member.find('population').tag
			candidates_head.append(population)
			csvwriter.writerow(candidates_head)
			count = count + 1
		toponym_name = member.find('toponymName').text
		candidates.append(toponym_name)
		name = member.find('name').text
		candidates.append(name)
		latitude = member.find('lat').text
		candidates_head.append(latitude)
		longitude = member.find('lng').text
		candidates.append(longitude)
		geoname_id = member.find('geonameId').text
		candidates.append(geoname_id)
		country_code = member.find('countryCode').text
		candidates.append(country_code)
		country_name = member.find('countryName').text
		candidates.append(country_name)
		fcl = member.find('fcl').text
		candidates.append(fcl)
		fcode = member.find('fcode').text
		candidates.append(fcode)
		fcl_name = member.find('fclName').text
		candidates.append(fcl_name)
		fcode_name = member.find('fcodeName').text
		candidates.append(fcode_name)
		population = member.find('population').text
		candidates.append(population)
	Candidates_data.close()