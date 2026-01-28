code = """import json
import pandas as pd
import re
import ast

# Read the publication data from file
with open(var_functions.query_db:9, 'r') as f:
    pub_data = json.load(f)

print(f"Total records: {len(pub_data)}")
print("Sample record:", pub_data[0])

# Parse CPC codes and publication dates
parsed_data = []

for record in pub_data:
    if not record.get('cpc') or not record.get('publication_date'):
        continue
    
    # Parse publication date - extract year from format like "Aug 3rd, 2021"
    date_str = record['publication_date']
    year_match = re.search(r'(\d{4})', date_str)
    if year_match:
        year = int(year_match.group(1))
    else:
        continue
    
    # Parse CPC codes (JSON-like format)
    cpc_str = record['cpc']
    try:
        cpc_list = json.loads(cpc_str)
    except:
        try:
            cpc_list = ast.literal_eval(cpc_str)
        except:
            continue
    
    if isinstance(cpc_list, list):
        for cpc_item in cpc_list:
            if isinstance(cpc_item, dict) and 'code' in cpc_item:
                code = cpc_item['code']
                parsed_data.append({
                    'cpc_code': code,
                    'year': year
                })

print(f"Parsed {len(parsed_data)} CPC-year records")
print("Sample parsed:", parsed_data[:10])

# Save to file for next steps
with open('/tmp/parsed_data.json', 'w') as f:
    json.dump(parsed_data, f)

print("__RESULT__:")
print(json.dumps({"status": "parsed", "count": len(parsed_data), "sample": parsed_data[:5]}))"""

env_args = {'var_functions.list_db:0': ['publicationinfo'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.list_db:5': ['cpc_definition'], 'var_functions.query_db:9': 'file_storage/functions.query_db:9.json'}

exec(code, env_args)
