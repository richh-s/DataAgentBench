code = """import json
import pandas as pd
from datetime import datetime
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
        
        # Parse publication date to extract year
        date_clean = re.sub(r'(\d+)(st|nd|rd|th)', r'\1', pub_date_str)
        date_obj = datetime.strptime(date_clean, '%b %d, %Y')
        year = date_obj.year
        
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

# Count patent filings by CPC code and year
cpc_year_counts = df.groupby(['cpc_code', 'year']).size().reset_index(name='count')

# Get all years in the dataset
years = sorted(cpc_year_counts['year'].unique())

# For each CPC code, calculate exponential moving average
smoothing_factor = 0.2
results = []

for cpc_code in cpc_year_counts['cpc_code'].unique():
    # Get counts for this CPC code across all years
    cpc_data = cpc_year_counts[cpc_year_counts['cpc_code'] == cpc_code]
    
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
        # Get the top EMA values for this year
        top_cpc = year_data.nlargest(100, 'ema')  # Get top 100 for filtering
        for _, row in top_cpc.iterrows():
            yearly_top.append({
                'cpc_code': row['cpc_code'],
                'year': row['year'],
                'ema': row['ema'],
                'count': row['count']
            })

top_df = pd.DataFrame(yearly_top)

print('__RESULT__:')
print(json.dumps({
    'total_cpc_codes': len(df['cpc_code'].unique()),
    'years': years,
    'total_results': len(results_df),
    'top_results_sample': top_df.head(20).to_dict('records')
}))"""

env_args = {'var_functions.list_db:0': ['publicationinfo'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json', 'var_functions.query_db:9': 'file_storage/functions.query_db:9.json', 'var_functions.execute_python:12': {'file_path_variable': 'var_functions.query_db:9', 'file_path_value': 'file_storage/functions.query_db:9.json', 'type': "<class 'str'>", 'available_vars': ['var_functions.list_db:0', 'var_functions.query_db:2', 'var_functions.query_db:5', 'var_functions.query_db:9']}, 'var_functions.execute_python:16': {'first_item_keys': ['cpc', 'publication_date'], 'first_item_cpc_preview': '[\n  {\n    "code": "C01B33/00",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "C01B35/00",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code"', 'first_item_pub_date': 'Aug 3rd, 2021', 'total_records': 277813}, 'var_functions.execute_python:20': {'total_processed': 277813, 'success_count': 0, 'error_count': 10000, 'records_extracted': 0, 'first_few_records': []}, 'var_functions.execute_python:22': {'cpc_field_type': "<class 'str'>", 'cpc_field_preview': '[\n  {\n    "code": "C01B33/00",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "C01B35/00",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "H01M10/0565",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "H01M10/0562",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "C01G45/006",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "H01M10/0566",\n  ', 'is_list': False, 'is_string': True}, 'var_functions.execute_python:24': {'success': True, 'cpc_list_length': 38, 'first_cpc_entry': {'code': 'C01B33/00', 'first': False, 'inventive': True, 'tree': []}}}

exec(code, env_args)
