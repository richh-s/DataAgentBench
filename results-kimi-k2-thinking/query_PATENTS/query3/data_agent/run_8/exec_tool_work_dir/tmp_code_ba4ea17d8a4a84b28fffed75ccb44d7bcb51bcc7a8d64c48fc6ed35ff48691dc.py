code = """import json
import re

# Load UNIV CALIFORNIA patents with CPC data
with open(var_functions.query_db:56, 'r') as f:
    univ_data = json.load(f)

# Process UNIV CALIFORNIA patents - extract publication numbers and primary CPC codes
univ_patent_info = []
for patent in univ_data:
    patents_info = patent['Patents_info']
    
    # Extract publication number
    pub_num = None
    patterns = [
        r'pub\. number\s+([A-Z]{2}-[^\s,\.]+)',
        r'publication number\s+([A-Z]{2}-[^\s,\.]+)',
        r'publication no\.\s+([A-Z]{2}-[^\s,\.]+)'
    ]
    
    for pattern in patterns:
        match = re.search(pattern, patents_info, re.IGNORECASE)
        if match:
            pub_num = match.group(1).strip()
            break
    
    # Extract primary CPC codes (first: true)
    cpc_str = patent['cpc']
    primary_cpc_codes = []
    if cpc_str and cpc_str != '[]':
        try:
            cpc_data = json.loads(cpc_str)
            primary_cpc_codes = [item['code'] for item in cpc_data if item.get('first', False)]
        except:
            pass
    
    if pub_num:
        univ_patent_info.append({
            'publication_number': pub_num,
            'primary_cpc_codes': primary_cpc_codes,
            'patents_info': patents_info
        })

print('__RESULT__:') 
print(json.dumps({
    'total_univ_patents': len(univ_patent_info),
    'sample_data': univ_patent_info[:3]
}))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.execute_python:10': {'storage_keys': ['var_functions.query_db:0', 'var_functions.query_db:2'], 'current_dir': []}, 'var_functions.query_db:12': 'file_storage/functions.query_db:12.json', 'var_functions.query_db:14': 'file_storage/functions.query_db:14.json', 'var_functions.query_db:16': 'file_storage/functions.query_db:16.json', 'var_functions.query_db:20': 'file_storage/functions.query_db:20.json', 'var_functions.query_db:26': [{'Patents_info': 'In US, the application (number US-202117472182-A) is owned by UNIV CALIFORNIA and has pub. number US-2022074631-A1.'}, {'Patents_info': 'UNIV CALIFORNIA holds the TW patent filing (app. number TW-107142982-A), with pub. number TW-201925402-A.'}, {'Patents_info': 'In US, the patent application (no. US-201916454755-A) is assigned to UNIV CALIFORNIA and has publication number US-11421276-B2.'}, {'Patents_info': 'UNIV CALIFORNIA holds the AU patent application (no. AU-2019275518-A), with pub. number AU-2019275518-B2.'}, {'Patents_info': 'UNIV CALIFORNIA holds the US patent application (no. US-201515313510-A), with publication no. US-2017194630-A1.'}], 'var_functions.query_db:34': [{'symbol': 'A01K2227/108', 'titleFull': 'Swine'}, {'symbol': 'A01K2227/105', 'titleFull': 'Murine'}, {'symbol': 'A01K2227/101', 'titleFull': 'Bovine'}, {'symbol': 'A01K2227/107', 'titleFull': 'Rabbit'}, {'symbol': 'A01K2227/103', 'titleFull': 'Ovine'}], 'var_functions.query_db:38': 'file_storage/functions.query_db:38.json', 'var_functions.query_db:40': 'file_storage/functions.query_db:40.json', 'var_functions.query_db:46': [{'Patents_info': 'PANASONIC IP MAN CO LTD holds the US patent application (ID US-201916293577-A), with publication number US-11081687-B2.'}], 'var_functions.query_db:48': [{'total': '277813'}], 'var_functions.execute_python:50': 'Starting analysis...', 'var_functions.query_db:52': 'file_storage/functions.query_db:52.json', 'var_functions.query_db:56': 'file_storage/functions.query_db:56.json'}

exec(code, env_args)
