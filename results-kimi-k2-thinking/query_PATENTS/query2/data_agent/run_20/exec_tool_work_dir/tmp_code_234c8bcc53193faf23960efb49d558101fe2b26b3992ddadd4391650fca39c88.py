code = """import json
import re

# Load the preview data from file path stored in var_functions.query_db:2
file_path = var_functions.query_db:2
with open(file_path, 'r') as f:
    data_preview = json.load(f)

# Preview first few records
print(f'Total records preview: {len(data_preview)}')
print('First record:')
print(json.dumps(data_preview[0], indent=2))

# Function to parse grant date
def parse_grant_date(date_str):
    if not date_str or 'grant' in date_str.lower():
        return None
    # Clean up date string - remove ordinal suffixes
    date_str_clean = re.sub(r'(\d{1,2})(st|nd|rd|th)', r'\1', date_str.lower().replace('dated ', ''))
    date_str_clean = date_str_clean.strip()
    
    # Try to extract month and year
    patterns = [
        r'(\w+)\s+(\d{4})',
        r'(\d{1,2})\s+(\w+)\s+(\d{4})',
    ]
    
    for pattern in patterns:
        match = re.search(pattern, date_str_clean)
        if match:
            if len(match.groups()) == 2:
                month, year = match.groups()
                return year, month
            elif len(match.groups()) == 3:
                _, month, year = match.groups()
                return year, month
    return None, None

# Test date parsing with sample data
for i, record in enumerate(data_preview[:3]):
    date_str = record.get('grant_date', '')
    year, month = parse_grant_date(date_str)
    print(f'Record {i}: {date_str} -> Year: {year}, Month: {month}')

# Also check Patents_info for country code patterns
print('\nPatents_info examples:')
for i, record in enumerate(data_preview[:3]):
    patents_info = record.get('Patents_info', '')
    print(f'Record {i}: {patents_info}')"""

env_args = {'var_functions.list_db:0': ['publicationinfo'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json'}

exec(code, env_args)
