code = """import json

# Get the file path from storage
result_file_path = locals()['var_functions.query_db:5']
print('File path type:', type(result_file_path))
print('File path:', str(result_file_path))

# Load and process the data
with open(result_file_path, 'r') as f:
    data = json.load(f)

print('Total records loaded:', len(data))

# Initialize counters
valid_records = 0
patent_records = []

# Process records to extract CPC codes and years
for record in data:
    try:
        # Parse publication date
        pub_date_str = record['publication_date']
        # Clean date string
        date_clean = pub_date_str.replace('st,', ',').replace('nd,', ',')
        date_clean = date_clean.replace('rd,', ',').replace('th,', ',')
        from datetime import datetime
        pub_date = datetime.strptime(date_clean, '%b %d, %Y')
        year = pub_date.year
        
        # Parse CPC codes
        cpc_list = json.loads(record['cpc'])
        for cpc_item in cpc_list:
            code = cpc_item.get('code', '')
            if code and '/' in code:
                # Check if it's a group code (Level 5)
                parts = code.split('/')
                if len(parts) == 2 and len(parts[1]) >= 3:
                    patent_records.append({'cpc_code': code, 'year': year})
        
        valid_records += 1
    except:
        continue

print(f'Processed {valid_records} valid records')
print(f'Extracted {len(patent_records)} CPC-year pairs')

# Print result
print('\n__RESULT__:')
print(json.dumps({'records': len(patent_records), 'valid_records': valid_records}))"""

env_args = {'var_functions.list_db:0': ['publicationinfo'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json'}

exec(code, env_args)
