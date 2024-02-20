from util import *
from importlib import import_module
import urllib.request
import re

CCF_CPAPER_list = {
    'A' : ['SIGIR', 'WWW', 'AAAI', 'KDD'],
    'B' : ['CIKM','WSDM','EMNLP'],
    'C' : ['ECIR']
}

CCF_JOUR_list = {
    'A' : ['Trans. Inf. Syst.'],
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

def convert_to_datetime(time_string):
    try:
        return datetime.strptime(time_string, "%Y-%m-%d")
    except:
        try:
            return datetime.strptime(time_string, "%Y-%m")
        except:
            return datetime.strptime(time_string, "%Y")

# config info for input/output files and plugins
config = {}
try:
    config = load_data("../_config.yaml", type_check=False).get("auto-cite")
    if not config:
        raise Exception("Couldn't find auto-cite key in config")
except Exception as e:
    log(e, 3, "red")
    exit(1)

log("Compiling list of sources to cite")

# error exit flag
will_exit = False

# loop through plugins
# exit at end of loop if error occurred
if will_exit:
    log("One or more input files or plugins failed", 3, "red")
    exit(1)

log("Generating citations for sources")

# load existing citations
citations = []
try:
    citations = load_data(config["output"])
except Exception as e:
    log(e, 2, "yellow")

# error exit flag
will_exit = False

# list of new citations to overwrite existing citations
dblp_pubs = load_publication_ris_from_dblp(config["dblp-link"])

publications = {}
        
for pub in citations:
    title = pub["title"]
    if 'id' in pub:
        pub.pop("id")
    if '_cache' in pub:
        pub.pop("_cache")
    publications[title.lower()] = pub

cur_year = 0
cur_month = 12
cur_day = 31
for entry in dblp_pubs:
    title = entry['TI'].strip()
    id = title.lower()
    new = True if id not in publications else True if publications[id]['publisher'] == 'CoRR' else False
    if entry['TY'] not in set(['CPAPER', 'Informal or Other Publication', 'JOUR']):
        continue
    if new:
        publisher = entry['BT'] if entry['TY'] == 'CPAPER' else entry['JO']
        link = entry['UR'] if 'UR' in entry else None
        authors = []
        if isinstance(entry['AU'], list):
            for au in entry['AU']:
                aname = format_author_first_last_name(au)
                authors.append(aname)
        else:
            authors.append(format_author_first_last_name(entry['AU']))
        # format year
        arr = entry['PY'].split('/')
        cur_year = int(arr[0])
        cur_month = cur_month if len(arr[1])<1 else int(arr[1])
        cur_day = cur_day-1 if len(arr[2])<1 else int(arr[2])
        if cur_day<1:
            cur_month = cur_month-1
            cur_day = 31
        year = str(cur_year)
        #month = '01' if len(arr[1])<1 else arr[1]
        #day = '01' if len(arr[2])<1 else arr[2]
        month = str(cur_month)
        day = str(cur_day)
        date = '%s-%s-%s' % (year, month, day)
        if id not in publications:
            publications[id] = {
                'id': id,
                'title': title,
                'authors': authors,
                'publisher': publisher,
                'date': date
            }
        elif entry['TY'] in set(['CPAPER', 'JOUR']):
            publications[id]['authors'] = authors
            publications[id]['publisher'] = publisher
            publications[id]['date'] = date
        if link:
            publications[id]['link'] = link

new_citations = []
unique_id_set = set()
for entry in dblp_pubs:
    title = entry['TI'].strip()
    id = title.lower()
    if id in publications and id not in unique_id_set:        
        new_citations.append(publications[id])
        unique_id_set.add(id)


#new_citations = list(publications.values())
#new_citations.sort(key=lambda x:convert_to_datetime(x['date']),reverse=True)
# exit at end of loop if error occurred
if will_exit:
    log("One or more sources failed to be cited", 3, "red")
    exit(1)

log("Exporting citations")

# save new citations
try:
    save_data(config["output"], new_citations)
except Exception as e:
    log(e, 2, "red")
    exit(1)

log(f"Exported {len(new_citations)} citations", 2, "green")
