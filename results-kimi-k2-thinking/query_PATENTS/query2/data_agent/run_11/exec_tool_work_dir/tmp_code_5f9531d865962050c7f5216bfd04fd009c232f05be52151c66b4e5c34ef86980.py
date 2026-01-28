code = """import json
import pandas as pd
import re
from datetime import datetime

# Load the data from the file
file_path = var_functions.query_db:2
with open(file_path, 'r') as f:
    data = json.load(f)

print(f"Total records loaded: {len(data)}")

# Filter for German patents (DE in Patents_info)
german_patents = []
for record in data:
    if 'DE-' in record['Patents_info']:
        german_patents.append(record)

print(f"German patents found: {len(german_patents)}")

# Parse grant dates to identify second half of 2019 (July-December 2019)
h2_2019_patents = []
for record in german_patents:
    grant_date_str = record['grant_date']
    # Extract date information using regex
    date_match = re.search(r'(\d{1,2}).*?(Jan|Feb|Mar|Apr|May|Jun|Jul|Aug|Sep|Oct|Nov|Dec).*?2019', grant_date_str, re.IGNORECASE)
    if date_match:
        day = int(date_match.group(1))
        month_str = date_match.group(2).lower()
        
        # Convert month string to month number
        month_map = {
            'jan': 1, 'feb': 2, 'mar': 3, 'apr': 4, 'may': 5, 'jun': 6,
            'jul': 7, 'aug': 8, 'sep': 9, 'oct': 10, 'nov': 11, 'dec': 12
        }
        month = month_map.get(month_str)
        
        if month and month >= 7:  # July to December
            h2_2019_patents.append(record)
    elif '2019' in grant_date_str and ('Jul' in grant_date_str or 'Aug' in grant_date_str or 'Sep' in grant_date_str or 
                                       'Oct' in grant_date_str or 'Nov' in grant_date_str or 'Dec' in grant_date_str):
        h2_2019_patents.append(record)

print(f"German patents granted in H2 2019: {len(h2_2019_patents)}")

# Extract CPC codes
patent_data = []
for idx, record in enumerate(h2_2019_patents):
    cpc_json = record['cpc']
    if cpc_json and cpc_json != '[]':
        try:
            cpc_list = json.loads(cpc_json)
            for cpc_item in cpc_list:
                code = cpc_item.get('code', '')
                if code:
                    patent_data.append({
                        'patent_index': idx,
                        'cpc_code': code,
                        'patents_info': record['Patents_info'],
                        'grant_date': record['grant_date']
                    })
        except:
            # Fallback for malformed JSON
            if '[{"code":' in cpc_json:
                codes = re.findall(r'"code":\s*"([^"]+)"', cpc_json)
                for code in codes:
                    patent_data.append({
                        'patent_index': idx,
                        'cpc_code': code,
                        'patents_info': record['Patents_info'],
                        'grant_date': record['grant_date']
                    })

print(f"CPC code entries extracted: {len(patent_data)}")

# Create DataFrame for easier manipulation
df = pd.DataFrame(patent_data)
if not df.empty:
    print("Sample CPC codes:")
    print(df['cpc_code'].head(10).tolist())

__RESULT__:
json.dumps({
    'total_patents': len(h2_2019_patents),
    'cpc_entries': len(patent_data),
    'sample_cpc': df['cpc_code'].head(10).tolist() if not df.empty else []
})"""

env_args = {'var_functions.list_db:0': ['publicationinfo'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json'}

exec(code, env_args)
