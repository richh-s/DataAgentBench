code = """import json
import datetime

# Get file path
fp = locals()['var_functions.query_db:40']

# Load data
with open(fp, 'r') as f:
    data = json.load(f)

# Collect CPC counts by year
cpc_counts = {}
years_set = set()

for r in data:
    try:
        # Parse date
        ds = r['publication_date']
        for sfx in ['st,', 'nd,', 'rd,', 'th,']:
            ds = ds.replace(sfx, ',')
        yr = datetime.datetime.strptime(ds.strip(), '%b %d, %Y').year
        years_set.add(yr)
        
        # Parse CPC codes
        for itm in json.loads(r['cpc']):
            cd = itm.get('code', '')
            # Filter level 5 codes
            if '/' in cd and len(cd.split('/')[1]) >= 3:
                if cd not in cpc_counts:
                    cpc_counts[cd] = {}
                cpc_counts[cd][yr] = cpc_counts[cd].get(yr, 0) + 1
    except Exception:
        pass

# Calculate EMA
alpha = 0.2
results = []

for cd, yr_counts in cpc_counts.items():
    years = sorted(list(years_set))
    ema = 0
    best_yr = None
    best_ema = 0
    
    for y in years:
        cnt = yr_counts.get(y, 0)
        ema = alpha * cnt + (1 - alpha) * ema
        if ema > best_ema:
            best_ema = ema
            best_yr = y
    
    if best_yr == 2022:
        results.append((cd, best_ema))

# Sort by EMA descending
results.sort(key=lambda x: x[1], reverse=True)

# Extract CPC codes
cpc_codes = [x[0] for x in results]

print('__RESULT__:')
print(json.dumps(cpc_codes))"""

env_args = {'var_functions.list_db:0': ['publicationinfo'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json', 'var_functions.query_db:22': 'file_storage/functions.query_db:22.json', 'var_functions.query_db:30': 'file_storage/functions.query_db:30.json', 'var_functions.query_db:34': 'file_storage/functions.query_db:34.json', 'var_functions.query_db:40': 'file_storage/functions.query_db:40.json'}

exec(code, env_args)
