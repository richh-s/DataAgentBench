code = """import json
import pandas as pd
import re

# Load the publication data from the stored variable
result_key = 'var_functions.query_db:6'
result_file = locals()[result_key]

if isinstance(result_file, str) and result_file.endswith('.json'):
    with open(result_file, 'r') as f:
        publications = json.load(f)
else:
    publications = result_file

print(f"Total publications loaded: {len(publications)}")

# Parse CPC codes and extract years - let's be more careful
cpc_year_data = []
parse_errors = 0
missing_dates = 0
invalid_cpc = 0

for i, pub in enumerate(publications):
    cpc_str = pub.get('cpc', '')
    pub_date_str = pub.get('publication_date', '')
    
    if not cpc_str or not pub_date_str:
        if not cpc_str:
            invalid_cpc += 1
        if not pub_date_str:
            missing_dates += 1
        continue
    
    # Extract year from publication date (format: "Aug 3rd, 2021")
    year_match = re.search(r',\s*(\d{4})', pub_date_str)
    if year_match:
        year = int(year_match.group(1))
    else:
        missing_dates += 1
        continue
    
    # Parse CPC JSON string
    try:
        # First try to clean up the string
        cleaned_cpc = cpc_str.strip()
        if cleaned_cpc.startswith('['):
            cpc_list = json.loads(cleaned_cpc)
        else:
            # If it's not valid JSON, skip
            invalid_cpc += 1
            continue
    except Exception as e:
        parse_errors += 1
        continue
    
    if not isinstance(cpc_list, list):
        invalid_cpc += 1
        continue
    
    for cpc_item in cpc_list:
        if isinstance(cpc_item, dict) and 'code' in cpc_item:
            code = cpc_item['code']
            # Store the full code and also extract group (first part before /)
            if '/' in code:
                group = code.split('/')[0]
            else:
                group = code
            
            cpc_year_data.append({
                'full_code': code,
                'group_code': group,
                'year': year,
                'inventive': cpc_item.get('inventive', False),
                'first': cpc_item.get('first', False)
            })

print(f"CPC entries extracted: {len(cpc_year_data)}")
print(f"Parse errors: {parse_errors}")
print(f"Missing dates: {missing_dates}")
print(f"Invalid CPC entries: {invalid_cpc}")

if cpc_year_data:
    # Convert to DataFrame
    df = pd.DataFrame(cpc_year_data)
    print(f"DataFrame shape: {df.shape}")
    print(f"Columns: {list(df.columns)}")
    print(f"First few rows:")
    print(df.head())
    print(f"\nYear range: {df['year'].min()} to {df['year'].max()}")
    print(f"Unique groups: {len(df['group_code'].unique())}")
else:
    print("No CPC data could be extracted")
    df = pd.DataFrame()

# Store data in a way we can access later
result_summary = {
    'total_publications': len(publications),
    'cpc_entries': len(cpc_year_data),
    'dataframe_shape': df.shape if not df.empty else (0, 0),
    'columns': list(df.columns) if not df.empty else []
}

print('__RESULT__:')
print(json.dumps(result_summary))"""

env_args = {'var_functions.list_db:0': ['publicationinfo'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:5': [{'symbol': 'A01H', 'level': '5.0'}, {'symbol': 'A01F', 'level': '5.0'}, {'symbol': 'A01C', 'level': '5.0'}, {'symbol': 'A01G', 'level': '5.0'}, {'symbol': 'A23J', 'level': '5.0'}, {'symbol': 'A01N', 'level': '5.0'}, {'symbol': 'A01P', 'level': '5.0'}, {'symbol': 'A01D', 'level': '5.0'}, {'symbol': 'A01L', 'level': '5.0'}, {'symbol': 'A01K', 'level': '5.0'}], 'var_functions.query_db:6': 'file_storage/functions.query_db:6.json'}

exec(code, env_args)
