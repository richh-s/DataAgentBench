code = """import json, pandas as pd, re, numpy as np
from datetime import datetime
from collections import defaultdict

# Access the patent data from the global variable
patent_result = globals()['var_functions.query_db:17']

# Load the patent data (if it's a file path or already loaded)
if isinstance(patent_result, str) and '.json' in patent_result:
    with open(patent_result, 'r') as f:
        patent_data = json.load(f)
else:
    patent_data = patent_result

# Initialize counters for patent filings per CPC code per year
cpc_year_counts = defaultdict(lambda: defaultdict(int))
cpc_codes_all = set()

# Process each patent record
records_processed = 0
for record in patent_data:
    try:
        # Parse CPC field
        cpc_str = record.get('cpc', '[]')
        if not cpc_str or cpc_str == 'null':
            continue
        
        cpc_list = json.loads(cpc_str)
        
        # Extract year from publication date
        pub_date_str = record.get('publication_date', '')
        if not pub_date_str:
            continue
        
        year_match = re.search(r'\b(20\d{2})\b', pub_date_str)
        if not year_match:
            continue
        
        year = int(year_match.group(1))
        if year < 2000 or year > 2030:  # Basic validation
            continue
        
        # Extract CPC codes
        for cpc_item in cpc_list:
            cpc_code = cpc_item.get('code', '')
            if cpc_code:
                # Store the full CPC code
                cpc_codes_all.add(cpc_code)
                cpc_year_counts[cpc_code][year] += 1
        
        records_processed += 1
        
    except:
        continue

print(f"Processed {records_processed:,} patent records")
print(f"Total unique CPC codes: {len(cpc_codes_all)}")
print(f"Year range: {min([min(years.keys()) for years in cpc_year_counts.values()])} to {max([max(years.keys()) for years in cpc_year_counts.values()])}")

# Show sample CPC codes
sample_codes = list(cpc_codes_all)[:10]
print(f"Sample CPC codes: {sample_codes}")

# Save the processed data for next step
cpc_year_counts_dict = {cpc: dict(years) for cpc, years in cpc_year_counts.items()}
print(f"__RESULT__:")
print(json.dumps({
    'cpc_year_counts': cpc_year_counts_dict,
    'total_records': records_processed,
    'unique_cpc_codes': len(cpc_codes_all)
}))"""

env_args = {'var_functions.list_db:0': ['publicationinfo'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.list_db:5': ['cpc_definition'], 'var_functions.query_db:15': [{'symbol': 'A01H', 'level': '5.0'}, {'symbol': 'A01F', 'level': '5.0'}, {'symbol': 'A01C', 'level': '5.0'}, {'symbol': 'A01G', 'level': '5.0'}, {'symbol': 'A23J', 'level': '5.0'}, {'symbol': 'A01N', 'level': '5.0'}, {'symbol': 'A01P', 'level': '5.0'}, {'symbol': 'A01D', 'level': '5.0'}, {'symbol': 'A01L', 'level': '5.0'}, {'symbol': 'A01K', 'level': '5.0'}], 'var_functions.query_db:14': 'file_storage/functions.query_db:14.json', 'var_functions.query_db:17': 'file_storage/functions.query_db:17.json'}

exec(code, env_args)
