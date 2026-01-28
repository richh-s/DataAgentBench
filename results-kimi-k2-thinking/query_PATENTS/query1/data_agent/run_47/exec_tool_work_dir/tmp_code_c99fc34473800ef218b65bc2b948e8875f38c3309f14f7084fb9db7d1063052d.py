code = """import json
import pandas as pd

# Load the yearly counts data
yearly_counts_file = 'yearly_counts.json'
yearly_counts = pd.read_json(yearly_counts_file)

# Focus on relevant years
recent_data = yearly_counts[(yearly_counts['year'] >= 2018) & (yearly_counts['year'] <= 2024)].copy()

# Get CPC codes with 2022 data
codes_with_2022 = recent_data[recent_data['year'] == 2022]['cpc_code'].unique()

# Calculate EMA efficiently for each code
import numpy as np
import re

alpha = 0.2
all_years = range(2018, 2025)
level5_winners = []

for cpc_code in codes_with_2022:
    group = recent_data[recent_data['cpc_code'] == cpc_code]
    if len(group) >= 3:
        # Create complete year series
        filings_by_year = {row['year']: row['filings'] for _, row in group.iterrows()}
        filings = np.array([filings_by_year.get(year, 0) for year in all_years])
        
        # Calculate EMA
        ema_values = np.zeros(len(filings))
        ema_values[0] = filings[0]
        for i in range(1, len(filings)):
            ema_values[i] = alpha * filings[i] + (1 - alpha) * ema_values[i-1]
        
        # Check if 2022 is the best year (2022 is index 4 in all_years: 2018,2019,2020,2021,2022,2023,2024)
        if 2022 in filings_by_year:
            year_2022_idx = list(all_years).index(2022)
            if np.argmax(ema_values) == year_2022_idx:
                # Check if it's level 5
                if re.match(r'^[A-Z][0-9]{2}[A-Z][0-9]+/[0-9]{2}$', cpc_code):
                    level5_winners.append(cpc_code)

# Save the complete list
output_file = 'level5_cpc_best_2022.json'
with open(output_file, 'w') as f:
    json.dump(level5_winners, f, indent=2)

result = {
    "total_level5_codes": len(level5_winners),
    "first_20_codes": level5_winners[:20],
    "last_20_codes": level5_winners[-20:] if len(level5_winners) > 20 else [],
    "output_file": output_file
}

print("__RESULT__:")
print(json.dumps(result))"""

env_args = {'var_functions.list_db:0': ['publicationinfo'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json', 'var_functions.execute_python:12': {'total_records': 277813, 'sample_keys': ['cpc', 'publication_date'], 'sample_date': 'Aug 3rd, 2021'}, 'var_functions.execute_python:16': {'total_raw_records': 277813, 'parsed_records': 0, 'unique_cpc_codes': 0, 'year_range': '0 to 0', 'sample_cpc': [], 'data_check': False}, 'var_functions.execute_python:18': {'type_first_cpc': "<class 'str'>", 'first_cpc_preview': '[\n  {\n    "code": "C01B33/00",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "C01B35/00",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "H01M10/0565",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "H01', 'is_first_list': False, 'type_second_cpc': "<class 'str'>", 'second_cpc_preview': '[\n  {\n    "code": "F16H47/04",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "F16H37/08",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "F16H47/04",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "F16H4', 'is_second_list': False}, 'var_functions.execute_python:20': {'total_raw_records': 277813, 'parsed_records': 2677930, 'unique_cpc_codes': 175403, 'year_range': '1900 to 2024', 'sample_cpc': ['C01B33/00', 'C01B35/00', 'H01M10/0565', 'H01M10/0562', 'C01G45/006', 'H01M10/0566', 'H01M10/052', 'C01P2002/76', 'Y02E60/10', 'H01M10/0525'], 'data_check': True}, 'var_functions.execute_python:22': {'total_cpc_year_combinations': 917982, 'year_range': '1900 to 2024', 'total_records': 2677930, 'saved_file': 'yearly_counts.json'}, 'var_functions.list_db:26': ['cpc_definition'], 'var_functions.query_db:28': [{'symbol': 'A01H', 'level': '5.0'}, {'symbol': 'A01F', 'level': '5.0'}, {'symbol': 'A01C', 'level': '5.0'}, {'symbol': 'A01G', 'level': '5.0'}, {'symbol': 'A23J', 'level': '5.0'}, {'symbol': 'A01N', 'level': '5.0'}, {'symbol': 'A01P', 'level': '5.0'}, {'symbol': 'A01D', 'level': '5.0'}, {'symbol': 'A01L', 'level': '5.0'}, {'symbol': 'A01K', 'level': '5.0'}], 'var_functions.execute_python:32': {'total_cpc_codes': 175403, 'sample_codes': ['A01B1/00', 'A01B1/02', 'A01B1/022', 'A01B1/026', 'A01B1/028', 'A01B1/04', 'A01B1/06', 'A01B1/065', 'A01B1/08', 'A01B1/14']}, 'var_functions.execute_python:36': {'sample_codes': ['A01B27/00', 'A01B35/16', 'A01B35/20', 'A01B35/26', 'A01B35/28', 'A01B39/06', 'A01B39/085', 'A01B39/18', 'A01B39/22', 'A01B41/06'], 'sample_level5': ['A01B27/00', 'A01B35/16', 'A01B35/20', 'A01B35/26', 'A01B35/28', 'A01B39/06', 'A01B39/18', 'A01B39/22', 'A01B41/06', 'A01B43/00'], 'total_with_2022': 46201}, 'var_functions.list_db:38': ['publicationinfo'], 'var_functions.execute_python:40': {'total_best_2022': 7171, 'level5_best_2022': 2034, 'sample_winners': ['A01B49/04', 'A01B77/00', 'A01D2101/00', 'A01D41/12', 'A01D67/00', 'A01D75/00', 'A01F12/46', 'A01G13/04', 'A01G23/04', 'A01G31/04', 'A01K2227/30', 'A01K2227/70', 'A01K2267/02', 'A01K59/00', 'A01K61/00', 'A01K61/80', 'A01K79/00', 'A01K89/01', 'A01M29/10', 'A01M29/16'], 'top_by_ema': ['A01D2101/00', 'A01K61/80', 'A01K2267/02', 'A01K61/00', 'A01M29/16', 'A01D41/12', 'A01F12/46', 'A01D67/00', 'A01M29/10', 'A01B49/04', 'A01K2227/70', 'A01K89/01', 'A01D75/00', 'A01G23/04', 'A01G13/04', 'A01B77/00', 'A01K2227/30', 'A01G31/04', 'A01K79/00', 'A01K59/00']}}

exec(code, env_args)
