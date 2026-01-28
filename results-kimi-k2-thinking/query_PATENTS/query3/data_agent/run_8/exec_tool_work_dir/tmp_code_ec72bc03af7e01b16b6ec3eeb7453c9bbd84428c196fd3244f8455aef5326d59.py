code = """import json
import re

# Load UNIV CALIFORNIA patents
univ_california_file = var_functions.query_db:20
with open(univ_california_file, 'r') as f:
    univ_california_patents = json.load(f)

# Extract publication numbers of UNIV CALIFORNIA patents
univ_pub_numbers = []
for patent in univ_california_patents:
    patents_info = patent['Patents_info']
    # Find all publication numbers in US-XXX or TW-XXX format
    matches = re.findall(r'(US|TW|AU|WO|EP|CA|CN|KR|JP|DE|FR|GB)-[^\s,-]+', patents_info)
    for match in matches:
        if match.startswith(('US', 'TW', 'AU', 'WO', 'EP', 'CA', 'CN', 'KR', 'JP', 'DE', 'FR', 'GB')):
            # Extract full publication number
            if 'pub. number' in patents_info or 'publication number' in patents_info:
                # Get the portion after "pub. number" or "publication number"
                pub_part = patents_info.split('pub. number')[1] if 'pub. number' in patents_info else patents_info.split('publication number')[1]
                if match in pub_part:
                    end_idx = pub_part.find(match) + len(match)
                    # Look for the actual end (space, comma, period, or end of string)
                    temp_pub = pub_part[pub_part.find(match):]
                    actual_end = len(temp_pub)
                    for i, char in enumerate(temp_pub):
                        if char in '.,\s' and i > 0:
                            actual_end = i
                            break
                    pub_num = temp_pub[:actual_end].strip()
                    if pub_num and pub_num not in univ_pub_numbers:
                        univ_pub_numbers.append(pub_num)
            else:
                # Basic extraction if format is simple
                pub_num = match
                if pub_num and pub_num not in univ_pub_numbers:
                    univ_pub_numbers.append(pub_num)

# Extract CPC codes from UNIV CALIFORNIA patents
univ_cpc_codes = {}
for patent in univ_california_patents:
    patents_info = patent['Patents_info']
    pub_num = None
    
    # Extract publication number for this patent
    for candidate in univ_pub_numbers:
        if candidate in patents_info:
            pub_num = candidate
            break
    
    if not pub_num and 'pub. number' in patents_info:
        pub_part = patents_info.split('pub. number')[1]
        match = re.search(r'(US|TW|AU|WO|EP|CA|CN|KR|JP|DE|FR|GB)-[^\s,.]+', pub_part)
        if match:
            pub_num = match.group(0)
    
    # Extract CPC codes
    cpc_str = patent['cpc']
    if cpc_str and cpc_str != '[]':
        try:
            cpc_data = json.loads(cpc_str)
            cpc_codes = [item['code'] for item in cpc_data if 'code' in item]
            if cpc_codes:
                univ_cpc_codes[pub_num] = cpc_codes
                if not pub_num:
                    pub_num = f'unknown_{len(univ_cpc_codes)}'
        except:
            pass

print('__RESULT__:')
print(json.dumps({
    'univ_california_patent_count': len(univ_california_patents),
    'extracted_pub_numbers_count': len(univ_pub_numbers),
    'sample_pub_numbers': univ_pub_numbers[:10],
    'cpc_codes_count': len(univ_cpc_codes),
    'sample_cpc_codes': {k: v[:3] for k, v in list(univ_cpc_codes.items())[:3]}
}, indent=2))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.execute_python:10': {'storage_keys': ['var_functions.query_db:0', 'var_functions.query_db:2'], 'current_dir': []}, 'var_functions.query_db:12': 'file_storage/functions.query_db:12.json', 'var_functions.query_db:14': 'file_storage/functions.query_db:14.json', 'var_functions.query_db:16': 'file_storage/functions.query_db:16.json', 'var_functions.query_db:20': 'file_storage/functions.query_db:20.json', 'var_functions.query_db:26': [{'Patents_info': 'In US, the application (number US-202117472182-A) is owned by UNIV CALIFORNIA and has pub. number US-2022074631-A1.'}, {'Patents_info': 'UNIV CALIFORNIA holds the TW patent filing (app. number TW-107142982-A), with pub. number TW-201925402-A.'}, {'Patents_info': 'In US, the patent application (no. US-201916454755-A) is assigned to UNIV CALIFORNIA and has publication number US-11421276-B2.'}, {'Patents_info': 'UNIV CALIFORNIA holds the AU patent application (no. AU-2019275518-A), with pub. number AU-2019275518-B2.'}, {'Patents_info': 'UNIV CALIFORNIA holds the US patent application (no. US-201515313510-A), with publication no. US-2017194630-A1.'}]}

exec(code, env_args)
