code = """import json 
import pandas as pd
import numpy as np

# Load the yearly counts data
yearly_counts_file = 'yearly_counts.json'
yearly_counts = pd.read_json(yearly_counts_file)

# Filter for recent years to focus on relevant data
recent_data = yearly_counts[yearly_counts['year'] >= 2000].copy()

print(f"Processing {len(recent_data)} records from {len(recent_data['cpc_code'].unique())} CPC codes")

# Sort data for EMA calculation
recent_data = recent_data.sort_values(['cpc_code', 'year'])

# Function to calculate EMA
def calculate_ema(filings_series, alpha=0.2):
    if len(filings_series) == 0:
        return np.array([])
    
    ema_values = np.zeros(len(filings_series))
    ema_values[0] = filings_series.iloc[0]  # First value is the EMA
    
    for i in range(1, len(filings_series)):
        ema_values[i] = alpha * filings_series.iloc[i] + (1 - alpha) * ema_values[i-1]
    
    return ema_values

# Process in batches to avoid memory issues
batch_size = 1000
cpc_codes = recent_data['cpc_code'].unique()
results_2022 = []

total_codes = len(cpc_codes)
for i in range(0, total_codes, batch_size):
    batch_codes = cpc_codes[i:i+batch_size]
    batch_data = recent_data[recent_data['cpc_code'].isin(batch_codes)]
    
    # Calculate EMA for each CPC code in batch
    for cpc_code, group in batch_data.groupby('cpc_code'):
        if len(group) >= 3:  # Need at least 3 years of data
            filings_series = group.set_index('year')['filings']
            
            # Reindex to ensure all years are present
            all_years = range(group['year'].min(), group['year'].max() + 1)
            filings_series = filings_series.reindex(all_years, fill_value=0)
            
            # Calculate EMA
            ema_values = calculate_ema(filings_series, alpha=0.2)
            
            # Create results dataframe for this CPC code
            cpc_results = pd.DataFrame({
                'year': all_years,
                'cpc_code': cpc_code,
                'filings': filings_series.values,
                'ema': ema_values
            })
            
            # Find best year
            best_year_idx = cpc_results['ema'].idxmax()
            best_year = cpc_results.loc[best_year_idx, 'year']
            
            if best_year == 2022:
                results_2022.append({
                    'cpc_code': cpc_code,
                    'ema_2022': cpc_results.loc[best_year_idx, 'ema'],
                    'total_years': len(group)
                })

# Create results dataframe
results_df = pd.DataFrame(results_2022)

if not results_df.empty:
    # Filter for level 5 CPC codes (format like A01B1/02)
    # Level 5 typically has pattern: letters + numbers + / + exactly 2 digits
    # where the second digit is often 0 for main groups
    pattern = r'^[A-Z][0-9]{2}[A-Z][0-9]+/[0-9]{2}$'
    
    # Look at the format of our winning codes
    winning_codes = results_df['cpc_code'].tolist()
    sample_codes = winning_codes[:20]
    
    result = {
        "total_best_2022": len(results_df),
        "sample_winning_codes": sample_codes,
        "ema_range": f"{results_df['ema_2022'].min():.2f} to {results_df['ema_2022'].max():.2f}"
    }
else:
    result = {
        "total_best_2022": 0,
        "message": "No CPC codes found with best year 2022"
    }

print("__RESULT__:")
print(json.dumps(result))"""

env_args = {'var_functions.list_db:0': ['publicationinfo'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json', 'var_functions.execute_python:12': {'total_records': 277813, 'sample_keys': ['cpc', 'publication_date'], 'sample_date': 'Aug 3rd, 2021'}, 'var_functions.execute_python:16': {'total_raw_records': 277813, 'parsed_records': 0, 'unique_cpc_codes': 0, 'year_range': '0 to 0', 'sample_cpc': [], 'data_check': False}, 'var_functions.execute_python:18': {'type_first_cpc': "<class 'str'>", 'first_cpc_preview': '[\n  {\n    "code": "C01B33/00",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "C01B35/00",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "H01M10/0565",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "H01', 'is_first_list': False, 'type_second_cpc': "<class 'str'>", 'second_cpc_preview': '[\n  {\n    "code": "F16H47/04",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "F16H37/08",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "F16H47/04",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "F16H4', 'is_second_list': False}, 'var_functions.execute_python:20': {'total_raw_records': 277813, 'parsed_records': 2677930, 'unique_cpc_codes': 175403, 'year_range': '1900 to 2024', 'sample_cpc': ['C01B33/00', 'C01B35/00', 'H01M10/0565', 'H01M10/0562', 'C01G45/006', 'H01M10/0566', 'H01M10/052', 'C01P2002/76', 'Y02E60/10', 'H01M10/0525'], 'data_check': True}, 'var_functions.execute_python:22': {'total_cpc_year_combinations': 917982, 'year_range': '1900 to 2024', 'total_records': 2677930, 'saved_file': 'yearly_counts.json'}, 'var_functions.list_db:26': ['cpc_definition'], 'var_functions.query_db:28': [{'symbol': 'A01H', 'level': '5.0'}, {'symbol': 'A01F', 'level': '5.0'}, {'symbol': 'A01C', 'level': '5.0'}, {'symbol': 'A01G', 'level': '5.0'}, {'symbol': 'A23J', 'level': '5.0'}, {'symbol': 'A01N', 'level': '5.0'}, {'symbol': 'A01P', 'level': '5.0'}, {'symbol': 'A01D', 'level': '5.0'}, {'symbol': 'A01L', 'level': '5.0'}, {'symbol': 'A01K', 'level': '5.0'}], 'var_functions.execute_python:32': {'total_cpc_codes': 175403, 'sample_codes': ['A01B1/00', 'A01B1/02', 'A01B1/022', 'A01B1/026', 'A01B1/028', 'A01B1/04', 'A01B1/06', 'A01B1/065', 'A01B1/08', 'A01B1/14']}}

exec(code, env_args)
