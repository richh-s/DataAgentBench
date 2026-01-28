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
    if '2019' in grant_date_str:
        # Check for second half months
        h2_months = ['Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
        if any(month in grant_date_str for month in h2_months):
            h2_2019_patents.append(record)
        else:
            # Try to parse more specifically
            date_match = re.search(r'(\d{1,2}).*?(Jan|Feb|Mar|Apr|May|Jun|Jul|Aug|Sep|Oct|Nov|Dec).*?2019', grant_date_str, re.IGNORECASE)
            if date_match:
                month_str = date_match.group(2).lower()
                month_map = {
                    'jan': 1, 'feb': 2, 'mar': 3, 'apr': 4, 'may': 5, 'jun': 6,
                    'jul': 7, 'aug': 8, 'sep': 9, 'oct': 10, 'nov': 11, 'dec': 12
                }
                month = month_map.get(month_str)
                if month and month >= 7:
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

# Group by CPC group code (level 4: first 4 parts of the code)
cpc_groups = {}
for item in patent_data:
    code = item['cpc_code']
    # Take the group code (first 4 components)
    parts = code.split('/')[0].split('-')[0]
    group_code = parts[:4] if len(parts) >= 4 else parts
    
    if group_code not in cpc_groups:
        cpc_groups[group_code] = []
    cpc_groups[group_code].append(item)

print(f"Number of CPC groups: {len(cpc_groups)}")
print("Top CPC groups by volume:")
sorted_groups = sorted(cpc_groups.items(), key=lambda x: len(x[1]), reverse=True)
for group, items in sorted_groups[:10]:
    print(f"  {group}: {len(items)} patents")

# For now, let's just return summary statistics
result = {
    'german_patents_h2_2019': len(h2_2019_patents),
    'total_cpc_entries': len(patent_data),
    'cpc_groups': len(cpc_groups),
    'top_groups': [(group, len(items)) for group, items in sorted_groups[:10]]
}

print("__RESULT__:")
print(json.dumps(result))"""

env_args = {'var_functions.list_db:0': ['publicationinfo'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json'}

exec(code, env_args)
