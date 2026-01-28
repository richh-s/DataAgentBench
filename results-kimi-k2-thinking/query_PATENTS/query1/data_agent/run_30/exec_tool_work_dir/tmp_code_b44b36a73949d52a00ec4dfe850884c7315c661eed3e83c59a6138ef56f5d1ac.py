code = """import json
import pandas as pd
import re
import numpy as np

# Get the file path from the variable
file_storage_path = locals()['var_functions.query_db:9']

with open(file_storage_path, 'r') as f:
    data = json.load(f)

# Extract CPC codes and publication dates
records = []

for item in data:
    try:
        cpc_json_str = item['cpc']
        pub_date_str = item['publication_date']
        
        # Clean publication date
        clean_date_str = pub_date_str.replace('\x01', '').strip()
        
        # Extract year using regex
        year_match = re.search(r'(\d{4})', clean_date_str)
        if not year_match:
            continue
            
        year = int(year_match.group(1))
        
        # Only consider recent years for EMA calculation
        if year < 2010 or year > 2024:
            continue
            
        # Parse CPC JSON string
        cpc_list = json.loads(cpc_json_str)
        
        # Extract CPC codes
        for cpc_entry in cpc_list:
            code = cpc_entry.get('code', '')
            if code:
                records.append({
                    'cpc_code': code,
                    'year': year
                })
        
    except Exception:
        continue

# Create DataFrame
df = pd.DataFrame(records)

if df.empty:
    print('__RESULT__:')
    print(json.dumps({'error': 'No valid records extracted'}))
    exit()

# Count patent filings by CPC code and year
cpc_year_counts = df.groupby(['cpc_code', 'year']).size().reset_index(name='count')

# Get all years in the dataset
years = sorted(cpc_year_counts['year'].unique())

# Load level 5 CPC codes
level5_file = locals()['var_functions.query_db:38']
with open(level5_file, 'r') as f:
    level5_data = json.load(f)

# Create set of level 5 codes
level5_codes = set([item['symbol'].upper() for item in level5_data])

# Function to extract level 5 code from full CPC code
def extract_level5_code(full_cpc_code):
    code = full_cpc_code.strip().upper()
    match = re.match(r'^([A-Z])(\d{2})([A-Z])', code)
    if match:
        return f"{match.group(1)}{match.group(2)}{match.group(3)}"
    return None

# Filter to level 5 codes
cpc_year_counts_filtered = []
for _, row in cpc_year_counts.iterrows():
    full_code = row['cpc_code']
    level5_code = extract_level5_code(full_code)
    if level5_code and level5_code in level5_codes:
        cpc_year_counts_filtered.append({
            'cpc_code': level5_code,
            'year': int(row['year']),
            'count': int(row['count'])
        })

cpc_year_counts_filtered_df = pd.DataFrame(cpc_year_counts_filtered)

if cpc_year_counts_filtered_df.empty:
    print('__RESULT__:')
    print(json.dumps({'error': 'No level 5 CPC codes found'}))
    exit()

# Aggregate counts by level 5 code
cpc_year_counts_final = cpc_year_counts_filtered_df.groupby(['cpc_code', 'year'])['count'].sum().reset_index()

# Calculate exponential moving average
smoothing_factor = 0.2
results = []

for cpc_code in cpc_year_counts_final['cpc_code'].unique():
    cpc_data = cpc_year_counts_final[cpc_year_counts_final['cpc_code'] == cpc_code]
    
    yearly_counts = []
    for year in years:
        count_row = cpc_data[cpc_data['year'] == year]
        count = int(count_row['count'].iloc[0]) if not count_row.empty else 0
        yearly_counts.append(count)
    
    ema_values = []
    ema = yearly_counts[0] if yearly_counts else 0
    ema_values.append(ema)
    
    for i in range(1, len(yearly_counts)):
        ema = (smoothing_factor * yearly_counts[i]) + ((1 - smoothing_factor) * ema_values[-1])
        ema_values.append(ema)
    
    for i, year in enumerate(years):
        results.append({
            'cpc_code': cpc_code,
            'year': int(year),
            'count': int(yearly_counts[i]),
            'ema': float(ema_values[i])
        })

results_df = pd.DataFrame(results)

# For each year, find CPC codes with highest EMA
yearly_top = []
for year in years:
    year_data = results_df[results_df['year'] == year]
    if not year_data.empty and len(year_data) >= 10:
        top_percentile = float(year_data['ema'].quantile(0.9))
        top_cpc = year_data[year_data['ema'] >= top_percentile]
        for _, row in top_cpc.iterrows():
            yearly_top.append({
                'cpc_code': row['cpc_code'],
                'year': int(row['year']),
                'ema': float(row['ema']),
                'count': int(row['count'])
            })

top_df = pd.DataFrame(yearly_top)

# Find CPC codes where 2022 was their best year
best_year_2022 = []
for cpc_code in top_df['cpc_code'].unique():
    cpc_data = top_df[top_df['cpc_code'] == cpc_code]
    if len(cpc_data) > 0:
        max_ema_idx = cpc_data['ema'].idxmax()
        max_ema_row = cpc_data.loc[max_ema_idx]
        if max_ema_row['year'] == 2022:
            best_year_2022.append(max_ema_row['cpc_code'])

print('__RESULT__:')
print(json.dumps({
    'total_level5_cpc_codes': len(level5_codes),
    'years_analyzed': [int(y) for y in years],
    'level5_cpc_with_patents': len(cpc_year_counts_final['cpc_code'].unique()),
    'top_cpc_per_year': len(top_df),
    'best_year_2022_cpc_codes': sorted(best_year_2022),
    'count_best_2022': len(best_year_2022)
}))"""

env_args = {'var_functions.list_db:0': ['publicationinfo'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json', 'var_functions.query_db:9': 'file_storage/functions.query_db:9.json', 'var_functions.execute_python:12': {'file_path_variable': 'var_functions.query_db:9', 'file_path_value': 'file_storage/functions.query_db:9.json', 'type': "<class 'str'>", 'available_vars': ['var_functions.list_db:0', 'var_functions.query_db:2', 'var_functions.query_db:5', 'var_functions.query_db:9']}, 'var_functions.execute_python:16': {'first_item_keys': ['cpc', 'publication_date'], 'first_item_cpc_preview': '[\n  {\n    "code": "C01B33/00",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "C01B35/00",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code"', 'first_item_pub_date': 'Aug 3rd, 2021', 'total_records': 277813}, 'var_functions.execute_python:20': {'total_processed': 277813, 'success_count': 0, 'error_count': 10000, 'records_extracted': 0, 'first_few_records': []}, 'var_functions.execute_python:22': {'cpc_field_type': "<class 'str'>", 'cpc_field_preview': '[\n  {\n    "code": "C01B33/00",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "C01B35/00",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "H01M10/0565",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "H01M10/0562",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "C01G45/006",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "H01M10/0566",\n  ', 'is_list': False, 'is_string': True}, 'var_functions.execute_python:24': {'success': True, 'cpc_list_length': 38, 'first_cpc_entry': {'code': 'C01B33/00', 'first': False, 'inventive': True, 'tree': []}}, 'var_functions.execute_python:28': {'total_records_processed': 0, 'dataframe_columns': [], 'debug_sample': [{'record_index': 0, 'error': "time data 'Aug \\x01, 2021' does not match format '%b %d, %Y'", 'success': False}, {'record_index': 1, 'error': "time data 'Oct \\x01, 2020' does not match format '%b %d, %Y'", 'success': False}, {'record_index': 2, 'error': "time data 'Sep \\x01, 2021' does not match format '%b %d, %Y'", 'success': False}, {'record_index': 3, 'error': "time data '2020, April \\x01' does not match format '%b %d, %Y'", 'success': False}, {'record_index': 4, 'error': "time data 'Mar \\x01, 2021' does not match format '%b %d, %Y'", 'success': False}, {'record_index': 5, 'error': "time data 'March \\x01, 2021' does not match format '%b %d, %Y'", 'success': False}, {'record_index': 6, 'error': "time data '2021, November \\x01' does not match format '%b %d, %Y'", 'success': False}, {'record_index': 7, 'error': "time data '\\x01 June 2020' does not match format '%b %d, %Y'", 'success': False}, {'record_index': 8, 'error': "time data '2021 on Mar \\x01' does not match format '%b %d, %Y'", 'success': False}, {'record_index': 9, 'error': "time data '\\x01 Nov 2021' does not match format '%b %d, %Y'", 'success': False}], 'sample_records': []}, 'var_functions.query_db:32': [{'symbol': 'A01H', 'level': '5.0'}, {'symbol': 'A01F', 'level': '5.0'}, {'symbol': 'A01C', 'level': '5.0'}, {'symbol': 'A01G', 'level': '5.0'}, {'symbol': 'A23J', 'level': '5.0'}, {'symbol': 'A01N', 'level': '5.0'}, {'symbol': 'A01P', 'level': '5.0'}, {'symbol': 'A01D', 'level': '5.0'}, {'symbol': 'A01L', 'level': '5.0'}, {'symbol': 'A01K', 'level': '5.0'}], 'var_functions.execute_python:36': {'total_records_processed': 2681388, 'unique_cpc_codes': 175852, 'year_range': '1837-2024', 'sample_cpc_codes': ['C01B33/00', 'C01B35/00', 'H01M10/0565', 'H01M10/0562', 'C01G45/006', 'H01M10/0566', 'H01M10/052', 'C01P2002/76', 'Y02E60/10', 'H01M10/0525'], 'sample_years': [1837, 1839, 1841, 1842, 1843, 1844, 1845, 1846, 1847, 1848]}, 'var_functions.query_db:38': 'file_storage/functions.query_db:38.json'}

exec(code, env_args)
