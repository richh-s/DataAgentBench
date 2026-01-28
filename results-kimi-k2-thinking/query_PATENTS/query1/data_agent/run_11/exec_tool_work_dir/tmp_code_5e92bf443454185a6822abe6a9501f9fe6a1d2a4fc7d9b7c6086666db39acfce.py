code = """import json
from datetime import datetime
import sys

# Get the file path from the query result
file_path_key = 'var_functions.query_db:34'
if file_path_key in locals():
    file_path = locals()[file_path_key]
    print('Found file path:', file_path[:100])
else:
    print('Variable not found in locals()')
    sys.exit(1)

# Read the json data from the file
with open(file_path, 'r') as file_handle:
    data = json.load(file_handle)

print('Total records:', len(data))

# Process data to extract CPC codes and years
cpc_year_counts = {}
all_years = set()

for record in data:
    try:
        # Parse date
        date_str = record['publication_date']
        for suffix in ['st,', 'nd,', 'rd,', 'th,']:
            date_str = date_str.replace(suffix, ',')
        date_obj = datetime.strptime(date_str.strip(), '%b %d, %Y')
        year = date_obj.year
        all_years.add(year)
        
        # Parse CPC codes
        cpc_list = json.loads(record['cpc'])
        for cpc_item in cpc_list:
            code = cpc_item.get('code', '')
            if code and '/' in code:
                parts = code.split('/')
                if len(parts) == 2:
                    subgroup = parts[1]
                    # Level 5 codes have subgroups of 3+ digits
                    if len(subgroup) >= 3 and subgroup.isdigit():
                        if code not in cpc_year_counts:
                            cpc_year_counts[code] = {}
                        cpc_year_counts[code][year] = cpc_year_counts[code].get(year, 0) + 1
    except:
        continue

print('Processed CPC codes:', len(cpc_year_counts))
print('Year range:', sorted(list(all_years)))

# Calculate EMA
alpha = 0.2
cpc_best_2022 = []

for cpc_code, yearly_counts in cpc_year_counts.items():
    sorted_years = sorted(list(all_years))
    ema_vals = {}
    ema = 0
    
    for year in sorted_years:
        count = yearly_counts.get(year, 0)
        ema = alpha * count + (1 - alpha) * ema
        ema_vals[year] = ema
    
    if ema_vals:
        best_year = max(ema_vals.keys(), key=lambda y: ema_vals[y])
        if best_year == 2022:
            cpc_best_2022.append((cpc_code, ema_vals[2022]))

# Sort by EMA descending
cpc_best_2022.sort(key=lambda x: x[1], reverse=True)
final_codes = [code for code, ema in cpc_best_2022]

print('Final result count:', len(final_codes))

print('\n__RESULT__:')
print(json.dumps(final_codes))"""

env_args = {'var_functions.list_db:0': ['publicationinfo'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json', 'var_functions.query_db:22': 'file_storage/functions.query_db:22.json', 'var_functions.query_db:30': 'file_storage/functions.query_db:30.json', 'var_functions.query_db:34': 'file_storage/functions.query_db:34.json'}

exec(code, env_args)
