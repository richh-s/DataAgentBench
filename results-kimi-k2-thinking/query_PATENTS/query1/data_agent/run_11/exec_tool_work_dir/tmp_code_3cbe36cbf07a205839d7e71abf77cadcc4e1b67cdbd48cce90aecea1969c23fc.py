code = """import json
from datetime import datetime

# Get the file path from the query result  
file_path = var_functions.query_db:40

# Load the data
with open(file_path, 'r') as f:
    data = json.load(f)

# Process records to extract CPC and year
cpc_counts = {}
all_years = set()

for rec in data:
    try:
        # Parse date
        date_str = rec['publication_date']
        for suffix in ['st,', 'nd,', 'rd,', 'th,']:
            date_str = date_str.replace(suffix, ',')
        year = datetime.strptime(date_str.strip(), '%b %d, %Y').year
        all_years.add(year)
        
        # Parse CPC codes
        for item in json.loads(rec['cpc']):
            code = item.get('code', '')
            # Filter level 5 codes (format: class/subclass with subgroup of 3+ digits)
            if '/' in code and len(code.split('/')[1]) >= 3:
                if code not in cpc_counts:
                    cpc_counts[code] = {}
                cpc_counts[code][year] = cpc_counts[code].get(year, 0) + 1
    except:
        continue

# Calculate EMA (smoothing factor 0.2)
alpha = 0.2
cpc_best_2022 = []

for code, yearly_counts in cpc_counts.items():
    years = sorted(list(all_years))
    ema = 0
    best_year = None
    best_ema = 0
    
    for year in years:
        cnt = yearly_counts.get(year, 0)
        ema = alpha * cnt + (1 - alpha) * ema
        if ema > best_ema:
            best_ema = ema
            best_year = year
    
    if best_year == 2022:
        cpc_best_2022.append((code, best_ema))

# Sort by EMA and extract codes
cpc_best_2022.sort(key=lambda x: x[1], reverse=True)
result = [code for code, ema in cpc_best_2022]

print('\n__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.list_db:0': ['publicationinfo'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json', 'var_functions.query_db:22': 'file_storage/functions.query_db:22.json', 'var_functions.query_db:30': 'file_storage/functions.query_db:30.json', 'var_functions.query_db:34': 'file_storage/functions.query_db:34.json', 'var_functions.query_db:40': 'file_storage/functions.query_db:40.json'}

exec(code, env_args)
