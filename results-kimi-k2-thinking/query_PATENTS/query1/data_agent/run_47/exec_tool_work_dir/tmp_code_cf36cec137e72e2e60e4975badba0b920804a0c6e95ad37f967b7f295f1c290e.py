code = """import json
import pandas as pd
import numpy as np
import re

# Load the yearly counts data
yearly_counts_file = 'yearly_counts.json'
yearly_counts = pd.read_json(yearly_counts_file)

# Focus on recent years
recent_data = yearly_counts[(yearly_counts['year'] >= 2018) & (yearly_counts['year'] <= 2024)].copy()

# Pre-filter for level 5 CPC codes
level5_pattern = r'^[A-Z][0-9]{2}[A-Z][0-9]+/[0-9]{2}$'
all_cpc_codes = recent_data['cpc_code'].unique()
level5_codes = [code for code in all_cpc_codes if re.match(level5_pattern, code) and code.count('/') == 1]

# Filter to level 5 codes only
level5_data = recent_data[recent_data['cpc_code'].isin(level5_codes)]

# Get codes with 2022 data
codes_with_2022 = level5_data[level5_data['year'] == 2022]['cpc_code'].unique()

# Process all codes efficiently
all_years = [2018, 2019, 2020, 2021, 2022, 2023, 2024]
year_2022_idx = 4
alpha = 0.2

level5_winners = []

count_total = len(codes_with_2022)
print(f"Processing {count_total} CPC codes...")

for idx, cpc_code in enumerate(codes_with_2022):
    group = level5_data[level5_data['cpc_code'] == cpc_code]
    if len(group) >= 3:
        filings_dict = dict(zip(group['year'], group['filings']))
        
        # Calculate EMA for all years efficiently
        ema = filings_dict.get(2018, 0)
        max_ema = ema
        max_year_idx = 0
        
        for year_idx, year in enumerate(all_years):
            filing = filings_dict.get(year, 0)
            # EMA calculation
            ema = alpha * filing + (1 - alpha) * ema
            
            if ema > max_ema:
                max_ema = ema
                max_year_idx = year_idx
        
        if max_year_idx == year_2022_idx:
            level5_winners.append(cpc_code)

# Sort for consistent output
level5_winners.sort()

# Output in the required format
result = {
    "cpc_level5_codes_best_2022": level5_winners
}

print("__RESULT__:")
print(json.dumps(result))"""

env_args = {'var_functions.list_db:0': ['publicationinfo'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json', 'var_functions.execute_python:12': {'total_records': 277813, 'sample_keys': ['cpc', 'publication_date'], 'sample_date': 'Aug 3rd, 2021'}, 'var_functions.execute_python:16': {'total_raw_records': 277813, 'parsed_records': 0, 'unique_cpc_codes': 0, 'year_range': '0 to 0', 'sample_cpc': [], 'data_check': False}, 'var_functions.execute_python:18': {'type_first_cpc': "<class 'str'>", 'first_cpc_preview': '[\n  {\n    "code": "C01B33/00",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "C01B35/00",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "H01M10/0565",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "H01', 'is_first_list': False, 'type_second_cpc': "<class 'str'>", 'second_cpc_preview': '[\n  {\n    "code": "F16H47/04",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "F16H37/08",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "F16H47/04",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "F16H4', 'is_second_list': False}, 'var_functions.execute_python:20': {'total_raw_records': 277813, 'parsed_records': 2677930, 'unique_cpc_codes': 175403, 'year_range': '1900 to 2024', 'sample_cpc': ['C01B33/00', 'C01B35/00', 'H01M10/0565', 'H01M10/0562', 'C01G45/006', 'H01M10/0566', 'H01M10/052', 'C01P2002/76', 'Y02E60/10', 'H01M10/0525'], 'data_check': True}, 'var_functions.execute_python:22': {'total_cpc_year_combinations': 917982, 'year_range': '1900 to 2024', 'total_records': 2677930, 'saved_file': 'yearly_counts.json'}, 'var_functions.list_db:26': ['cpc_definition'], 'var_functions.query_db:28': [{'symbol': 'A01H', 'level': '5.0'}, {'symbol': 'A01F', 'level': '5.0'}, {'symbol': 'A01C', 'level': '5.0'}, {'symbol': 'A01G', 'level': '5.0'}, {'symbol': 'A23J', 'level': '5.0'}, {'symbol': 'A01N', 'level': '5.0'}, {'symbol': 'A01P', 'level': '5.0'}, {'symbol': 'A01D', 'level': '5.0'}, {'symbol': 'A01L', 'level': '5.0'}, {'symbol': 'A01K', 'level': '5.0'}], 'var_functions.execute_python:32': {'total_cpc_codes': 175403, 'sample_codes': ['A01B1/00', 'A01B1/02', 'A01B1/022', 'A01B1/026', 'A01B1/028', 'A01B1/04', 'A01B1/06', 'A01B1/065', 'A01B1/08', 'A01B1/14']}, 'var_functions.execute_python:36': {'sample_codes': ['A01B27/00', 'A01B35/16', 'A01B35/20', 'A01B35/26', 'A01B35/28', 'A01B39/06', 'A01B39/085', 'A01B39/18', 'A01B39/22', 'A01B41/06'], 'sample_level5': ['A01B27/00', 'A01B35/16', 'A01B35/20', 'A01B35/26', 'A01B35/28', 'A01B39/06', 'A01B39/18', 'A01B39/22', 'A01B41/06', 'A01B43/00'], 'total_with_2022': 46201}, 'var_functions.list_db:38': ['publicationinfo'], 'var_functions.execute_python:40': {'total_best_2022': 7171, 'level5_best_2022': 2034, 'sample_winners': ['A01B49/04', 'A01B77/00', 'A01D2101/00', 'A01D41/12', 'A01D67/00', 'A01D75/00', 'A01F12/46', 'A01G13/04', 'A01G23/04', 'A01G31/04', 'A01K2227/30', 'A01K2227/70', 'A01K2267/02', 'A01K59/00', 'A01K61/00', 'A01K61/80', 'A01K79/00', 'A01K89/01', 'A01M29/10', 'A01M29/16'], 'top_by_ema': ['A01D2101/00', 'A01K61/80', 'A01K2267/02', 'A01K61/00', 'A01M29/16', 'A01D41/12', 'A01F12/46', 'A01D67/00', 'A01M29/10', 'A01B49/04', 'A01K2227/70', 'A01K89/01', 'A01D75/00', 'A01G23/04', 'A01G13/04', 'A01B77/00', 'A01K2227/30', 'A01G31/04', 'A01K79/00', 'A01K59/00']}, 'var_functions.execute_python:48': {'cpc_level5_codes_best_2022': ['A01B49/04', 'A01B77/00', 'A01D2101/00', 'A01D41/12', 'A01D67/00', 'A01D75/00', 'A01F12/46', 'A01G13/04', 'A01G23/04', 'A01G3/08', 'A01G31/04', 'A01G5/04', 'A01G7/00', 'A01G7/04', 'A01G9/12', 'A01G9/14', 'A01G9/16', 'A01G9/20', 'A01K2227/30', 'A01K2227/70', 'A01K2267/02', 'A01K59/00', 'A01K61/00', 'A01K61/80', 'A01K79/00', 'A01K89/01', 'A01M1/04', 'A01M29/10', 'A01M29/16', 'A01M29/22', 'A01N25/04', 'A01N25/08', 'A01N37/24', 'A01N39/04', 'A01N43/40', 'A01N43/54', 'A01N43/66', 'A01N43/70', 'A01N43/88', 'A01N47/14', 'A01N47/44', 'A01N63/22', 'A01N63/28', 'A23B4/06', 'A23B7/02', 'A23F3/18', 'A23G3/02', 'A23J1/00', 'A23K10/14', 'A23K20/24', 'A23K40/00', 'A23K40/25', 'A23L11/05', 'A23L13/00', 'A23L17/40', 'A23L17/65', 'A23L19/03', 'A23L2/04', 'A23L2/66', 'A23L27/50', 'A23L29/03', 'A23L29/20', 'A23L3/40', 'A23L33/12', 'A23L33/14', 'A23L33/17', 'A23L33/22', 'A23L5/17', 'A23L5/41', 'A23L7/00', 'A23N12/02', 'A23P20/10', 'A24B3/04', 'A24D1/22', 'A24F40/00', 'A24F40/65', 'A24F47/00', 'A41B2500/10', 'A41B2500/50', 'A41B9/12', 'A41D1/00', 'A41D1/06', 'A41D13/05', 'A41D19/04', 'A41D2200/10', 'A41D2400/12', 'A41D2600/10', 'A41D2600/20', 'A41D27/00', 'A41D3/00', 'A41D31/00', 'A41H43/02', 'A43B13/14', 'A43B13/18', 'A43B13/20', 'A43B13/32', 'A43B13/38', 'A43B17/14', 'A43B3/38', 'A43B3/44'], 'total_found': 100}}

exec(code, env_args)
