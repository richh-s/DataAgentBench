code = """import json
from datetime import datetime

# Get file path
fp = locals()['var_functions.query_db:40']

# Load data
with open(fp, 'r') as f:
    data = json.load(f)

# Extract CPC counts by year
cpc_data = {}
years_set = set()

for r in data:
    try:
        # Parse date
        ds = r['publication_date']
        for sfx in ['st,', 'nd,', 'rd,', 'th,']:
            ds = ds.replace(sfx, ',')
        yr = datetime.strptime(ds.strip(), '%b %d, %Y').year
        years_set.add(yr)
        
        # Parse CPC codes
        for itm in json.loads(r['cpc']):
            cd = itm.get('code', '')
            # Level 5: has / and subgroup >= 3 digits
            if '/' in cd and len(cd.split('/')[1]) >= 3:
                if cd not in cpc_data:
                    cpc_data[cd] = {}
                cpc_data[cd][yr] = cpc_data[cd].get(yr, 0) + 1
    except:
        pass

# Calculate EMA (alpha=0.2)
alpha = 0.2
result = []

for cd, yr_counts in cpc_data.items():
    sy = sorted(list(years_set))
    ema_val = 0
    best_yr = None
    best_ema = 0
    
    for y in sy:
        cnt = yr_counts.get(y, 0)
        ema_val = alpha * cnt + (1 - alpha) * ema_val
        if ema_val > best_ema:
            best_ema = ema_val
            best_yr = y
    
    if best_yr == 2022:
        result.append((cd, best_ema))

# Sort by EMA descending
result.sort(key=lambda x: x[1], reverse=True)
final_codes = [x[0] for x in result]

print('\n__RESULT__:')
print(json.dumps(final_codes))"""

env_args = {'var_functions.list_db:0': ['publicationinfo'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json', 'var_functions.query_db:22': 'file_storage/functions.query_db:22.json', 'var_functions.query_db:30': 'file_storage/functions.query_db:30.json', 'var_functions.query_db:34': 'file_storage/functions.query_db:34.json', 'var_functions.query_db:40': 'file_storage/functions.query_db:40.json'}

exec(code, env_args)
