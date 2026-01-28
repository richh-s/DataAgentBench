code = """import json
import re
from collections import defaultdict, Counter

# Load the data
file_path = locals()['var_functions.query_db:14']
if isinstance(file_path, str) and file_path.endswith('.json'):
    with open(file_path, 'r') as f:
        patents_2019 = json.load(f)
else:
    patents_2019 = file_path

# Function to extract month from grant_date
def extract_month(grant_date):
    if not grant_date:
        return None
    month_patterns = [
        r'(Jan|Feb|Mar|Apr|May|Jun|Jul|Aug|Sep|Oct|Nov|Dec)[a-z]*',
        r'(January|February|March|April|May|June|July|August|September|October|November|December)'
    ]
    for pattern in month_patterns:
        match = re.search(pattern, grant_date, re.IGNORECASE)
        if match:
            month_str = match.group(1).lower()
            month_map = {
                'jan': 1, 'feb': 2, 'mar': 3, 'apr': 4, 'may': 5, 'jun': 6,
                'jul': 7, 'aug': 8, 'sep': 9, 'oct': 10, 'nov': 11, 'dec': 12,
                'january': 1, 'february': 2, 'march': 3, 'april': 4, 'may': 5, 'june': 6,
                'july': 7, 'august': 8, 'september': 9, 'october': 10, 'november': 11, 'december': 12
            }
            return month_map.get(month_str)
    return None

# Function to extract CPC level 4 group (format: SectionClassSubclass/Group)
def get_cpc_level_4(code):
    if not code:
        return None
    # CPC codes look like "G06F9/45533" - we want level 4 = "G06F9/45"
    parts = code.split('/')
    if len(parts) != 2:
        return None
    
    section_class_subclass = parts[0]  # G06F9
    subgroup = parts[1]  # 45533
    
    # Extract first 2 digits of subgroup for level 4
    if len(subgroup) >= 2:
        level4_group = section_class_subclass + '/' + subgroup[:2]
        return level4_group
    return None

# Parse CPC codes from JSON string
def parse_cpc_codes(cpc_json):
    if not cpc_json:
        return []
    try:
        # Clean up the JSON string
        cpc_list = json.loads(cpc_json)
        return [item.get('code') for item in cpc_list if item.get('code')]
    except:
        return []

# Filter for German patents in second half of 2019
german_patents = []
for patent in patents_2019:
    grant_date = patent.get('grant_date', '')
    patents_info = patent.get('Patents_info', '')
    cpc_data = patent.get('cpc', '')
    
    month = extract_month(grant_date)
    if month and month >= 7:  # Second half: July to December
        if 'from DE' in patents_info or 'DE-' in patents_info:
            cpc_codes = parse_cpc_codes(cpc_data)
            if cpc_codes:
                german_patents.append({
                    'grant_date': grant_date,
                    'patents_info': patents_info,
                    'cpc_codes': cpc_codes
                })

# Count CPC level 4 groups by year
cpc_year_counts = defaultdict(lambda: defaultdict(int))
years = ['2019']  # We're only looking at 2019 data
year = '2019'

for patent in german_patents:
    for code in patent['cpc_codes']:
        level4 = get_cpc_level_4(code)
        if level4:
            cpc_year_counts[level4][year] += 1

# Calculate Exponential Moving Average (EMA) with smoothing factor 0.1
# EMA_t = alpha * value_t + (1-alpha) * EMA_{t-1}
alpha = 0.1
cpc_ema = {}

for cpc_group in cpc_year_counts:
    # For 2019, since we only have one year, EMA = count
    count = cpc_year_counts[cpc_group]['2019']
    cpc_ema[cpc_group] = {'2019': count}

# Sort CPC groups by EMA value
cpc_ranking = sorted(cpc_ema.items(), key=lambda x: x[1]['2019'], reverse=True)

# Get top CPC groups
top_cpc_groups = cpc_ranking[:10]  # Top 10 for now
result = {
    'german_patents_found': len(german_patents),
    'top_cpc_groups': top_cpc_groups
}

# Prepare output for PRINT FORMAT
output_data = {
    'total_german_patents_2019_second_half': len(german_patents),
    'top_cpc_by_ema': [],
    'note': 'Need to join with CPC definition table for full titles'
}

for i, (cpc_group, ema_data) in enumerate(top_cpc_groups):
    output_data['top_cpc_by_ema'].append({
        'rank': i + 1,
        'cpc_level4_code': cpc_group,
        'patent_count_2019': ema_data['2019'],
        'ema_2019': ema_data['2019'],
        'best_year': '2019'
    })

# Print in required format
print('__RESULT__:')
print(json.dumps(output_data, indent=2))"""

env_args = {'var_functions.list_db:0': ['publicationinfo'], 'var_functions.query_db:2': [{'grant_date': '14th Mar 2019', 'Patents_info': 'Patent application (no. DE-102013211266-A) from DE, assigned to IBM, with publication number DE-102013211266-B4.', 'cpc': '[\n  {\n    "code": "G06F9/45533",\n    "first": true,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "G06F9/45533",\n    "first": true,\n    "inventive": true,\n    "tree": []\n  }\n]'}, {'grant_date': 'Mar 19th, 2019', 'Patents_info': 'In RU, the patent filing (app. number RU-2017142236-A) is held by Sletov Aleksandr Anatolevich and has publication no. RU-2682615-C1.', 'cpc': '[\n  {\n    "code": "A61D1/00",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "A61B17/645",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "A61B17/6425",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "A61B17/64",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "A61B17/60",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "A61B17/58",\n    "first": true,\n    "inventive": true,\n    "tree": []\n  }\n]'}, {'grant_date': 'Mar 12th, 2019', 'Patents_info': 'The RU patent application (number RU-2018105657-A) is held by OBSHCHESTVO S OGRANICHENNOJ OTVETSTVENNOSTYU VORMKHOLS VNEDRENIE and has publication no. RU-2681783-C1.', 'cpc': '[\n  {\n    "code": "E21B33/136",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "E21B33/134",\n    "first": true,\n    "inventive": true,\n    "tree": []\n  }\n]'}, {'grant_date': '2019 on Jul 12th', 'Patents_info': 'Application (no. RU-2018119076-A) from RU, assigned to FEDERALNOE GOSUDARSTVENNOE KAZENNOE VOENNOE OBRAZOVATELNOE UCHREZHDENIE VYSSHEGO OBRAZOVANIYA VOENNA, with publication no. RU-2694421-C1.', 'cpc': '[\n  {\n    "code": "G01S13/42",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "G01S5/18",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "F41G3/00",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "F41H13/00",\n    "first": true,\n    "inventive": true,\n    "tree": []\n  }\n]'}, {'grant_date': 'on March 14th, 2019', 'Patents_info': 'Patent application (number RU-2016134259-A) from RU, owned by KVINETIK LTD, with publication number RU-2681957-C2.', 'cpc': '[\n  {\n    "code": "G01S19/30",\n    "first": true,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "G01S19/30",\n    "first": true,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "G01S19/30",\n    "first": true,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "G01S19/37",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "G01S19/30",\n    "first": true,\n    "inventive": true,\n    "tree": []\n  }\n]'}], 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json', 'var_functions.list_db:8': ['cpc_definition'], 'var_functions.query_db:10': 'file_storage/functions.query_db:10.json', 'var_functions.query_db:12': 'file_storage/functions.query_db:12.json', 'var_functions.query_db:14': 'file_storage/functions.query_db:14.json'}

exec(code, env_args)
