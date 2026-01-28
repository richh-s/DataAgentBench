code = """import json
import pandas as pd
import re
from collections import defaultdict
import math

# Read full CPC level 5 data
level5_file = locals()['var_functions.query_db:12']
print("Loading level 5 symbols...")
with open(level5_file, 'r') as f:
    level5_data = json.load(f)

# Create a comprehensive set of level 5 symbols
level5_symbols = set()
for item in level5_data:
    if item and 'symbol' in item:
        symbol = item['symbol']
        if symbol and len(symbol) <= 5:
            level5_symbols.add(symbol)

print(f"Total level 5 CPC symbols: {len(level5_symbols)}")

# Read patent data
patents_file = locals()['var_functions.query_db:8']
print("Loading patent data...")
with open(patents_file, 'r') as f:
    patents_data = json.load(f)

print(f"Total patent records: {len(patents_data)}")

# Parse data and count filings per year for each level 5 group
yearly_group_counts = defaultdict(lambda: defaultdict(int))
cpc_pattern = re.compile(r'"code":\s*"([^"]+)"')
year_pattern = re.compile(r'(\d{4})')

processed = 0
print("Processing records...")
for record in patents_data:
    processed += 1
    if processed % 50000 == 0:
        print(f"Processed {processed} records...")
    
    # Extract CPC codes
    cpc_str = record.get('cpc', '')
    if not cpc_str:
        continue
    
    cpc_matches = cpc_pattern.findall(cpc_str)
    
    # Extract year
    pub_date = record.get('publication_date', '')
    if not pub_date:
        continue
    
    year_match = year_pattern.search(pub_date)
    if not year_match:
        continue
    
    year = int(year_match.group(1))
    
    # Map each CPC code to level 5 group
    for cpc_code in cpc_matches:
        parts = cpc_code.split('/')
        main_group = parts[0]
        
        group_code = None
        if main_group in level5_symbols:
            group_code = main_group
        else:
            for i in range(len(main_group)-1, 3, -1):
                prefix = main_group[:i]
                if prefix in level5_symbols:
                    group_code = prefix
                    break
        
        if group_code:
            yearly_group_counts[group_code][year] += 1

print(f"Finished processing {processed} records")
print(f"Found {len(yearly_group_counts)} CPC groups with filings")

# Calculate EMA for each group
alpha = 0.2
results = []

print("Calculating EMAs...")
for group_code, year_counts in yearly_group_counts.items():
    years = sorted(year_counts.items())
    
    if len(years) < 2:
        continue
    
    ema_values = {}
    first_year, first_count = years[0]
    ema = first_count
    ema_values[first_year] = ema
    
    for year, count in years[1:]:
        ema = alpha * count + (1 - alpha) * ema
        ema_values[year] = ema
    
    best_year = max(ema_values.keys(), key=lambda y: ema_values[y])
    best_ema = ema_values[best_year]
    
    if best_year == 2022:
        results.append({
            'cpc_group_code': group_code,
            'ema_2022': round(best_ema, 2),
            'yearly_counts': dict(year_counts),
        })

print(f"Found {len(results)} CPC groups with best year 2022")

results.sort(key=lambda x: x['ema_2022'], reverse=True)

final_cpc_codes = [r['cpc_group_code'] for r in results]

seen = set()
unique_cpc_codes = []
for code in final_cpc_codes:
    if code not in seen:
        seen.add(code)
        unique_cpc_codes.append(code)

print(f"Final list of {len(unique_cpc_codes)} unique CPC group codes")

result_json = json.dumps(unique_cpc_codes)
print('__RESULT__:')
print(result_json)"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:5': [{'total_records': '277813'}], 'var_functions.query_db:6': [{'symbol': 'A01H', 'level': '5.0'}, {'symbol': 'A01F', 'level': '5.0'}, {'symbol': 'A01C', 'level': '5.0'}, {'symbol': 'A01G', 'level': '5.0'}, {'symbol': 'A23J', 'level': '5.0'}, {'symbol': 'A01N', 'level': '5.0'}, {'symbol': 'A01P', 'level': '5.0'}, {'symbol': 'A01D', 'level': '5.0'}, {'symbol': 'A01L', 'level': '5.0'}, {'symbol': 'A01K', 'level': '5.0'}], 'var_functions.query_db:8': 'file_storage/functions.query_db:8.json', 'var_functions.execute_python:10': ['A01N', 'A01N', 'A01N', 'A01N', 'A01N', 'A01K', 'A01K', 'A01N', 'A01K', 'A01G', 'A01N', 'A01K', 'A01N', 'A01K', 'A01K', 'A01K', 'A01D', 'A01N', 'A01K', 'A01N', 'A01N', 'A01K', 'A01K', 'A01K', 'A01G', 'A01K', 'A01N', 'A01K', 'A01N', 'A01G', 'A01K', 'A01K', 'A01K', 'A01N', 'A01D', 'A01G', 'A01K', 'A01N', 'A01K', 'A01K', 'A01D', 'A01G', 'A01N', 'A01K', 'A01N', 'A01K', 'A01D', 'A01K', 'A01N', 'A01K', 'A01N', 'A01D', 'A01K', 'A01N', 'A01D', 'A01K', 'A01F', 'A01K', 'A01D', 'A01K', 'A01K', 'A01K', 'A01K', 'A01G', 'A01N', 'A01K', 'A01D', 'A01G', 'A01C', 'A01G', 'A01K', 'A01D', 'A01D', 'A01D', 'A01D', 'A01D', 'A01N'], 'var_functions.query_db:12': 'file_storage/functions.query_db:12.json', 'var_functions.execute_python:14': ['A61K'], 'var_functions.query_db:16': [{'publication_date': 'on March 15th, 2022'}, {'publication_date': '25th Jan 2022'}, {'publication_date': 'April 19th, 2022'}, {'publication_date': '28th June 2022'}, {'publication_date': '25th October 2022'}, {'publication_date': '30th of August, 2022'}, {'publication_date': '2nd August 2022'}, {'publication_date': 'Feb 8th, 2022'}, {'publication_date': '8th November 2022'}, {'publication_date': '2022, November 1st'}]}

exec(code, env_args)
