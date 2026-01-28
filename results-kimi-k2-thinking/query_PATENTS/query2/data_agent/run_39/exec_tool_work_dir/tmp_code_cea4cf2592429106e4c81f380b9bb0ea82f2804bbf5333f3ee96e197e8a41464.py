code = """import json
from collections import defaultdict

# Load filtered patents from previous result
filtered_result = locals()['var_functions.execute_python:22']
filtered_patents = filtered_result['sample_patents']  # Using sample here, but we have all filtered

# Actually load all filtered patents properly
result_path = locals()['var_functions.query_db:6']
with open(result_path, 'r') as f:
    patents_data = json.load(f)

# Re-filter all patents (same logic as before)
def extract_level4_cpc(cpc_json):
    try:
        if isinstance(cpc_json, str):
            cpc_list = json.loads(cpc_json)
        else:
            cpc_list = cpc_json
        codes = [item.get('code') for item in cpc_list if item.get('code')]
        level4_groups = []
        for code in codes:
            if '/' in code:
                parts = code.split('/')
                if len(parts[1]) == 2:  # exactly 2 digits after slash
                    level4_groups.append(code)
        return level4_groups
    except:
        return []

def parse_grant_date_half(date_str):
    if not date_str or '2019' not in date_str.lower():
        return None
    date_str_lower = date_str.lower()
    month_patterns = {
        'jul': 7, 'july': 7, 'aug': 8, 'august': 8, 
        'sep': 9, 'september': 9, 'oct': 10, 'october': 10,
        'nov': 11, 'november': 11, 'dec': 12, 'december': 12
    }
    for month_name, num in month_patterns.items():
        if month_name in date_str_lower:
            return 2019, num
    return None

all_filtered = []
for patent in patents_data:
    if 'DE-' in patent.get('Patents_info', ''):
        date_parsed = parse_grant_date_half(patent.get('grant_date', ''))
        if date_parsed:
            cpc_level4 = extract_level4_cpc(patent.get('cpc', '[]'))
            if cpc_level4:
                all_filtered.append({
                    'grant_month': date_parsed[1],
                    'cpc_level4': cpc_level4
                })

print('Total filtered German patents (Jul-Dec 2019):', len(all_filtered))

# Count patents per CPC group per month
monthly_counts = defaultdict(lambda: defaultdict(int))
month_order = [7, 8, 9, 10, 11, 12]

for patent in all_filtered:
    month = patent['grant_month']
    for cpc in patent['cpc_level4']:
        monthly_counts[cpc][month] += 1

# Show CPC groups found
cpc_groups = list(monthly_counts.keys())
print('CPC level 4 groups found:', len(cpc_groups))
print('Sample groups:', cpc_groups[:10])

# Calculate Exponential Moving Average (EMA) for each CPC group
# EMA formula: EMA_t = alpha * value_t + (1 - alpha) * EMA_{t-1}
alpha = 0.1

ema_results = {}

for cpc in cpc_groups:
    # Create ordered monthly values (Jul-Dec 2019)
    values = [monthly_counts[cpc][month] for month in month_order]
    
    # Calculate EMA
    ema = None
    for val in values:
        if ema is None:
            ema = val  # Initialize with first value
        else:
            ema = alpha * val + (1 - alpha) * ema
    
    # Store max EMA (which will be the final EMA after processing all months)
    ema_results[cpc] = ema if ema is not None else 0

# Sort CPC groups by EMA value
sorted_cpc = sorted(ema_results.items(), key=lambda x: x[1], reverse=True)

print('Top CPC groups by EMA:')
for i, (cpc, ema) in enumerate(sorted_cpc[:10]):
    print(f"{i+1}. {cpc}: EMA = {ema:.2f}")

# Prepare output for next step (get titles)
top_cpc_groups = [cpc for cpc, _ in sorted_cpc[:20]]  # Get top 20
print('\nTop CPC groups to fetch titles for:', top_cpc_groups[:5])

print('__RESULT__:')
print(json.dumps({
    'sorted_cpc_ema': sorted_cpc,
    'monthly_counts': dict(monthly_counts),
    'total_patents': len(all_filtered)
}))"""

env_args = {'var_functions.list_db:0': ['publicationinfo'], 'var_functions.list_db:1': ['cpc_definition'], 'var_functions.query_db:4': [{'Patents_info': 'Patent application (no. DE-102013211266-A) from DE, assigned to IBM, with publication number DE-102013211266-B4.', 'grant_date': '14th Mar 2019', 'cpc': '[\n  {\n    "code": "G06F9/45533",\n    "first": true,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "G06F9/45533",\n    "first": true,\n    "inventive": true,\n    "tree": []\n  }\n]'}, {'Patents_info': 'In RU, the patent filing (app. number RU-2017142236-A) is held by Sletov Aleksandr Anatolevich and has publication no. RU-2682615-C1.', 'grant_date': 'Mar 19th, 2019', 'cpc': '[\n  {\n    "code": "A61D1/00",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "A61B17/645",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "A61B17/6425",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "A61B17/64",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "A61B17/60",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "A61B17/58",\n    "first": true,\n    "inventive": true,\n    "tree": []\n  }\n]'}, {'Patents_info': 'The RU patent application (number RU-2018105657-A) is held by OBSHCHESTVO S OGRANICHENNOJ OTVETSTVENNOSTYU VORMKHOLS VNEDRENIE and has publication no. RU-2681783-C1.', 'grant_date': 'Mar 12th, 2019', 'cpc': '[\n  {\n    "code": "E21B33/136",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "E21B33/134",\n    "first": true,\n    "inventive": true,\n    "tree": []\n  }\n]'}, {'Patents_info': 'Patent application (number RU-2016134259-A) from RU, owned by KVINETIK LTD, with publication number RU-2681957-C2.', 'grant_date': 'on March 14th, 2019', 'cpc': '[\n  {\n    "code": "G01S19/30",\n    "first": true,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "G01S19/30",\n    "first": true,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "G01S19/30",\n    "first": true,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "G01S19/37",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "G01S19/30",\n    "first": true,\n    "inventive": true,\n    "tree": []\n  }\n]'}, {'Patents_info': 'The DK patent application (number DK-14719221-T) is held by JASKE WOLFGANG and has publication number DK-2965013-T3.', 'grant_date': 'July 8th, 2019', 'cpc': '[\n  {\n    "code": "F25B2339/047",\n    "first": false,\n    "inventive": false,\n    "tree": []\n  },\n  {\n    "code": "F24D17/02",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "F25B2400/061",\n    "first": false,\n    "inventive": false,\n    "tree": []\n  },\n  {\n    "code": "Y02B10/70",\n    "first": false,\n    "inventive": false,\n    "tree": []\n  },\n  {\n    "code": "F24D2200/20",\n    "first": false,\n    "inventive": false,\n    "tree": []\n  },\n  {\n    "code": "Y02B30/52",\n    "first": false,\n    "inventive": false,\n    "tree": []\n  },\n  {\n    "code": "F24D17/0005",\n    "first": true,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "Y02B30/18",\n    "first": false,\n    "inventive": false,\n    "tree": []\n  },\n  {\n    "code": "F24D2200/123",\n    "first": false,\n    "inventive": false,\n    "tree": []\n  }\n]'}], 'var_functions.query_db:6': 'file_storage/functions.query_db:6.json', 'var_functions.execute_python:20': {'total_patents': 50, 'first_patent_keys': ['Patents_info', 'grant_date', 'cpc', 'title_localized'], 'sample_grant_date': '14th Mar 2019', 'sample_cpc': '[\n  {\n    "code": "G06F9/45533",\n    "first": true,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "G06F9/45533",\n    "first": true,\n    "inventive": true,\n    "tree": []\n  }\n]', 'sample_extracted_cpc': ['G06F9/45533', 'G06F9/45533'], 'date_parsing_tests': {'14th Mar 2019': None, 'dated 21st November 2019': [2019, 11], 'Mar 21st, 2019': None, '5th of December, 2019': [2019, 12], '22nd of August, 2019': [2019, 8], 'July 8th, 2019': [2019, 7]}}, 'var_functions.execute_python:22': {'total_filtered': 21, 'sample_patents': [{'patent_info': 'In DE, the application (number DE-102007032978-A) is held by HEIDELBERGER DRUCKMASCH AG and has publication number DE-102007032978-B4.', 'grant_date': 'dated 21st November 2019', 'year': 2019, 'month': 11, 'cpc_level4': ['B41F22/00', 'B41F21/00'], 'title_localized': '[\n  {\n    "language": "de",\n    "text": "Trommel zum Fördern eines Bogens",\n    "truncated": false\n  }\n]'}, {'patent_info': 'The DE patent application (no. DE-102010042467-A) is owned by CONTINENTAL AUTOMOTIVE GMBH and has pub. number DE-102010042467-B4.', 'grant_date': '5th of December, 2019', 'year': 2019, 'month': 12, 'cpc_level4': ['F02D41/20', 'F02D41/00'], 'title_localized': '[\n  {\n    "language": "de",\n    "text": "Ermittlung des Öffnungszeitpunkts eines Steuerventils eines indirekt angetriebenen Kraftstoffinjektors",\n    "truncated": false\n  }\n]'}, {'patent_info': 'In DE, the patent filing (application no. DE-112014003420-T) is assigned to TOYOTA MOTOR CO LTD and has publication number DE-112014003420-B4.', 'grant_date': '22nd of August, 2019', 'year': 2019, 'month': 8, 'cpc_level4': ['F02M59/44', 'F02M59/06', 'F02M55/04'], 'title_localized': '[\n  {\n    "language": "de",\n    "text": "Pulsationsdämpfer und Hochdruckkraftstoffpumpe",\n    "truncated": false\n  }\n]'}, {'patent_info': 'In DE, the patent filing (application number DE-102015221196-A) is owned by SCHOTT AG and has pub. number DE-102015221196-B4.', 'grant_date': 'September the 19th, 2019', 'year': 2019, 'month': 9, 'cpc_level4': ['G01D11/24'], 'title_localized': '[\n  {\n    "language": "de",\n    "text": "Verfahren zur Herstellung eines Bauteiles, Bauteil und Drucksensor",\n    "truncated": false\n  }\n]'}, {'patent_info': 'The DE application (number DE-102014111322-A) is owned by LEMKE SEBASTIAN and has publication no. DE-102014111322-B4.', 'grant_date': '17th of October, 2019', 'year': 2019, 'month': 10, 'cpc_level4': ['B63B21/50'], 'title_localized': '[\n  {\n    "language": "de",\n    "text": "Wasserkraftwerk",\n    "truncated": false\n  }\n]'}]}}

exec(code, env_args)
