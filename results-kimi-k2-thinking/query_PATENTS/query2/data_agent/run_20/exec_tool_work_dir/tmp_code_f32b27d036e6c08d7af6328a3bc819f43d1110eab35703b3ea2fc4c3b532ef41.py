code = """import json
import re

# Load the full data from file path stored in var_functions.query_db:2
file_path = var_functions.query_db:2
with open(file_path, 'r') as f:
    data_parsed = json.load(f)

print('Total records:', len(data_parsed))
print('First record grant_date:', data_parsed[0].get('grant_date'))
print('First record patents_info:', data_parsed[0].get('Patents_info')[:200])

# Function to parse grant date more accurately
def parse_complete_date(date_str):
    if not date_str:
        return None
    
    # List of month names
    months = ['january', 'february', 'march', 'april', 'may', 'june',
              'july', 'august', 'september', 'october', 'november', 'december']
    
    # Clean the date string
    date_str = date_str.lower().replace('dated', '').strip()
    date_str = re.sub(r'([0-9]{1,2})(st|nd|rd|th|,)', r'\1', date_str)
    date_str = date_str.replace('of', '').strip()
    
    # Try to parse various formats
    # Format: "6th October 2020" or "21st September 2021"
    for i, month_name in enumerate(months):
        if month_name in date_str:
            # Find year (4 digits)
            year_match = re.search(r'([0-9]{4})', date_str)
            if year_match:
                year = int(year_match.group(1))
                month_num = i + 1
                return year, month_num
    
    return None

# Test parsing
for i, record in enumerate(data_parsed[:5]):
    grant_date = record.get('grant_date', '')
    parsed = parse_complete_date(grant_date)
    print(f'Record {i}: "{grant_date}" -> {parsed}')

# Check for Germany patents
print('\nLooking for German patents...')
for i, record in enumerate(data_parsed[:20]):
    patents_info = record.get('Patents_info', '').lower()
    # Look for Germany indicators
    if 'germany' in patents_info or 'de' in patents_info.split() or 'ep' in patents_info.split():
        print(f'Potential Germany patent {i}: {record.get("Patents_info")[:150]}')

# Print result format
result = 'Test completed'
print('__RESULT__:')
print(result)"""

env_args = {'var_functions.list_db:0': ['publicationinfo'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json'}

exec(code, env_args)
