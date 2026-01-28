code = """import json
import pandas as pd

# Load the query result from storage
file_path = var_functions.query_db:6
with open(file_path, 'r') as f:
    data = json.load(f)

# Extract UNIV CALIFORNIA patents and their publication numbers
uc_patents = []
for record in data:
    patents_info = record.get('Patents_info', '')
    cpc = record.get('cpc', '[]')
    citation = record.get('citation', '[]')
    
    # Extract publication number from patents_info
    import re
    # Look for patterns like "pub. number XXXX" or "publication number XXXX"
    pub_num_match = re.search(r'(?:pub\. number|publication number)\s+([A-Z]{2}-[A-Z0-9-]+)', patents_info)
    if pub_num_match:
        pub_num = pub_num_match.group(1)
        uc_patents.append({
            'publication_number': pub_num,
            'cpc_codes': json.loads(cpc) if cpc else [],
            'citations': json.loads(citation) if citation else []
        })

print('__RESULT__:')
print(json.dumps({
    'total_uc_patents': len(uc_patents),
    'sample_uc_patents': uc_patents[:3]
}))"""

env_args = {'var_functions.list_db:0': ['publicationinfo'], 'var_functions.list_db:2': ['cpc_definition'], 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json', 'var_functions.query_db:6': 'file_storage/functions.query_db:6.json'}

exec(code, env_args)
