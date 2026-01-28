code = """import json
import re
from datetime import datetime

# Read the publication data from the file
with open('/tmp/tmp0j5w3l0y.json', 'r') as f:
    publication_data = json.load(f)

# Function to extract year from natural language date
def extract_year(date_str):
    if not date_str:
        return None
    # Look for 4-digit year pattern
    match = re.search(r'\d{4}', date_str)
    if match:
        return int(match.group())
    return None

# Function to parse CPC JSON and extract codes
def extract_cpc_codes(cpc_json_str):
    if not cpc_json_str:
        return []
    try:
        # Clean up the string and parse as JSON
        cpc_data = json.loads(cpc_json_str)
        codes = []
        for item in cpc_data:
            if 'code' in item:
                codes.append(item['code'])
        return codes
    except:
        return []

# Process all records
cpc_year_counts = {}
valid_records = 0

for record in publication_data:
    cpc_str = record.get('cpc', '')
    pub_date = record.get('publication_date', '')
    
    year = extract_year(pub_date)
    cpc_codes = extract_cpc_codes(cpc_str)
    
    if year and cpc_codes:
        valid_records += 1
        for code in cpc_codes:
            # Get the base CPC group (first part before /)
            base_code = code.split('/')[0]
            key = (base_code, year)
            cpc_year_counts[key] = cpc_year_counts.get(key, 0) + 1

print(f"Processed {valid_records} valid records")
print(f"Total unique (CPC, year) combinations: {len(cpc_year_counts)}")

# Show sample data
sample_items = list(cpc_year_counts.items())[:10]
print("Sample counts:")
for (code, year), count in sample_items:
    print(f"  {code} - {year}: {count}")

# Save the processed data
result = {
    'cpc_year_counts': cpc_year_counts,
    'total_records': valid_records,
    'total_combinations': len(cpc_year_counts)
}

print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.list_db:0': ['publicationinfo'], 'var_functions.list_db:2': ['cpc_definition'], 'var_functions.query_db:4': 'file_storage/functions.query_db:4.json', 'var_functions.query_db:6': 'file_storage/functions.query_db:6.json'}

exec(code, env_args)
