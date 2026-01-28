code = """import json
import re

# Load UNIV CALIFORNIA patents and extract publication numbers
with open(locals()['var_functions.query_db:30'], 'r') as f:
    uc_data = json.load(f)

print('Loaded UC patents:', len(uc_data))

# Extract UC publication numbers
uc_pub_numbers = set()
pub_pattern = re.compile(r'pub\. number\s+([A-Z]{2}-[A-Z0-9-]+)')

for item in uc_data[:100]:  # Process first 100 for testing
    info = item['Patents_info']
    match = pub_pattern.search(info)
    if match:
        uc_pub_numbers.add(match.group(1))

print('UC pub numbers found:', len(uc_pub_numbers))

# Now check citation data from other file
with open(locals()['var_functions.query_db:42'], 'r') as f:
    citation_data = json.load(f)

print('Citation records loaded:', len(citation_data))

# Find which patents cite UC patents
matches = []
for item in citation_data:
    if 'citation' in item and item['citation'] != []:
        citations = item['citation']
        if isinstance(citations, str):
            citations = json.loads(citations)
        
        for cite in citations:
            pub_num = cite.get('publication_number')
            if pub_num in uc_pub_numbers:
                matches.append({
                    'citing_patent': item['Patents_info']
                })
                break

print('Found matches:', len(matches))
print('Sample match:', matches[0] if matches else 'None')"""

env_args = {'var_functions.list_db:0': ['publicationinfo'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:22': [{'total_rows': '277813'}], 'var_functions.query_db:24': 'file_storage/functions.query_db:24.json', 'var_functions.query_db:30': 'file_storage/functions.query_db:30.json', 'var_functions.execute_python:32': {'count': 59, 'publication_numbers': ['US-2022074631-A1', 'TW-201925402-A', 'AU-2019275518-B2', 'JP-S6163700-A', 'US-2017281687-A1', 'US-9061071-B2', 'EP-0826155-A4', 'RO-70061-A', 'WO-2021102420-A1', 'WO-2012162563-A2', 'US-11376346-B2', 'CN-100339724-C', 'US-2017145219-A1', 'KR-20200041324-A', 'CN-103189548-A', 'CA-2298540-A1', 'US-2021000566-A1', 'US-2006051790-A1', 'US-2023171142-A1', 'WO-2018026404-A3', 'US-2006292670-A1', 'US-2021101879-A1', 'US-2023321419-A1', 'AU-2003297741-A1', 'WO-2017214343-A1', 'US-11667770-B2', 'CA-2562038-C', 'US-6750960-B2', 'US-2020025859-A1', 'EP-1212462-A1', 'US-5547866-A', 'US-2023279470-A1', 'AU-2008349842-A1', 'EP-4284234-A1', 'WO-2020055916-A9', 'US-6767662-B2', 'AU-2015364602-B2', 'IL-274176-A', 'JP-2014224156-A', 'IL-244029-A0', 'AU-2010214112-B2', 'MX-2013002850-A', 'US-2019328740-A1', 'US-2022018060-A1', 'WO-2023225482-A3', 'WO-2024044766-A3', 'AU-2007297661-A1', 'WO-2024112568-A1', 'CA-2550552-A1', 'CN-102584712-A', 'CN-102067370-B', 'US-11546022-B2', 'US-2023155090-A1', 'WO-2010045542-A3', 'HK-1250569-A1', 'ID-23426-A', 'US-5304932-A', 'US-2018243924-A1', 'AU-6535890-A']}, 'var_functions.query_db:34': 'file_storage/functions.query_db:34.json', 'var_functions.query_db:38': 'file_storage/functions.query_db:38.json', 'var_functions.query_db:42': 'file_storage/functions.query_db:42.json'}

exec(code, env_args)
