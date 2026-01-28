code = """import json
import re
import pandas as pd

# Load the publication data
storage_key = 'var_functions.query_db:8'
file_path = locals().get(storage_key, None)

result = {}
if file_path is None:
    result = {'error': 'File path not accessible'}
else:
    # Read the data
    with open(file_path, 'r') as f:
        publications = json.load(f)
    
    # Extract CPC codes and years
    extracted_data = []
    for pub in publications[:10000]:  # Process subset for now
        cpc_json = pub.get('cpc', '[]')
        pub_date = pub.get('publication_date', '')
        
        # Get year from date
        year = None
        if pub_date:
            match = re.search(r'(\d{4})', pub_date)
            if match:
                year = int(match.group(1))
        
        if not year:
            continue
        
        # Parse CPC codes
        try:
            if isinstance(cpc_json, str):
                cpc_list = json.loads(cpc_json)
            else:
                cpc_list = cpc_json
                
            for cpc_item in cpc_list:
                code = cpc_item.get('code', '')
                # Check if level 5: has subgroup and length is appropriate
                if code and '/' in code and len(code.split('/')[0]) >= 3:
                    extracted_data.append({'cpc_code': code, 'year': year})
        except:
            continue
    
    result = {
        'total_publications': len(publications),
        'extracted_pairs': len(extracted_data),
        'sample': extracted_data[:10] if extracted_data else []
    }

print("__RESULT__:")
print(json.dumps(result))"""

env_args = {'var_functions.list_db:0': ['publicationinfo'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.list_db:5': ['cpc_definition'], 'var_functions.query_db:6': [{'total': '277813'}], 'var_functions.query_db:8': 'file_storage/functions.query_db:8.json'}

exec(code, env_args)
