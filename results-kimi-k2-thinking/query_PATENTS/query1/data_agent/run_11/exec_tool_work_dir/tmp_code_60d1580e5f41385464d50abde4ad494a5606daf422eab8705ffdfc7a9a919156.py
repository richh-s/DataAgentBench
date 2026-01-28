code = """import json
from datetime import datetime
import sys

# Get the query result file path
qp = locals()['var_functions.query_db:34']
print('File path preview:', str(qp)[:50])

# Read data from file
with open(qp, 'r') as f:
    raw_data = f.read()

# Parse JSON data
try:
    data = json.loads(raw_data)
except:
    data = eval(raw_data)

print('Records:', len(data))

# Extract CPC codes and years
cpc_counts = {}
years = set()
count = 0

for record in data:
    try:
        # Parse date
        date_str = record['publication_date']
        date_str = date_str.replace('st,', ',').replace('nd,', ',')
        date_str = date_str.replace('rd,', ',').replace('th,', ',')
        date_obj = datetime.strptime(date_str.strip(), '%b %d, %Y')
        year = date_obj.year
        years.add(year)
        
        # Parse CPC
        cpc_list = json.loads(record['cpc'])
        for item in cpc_list:
            code = item.get('code', '')
            if code and '/' in code:
                parts = code.split('/')
                if len(parts) == 2 and len(parts[1]) >= 3 and parts[1].isdigit():
                    if code not in cpc_counts:
                        cpc_counts[code] = {}
                    cpc_counts[code][year] = cpc_counts[code].get(year, 0) + 1
    except:
        pass

print('CPC codes:', len(cpc_counts))
print('Years:', sorted(list(years)))

# Calculate EMA
alpha = 0.2
result_codes = []

for code, yearly in cpc_counts.items():
    sy = sorted(list(years))
    ema = 0
    best_year = None
    best_ema = 0
    
    for year in sy:
        cnt = yearly.get(year, 0)
        ema = alpha * cnt + (1 - alpha) * ema
        if ema > best_ema:
            best_ema = ema
            best_year = year
    
    if best_year == 2022:
        result_codes.append((code, best_ema))

# Sort by EMA
def get_ema(x):
    return x[1]

result_codes.sort(key=get_ema, reverse=True)
final_list = [x[0] for x in result_codes]

print('Best 2022:', len(final_list))
print('\n__RESULT__:')
print(json.dumps(final_list))"""

env_args = {'var_functions.list_db:0': ['publicationinfo'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json', 'var_functions.query_db:22': 'file_storage/functions.query_db:22.json', 'var_functions.query_db:30': 'file_storage/functions.query_db:30.json', 'var_functions.query_db:34': 'file_storage/functions.query_db:34.json'}

exec(code, env_args)
