code = """import json
import re

# Get the file path from storage
file_path = locals()['var_functions.query_db:6']

# Load the query result
with open(file_path, 'r') as f:
    data = json.load(f)

uc_pub_nums = []
ac_uc_pub_nums = []

for record in data:
    patents_info = record.get('Patents_info', '')
    cpc = record.get('cpc', '[]')
    citation = record.get('citation', '[]')
    
    # Look for publication numbers
    # Pattern 1: "has pub. number XXXX"
    pub_num_match = re.search(r'(?:pub\. number|publication number|number)\s+([A-Z]{2}-[A-Z0-9-]+)', patents_info)
    
    # Pattern 2: "publication number XXXX" 
    pub_num_match2 = re.search(r'publication number\s+([A-Z]{2}-[A-Z0-9-]+)', patents_info)
    
    if pub_num_match:
        pub_num = pub_num_match.group(1)
    elif pub_num_match2:
        pub_num = pub_num_match2.group(1)
    else:
        continue
        
    # Store publication number
    uc_pub_nums.append(pub_num)
    
    # Extract citations
    citations = []
    try:
        citations = json.loads(citation)
    except:
        pass
        
    for cite in citations:
        if cite.get('publication_number'):
            ac_uc_pub_nums.append(cite['publication_number'])

print(f"Found {len(uc_pub_nums)} UC patents")
print(f"First few: {uc_pub_nums[:5]}")
print('__RESULT__:')
print(json.dumps({
    'uc_patents': uc_pub_nums,
    'citations': ac_uc_pub_nums[:10]
}))"""

env_args = {'var_functions.list_db:0': ['publicationinfo'], 'var_functions.list_db:2': ['cpc_definition'], 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json', 'var_functions.query_db:6': 'file_storage/functions.query_db:6.json', 'var_functions.execute_python:10': 'Loaded 100 records'}

exec(code, env_args)
