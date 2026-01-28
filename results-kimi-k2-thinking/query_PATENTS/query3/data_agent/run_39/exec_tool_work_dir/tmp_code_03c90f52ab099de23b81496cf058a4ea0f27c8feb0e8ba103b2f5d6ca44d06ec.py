code = """import json
import re

# Read UNIV CALIFORNIA patents data
uc_file = locals()['var_functions.query_db:30']
with open(uc_file, 'r') as f:
    uc_patents = json.load(f)

print(f"Total UNIV CALIFORNIA patents: {len(uc_patents)}")

# Extract publication numbers from Patents_info
uc_pub_numbers = set()
uc_pub_to_cpc = {}

for patent in uc_patents:
    patents_info = patent['Patents_info']
    cpc_data = patent.get('cpc', '[]')
    
    # Extract publication number (e.g., US-2022074631-A1, US-11421276-B2, etc.)
    # Pattern looks for: "pub. number US-2022074631-A1" or similar
    match = re.search(r'(?:pub\.|publication|pub\s+no|publication\s+no|pub\s+number|has\s+publication\s+no|has\s+pub\.|with\s+pub\.)\s+(?:[A-Z]+-)?([A-Z]{2}-\d+-[A-Z]\d*)', patents_info, re.IGNORECASE)
    
    if match:
        pub_num = match.group(1)
        uc_pub_numbers.add(pub_num)
        uc_pub_to_cpc[pub_num] = cpc_data
    else:
        # Try alternative pattern for cases like "pub. number US-11081687-B2"
        alt_match = re.search(r'publication\s+number\s+([A-Z]{2}-\d+-[A-Z]\d*)', patents_info, re.IGNORECASE)
        if alt_match:
            pub_num = alt_match.group(1)
            uc_pub_numbers.add(pub_num)
            uc_pub_to_cpc[pub_num] = cpc_data

print(f"Extracted {len(uc_pub_numbers)} unique UNIV CALIFORNIA publication numbers")
print("Sample publication numbers:", list(uc_pub_numbers)[:10])

# Store results
result = {
    'uc_pub_numbers': list(uc_pub_numbers),
    'uc_pub_to_cpc': uc_pub_to_cpc,
    'count': len(uc_pub_numbers)
}

print('__RESULT__:')
print(json.dumps(result, indent=2))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:4': 'file_storage/functions.query_db:4.json', 'var_functions.query_db:6': 'file_storage/functions.query_db:6.json', 'var_functions.query_db:8': 'file_storage/functions.query_db:8.json', 'var_functions.execute_python:12': [], 'var_functions.query_db:14': 'file_storage/functions.query_db:14.json', 'var_functions.query_db:16': 'file_storage/functions.query_db:16.json', 'var_functions.execute_python:20': {'uc_pub_to_cpc': {}, 'uc_pub_numbers': []}, 'var_functions.query_db:22': 'file_storage/functions.query_db:22.json', 'var_functions.query_db:24': [{'Patents_info': 'In US, the application (number US-202117472182-A) is owned by UNIV CALIFORNIA and has pub. number US-2022074631-A1.'}, {'Patents_info': 'UNIV CALIFORNIA holds the TW patent filing (app. number TW-107142982-A), with pub. number TW-201925402-A.'}, {'Patents_info': 'In US, the patent application (no. US-201916454755-A) is assigned to UNIV CALIFORNIA and has publication number US-11421276-B2.'}, {'Patents_info': 'UNIV CALIFORNIA holds the AU patent application (no. AU-2019275518-A), with pub. number AU-2019275518-B2.'}, {'Patents_info': 'UNIV CALIFORNIA holds the US patent application (no. US-201515313510-A), with publication no. US-2017194630-A1.'}], 'var_functions.query_db:26': 'file_storage/functions.query_db:26.json', 'var_functions.query_db:28': 'file_storage/functions.query_db:28.json', 'var_functions.query_db:30': 'file_storage/functions.query_db:30.json'}

exec(code, env_args)
