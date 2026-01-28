code = """import json
import pandas as pd
from collections import defaultdict
import re

# Load data from the JSON file
file_key = 'var_functions.query_db:18'
file_path = locals()[file_key]

# Read data in chunks to avoid memory issues
def load_data_efficiently(file_path, chunk_size=50000):
    with open(file_path, 'r') as f:
        data = json.load(f)
    return data

# Load the data
data = load_data_efficiently(file_path)

# Extract patent counts per CPC code per year - more efficient approach
patent_counts = defaultdict(lambda: defaultdict(int))
year_pattern = re.compile(r'(\d{4})')

for record in data:
    pub_date = record.get('publication_date', '')
    cpc_data = record.get('cpc', '')
    
    if pub_date and cpc_data and str(pub_date) != 'None':
        year_match = year_pattern.search(str(pub_date))
        if year_match:
            year = int(year_match.group(1))
            if 2010 <= year <= 2024:  # Focus on recent years
                try:
                    cpc_list = json.loads(cpc_data)
                    for cpc_entry in cpc_list:
                        if isinstance(cpc_entry, dict) and 'code' in cpc_entry:
                            code = str(cpc_entry['code'])
                            if '/' in code:  # Level 5 CPC codes
                                patent_counts[code][year] += 1
                except:
                    continue

# Convert to DataFrame
records = []
for code, years in patent_counts.items():
    for year, count in years.items():
        records.append({'cpc_code': code, 'year': year, 'count': count})

df = pd.DataFrame(records)

# Calculate EMA for each CPC code
alpha = 0.2
ema_results = []

cpc_codes = list(patent_counts.keys())
sample_size = min(5000, len(cpc_codes))  # Process a sample to avoid timeout
cpc_codes_sample = cpc_codes[:sample_size]

for cpc_code in cpc_codes_sample:
    years_data = patent_counts[cpc_code]
    if len(years_data) > 1:
        # Sort years
        sorted_years = sorted(years_data.items())
        
        # Calculate EMA
        ema_prev = sorted_years[0][1]  # First year count
        for year, count in sorted_years:
            ema_current = alpha * count + (1 - alpha) * ema_prev
            ema_results.append({
                'cpc_code': cpc_code,
                'year': year,
                'count': count,
                'ema': ema_current
            })
            ema_prev = ema_current

ema_df = pd.DataFrame(ema_results)

# Find best CPC code for each year
best_per_year = {}
for _, row in ema_df.iterrows():
    year = row['year']
    if year not in best_per_year or row['ema'] > best_per_year[year]['ema']:
        best_per_year[year] = {
            'cpc_code': row['cpc_code'],
            'ema': row['ema'],
            'count': row['count']
        }

# Find codes with best year = 2022
codes_best_in_2022 = []
if 2022 in best_per_year:
    target_code = best_per_year[2022]['cpc_code']
    
    # Find this code's best year
    code_years = ema_df[ema_df['cpc_code'] == target_code]
    if not code_years.empty:
        best_row = code_years.loc[code_years['ema'].idxmax()]
        if best_row['year'] == 2022:
            codes_best_in_2022.append(target_code)

result = {
    'total_cpc_codes': len(cpc_codes),
    'sample_processed': sample_size,
    'years_range': f"{df['year'].min() if not df.empty else 'N/A'} to {df['year'].max() if not df.empty else 'N/A'}",
    'codes_with_best_year_2022': codes_best_in_2022,
    'best_codes_2022_details': []
}

# Get details for codes with best year 2022
for code in codes_best_in_2022:
    code_data = ema_df[ema_df['cpc_code'] == code]
    best_row = code_data.loc[code_data['ema'].idxmax()]
    result['best_codes_2022_details'].append({
        'cpc_code': code,
        'best_year': int(best_row['year']),
        'ema_value': float(best_row['ema']),
        'count_at_best': int(best_row['count'])
    })

print('__RESULT__:')
print(json.dumps(result, indent=2))"""

env_args = {'var_functions.list_db:0': ['publicationinfo'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.execute_python:6': {'total_records': 250551, 'unique_cpc_codes': 97719, 'year_range': '1837 to 2024', 'sample_cpc_codes': ['C01B33/00', 'C01B35/00', 'H01M10/0565', 'H01M10/0562', 'C01G45/006', 'H01M10/0566', 'H01M10/052', 'C01P2002/76', 'Y02E60/10', 'H01M10/0525'], 'has_2022': True}, 'var_functions.list_db:12': ['cpc_definition'], 'var_functions.query_db:16': 'file_storage/functions.query_db:16.json', 'var_functions.query_db:18': 'file_storage/functions.query_db:18.json'}

exec(code, env_args)
