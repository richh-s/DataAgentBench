code = """import json
import re
from collections import defaultdict

# Load the DE 2019 patents data
result_file = locals()['var_functions.query_db:18']
with open(result_file, 'r') as f:
    patents_data = json.load(f)

# Function to extract month from grant date
def parse_grant_date(date_str):
    if not date_str:
        return None
    month_match = re.search(r'(Jan|Feb|Mar|Apr|May|Jun|Jul|Aug|Sep|Oct|Nov|Dec)', date_str, re.IGNORECASE)
    if month_match:
        month_name = month_match.group(1).lower()
        month_map = {
            'jan': 1, 'feb': 2, 'mar': 3, 'apr': 4, 'may': 5, 'jun': 6,
            'jul': 7, 'aug': 8, 'sep': 9, 'oct': 10, 'nov': 11, 'dec': 12
        }
        return month_map.get(month_name, 0)
    return 0

# Extract CPC codes and their frequencies for second half of 2019
cpc_year_counts = defaultdict(int)

for patent in patents_data:
    grant_date = patent.get('grant_date', '')
    month = parse_grant_date(grant_date)
    
    # Only consider second half of 2019
    if month >= 7:
        cpc_field = patent.get('cpc', '[]')
        if cpc_field:
            try:
                cpc_list = json.loads(cpc_field)
                for cpc_item in cpc_list:
                    code = cpc_item.get('code', '')
                    if code:
                        # Extract level 4 CPC (format: Section/Class/Subclass/Group)
                        # For level 4, we want the group level (before the slash)
                        if '/' in code:
                            group_part = code.split('/')[0]
                            # CPC at level 4 has format like H02J7
                            if len(group_part) >= 4:
                                cpc_year_counts[code] += 1
            except:
                continue

# Calculate exponential moving average (smoothing factor 0.1)
# For first year, EMA = actual count
# For subsequent years: EMA_today = (price_today * multiplier) + (EMA_yesterday * (1 - multiplier))

# Group by CPC codes and prepare for EMA calculation
cpc_data = []
for code, count in cpc_year_counts.items():
    # For 2019 (our only year), EMA is just the count
    ema = count
    cpc_data.append({
        'cpc_code': code,
        'year': 2019,
        'count': count,
        'ema': ema
    })

# Sort by EMA descending
cpc_data_sorted = sorted(cpc_data, key=lambda x: x['ema'], reverse=True)

print('__RESULT__:')
print(json.dumps({
    'total_cpc_groups': len(cpc_data_sorted),
    'top_10_cpc': cpc_data_sorted[:10],
    'all_cpc_codes': list(cpc_year_counts.keys())[:20]  # First 20 for reference
}))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json', 'var_functions.query_db:6': 'file_storage/functions.query_db:6.json', 'var_functions.execute_python:12': {'total_records': 68, 'sample_cpc_codes': ['H02J1/10', 'H02J7/34', 'H02J7/007182', 'H02J1/10', 'H02J7/34', 'H02J7/007182'], 'sample_grant_date': '14th Aug 2019'}, 'var_functions.query_db:14': 'file_storage/functions.query_db:14.json', 'var_functions.execute_python:16': {'total_records': 68, 'first_few': [{'Patents_info': 'Patent application (ID DE-102009033309-A) from DE, assigned to CONTINENTAL AUTOMOTIVE GMBH, with pub. number DE-102009033309-B4.', 'grant_date': '14th Aug 2019', 'cpc': '[\n  {\n    "code": "H02J1/10",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "H02J7/34",\n    "first": true,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "H02J7/007182",\n    "first": false,\n    "inventive": false,\n    "tree": []\n  },\n  {\n    "code": "H02J1/10",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "H02J7/34",\n    "first": true,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "H02J7/007182",\n    "first": false,\n    "inventive": false,\n    "tree": []\n  }\n]'}, {'Patents_info': 'Patent application (no. DE-102013211266-A) from DE, assigned to IBM, with publication number DE-102013211266-B4.', 'grant_date': '14th Mar 2019', 'cpc': '[\n  {\n    "code": "G06F9/45533",\n    "first": true,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "G06F9/45533",\n    "first": true,\n    "inventive": true,\n    "tree": []\n  }\n]'}, {'Patents_info': 'The DE application (number DE-102014111322-A) is owned by LEMKE SEBASTIAN and has publication no. DE-102014111322-B4.', 'grant_date': '17th of October, 2019', 'cpc': '[\n  {\n    "code": "B63B21/50",\n    "first": true,\n    "inventive": true,\n    "tree": []\n  }\n]'}]}, 'var_functions.query_db:18': 'file_storage/functions.query_db:18.json', 'var_functions.execute_python:20': {'total_de_2019': 68, 'second_half_2019': 34, 'sample_patent': {'Patents_info': 'In DE, the application (number DE-102007032978-A) is held by HEIDELBERGER DRUCKMASCH AG and has publication number DE-102007032978-B4.', 'grant_date': 'dated 21st November 2019', 'cpc': '[\n  {\n    "code": "B41F21/102",\n    "first": true,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "B41F22/00",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "B41F21/00",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  }\n]'}}}

exec(code, env_args)
