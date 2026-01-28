code = """import json
import re
from collections import defaultdict

# Load California patents data
cal_pats_file = 'file_storage/functions.query_db:70.json'
with open(cal_pats_file, 'r') as f:
    cal_pats = json.load(f)

# Extract California publication numbers
cal_pub_numbers = set()
for patent in cal_pats:
    patents_info = patent['Patents_info']
    
    # Extract publication number
    patterns = [
        r'pub\. number ([A-Z0-9-]+)',
        r'publication number ([A-Z0-9-]+)',
        r'publication no\. ([A-Z0-9-]+)'
    ]
    
    for pattern in patterns:
        match = re.search(pattern, patents_info)
        if match:
            cal_pub_numbers.add(match.group(1))
            break

print('__RESULT__:')
print(json.dumps(f'California publication numbers: {len(cal_pub_numbers)}'))"""

env_args = {'var_functions.list_db:0': ['publicationinfo'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:6': [{'name': 'publicationinfo'}], 'var_functions.query_db:8': 'file_storage/functions.query_db:8.json', 'var_functions.query_db:10': 'file_storage/functions.query_db:10.json', 'var_functions.query_db:12': [{'Patents_info': 'In US, the application (number US-202117472182-A) is owned by UNIV CALIFORNIA and has pub. number US-2022074631-A1.'}, {'Patents_info': 'UNIV CALIFORNIA holds the TW patent filing (app. number TW-107142982-A), with pub. number TW-201925402-A.'}, {'Patents_info': 'In US, the patent application (no. US-201916454755-A) is assigned to UNIV CALIFORNIA and has publication number US-11421276-B2.'}, {'Patents_info': 'UNIV CALIFORNIA holds the AU patent application (no. AU-2019275518-A), with pub. number AU-2019275518-B2.'}, {'Patents_info': 'UNIV CALIFORNIA holds the US patent application (no. US-201515313510-A), with publication no. US-2017194630-A1.'}, {'Patents_info': 'The JP patent filing (application no. JP-13313985-A) is assigned to UNIV CALIFORNIA and has pub. number JP-S6163700-A.'}, {'Patents_info': 'The US patent application (number US-201715625819-A) is assigned to UNIV CALIFORNIA and has pub. number US-2017281687-A1.'}, {'Patents_info': 'UNIV CALIFORNIA holds the EP patent application (ID EP-00992018-A), with publication no. EP-1224461-B1.'}, {'Patents_info': 'The AU application (number AU-2003247814-A) is belonging to UNIV CALIFORNIA and has publication number AU-2003247814-A1.'}, {'Patents_info': 'Patent filing (application no. AU-2017356943-A) from AU, held by UNIV CALIFORNIA, with publication number AU-2017356943-A1.'}], 'var_functions.query_db:18': 'file_storage/functions.query_db:18.json', 'var_functions.query_db:22': 'file_storage/functions.query_db:22.json', 'var_functions.query_db:24': 'file_storage/functions.query_db:24.json', 'var_functions.execute_python:26': 'Found the file path variable', 'var_functions.query_db:32': [{'symbol': 'A', 'titleFull': 'HUMAN NECESSITIES'}, {'symbol': 'A01', 'titleFull': 'AGRICULTURE; FORESTRY; ANIMAL HUSBANDRY; HUNTING; TRAPPING; FISHING'}, {'symbol': 'A01B', 'titleFull': 'SOIL WORKING IN AGRICULTURE OR FORESTRY; PARTS, DETAILS, OR ACCESSORIES OF AGRICULTURAL MACHINES OR IMPLEMENTS, IN GENERAL'}, {'symbol': 'A01B1/00', 'titleFull': 'Hand tools'}, {'symbol': 'A01B1/02', 'titleFull': 'Spades; Shovels'}], 'var_functions.query_db:34': 'file_storage/functions.query_db:34.json', 'var_functions.execute_python:40': 'File path retrieved: file_storage/functions.query_db:34.json', 'var_functions.execute_python:42': 'Loaded 169 California patents', 'var_functions.execute_python:44': 'Total California patents loaded: 169', 'var_functions.execute_python:46': "Found 59 California publication numbers: ['US-2022074631-A1', 'TW-201925402-A', 'AU-2019275518-B2', 'JP-S6163700-A', 'US-2017281687-A1', 'US-9061071-B2', 'EP-0826155-A4', 'RO-70061-A', 'WO-2021102420-A1', 'WO-2012162563-A2']...", 'var_functions.query_db:48': 'file_storage/functions.query_db:48.json', 'var_functions.query_db:50': 'file_storage/functions.query_db:50.json', 'var_functions.query_db:52': 'file_storage/functions.query_db:52.json', 'var_functions.query_db:54': 'file_storage/functions.query_db:54.json', 'var_functions.execute_python:56': 'Total patents to analyze: 5000', 'var_functions.execute_python:58': 'Loaded 169 California patents and 5000 total patents', 'var_functions.execute_python:60': 'Found 59 California publication numbers', 'var_functions.execute_python:62': 'Found 0 citing patents from 5000 records', 'var_functions.execute_python:64': 'Found 169 California publication numbers', 'var_functions.execute_python:68': {'cal_pub_numbers_count': 59, 'cpc_mapping_count': 0, 'sample_cpc': []}, 'var_functions.query_db:70': 'file_storage/functions.query_db:70.json', 'var_functions.execute_python:71': {'total_cal_pubs': 169, 'total_with_cpc': 169, 'sample_entries': [['US-2022074631-A1', ['F25B21/00', 'F28D15/00', 'F25B21/00']], ['TW-201925402-A', ['C09J11/04', 'C09J9/02', 'C09D11/52']], ['US-11421276-B2', ['C12Q1/6883', 'C12Q1/6883', 'C12Q1/6883']], ['AU-2019275518-B2', ['A61K31/357', 'A61K31/34', 'A61K31/08']], ['US-2017194630-A1', ['H01M10/0525', 'H01M4/386', 'H01M4/0469']]]}, 'var_functions.query_db:74': 'file_storage/functions.query_db:74.json', 'var_functions.execute_python:76': {'total_cal_pubs': 169, 'total_with_cpc': 169, 'sample': {'US-2022074631-A1': ['F25B21', 'F28D15'], 'TW-201925402-A': ['C09J11', 'C09J9', 'C09D11', 'C08K3'], 'US-11421276-B2': ['C12Q1'], 'AU-2019275518-B2': ['A61K31', 'A61D7', 'A61P43', 'A61P25', 'A61P23'], 'US-2017194630-A1': ['H01M10', 'H01M4']}}}

exec(code, env_args)
