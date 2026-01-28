code = """import json
import pandas as pd
from collections import defaultdict, Counter
import re

# Load data
file_key = 'var_functions.query_db:18'
file_path = locals()[file_key]

with open(file_path, 'r') as f:
    data = json.load(f)

# Extract patent counts per CPC code per year - optimized version
year_pattern = re.compile(r'(\d{4})')

# Only track recent years (2018-2024) and common CPC codes to reduce complexity
patent_counts = defaultdict(lambda: defaultdict(int))
code_frequency = Counter()

for record in data:
    pub_date = record.get('publication_date', '')
    cpc_data = record.get('pc', '')
    
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

# Focus on most frequent CPC codes (top 20% by frequency)
top_n = int(len(code_frequency) * 0.2)
frequent_codes = [code for code, _ in code_frequency.most_common(top_n)]

print('__RESULT__:')
print(json.dumps({
    'total_unique_codes': len(code_frequency),
    'frequent_codes_analyzed': len(frequent_codes),
    'top_codes': [f"{code}: {code_frequency[code]}" for code in frequent_codes[:10]]
}))"""

env_args = {'var_functions.list_db:0': ['publicationinfo'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.execute_python:6': {'total_records': 250551, 'unique_cpc_codes': 97719, 'year_range': '1837 to 2024', 'sample_cpc_codes': ['C01B33/00', 'C01B35/00', 'H01M10/0565', 'H01M10/0562', 'C01G45/006', 'H01M10/0566', 'H01M10/052', 'C01P2002/76', 'Y02E60/10', 'H01M10/0525'], 'has_2022': True}, 'var_functions.list_db:12': ['cpc_definition'], 'var_functions.query_db:16': 'file_storage/functions.query_db:16.json', 'var_functions.query_db:18': 'file_storage/functions.query_db:18.json', 'var_functions.execute_python:20': {'total_cpc_codes': 128707, 'sample_processed': 5000, 'years_range': '2010 to 2024', 'codes_with_best_year_2022': [], 'best_codes_2022_details': []}}

exec(code, env_args)
