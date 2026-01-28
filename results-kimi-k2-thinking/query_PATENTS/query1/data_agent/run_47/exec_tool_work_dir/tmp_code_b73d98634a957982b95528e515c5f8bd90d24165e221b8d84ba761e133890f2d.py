code = """import json
import pandas as pd

# Load the yearly counts data from previous step
yearly_counts_file = 'yearly_counts.json'
yearly_counts = pd.read_json(yearly_counts_file)

# Calculate exponential moving average for each CPC code
def calculate_ema(group, alpha=0.2):
    # Sort by year
    group = group.sort_values('year')
    # Initialize EMA
    ema_values = []
    ema = None
    
    for _, row in group.iterrows():
        filings = row['filings']
        if ema is None:
            ema = filings  # First value is the EMA
        else:
            ema = alpha * filings + (1 - alpha) * ema
        ema_values.append(ema)
    
    group['ema'] = ema_values
    return group

# Calculate EMA for each CPC code
ema_data = yearly_counts.groupby('cpc_code').apply(calculate_ema, alpha=0.2).reset_index(drop=True)

# Find the best year (highest EMA) for each CPC code
best_years = ema_data.loc[ema_data.groupby('cpc_code')['ema'].idxmax()]

# Filter for those whose best year is 2022
cpc_best_2022 = best_years[best_years['year'] == 2022]

result = {
    "total_cpc_codes": len(yearly_counts['cpc_code'].unique()),
    "codes_with_2022_best": len(cpc_best_2022),
    "sample_codes": cpc_best_2022['cpc_code'].head(10).tolist()
}

print("__RESULT__:")
print(json.dumps(result))"""

env_args = {'var_functions.list_db:0': ['publicationinfo'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json', 'var_functions.execute_python:12': {'total_records': 277813, 'sample_keys': ['cpc', 'publication_date'], 'sample_date': 'Aug 3rd, 2021'}, 'var_functions.execute_python:16': {'total_raw_records': 277813, 'parsed_records': 0, 'unique_cpc_codes': 0, 'year_range': '0 to 0', 'sample_cpc': [], 'data_check': False}, 'var_functions.execute_python:18': {'type_first_cpc': "<class 'str'>", 'first_cpc_preview': '[\n  {\n    "code": "C01B33/00",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "C01B35/00",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "H01M10/0565",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "H01', 'is_first_list': False, 'type_second_cpc': "<class 'str'>", 'second_cpc_preview': '[\n  {\n    "code": "F16H47/04",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "F16H37/08",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "F16H47/04",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "F16H4', 'is_second_list': False}, 'var_functions.execute_python:20': {'total_raw_records': 277813, 'parsed_records': 2677930, 'unique_cpc_codes': 175403, 'year_range': '1900 to 2024', 'sample_cpc': ['C01B33/00', 'C01B35/00', 'H01M10/0565', 'H01M10/0562', 'C01G45/006', 'H01M10/0566', 'H01M10/052', 'C01P2002/76', 'Y02E60/10', 'H01M10/0525'], 'data_check': True}, 'var_functions.execute_python:22': {'total_cpc_year_combinations': 917982, 'year_range': '1900 to 2024', 'total_records': 2677930, 'saved_file': 'yearly_counts.json'}}

exec(code, env_args)
