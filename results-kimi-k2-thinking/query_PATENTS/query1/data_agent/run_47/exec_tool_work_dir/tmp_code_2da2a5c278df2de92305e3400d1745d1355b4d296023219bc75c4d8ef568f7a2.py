code = """import json
import pandas as pd
import numpy as np
import re
from datetime import datetime

# Load the yearly counts data
yearly_counts_file = 'yearly_counts.json'
yearly_counts = pd.read_json(yearly_counts_file)

# Focus on recent years (2018-2024) to reduce computation
recent_data = yearly_counts[(yearly_counts['year'] >= 2018) & (yearly_counts['year'] <= 2024)].copy()
print(f"Working with {len(recent_data)} records from {len(recent_data['cpc_code'].unique())} CPC codes (2018-2024)")

# Create a comprehensive year range for each CPC code
all_years = range(2018, 2025)  # 2018 to 2024 inclusive

# Function to calculate EMA efficiently
def calculate_ema_series(values, alpha=0.2):
    if len(values) == 0:
        return np.array([])
    ema = np.zeros(len(values))
    ema[0] = values[0]
    for i in range(1, len(values)):
        ema[i] = alpha * values[i] + (1 - alpha) * ema[i-1]
    return ema

# Only process CPC codes that have 2022 data
codes_with_2022 = recent_data[recent_data['year'] == 2022]['cpc_code'].unique()
print(f"Found {len(codes_with_2022)} CPC codes with 2022 data")

# Process in smaller batches
batch_size = 2000
results_2022 = []
alpha = 0.2

for i in range(0, len(codes_with_2022), batch_size):
    batch_codes = codes_with_2022[i:i+batch_size]
    batch_data = recent_data[recent_data['cpc_code'].isin(batch_codes)]
    
    for cpc_code, group in batch_data.groupby('cpc_code'):
        if len(group) >= 3:  # Need sufficient history
            # Create complete year series
            year_series = pd.Series(index=all_years, dtype=float).fillna(0)
            year_series.update(group.set_index('year')['filings'])
            
            # Calculate EMA
            ema_values = calculate_ema_series(year_series.values, alpha)
            ema_series = pd.Series(ema_values, index=all_years)
            
            # Find best year by EMA
            best_year = ema_series.idxmax()
            max_ema = ema_series.max()
            
            if best_year == 2022:
                results_2022.append({
                    'cpc_code': cpc_code,
                    'ema_2022': float(max_ema)
                })

print(f"Found {len(results_2022)} CPC codes with best year 2022")

# Save results
if results_2022:
    results_df = pd.DataFrame(results_2022)
    
    # Filter for level 5 codes (detailed pattern check)
    level5_pattern = r'^[A-Z][0-9]{2}[A-Z][0-9]+/[0-9]{2}$'
    
    # Check format of winning codes
    winning_codes = results_df['cpc_code'].tolist()
    
    # Filter for level 5 - must have pattern and be likely at proper hierarchy level
    level5_winners = []
    for code in winning_codes:
        if re.match(level5_pattern, code):
            # Additional check: should have numbers before the slash
            before_slash = code.split('/')[0]
            if len(before_slash) >= 6:  # e.g., A01B27 has 6 chars
                level5_winners.append(code)
    
    print(f"Level 5 codes with best year 2022: {len(level5_winners)}")
    
    result = {
        "total_best_2022": len(results_2022),
        "level5_best_2022": len(level5_winners),
        "sample_winners": level5_winners[:20],
        "top_by_ema": sorted(level5_winners[:20], key=lambda x: results_df[results_df['cpc_code'] == x]['ema_2022'].iloc[0] if not results_df[results_df['cpc_code'] == x].empty else 0, reverse=True)
    }
else:
    result = {
        "total_best_2022": 0,
        "message": "No codes found with 2022 as best year"
    }

print("__RESULT__:")
print(json.dumps(result))"""

env_args = {'var_functions.list_db:0': ['publicationinfo'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json', 'var_functions.execute_python:12': {'total_records': 277813, 'sample_keys': ['cpc', 'publication_date'], 'sample_date': 'Aug 3rd, 2021'}, 'var_functions.execute_python:16': {'total_raw_records': 277813, 'parsed_records': 0, 'unique_cpc_codes': 0, 'year_range': '0 to 0', 'sample_cpc': [], 'data_check': False}, 'var_functions.execute_python:18': {'type_first_cpc': "<class 'str'>", 'first_cpc_preview': '[\n  {\n    "code": "C01B33/00",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "C01B35/00",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "H01M10/0565",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "H01', 'is_first_list': False, 'type_second_cpc': "<class 'str'>", 'second_cpc_preview': '[\n  {\n    "code": "F16H47/04",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "F16H37/08",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "F16H47/04",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "F16H4', 'is_second_list': False}, 'var_functions.execute_python:20': {'total_raw_records': 277813, 'parsed_records': 2677930, 'unique_cpc_codes': 175403, 'year_range': '1900 to 2024', 'sample_cpc': ['C01B33/00', 'C01B35/00', 'H01M10/0565', 'H01M10/0562', 'C01G45/006', 'H01M10/0566', 'H01M10/052', 'C01P2002/76', 'Y02E60/10', 'H01M10/0525'], 'data_check': True}, 'var_functions.execute_python:22': {'total_cpc_year_combinations': 917982, 'year_range': '1900 to 2024', 'total_records': 2677930, 'saved_file': 'yearly_counts.json'}, 'var_functions.list_db:26': ['cpc_definition'], 'var_functions.query_db:28': [{'symbol': 'A01H', 'level': '5.0'}, {'symbol': 'A01F', 'level': '5.0'}, {'symbol': 'A01C', 'level': '5.0'}, {'symbol': 'A01G', 'level': '5.0'}, {'symbol': 'A23J', 'level': '5.0'}, {'symbol': 'A01N', 'level': '5.0'}, {'symbol': 'A01P', 'level': '5.0'}, {'symbol': 'A01D', 'level': '5.0'}, {'symbol': 'A01L', 'level': '5.0'}, {'symbol': 'A01K', 'level': '5.0'}], 'var_functions.execute_python:32': {'total_cpc_codes': 175403, 'sample_codes': ['A01B1/00', 'A01B1/02', 'A01B1/022', 'A01B1/026', 'A01B1/028', 'A01B1/04', 'A01B1/06', 'A01B1/065', 'A01B1/08', 'A01B1/14']}, 'var_functions.execute_python:36': {'sample_codes': ['A01B27/00', 'A01B35/16', 'A01B35/20', 'A01B35/26', 'A01B35/28', 'A01B39/06', 'A01B39/085', 'A01B39/18', 'A01B39/22', 'A01B41/06'], 'sample_level5': ['A01B27/00', 'A01B35/16', 'A01B35/20', 'A01B35/26', 'A01B35/28', 'A01B39/06', 'A01B39/18', 'A01B39/22', 'A01B41/06', 'A01B43/00'], 'total_with_2022': 46201}, 'var_functions.list_db:38': ['publicationinfo']}

exec(code, env_args)
