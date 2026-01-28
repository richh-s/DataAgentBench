code = """import json
import pandas as pd
import re
from datetime import datetime

# Get the file path from storage
file_path = locals()['var_functions.query_db:2']

# Load the full results from the query
with open(file_path, 'r') as f:
    patents_2019 = json.load(f)

print(f"Total patents granted in 2019: {len(patents_2019)}")

# Function to parse grant dates in various formats
def parse_grant_date(date_str):
    if not date_str:
        return None
    
    # Clean up the date string
    date_str = date_str.strip()
    
    # Common patterns
    patterns = [
        r'(\d{1,2})\w{2} (\w+) (\d{4})',  # "14th Mar 2019"
        r'(\w+) (\d{1,2})\w{2}, (\d{4})',  # "Mar 19th, 2019"
        r'on (\d{1,2})\w{2} of (\w+),? (\d{4})',  # "on 23rd of July, 2019"
        r'(\w+) (\d{1,2})\w{2} of (\d{4})',  # "July 8th of 2019"
        r'^(\w+) (\d{1,2})(?:st|nd|rd|th),? (\d{4})$',  # "July 8th, 2019" or "July 8, 2019"
    ]
    
    month_map = {
        'Jan': 1, 'January': 1,
        'Feb': 2, 'February': 2,
        'Mar': 3, 'March': 3,
        'Apr': 4, 'April': 4,
        'May': 5,
        'Jun': 6, 'June': 6,
        'Jul': 7, 'July': 7,
        'Aug': 8, 'August': 8,
        'Sep': 9, 'September': 9,
        'Oct': 10, 'October': 10,
        'Nov': 11, 'November': 11,
        'Dec': 12, 'December': 12
    }
    
    for pattern in patterns:
        match = re.match(pattern, date_str, re.IGNORECASE)
        if match:
            try:
                if pattern == patterns[0]:  # "14th Mar 2019"
                    day, month, year = match.groups()
                elif pattern == patterns[1]:  # "Mar 19th, 2019"
                    month, day, year = match.groups()
                elif pattern == patterns[2]:  # "on 23rd of July, 2019"
                    day, month, year = match.groups()
                elif pattern == patterns[3]:  # "July 8th of 2019"
                    month, day, year = match.groups()
                elif pattern == patterns[4]:  # "July 8th, 2019"
                    month, day, year = match.groups()
                
                month_num = month_map.get(month.strip())
                if month_num:
                    return datetime(int(year), month_num, int(day))
            except:
                continue
    
    return None

# Parse dates and extract country code (DE for Germany)
parsed_patents = []
for patent in patents_2019:
    parsed_date = parse_grant_date(patent['grant_date'])
    if parsed_date:
        patent_data = {
            'Patents_info': patent['Patents_info'],
            'grant_date': patent['grant_date'],
            'parsed_date': parsed_date,
            'cpc': patent['cpc'],
            'country_code': None
        }
        
        # Extract country code from Patents_info
        patents_info = patent['Patents_info']
        if 'DE-' in patents_info or ' from DE,' in patents_info or 'Germany' in patents_info:
            patent_data['country_code'] = 'DE'
        elif 'DE' in patents_info.split()[:3]:  # Check if DE appears early in the string
            patent_data['country_code'] = 'DE'
        
        parsed_patents.append(patent_data)

# Create DataFrame
df = pd.DataFrame(parsed_patents)

# Filter for Germany patents
patents_de = df[df['country_code'] == 'DE'].copy()
print(f"Total Germany patents in 2019: {len(patents_de)}")

# Filter for second half of 2019 (July - December)
patents_de['month'] = patents_de['parsed_date'].dt.month
patents_de_h2 = patents_de[patents_de['month'] >= 7].copy()

print(f"Germany patents granted in second half 2019: {len(patents_de_h2)}")

# Show some examples
print("\nSample Germany H2 2019 patents:")
for idx, row in patents_de_h2.head(3).iterrows():
    print(f"\nDate: {row['grant_date']}")
    print(f"Info: {row['Patents_info'][:100]}...")
    print(f"CPC: {row['cpc'][:100]}...")

result = {
    'total_de_patents_2019': len(patents_de),
    'de_patents_h2_2019': len(patents_de_h2),
    'date_range': {
        'min': patents_de_h2['parsed_date'].min().strftime('%Y-%m-%d') if len(patents_de_h2) > 0 else None,
        'max': patents_de_h2['parsed_date'].max().strftime('%Y-%m-%d') if len(patents_de_h2) > 0 else None
    }
}

print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.list_db:0': ['publicationinfo'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.execute_python:6': {'total_patents_2019': 3838, 'sample_records_count': 3}}

exec(code, env_args)
