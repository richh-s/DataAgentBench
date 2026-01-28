code = """import json
import pandas as pd
import re
from collections import defaultdict

# Load UNIV CALIFORNIA patents data
result_file = str(locals()['var_functions.query_db:18'])
with open(result_file, 'r') as f:
    uni_california_patents = json.load(f)

print("Loaded", len(uni_california_patents), "UNIV CALIFORNIA patent records")

# Extract publication numbers, assignees, and CPC codes
uni_cal_pub_numbers = []
uni_cal_cpc_codes = defaultdict(set)

for patent in uni_california_patents:
    # Extract publication number
    patents_info = patent['Patents_info']
    
    # Extract publication number using regex
    pub_match = re.search(r'pub\. number\s+([A-Z]{2}-[A-Z0-9-]+)', patents_info)
    if not pub_match:
        pub_match = re.search(r'publication\s+no\.\s+([A-Z]{2}-[A-Z0-9-]+)', patents_info)
    if not pub_match:
        pub_match = re.search(r'publication\s+number\s+([A-Z]{2}-[A-Z0-9-]+)', patents_info)
    
    if pub_match:
        pub_num = pub_match.group(1)
        uni_cal_pub_numbers.append(pub_num)
        
        # Extract CPC codes
        if patent['cpc']:
            try:
                cpc_list = json.loads(patent['cpc'])
                for cpc_entry in cpc_list:
                    if cpc_entry.get('code'):
                        # Get subclass level (first 4 characters)
                        subclass = cpc_entry['code'][:4]
                        uni_cal_cpc_codes[pub_num].add(subclass)
            except:
                pass

print("Found", len(uni_cal_pub_numbers), "UNIV CALIFORNIA publication numbers")
print("Sample publication numbers:", uni_cal_pub_numbers[:5])
print("Sample CPC codes:", list(uni_cal_cpc_codes.items())[:2])

# Create a dictionary for easier lookup
uni_cal_lookup = {pub: list(cpcs) for pub, cpcs in uni_cal_cpc_codes.items() if cpcs}

print("__RESULT__:")
print(json.dumps({
    'total_uni_cal_patents': len(uni_cal_pub_numbers),
    'sample_pubs': uni_cal_pub_numbers[:10],
    'sample_cpc': {k: list(v) for k, v in list(uni_cal_cpc_codes.items())[:2]}
}))"""

env_args = {'var_functions.list_db:0': ['publicationinfo'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.execute_python:12': {'total': 5, 'uni_california': 0}, 'var_functions.query_db:16': [{'Patents_info': 'In US, the application (number US-202117472182-A) is owned by UNIV CALIFORNIA and has pub. number US-2022074631-A1.'}, {'Patents_info': 'UNIV CALIFORNIA holds the TW patent filing (app. number TW-107142982-A), with pub. number TW-201925402-A.'}, {'Patents_info': 'In US, the patent application (no. US-201916454755-A) is assigned to UNIV CALIFORNIA and has publication number US-11421276-B2.'}, {'Patents_info': 'UNIV CALIFORNIA holds the AU patent application (no. AU-2019275518-A), with pub. number AU-2019275518-B2.'}, {'Patents_info': 'UNIV CALIFORNIA holds the US patent application (no. US-201515313510-A), with publication no. US-2017194630-A1.'}, {'Patents_info': 'The JP patent filing (application no. JP-13313985-A) is assigned to UNIV CALIFORNIA and has pub. number JP-S6163700-A.'}, {'Patents_info': 'The US patent application (number US-201715625819-A) is assigned to UNIV CALIFORNIA and has pub. number US-2017281687-A1.'}, {'Patents_info': 'UNIV CALIFORNIA holds the EP patent application (ID EP-00992018-A), with publication no. EP-1224461-B1.'}, {'Patents_info': 'The AU application (number AU-2003247814-A) is belonging to UNIV CALIFORNIA and has publication number AU-2003247814-A1.'}, {'Patents_info': 'Patent filing (application no. AU-2017356943-A) from AU, held by UNIV CALIFORNIA, with publication number AU-2017356943-A1.'}], 'var_functions.query_db:18': 'file_storage/functions.query_db:18.json'}

exec(code, env_args)
