code = """import json
import pandas as pd
from collections import defaultdict, Counter
import re

# Load data
file_key = 'var_functions.query_db:18'
file_path = locals()[file_key]

with open(file_path, 'r') as f:
    data = json.load(f)

# Extract patent counts per CPC code per year - comprehensive analysis
year_pattern = re.compile(r'(\d{4})')

# Track all years 2010-2024
patent_counts = defaultdict(lambda: defaultdict(int))

for record in data:
    pub_date = record.get('publication_date', '')
    cpc_data = record.get('cpc', '')
    
    if pub_date and cpc_data and str(pub_date) != 'None':
        year_match = year_pattern.search(str(pub_date))
        if year_match:
            year = int(year_match.group(1))
            if 2010 <= year <= 2024:
                try:
                    cpc_list = json.loads(cpc_data)
                    for cpc_entry in cpc_list:
                        if isinstance(cpc_entry, dict) and 'code' in cpc_entry:
                            code = str(cpc_entry['code'])
                            if '/' in code:  # All level 5 CPC codes have /
                                patent_counts[code][year] += 1
                except:
                    continue

# For each CPC code, calculate EMA and find its best year
alpha = 0.2
cpc_best_years = []

for cpc_code, years_data in patent_counts.items():
    if len(years_data) >= 3:  # At least 3 years of data
        sorted_years = sorted(years_data.items())
        
        # Calculate EMA
        ema_prev = sorted_years[0][1]  # First year as initial EMA
        best_year = sorted_years[0][0]
        best_ema = ema_prev
        best_count = ema_prev
        
        for year, count in sorted_years[1:]:
            ema_current = alpha * count + (1 - alpha) * ema_prev
            if ema_current > best_ema:
                best_year = year
                best_ema = ema_current
                best_count = count
            ema_prev = ema_current
        
        # Store result if best year is 2022
        if best_year == 2022:
            cpc_best_years.append({
                'cpc_code': cpc_code,
                'best_ema': round(best_ema, 2),
                'best_count': int(best_count)
            })

# Sort by EMA value (descending)
cpc_best_years.sort(key=lambda x: x['best_ema'], reverse=True)

result = {
    'cpc_codes_best_year_2022': [item['cpc_code'] for item in cpc_best_years],
    'total_codes': len(cpc_best_years),
    'details': cpc_best_years[:50]  # Top 50 for verification
}

print('__RESULT__:')
print(json.dumps(result, indent=2))"""

env_args = {'var_functions.list_db:0': ['publicationinfo'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.execute_python:6': {'total_records': 250551, 'unique_cpc_codes': 97719, 'year_range': '1837 to 2024', 'sample_cpc_codes': ['C01B33/00', 'C01B35/00', 'H01M10/0565', 'H01M10/0562', 'C01G45/006', 'H01M10/0566', 'H01M10/052', 'C01P2002/76', 'Y02E60/10', 'H01M10/0525'], 'has_2022': True}, 'var_functions.list_db:12': ['cpc_definition'], 'var_functions.query_db:16': 'file_storage/functions.query_db:16.json', 'var_functions.query_db:18': 'file_storage/functions.query_db:18.json', 'var_functions.execute_python:20': {'total_cpc_codes': 128707, 'sample_processed': 5000, 'years_range': '2010 to 2024', 'codes_with_best_year_2022': [], 'best_codes_2022_details': []}, 'var_functions.execute_python:22': {'total_unique_codes': 0, 'frequent_codes_analyzed': 0, 'top_codes': []}, 'var_functions.execute_python:24': {'total_cpc_codes_tracked': 102927, 'top_codes_analyzed': 2000, 'best_ema_codes_by_year': {'2018': {'cpc_code': 'Y02E60/10', 'ema': 269.0, 'count': 269}, '2019': {'cpc_code': 'A61P35/00', 'ema': 257.8, 'count': 241}, '2020': {'cpc_code': 'A61P35/00', 'ema': 270.64, 'count': 322}, '2021': {'cpc_code': 'Y02E60/10', 'ema': 298.84800000000007, 'count': 428}, '2022': {'cpc_code': 'A61P35/00', 'ema': 333.56960000000004, 'count': 473}, '2023': {'cpc_code': 'Y02E60/10', 'ema': 351.02272000000005, 'count': 466}, '2024': {'cpc_code': 'Y02E60/10', 'ema': 323.81817600000005, 'count': 215}}, 'codes_whose_best_year_is_2022': ['A61P35/00'], 'details_2022': [{'cpc_code': 'A61P35/00', 'best_year': 2022, 'best_ema': 333.56960000000004, 'best_count': 473}]}}

exec(code, env_args)
