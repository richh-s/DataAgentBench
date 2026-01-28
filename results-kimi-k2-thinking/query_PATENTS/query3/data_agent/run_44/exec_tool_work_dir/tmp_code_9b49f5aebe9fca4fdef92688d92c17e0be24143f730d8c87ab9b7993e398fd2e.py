code = """import json
import re

# Load UNIV CALIFORNIA patents
uc_file = locals().get('var_functions.query_db:5')
with open(uc_file, 'r') as f:
    uc_data = json.load(f)

# Extract UNIV CALIFORNIA publication numbers
uc_pub_numbers = set()
for record in uc_data:
    info = record.get('Patents_info', '')
    # Look for publication number patterns
    matches = re.findall(r'[A-Z]{2}-\d{6,12}-[A-Z]\d?', info)
    uc_pub_numbers.update(matches)

# Load non-UNIV CALIFORNIA patents
nonuc_file = locals().get('var_functions.query_db:18')
with open(nonuc_file, 'r') as f:
    nonuc_data = json.load(f)

# Check which non-UC patents cite UC patents
citing_patents = []
for record in nonuc_data:
    citations = record.get('citation', '[]')
    try:
        citation_list = json.loads(citations.replace('""', '"null"')) if citations else []
    except:
        citation_list = []
    
    # Check if any citation matches UC publication numbers
    for citation in citation_list:
        pub_num = citation.get('publication_number')
        if pub_num and pub_num in uc_pub_numbers:
            citing_patents.append(record)
            break

print('__RESULT__:')
print(json.dumps({
    'uc_patents_count': len(uc_data),
    'uc_pub_numbers_count': len(uc_pub_numbers),
    'nonuc_patents_checked': len(nonuc_data),
    'citing_patents_found': len(citing_patents)
}))"""

env_args = {'var_functions.list_db:0': ['publicationinfo'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json', 'var_functions.execute_python:16': {'count': 169, 'first_keys': ['Patents_info', 'citation'], 'first_patent_info': 'In US, the application (number US-202117472182-A) is owned by UNIV CALIFORNIA and has pub. number US-2022074631-A1.', 'first_citation_len': 653}, 'var_functions.query_db:18': 'file_storage/functions.query_db:18.json', 'var_functions.execute_python:20': {'message': 'Loaded UNIV CALIFORNIA patents', 'count': 169}, 'var_functions.execute_python:22': {'uc_patents_count': 169}, 'var_functions.execute_python:24': {'uc_patents': 169, 'nonuc_patents': 1000, 'uc_pub_numbers_found': 322, 'sample_uc_numbers': ['US-202318169681-A', 'CN-96195210-A', 'AU-2005269556-A', 'AU-5711401-A', 'US-201313787160-A', 'US-201514981715-A', 'US-202218054917-A', 'US-2019021660-W', 'CA-3027364-A1', 'US-2023321419-A1']}}

exec(code, env_args)
