code = """import json
import ast
from datetime import datetime

# Access the file path from storage
file_path = locals()['var_functions.query_db:10']
print(f"File path: {file_path}")

# Read the full result file
with open(file_path, 'r') as f:
    records = json.load(f)

print(f"Loaded {len(records)} patent records")
print(f"First record date: {records[0].get('publication_date')}")
print(f"First record CPC (first 100 chars): {str(records[0].get('cpc'))[:100]}")

# Parse CPC codes and extract years
patent_data = []
years_found = set()
cpc_patterns = {}

for i, record in enumerate(records):
    pub_date = record.get('publication_date', '')
    cpc_data = record.get('cpc', '[]')
    
    # Parse publication year
    year = None
    if pub_date:
        try:
            # Handle format like "Aug 3rd, 2021" or "Oct 6th, 2020"
            parts = pub_date.split(', ')
            if len(parts) >= 2:
                year_str = parts[1]
                year = int(year_str)
                years_found.add(year)
        except:
            pass
    
    # Parse CPC codes
    try:
        cpc_list = json.loads(cpc_data)
    except:
        try:
            cpc_list = ast.literal_eval(cpc_data)
        except:
            cpc_list = []
    
    # Extract CPC codes
    for cpc_entry in cpc_list:
        code = cpc_entry.get('code', '')
        if code and year:
            patent_data.append({
                'cpc_code': code,
                'year': year
            })
            
            # Track patterns for analysis
            if '/' in code:
                parts = code.split('/')
                pattern = parts[0] + '/X' * len(parts[1])
                cpc_patterns[pattern] = cpc_patterns.get(pattern, 0) + 1

print(f"\nExtracted {len(patent_data)} CPC-year entries")
print(f"Years found: {sorted(years_found)}")
if patent_data:
    print(f"Sample entries: {patent_data[:3]}")

print(f"\nTop CPC patterns:")
for pattern, count in sorted(cpc_patterns.items(), key=lambda x: x[1], reverse=True)[:5]:
    print(f"  {pattern}: {count}")

# Show unique CPC codes and their levels
from collections import Counter
unique_codes = [p['cpc_code'] for p in patent_data]
code_counter = Counter(unique_codes)
print(f"\nTop 10 most frequent CPC codes:")
for code, count in code_counter.most_common(10):
    print(f"  {code}: {count}")

# Determine what level 5 means
# CPC codes like: A01B01/00, C01B33/00, H01M10/0525
print("\nAnalyzing CPC code structure:")
sample_codes = code_counter.most_common(5)
for code, count in sample_codes:
    print(f"  {code}: sections={code.split('/')[0] if '/' in code else code}")"""

env_args = {'var_functions.list_db:0': ['publicationinfo'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:10': 'file_storage/functions.query_db:10.json'}

exec(code, env_args)
