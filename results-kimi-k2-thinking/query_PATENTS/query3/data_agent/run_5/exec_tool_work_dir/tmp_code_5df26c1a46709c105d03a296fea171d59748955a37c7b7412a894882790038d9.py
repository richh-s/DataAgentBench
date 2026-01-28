code = """import json
import re

# Load the UNIV CALIFORNIA patents data
file_path = var_functions.query_db:6

with open(file_path, 'r') as f:
    uc_patents = json.load(f)

# Extract publication numbers and CPC codes for UNIV CALIFORNIA patents
uc_data = []

for patent in uc_patents:
    patents_info = patent['Patents_info']
    cpc = patent['cpc']
    
    # Extract publication number using regex
    # Patterns: "pub. number XXXX", "publication number XXXX", "pub. number XXXX."
    pub_num_match = re.search(r'(?:pub\. number|publication number)\s+([A-Z0-9-]+)', patents_info)
    
    if pub_num_match:
        pub_num = pub_num_match.group(1)
        
        # Parse CPC codes (it's a JSON-like string)
        try:
            cpc_codes = json.loads(cpc)
            # Get unique CPC codes
            cpc_list = list(set([code['code'] for code in cpc_codes]))
        except:
            cpc_list = []
        
        uc_data.append({
            'publication_number': pub_num,
            'cpc_codes': cpc_list
        })

print('__RESULT__:')
print(json.dumps({
    'uc_patents_count': len(uc_data),
    'sample_uc_patents': uc_data[:3]
}))"""

env_args = {'var_functions.list_db:0': ['publicationinfo'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:5': [{'Patents_info': 'PANASONIC IP MAN CO LTD holds the US patent application (ID US-201916293577-A), with publication number US-11081687-B2.'}, {'Patents_info': 'GLASSNER RUDOLF holds the US patent filing (application no. US-201916355911-A), with publication number US-10794458-B2.'}, {'Patents_info': 'In US, the application (ID US-201916369247-A) is owned by COVESTRO LLC and has publication no. US-11124615-B2.'}, {'Patents_info': 'In US, the patent filing (app. number US-201916369879-A) is assigned to HOMOLOGY MEDICINES INC and has pub. number US-10610606-B2.'}, {'Patents_info': 'In US, the patent application (no. US-201916373467-A) is owned by APPLETON GRP LLC and has publication number US-10957507-B2.'}], 'var_functions.query_db:6': 'file_storage/functions.query_db:6.json', 'var_functions.query_db:8': 'file_storage/functions.query_db:8.json'}

exec(code, env_args)
