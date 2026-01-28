code = """import json
import re
from collections import defaultdict
import pandas as pd

# Read the query results
result_file = var_functions.query_db:5
with open(result_file, 'r') as f:
    data = json.load(f)

# Sample the data to understand structure
print("Number of records:", len(data))
print("\nFirst record CPC:")
cpc_sample = data[0]['cpc']
print(cpc_sample[:200])

# Extract CPC codes and publication dates
cpc_year_counts = defaultdict(lambda: defaultdict(int))
years = set()

for record in data:
    cpc_json_str = record['cpc']
    pub_date = record['publication_date']
    
    # Extract year from publication date
    if pub_date:
        year_match = re.search(r'(\d{4})', pub_date)
        if year_match:
            year = int(year_match.group(1))
            years.add(year)
            
            # Parse CPC codes
            if cpc_json_str and cpc_json_str != '[]':
                try:
                    # Remove trailing backslashes and unescaped newlines if any
                    cleaned_cpc = cpc_json_str.replace('\\n', '\n')
                    cpc_list = json.loads(cleaned_cpc)
                    
                    for cpc_item in cpc_list:
                        code = cpc_item.get('code', '')
                        if code:
                            # Extract first 5 levels of CPC (e.g., H01M04)
                            parts = code.split('/')
                            if len(parts) >= 1:
                                main_group = parts[0]
                                # Pad to ensure consistent length
                                while len(main_group) < 7:
                                    main_group += '0'
                                level5_group = main_group[:7]  # First 7 chars for level 5
                                cpc_year_counts[level5_group][year] += 1
                except json.JSONDecodeError as e:
                    print(f"JSON parse error: {e}")
                    continue

print("\nUnique CPC groups (level 5):", len(cpc_year_counts))
print("Year range:", min(years) if years else None, "to", max(years) if years else None)
print("Sample CPC counts:")
for cpc, year_counts in list(cpc_year_counts.items())[:5]:
    print(f"{cpc}: {dict(list(year_counts.items())[:3])}")"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json'}

exec(code, env_args)
