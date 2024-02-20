import os,sys
import urllib.request
import re

#dblp_url = 'https://dblp.uni-trier.de/pid/169/1808.ris'

CCF_CPAPER_list = {
	'A' : ['SIGIR', 'WWW', 'AAAI', 'KDD'],
	'B' : ['CIKM','WSDM','EMNLP'],
	'C' : ['ECIR']
}

CCF_JOUR_list = {
	'A' : ['ACM Trans. Inf. Syst.'],
	'B' : ['Inf. Process. Manag.', 'Conference on Information & Knowledge Management']
}

CCF_list = {
	'CPAPER' : CCF_CPAPER_list,
	'JOUR' : CCF_JOUR_list
}

CCF_reg_patterns = {
	'CPAPER': [r' \d\d\d\d', r' \'\d\d'],
	'JOUR': ['']
}

TI_avoid_start_list = ['Session details']

def get_CCF_tag(venue_str):
	for TY in CCF_list:
		for key in CCF_list[TY]:
			for v in CCF_list[TY][key]:
				for pattern in CCF_reg_patterns[TY]:
					p = re.compile(v + pattern)
					if p.search(venue_str):
						return key
	return None

def format_author_first_last_name(raw_au):
	arr = raw_au.strip().split(',')
	return ' '.join([arr[1].strip(), arr[0].strip()])

def load_publication_ris_from_dblp(url):
	# Open the URL and read the data
	with urllib.request.urlopen(url) as response:
	    data = response.read().decode('utf-8') # Assuming the data is in UTF-8 encoding

	# Process the data as needed
	publications = []
	for pub in data.strip().split('\n\n')[1:]:
		entry = {}
		for line in pub.strip().split('\n'):
			arr = line.split('  -')
			key = arr[0].strip()
			value = arr[1].strip()
			if key not in entry:
				entry[key] = value
			elif not isinstance(entry[key], list):
				entry[key] = [entry[key]]
				entry[key].append(value)
			else:
				entry[key].append(value)
		# format years
		entry['PY'] = entry['PY'].replace('/','')
		entry['TI'] = entry['TI'].replace('.','')
		# Remove session chairs pub:
		flag = False
		for ts in TI_avoid_start_list:
			if entry['TI'].startswith(ts):
				flag = True
		if flag:
			continue
		publications.append(entry)
	
	return publications

# Format publication and output
#print(load_publication_ris_from_dblp(dblp_url))








