code = """import json
import pandas as pd
from collections import defaultdict, Counter
import re

# Load data
file_key = 'var_functions.query_db:18'
file_path = locals()[file_key]

with open(file_path, 'r') as f:
    data = json.load(f)

# Extract patent counts per CPC code per year - fix the typo
year_pattern = re.compile(r'(\d{4})')

# Track recent years (2018-2024) and count CPC codes
patent_counts = defaultdict(lambda: defaultdict(int))
code_frequency = Counter()

for record in data:
    pub_date = record.get('publication_date', '')
    cpc_data = record.get('cpc', '')  # Fixed typo here
    
    if pub_date and cpc_data and str(pub_date) != 'None':
        year_match = year_pattern.search(str(pub_date))
        if year_match:
            year = int(year_match.group(1))
            if 2018 <= year <= 2024:
                try:
                    cpc_list = json.loads(cpc_data)
                    for cpc_entry in cpc_list:
                        if isinstance(cpc_entry, dict) and 'code' in cpc_entry:
                            code = str(cpc_entry['code'])
                            if '/' in code:
                                patent_counts[code][year] += 1
                                code_frequency[code] += 1
                except:
                    continue

# Focus on most frequent CPC codes
top_n = min(2000, len(code_frequency))  # Limit to top 2000
top_codes = [code for code, _ in code_frequency.most_common(top_n)]

# Calculate EMA with smoothing factor 0.2
alpha = 0.2
ema_results = []

for cpc_code in top_codes:
    years_data = patent_counts[cpc_code]
    if len(years_data) >= 2:  # Need at least 2 years
        sorted_years = sorted(years_data.items())
        ema_prev = sorted_years[0][1]
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

# For each year 2018-2024, find which CPC code has the highest EMA
best_ema_per_year = {}
for year in range(2018, 2025):
    year_data = ema_df[ema_df['year'] == year]
    if not year_data.empty:
        max_idx = year_data['ema'].idxmax()
        best_row = year_data.loc[max_idx]
        best_ema_per_year[year] = {
            'cpc_code': best_row['cpc_code'],
            'ema': float(best_row['ema']),
            'count': int(best_row['count'])
        }

# For each CPC code that was EVER the best, find its overall best year
codes_and_their_best = []
for cpc_code in set([info['cpc_code'] for info in best_ema_per_year.values()]):
    code_data = ema_df[ema_df['cpc_code'] == cpc_code]
    if not code_data.empty:
        max_idx = code_data['ema'].idxmax()
        best_row = code_data.loc[max_idx]
        codes_and_their_best.append({
            'cpc_code': cpc_code,
            'best_year': int(best_row['year']),
            'best_ema': float(best_row['ema']),
            'best_count': int(best_row['count'])
        })

codes_best_df = pd.DataFrame(codes_and_their_best)

# Filter for CPC codes whose best year is 2022
codes_best_in_2022 = codes_best_df[codes_best_df['best_year'] == 2022]

result = {
    'total_cpc_codes_tracked': len(code_frequency),
    'top_codes_analyzed': len(top_codes),
    'best_ema_codes_by_year': best_ema_per_year,
    'codes_whose_best_year_is_2022': codes_best_in_2022['cpc_code'].tolist(),
    'details_2022': codes_best_in_2022.to_dict('records')
}

print('__RESULT__:')
print(json.dumps(result, indent=2))"""

env_args = {'var_functions.list_db:0': ['publicationinfo'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.execute_python:6': {'total_records': 250551, 'unique_cpc_codes': 97719, 'year_range': '1837 to 2024', 'sample_cpc_codes': ['C01B33/00', 'C01B35/00', 'H01M10/0565', 'H01M10/0562', 'C01G45/006', 'H01M10/0566', 'H01M10/052', 'C01P2002/76', 'Y02E60/10', 'H01M10/0525'], 'has_2022': True}, 'var_functions.list_db:12': ['cpc_definition'], 'var_functions.query_db:16': 'file_storage/functions.query_db:16.json', 'var_functions.query_db:18': 'file_storage/functions.query_db:18.json', 'var_functions.execute_python:20': {'total_cpc_codes': 128707, 'sample_processed': 5000, 'years_range': '2010 to 2024', 'codes_with_best_year_2022': [], 'best_codes_2022_details': []}, 'var_functions.execute_python:22': {'total_unique_codes': 0, 'frequent_codes_analyzed': 0, 'top_codes': []}}

exec(code, env_args)
