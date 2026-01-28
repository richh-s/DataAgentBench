code = """import json
import re

# Load all data needed
cal_pats_file = 'file_storage/functions.query_db:54.json'
all_patents_file = 'file_storage/functions.query_db:52.json'

with open(cal_pats_file, 'r') as f:
    cal_pats = json.load(f)

with open(all_patents_file, 'r') as f:
    all_patents = json.load(f)

# Extract California publication numbers from California patents data
cal_pub_numbers = set()
for patent in cal_pats:
    patents_info = patent['Patents_info']
    match = re.search(r'pub\. number ([A-Z0-9-]+)', patents_info)
    if match:
        cal_pub_numbers.add(match.group(1))

print('__RESULT__:')
print(json.dumps(f'California publication numbers: {len(cal_pub_numbers)}'))

# Also get mapping from publication number to CPC codes
cal_pub_to_cpc = {}
for patent in cal_pats:
    patents_info = patent['Patents_info']
    match = re.search(r'pub\. number ([A-Z0-9-]+)', patents_info)
    if match:
        pub_num = match.group(1)
        if 'cpc' in patent and patent['cpc']:
            try:
                cpc_data = json.loads(patent['cpc'])
                cal_pub_to_cpc[pub_num] = cpc_data
            except:
                cal_pub_to_cpc[pub_num] = []

print(json.dumps(f'California pub to CPC mapping: {len(cal_pub_to_cpc)}'))"""

env_args = {'var_functions.list_db:0': ['publicationinfo'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:6': [{'name': 'publicationinfo'}], 'var_functions.query_db:8': 'file_storage/functions.query_db:8.json', 'var_functions.query_db:10': 'file_storage/functions.query_db:10.json', 'var_functions.query_db:12': [{'Patents_info': 'In US, the application (number US-202117472182-A) is owned by UNIV CALIFORNIA and has pub. number US-2022074631-A1.'}, {'Patents_info': 'UNIV CALIFORNIA holds the TW patent filing (app. number TW-107142982-A), with pub. number TW-201925402-A.'}, {'Patents_info': 'In US, the patent application (no. US-201916454755-A) is assigned to UNIV CALIFORNIA and has publication number US-11421276-B2.'}, {'Patents_info': 'UNIV CALIFORNIA holds the AU patent application (no. AU-2019275518-A), with pub. number AU-2019275518-B2.'}, {'Patents_info': 'UNIV CALIFORNIA holds the US patent application (no. US-201515313510-A), with publication no. US-2017194630-A1.'}, {'Patents_info': 'The JP patent filing (application no. JP-13313985-A) is assigned to UNIV CALIFORNIA and has pub. number JP-S6163700-A.'}, {'Patents_info': 'The US patent application (number US-201715625819-A) is assigned to UNIV CALIFORNIA and has pub. number US-2017281687-A1.'}, {'Patents_info': 'UNIV CALIFORNIA holds the EP patent application (ID EP-00992018-A), with publication no. EP-1224461-B1.'}, {'Patents_info': 'The AU application (number AU-2003247814-A) is belonging to UNIV CALIFORNIA and has publication number AU-2003247814-A1.'}, {'Patents_info': 'Patent filing (application no. AU-2017356943-A) from AU, held by UNIV CALIFORNIA, with publication number AU-2017356943-A1.'}], 'var_functions.query_db:18': 'file_storage/functions.query_db:18.json', 'var_functions.query_db:22': 'file_storage/functions.query_db:22.json', 'var_functions.query_db:24': 'file_storage/functions.query_db:24.json', 'var_functions.execute_python:26': 'Found the file path variable', 'var_functions.query_db:32': [{'symbol': 'A', 'titleFull': 'HUMAN NECESSITIES'}, {'symbol': 'A01', 'titleFull': 'AGRICULTURE; FORESTRY; ANIMAL HUSBANDRY; HUNTING; TRAPPING; FISHING'}, {'symbol': 'A01B', 'titleFull': 'SOIL WORKING IN AGRICULTURE OR FORESTRY; PARTS, DETAILS, OR ACCESSORIES OF AGRICULTURAL MACHINES OR IMPLEMENTS, IN GENERAL'}, {'symbol': 'A01B1/00', 'titleFull': 'Hand tools'}, {'symbol': 'A01B1/02', 'titleFull': 'Spades; Shovels'}], 'var_functions.query_db:34': 'file_storage/functions.query_db:34.json', 'var_functions.execute_python:40': 'File path retrieved: file_storage/functions.query_db:34.json', 'var_functions.execute_python:42': 'Loaded 169 California patents', 'var_functions.execute_python:44': 'Total California patents loaded: 169', 'var_functions.execute_python:46': "Found 59 California publication numbers: ['US-2022074631-A1', 'TW-201925402-A', 'AU-2019275518-B2', 'JP-S6163700-A', 'US-2017281687-A1', 'US-9061071-B2', 'EP-0826155-A4', 'RO-70061-A', 'WO-2021102420-A1', 'WO-2012162563-A2']...", 'var_functions.query_db:48': 'file_storage/functions.query_db:48.json', 'var_functions.query_db:50': 'file_storage/functions.query_db:50.json', 'var_functions.query_db:52': 'file_storage/functions.query_db:52.json', 'var_functions.query_db:54': 'file_storage/functions.query_db:54.json', 'var_functions.execute_python:56': 'Total patents to analyze: 5000', 'var_functions.execute_python:58': 'Loaded 169 California patents and 5000 total patents', 'var_functions.execute_python:60': 'Found 59 California publication numbers', 'var_functions.execute_python:62': 'Found 0 citing patents from 5000 records', 'var_functions.execute_python:64': 'Found 169 California publication numbers'}

exec(code, env_args)
