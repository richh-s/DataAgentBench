code = """import json
import re

# Load the full result from the previous query
uc_patents_path = locals()['var_functions.query_db:4']

# Read the full data from the file
with open(uc_patents_path, 'r') as f:
    uc_patents = json.load(f)

# Extract UC patent publication numbers and their CPC codes
uc_pub_numbers = []
uc_cpc_map = {}  # maps UC pub number to CPC codes

for patent in uc_patents:
    patents_info = patent['Patents_info']
    cpc_data = patent['cpc']
    
    # Extract publication number from Patents_info
    # Look for patterns like "pub. number US-2022074631-A1" or "publication number US-11421276-B2"
    pub_match = re.search(r'(?:pub\. number|publication number)\s+([A-Z]{2}-[A-Z0-9-]+)', patents_info)
    if pub_match:
        pub_num = pub_match.group(1)
        uc_pub_numbers.append(pub_num)
        
        # Parse CPC codes
        cpc_codes = []
        if cpc_data and cpc_data != '[]':
            try:
                cpc_list = json.loads(cpc_data)
                for cpc_item in cpc_list:
                    code = cpc_item.get('code', '')
                    if code:
                        # Extract subclass (first 4-5 characters like Y02B, F25B, etc.)
                        # For primary CPC subclass, we'll use the first 4 characters
                        subclass = re.match(r'([A-Z][0-9][A-Z][0-9]?)', code)
                        if subclass:
                            cpc_codes.append(subclass.group(1))
            except:
                pass
        
        uc_cpc_map[pub_num] = list(set(cpc_codes))  # deduplicate

result = {
    'uc_patent_count': len(uc_pub_numbers),
    'sample_pub_numbers': uc_pub_numbers[:10],
    'sample_cpc_map': dict(list(uc_cpc_map.items())[:2])
}

print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.query_db:4': 'file_storage/functions.query_db:4.json'}

exec(code, env_args)
