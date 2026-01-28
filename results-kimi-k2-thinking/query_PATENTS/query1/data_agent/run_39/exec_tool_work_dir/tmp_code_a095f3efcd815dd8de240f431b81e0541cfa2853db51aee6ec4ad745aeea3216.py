code = """import json
import re
from datetime import datetime

# Read the query result file using locals()
file_path = locals()['var_functions.query_db:6']
with open(file_path, 'r') as f:
    data = json.load(f)

# Parse publication dates and extract CPC codes
patents_by_year = {}
cpc_count_by_year = {}

for record in data:
    # Parse publication date
    pub_date_str = record['publication_date']
    # Extract year from date string like "Aug 3rd, 2021"
    year_match = re.search(r'\d{4}', pub_date_str)
    if year_match:
        year = int(year_match.group())
        
        # Parse CPC codes (it's a JSON string)
        cpc_data = json.loads(record['cpc'])
        for cpc_entry in cpc_data:
            cpc_code = cpc_entry['code']
            # Extract CPC group (first 4 characters for section+class+subclass+group)
            # For level 5, we need section+class+subclass+group+subgroup
            # CPC format: Section (1 char) + Class (2 digits) + Subclass (1 letter) + Group (1-3 digits) + / + Subgroup (1-6 digits)
            # Level 5 is the full code including the subgroup
            # For the purpose of this analysis, we'll use the full code
            
            # Count patents by year and CPC
            year_key = str(year)
            if year_key not in patents_by_year:
                patents_by_year[year_key] = 0
                cpc_count_by_year[year_key] = {}
            
            patents_by_year[year_key] += 1
            if cpc_code not in cpc_count_by_year[year_key]:
                cpc_count_by_year[year_key][cpc_code] = 0
            cpc_count_by_year[year_key][cpc_code] += 1

# Calculate exponential moving average (EMA) for each CPC
cpc_ema = {}
smoothing = 0.2

# Get sorted years
years = sorted(patents_by_year.keys(), key=int)

for cpc_code in set(code for year_data in cpc_count_by_year.values() for code in year_data.keys()):
    ema_values = []
    prev_ema = None
    
    for year in years:
        year_int = int(year)
        count = cpc_count_by_year.get(year, {}).get(cpc_code, 0)
        
        if prev_ema is None:
            # First year - use actual value
            ema = count
        else:
            # EMA formula: EMA(today) = (Price(today) * k) + (EMA(yesterday) * (1 - k))
            ema = (count * smoothing) + (prev_ema * (1 - smoothing))
        
        ema_values.append((year, ema))
        prev_ema = ema
    
    cpc_ema[cpc_code] = ema_values

print("__RESULT__:")
print(json.dumps({
    "years_available": years,
    "total_cpc_codes": len(cpc_ema),
    "sample_ema": {k: v[:3] for k, v in list(cpc_ema.items())[:2]}
}))"""

env_args = {'var_functions.list_db:0': ['publicationinfo'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:6': 'file_storage/functions.query_db:6.json'}

exec(code, env_args)
