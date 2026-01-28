code = """import json
import re
from collections import defaultdict

# Access the stored data file
file_path = var_functions.query_db:38

# Load the data
with open(file_path, 'r') as f:
    publications = json.load(f)

print(f'Loaded {len(publications)} publications')

# Process data: extract year and CPC codes
year_cpc_counts = defaultdict(lambda: defaultdict(int))
cpc_year_counts = defaultdict(lambda: defaultdict(int))

for pub in publications:
    # Extract year from publication date
    date_str = pub.get('publication_date', '')
    year_match = re.search(r'(\d{4})', date_str)
    if not year_match:
        continue
    
    year = int(year_match.group(1))
    
    # Parse CPC codes
    cpc_str = pub.get('cpc', '[]')
    try:
        cpc_list = json.loads(cpc_str)
        for cpc_item in cpc_list:
            code = cpc_item.get('code', '')
            if code:
                # Extract level 5 code (first 5 characters of main class)
                main_class = code.split('/')[0]
                if len(main_class) >= 5:
                    level5_code = main_class[:5]
                    year_cpc_counts[year][level5_code] += 1
                    cpc_year_counts[level5_code][year] += 1
    except:
        continue

# Get all years sorted
all_years = sorted(year_cpc_counts.keys())
print(f'Year range: {min(all_years)} to {max(all_years)}')
print(f'Found {len(cpc_year_counts)} unique level 5 CPC codes')

# Calculate EMA for each CPC code
alpha = 0.2
results = []

for cpc_code in cpc_year_counts:
    counts_by_year = cpc_year_counts[cpc_code]
    
    # Build complete time series
    time_series = []
    ema_prev = None
    
    for year in range(min(all_years), max(all_years) + 1):
        count = counts_by_year.get(year, 0)
        
        # Calculate EMA
        if ema_prev is None:
            ema = float(count)
        else:
            ema = alpha * count + (1 - alpha) * ema_prev
        
        ema_prev = ema
        time_series.append((year, ema))
    
    # Find year with highest EMA
    if time_series:
        best_year, best_ema = max(time_series, key=lambda x: x[1])
        
        # Check if best year is 2022
        if best_year == 2022:
            results.append({
                'cpc_code': cpc_code,
                'best_year': best_year,
                'best_ema': best_ema
            })

# Sort by EMA (highest first)
results_sorted = sorted(results, key=lambda x: x['best_ema'], reverse=True)

print(f'Found {len(results_sorted)} CPC codes with best year 2022')

# Extract just the CPC codes
cpc_codes_2022 = [r['cpc_code'] for r in results_sorted]

result_json = json.dumps(cpc_codes_2022)
print('__RESULT__:')
print(result_json)"""

env_args = {'var_functions.list_db:0': ['publicationinfo'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.list_db:5': ['cpc_definition'], 'var_functions.query_db:6': [{'count': '277813'}], 'var_functions.query_db:11': 'file_storage/functions.query_db:11.json', 'var_functions.query_db:10': 'file_storage/functions.query_db:10.json', 'var_functions.query_db:12': [{'symbol': 'A01H', 'level': '5.0'}, {'symbol': 'A01F', 'level': '5.0'}, {'symbol': 'A01C', 'level': '5.0'}, {'symbol': 'A01G', 'level': '5.0'}, {'symbol': 'A23J', 'level': '5.0'}, {'symbol': 'A01N', 'level': '5.0'}, {'symbol': 'A01P', 'level': '5.0'}, {'symbol': 'A01D', 'level': '5.0'}, {'symbol': 'A01L', 'level': '5.0'}, {'symbol': 'A01K', 'level': '5.0'}], 'var_functions.execute_python:30': [], 'var_functions.query_db:32': 'file_storage/functions.query_db:32.json', 'var_functions.query_db:36': 'file_storage/functions.query_db:36.json', 'var_functions.query_db:38': 'file_storage/functions.query_db:38.json', 'var_functions.query_db:40': [{'publication_date': 'on March 15th, 2022'}, {'publication_date': '25th Jan 2022'}, {'publication_date': 'April 19th, 2022'}, {'publication_date': '28th June 2022'}, {'publication_date': '25th October 2022'}]}

exec(code, env_args)
