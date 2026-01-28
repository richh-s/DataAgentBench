code = """import json
import pandas as pd
from datetime import datetime
import re

# Read the file path from the storage variable
file_path = var_functions.query_db:7

# Load the data from the file
with open(file_path, 'r') as f:
    data = json.load(f)

print(f"Total records: {len(data)}")
print("Sample record:")
print(data[0])

# Parse CPC codes and extract years
records = []
for row in data:
    cpc_json = row['cpc']
    pub_date = row['publication_date']
    
    # Extract year from publication date
    year_match = re.search(r'(\d{4})', pub_date)
    if year_match:
        year = int(year_match.group(1))
    else:
        continue
    
    # Parse CPC JSON - it's already a string, try to load it
    try:
        if isinstance(cpc_json, str):
            cpc_list = json.loads(cpc_json)
        else:
            cpc_list = cpc_json
            
        for cpc_entry in cpc_list:
            code = cpc_entry['code']
            records.append({
                'cpc_code': code,
                'year': year
            })
    except Exception as e:
        continue

print(f"Total CPC records: {len(records)}")
if records:
    print("Sample CPC records:", records[:5])

# Create DataFrame and show basic stats
if records:
    df = pd.DataFrame(records)
    print("DataFrame shape:", df.shape)
    print("Year range:", df['year'].min(), "to", df['year'].max())
    print("Unique CPC codes:", df['cpc_code'].nunique())
else:
    print("No records found")"""

env_args = {'var_functions.list_db:0': ['publicationinfo'], 'var_functions.list_db:2': ['cpc_definition'], 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json', 'var_functions.query_db:7': 'file_storage/functions.query_db:7.json'}

exec(code, env_args)
