code = """import pandas as pd
import json
import re
from datetime import datetime

# Access the query result file
result_file = var_functions.query_db:6
print(f"Loading data from {result_file}")

# Read the JSON data from file
with open(result_file, 'r') as f:
    data = json.load(f)

print(f"Total records: {len(data)}")

# Parse CPC codes and dates
cpc_date_records = []
for record in data:
    cpc_json_str = record['cpc']
    publication_date_str = record['publication_date']
    
    # Skip if no CPC or date
    if not cpc_json_str or not publication_date_str:
        continue
    
    # Parse CPC JSON
    try:
        cpc_list = json.loads(cpc_json_str)
    except:
        # If parsing as JSON fails, it might already be a Python object representation
        try:
            cpc_list = eval(cpc_json_str)
        except:
            continue
    
    # Parse date
    try:
        # Handle various date formats like "Aug 3rd, 2021", "Oct 6th, 2020"
        date_match = re.search(r'(\w+)\s+\d+(st|nd|rd|th)?,?\s+(\d{4})', publication_date_str)
        if date_match:
            month_str, _, year_str = date_match.groups()
            # Create a date with the first day of the month
            month_num = datetime.strptime(month_str[:3], '%b').month
            pub_date = datetime(int(year_str), month_num, 1)
            year = pub_date.year
        else:
            # Try other formats
            pub_date = datetime.strptime(publication_date_str.replace('st,', ',').replace('nd,', ',').replace('rd,', ',').replace('th,', ','), '%b %d, %Y')
            year = pub_date.year
    except:
        continue
    
    # Extract CPC codes
    if isinstance(cpc_list, list):
        for cpc_item in cpc_list:
            if isinstance(cpc_item, dict) and 'code' in cpc_item:
                code = cpc_item['code']
                # Extract group code (first part before /)
                if '/' in code:
                    group_code = code.split('/')[0]
                    cpc_date_records.append({
                        'full_code': code,
                        'group_code': group_code,
                        'year': year
                    })

# Create DataFrame
df = pd.DataFrame(cpc_date_records)
print(f"Extracted {len(df)} CPC records")

if len(df) == 0:
    print("No records found")
else:
    print(f"Year range: {df['year'].min()} to {df['year'].max()}")
    print(f"Sample data:")
    print(df.head(10))

# Save intermediate results for next steps
df_json = df.to_json(orient='records')
print('__RESULT__:')
print(df_json)"""

env_args = {'var_functions.list_db:0': ['publicationinfo'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json', 'var_functions.query_db:6': 'file_storage/functions.query_db:6.json'}

exec(code, env_args)
