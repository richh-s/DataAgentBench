code = """import json
import pandas as pd
from datetime import datetime
import re

# Read the full publication data from file
file_path = locals()['var_functions.query_db:12']
with open(file_path, 'r') as f:
    pub_data = json.load(f)

print(f'Total records: {len(pub_data)}')
print('Sample record:')
print(json.dumps(pub_data[0], indent=2)[:500])

# Parse CPC codes and dates
records = []
for item in pub_data:
    try:
        # Parse publication date
        pub_date_str = item.get('publication_date', '')
        if pub_date_str:
            # Extract year from date strings like "Aug 3rd, 2021"
            year_match = re.search(r'(\d{4})', pub_date_str)
            if year_match:
                year = int(year_match.group(1))
                
                # Parse CPC codes (JSON string)
                cpc_str = item.get('cpc', '[]')
                if cpc_str and cpc_str != '[]':
                    try:
                        cpc_list = json.loads(cpc_str)
                        for cpc_entry in cpc_list:
                            cpc_code = cpc_entry.get('code', '')
                            if cpc_code:
                                records.append({
                                    'cpc_code': cpc_code,
                                    'year': year
                                })
                    except:
                        # If direct parsing fails, try to clean the string
                        pass
    except Exception as e:
        continue

print(f'Parsed {len(records)} CPC-year records')
print('Sample parsed records:')
for i in range(min(5, len(records))):
    print(records[i])

# Filter to get unique CPC codes
unique_cpcs = list(set(r['cpc_code'] for r in records))
print(f'Unique CPC codes: {len(unique_cpcs)}')
print('Sample CPC codes:', unique_cpcs[:10])

# Save to JSON file for further processing
with open('/tmp/cpc_yearly_data.json', 'w') as f:
    json.dump(records, f)

result = {
    'total_records': len(pub_data),
    'cpc_year_records': len(records),
    'unique_cpcs': len(unique_cpcs),
    'sample_cpcs': unique_cpcs[:10]
}

print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.list_db:0': ['publicationinfo'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.list_db:11': ['cpc_definition'], 'var_functions.query_db:10': [{'symbol': 'A01H', 'level': '5.0'}, {'symbol': 'A01F', 'level': '5.0'}, {'symbol': 'A01C', 'level': '5.0'}, {'symbol': 'A01G', 'level': '5.0'}, {'symbol': 'A23J', 'level': '5.0'}, {'symbol': 'A01N', 'level': '5.0'}, {'symbol': 'A01P', 'level': '5.0'}, {'symbol': 'A01D', 'level': '5.0'}, {'symbol': 'A01L', 'level': '5.0'}, {'symbol': 'A01K', 'level': '5.0'}], 'var_functions.query_db:12': 'file_storage/functions.query_db:12.json'}

exec(code, env_args)
