code = """import json
import pandas as pd
from datetime import datetime
import re
import numpy as np

# Get the file path from the variable
file_storage_path = locals()['var_functions.query_db:9']

with open(file_storage_path, 'r') as f:
    data = json.load(f)

# Extract CPC codes and publication dates with robust date parsing
records = []

for item in data:
    try:
        cpc_json_str = item['cpc']
        pub_date_str = item['publication_date']
        
        # Clean publication date by removing control characters
        clean_date_str = pub_date_str.replace('\x01', '').strip()
        
        # Extract year using regex - look for 4-digit year
        year_match = re.search(r'(\d{4})', clean_date_str)
        if not year_match:
            continue
            
        year = int(year_match.group(1))
        
        # Only consider recent years for EMA calculation (focus on 2010+)
        if year < 2010:
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
        
    except Exception as e:
        continue

# Create DataFrame
df = pd.DataFrame(records)

# Filter to only include years from 2010-2024
df = df[df['year'] >= 2010]
df = df[df['year'] <= 2024]

# Count patent filings by CPC code and year
cpc_year_counts = df.groupby(['cpc_code', 'year']).size().reset_index(name='count')

# Get all years in the dataset
years = sorted(cpc_year_counts['year'].unique())

# Load level 5 CPC codes from the database
level5_file = locals()['var_functions.query_db:38']
with open(level5_file, 'r') as f:
    level5_data = json.load(f)

# Create set of level 5 codes (convert to uppercase for comparison)
level5_codes = set([item['symbol'].upper() for item in level5_data])

# Filter CPC codes to only include level 5 codes
def extract_level5_code(full_cpc_code):
    """Extract level 5 code from full CPC code"""
    # Level 5 codes are format: A01B, C07D, etc (section + class + first two digits of subclass)
    # Full codes are format: A01B01/00, C07D213/00, etc
    
    # Remove any trailing spaces and convert to uppercase
    code = full_cpc_code.strip().upper()
    
    # Extract section, class, and first two digits of subclass
    # This gives us format like A01B, C07D, H01M
    match = re.match(r'^([A-Z])(\d{2})([A-Z])', code)
    if match:
        return f"{match.group(1)}{match.group(2)}{match.group(3)}"
    
    # If it doesn't match the pattern, return None
    return None

# Filter CPC year counts to only include level 5 codes
cpc_year_counts_filtered = []
for _, row in cpc_year_counts.iterrows():
    full_code = row['cpc_code']
    level5_code = extract_level5_code(full_code)
    if level5_code and level5_code in level5_codes:
        cpc_year_counts_filtered.append({
            'cpc_code': level5_code,
            'year': row['year'],
            'count': row['count']
        })

cpc_year_counts_filtered_df = pd.DataFrame(cpc_year_counts_filtered)

# Group by level 5 code to aggregate counts
if not cpc_year_counts_filtered_df.empty:
    cpc_year_counts_final = cpc_year_counts_filtered_df.groupby(['cpc_code', 'year'])['count'].sum().reset_index()
else:
    cpc_year_counts_final = pd.DataFrame(columns=['cpc_code', 'year', 'count'])

# Calculate exponential moving average for each CPC code
smoothing_factor = 0.2
results = []

for cpc_code in cpc_year_counts_final['cpc_code'].unique():
    # Get counts for this CPC code across all years
    cpc_data = cpc_year_counts_final[cpc_year_counts_final['cpc_code'] == cpc_code]
    
    # Create a complete series for all years, filling missing years with 0
    yearly_counts = []
    for year in years:
        count = cpc_data[cpc_data['year'] == year]['count'].iloc[0] if not cpc_data[cpc_data['year'] == year].empty else 0
        yearly_counts.append(count)
    
    # Calculate exponential moving average
    ema_values = []
    ema = yearly_counts[0] if yearly_counts else 0
    ema_values.append(ema)
    
    for i in range(1, len(yearly_counts)):
        ema = (smoothing_factor * yearly_counts[i]) + ((1 - smoothing_factor) * ema_values[-1])
        ema_values.append(ema)
    
    # Store results for this CPC code
    for i, year in enumerate(years):
        results.append({
            'cpc_code': cpc_code,
            'year': year,
            'count': yearly_counts[i],
            'ema': ema_values[i]
        })

# Create results DataFrame
results_df = pd.DataFrame(results)

# For each year, find CPC codes with highest EMA
yearly_top = []
for year in years:
    year_data = results_df[results_df['year'] == year]
    if not year_data.empty:
        # Get the top EMA values for this year (top 10%)
        top_percentile = year_data['ema'].quantile(0.9)
        top_cpc = year_data[year_data['ema'] >= top_percentile]
        for _, row in top_cpc.iterrows():
            yearly_top.append({
                'cpc_code': row['cpc_code'],
                'year': row['year'],
                'ema': float(row['ema']),
                'count': int(row['count'])
            })

top_df = pd.DataFrame(yearly_top)

# Find CPC codes where 2022 was their best year
best_year_2022 = []
for cpc_code in top_df['cpc_code'].unique():
    cpc_data = top_df[top_df['cpc_code'] == cpc_code]
    if len(cpc_data) > 0:
        # Find the year with maximum EMA for this CPC code
        max_ema_row = cpc_data.loc[cpc_data['ema'].idxmax()]
        if max_ema_row['year'] == 2022:
            best_year_2022.append({
                'cpc_code': cpc_code,
                'ema_2022': max_ema_row['ema'],
                'count_2022': max_ema_row['count']
            })

best_2022_df = pd.DataFrame(best_year_2022)

print('__RESULT__:')
print(json.dumps({
    'total_level5_cpc_codes': len(level5_codes),
    'years_analyzed': years,
    'filtered_cpc_records': len(cpc_year_counts_filtered_df),
    'top_cpc_per_year': len(top_df),
    'best_year_2022_count': len(best_2022_df),
    'sample_best_2022': best_2022_df.head(10).to_dict('records')
}))"""

env_args = {'var_functions.list_db:0': ['publicationinfo'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json', 'var_functions.query_db:9': 'file_storage/functions.query_db:9.json', 'var_functions.execute_python:12': {'file_path_variable': 'var_functions.query_db:9', 'file_path_value': 'file_storage/functions.query_db:9.json', 'type': "<class 'str'>", 'available_vars': ['var_functions.list_db:0', 'var_functions.query_db:2', 'var_functions.query_db:5', 'var_functions.query_db:9']}, 'var_functions.execute_python:16': {'first_item_keys': ['cpc', 'publication_date'], 'first_item_cpc_preview': '[\n  {\n    "code": "C01B33/00",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "C01B35/00",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code"', 'first_item_pub_date': 'Aug 3rd, 2021', 'total_records': 277813}, 'var_functions.execute_python:20': {'total_processed': 277813, 'success_count': 0, 'error_count': 10000, 'records_extracted': 0, 'first_few_records': []}, 'var_functions.execute_python:22': {'cpc_field_type': "<class 'str'>", 'cpc_field_preview': '[\n  {\n    "code": "C01B33/00",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "C01B35/00",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "H01M10/0565",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "H01M10/0562",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "C01G45/006",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "H01M10/0566",\n  ', 'is_list': False, 'is_string': True}, 'var_functions.execute_python:24': {'success': True, 'cpc_list_length': 38, 'first_cpc_entry': {'code': 'C01B33/00', 'first': False, 'inventive': True, 'tree': []}}, 'var_functions.execute_python:28': {'total_records_processed': 0, 'dataframe_columns': [], 'debug_sample': [{'record_index': 0, 'error': "time data 'Aug \\x01, 2021' does not match format '%b %d, %Y'", 'success': False}, {'record_index': 1, 'error': "time data 'Oct \\x01, 2020' does not match format '%b %d, %Y'", 'success': False}, {'record_index': 2, 'error': "time data 'Sep \\x01, 2021' does not match format '%b %d, %Y'", 'success': False}, {'record_index': 3, 'error': "time data '2020, April \\x01' does not match format '%b %d, %Y'", 'success': False}, {'record_index': 4, 'error': "time data 'Mar \\x01, 2021' does not match format '%b %d, %Y'", 'success': False}, {'record_index': 5, 'error': "time data 'March \\x01, 2021' does not match format '%b %d, %Y'", 'success': False}, {'record_index': 6, 'error': "time data '2021, November \\x01' does not match format '%b %d, %Y'", 'success': False}, {'record_index': 7, 'error': "time data '\\x01 June 2020' does not match format '%b %d, %Y'", 'success': False}, {'record_index': 8, 'error': "time data '2021 on Mar \\x01' does not match format '%b %d, %Y'", 'success': False}, {'record_index': 9, 'error': "time data '\\x01 Nov 2021' does not match format '%b %d, %Y'", 'success': False}], 'sample_records': []}, 'var_functions.query_db:32': [{'symbol': 'A01H', 'level': '5.0'}, {'symbol': 'A01F', 'level': '5.0'}, {'symbol': 'A01C', 'level': '5.0'}, {'symbol': 'A01G', 'level': '5.0'}, {'symbol': 'A23J', 'level': '5.0'}, {'symbol': 'A01N', 'level': '5.0'}, {'symbol': 'A01P', 'level': '5.0'}, {'symbol': 'A01D', 'level': '5.0'}, {'symbol': 'A01L', 'level': '5.0'}, {'symbol': 'A01K', 'level': '5.0'}], 'var_functions.execute_python:36': {'total_records_processed': 2681388, 'unique_cpc_codes': 175852, 'year_range': '1837-2024', 'sample_cpc_codes': ['C01B33/00', 'C01B35/00', 'H01M10/0565', 'H01M10/0562', 'C01G45/006', 'H01M10/0566', 'H01M10/052', 'C01P2002/76', 'Y02E60/10', 'H01M10/0525'], 'sample_years': [1837, 1839, 1841, 1842, 1843, 1844, 1845, 1846, 1847, 1848]}, 'var_functions.query_db:38': 'file_storage/functions.query_db:38.json'}

exec(code, env_args)
