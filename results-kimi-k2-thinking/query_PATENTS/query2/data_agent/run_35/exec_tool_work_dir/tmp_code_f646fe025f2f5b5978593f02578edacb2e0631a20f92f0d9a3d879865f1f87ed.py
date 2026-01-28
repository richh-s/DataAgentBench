code = """import json
import pandas as pd
from datetime import datetime
import re

# Load the data
result_file = var_functions.query_db:9
with open(result_file, 'r') as f:
    data = json.load(f)

# Convert to DataFrame
df = pd.DataFrame(data)

# Filter for Germany patents and second half of 2019
germany_patents = []

for idx, row in df.iterrows():
    # Check if it's a Germany patent
    patents_info = row['Patents_info']
    if 'DE-' not in patents_info:
        continue
    
    # Parse grant date
    grant_date_str = row['grant_date']
    if not grant_date_str or pd.isna(grant_date_str):
        continue
    
    # Clean and parse date
    # Remove ordinal suffixes like 'th', 'st', 'nd', 'rd'
    cleaned_date = re.sub(r'(\d+)(st|nd|rd|th)', r'\1', grant_date_str)
    cleaned_date = cleaned_date.replace('on ', '')
    
    try:
        # Try multiple date formats
        date_formats = ['%d %b %Y', '%b %d %Y', '%d %B %Y', '%B %d %Y']
        grant_date = None
        for fmt in date_formats:
            try:
                grant_date = datetime.strptime(cleaned_date, fmt)
                break
            except:
                continue
        
        if grant_date is None:
            continue
            
        # Check if in second half of 2019
        if grant_date.year == 2019 and grant_date.month >= 7:
            germany_patents.append({
                'patent_info': patents_info,
                'grant_date': grant_date,
                'cpc': row['cpc'],
                'title_localized': row['title_localized']
            })
    except:
        continue

print(f"Found {len(germany_patents)} Germany patents granted in second half 2019")
print('__RESULT__:')
print(json.dumps({"count": len(germany_patents), "sample": germany_patents[:2] if germany_patents else []}))"""

env_args = {'var_functions.list_db:2': ['publicationinfo'], 'var_functions.list_db:5': ['cpc_definition'], 'var_functions.query_db:9': 'file_storage/functions.query_db:9.json'}

exec(code, env_args)
