code = """import json

# Load patent data from file
result_path = locals()['var_functions.query_db:6']
with open(result_path, 'r') as f:
    patents_data = json.load(f)

# Function to extract CPC codes and get level 4 groups
def extract_level4_cpc(cpc_json):
    try:
        if isinstance(cpc_json, str):
            cpc_list = json.loads(cpc_json)
        else:
            cpc_list = cpc_json
        
        codes = [item.get('code') for item in cpc_list if item.get('code')]
        # Get level 4 groups (format: XXXX/YY where YY has exactly 2 digits after slash)
        level4_groups = set()
        for code in codes:
            if '/' in code:
                main_part = code.split('/')[0]
                subgroup = code.split('/')[1]
                if len(subgroup) == 2:
                    level4_groups.add(code)
        return list(level4_groups)
    except:
        return []

# Function to parse grant date for second half of 2019
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

# Filter patents: German, second half 2019
filtered_patents = []
for patent in patents_data:
    patents_info = patent.get('Patents_info', '')
    grant_date = patent.get('grant_date', '')
    
    # Check if German patent
    if 'DE-' in patents_info:
        date_parsed = parse_grant_date_half(grant_date)
        if date_parsed:
            year, month = date_parsed
            cpc_level4 = extract_level4_cpc(patent.get('cpc', '[]'))
            if cpc_level4:
                filtered_patents.append({
                    'patent_info': patents_info,
                    'grant_date': grant_date,
                    'year': year,
                    'month': month,
                    'cpc_level4': cpc_level4,
                    'title_localized': patent.get('title_localized', '')
                })

print('__RESULT__:')
print(json.dumps({
    'total_filtered': len(filtered_patents),
    'sample_patents': filtered_patents[:5]
}, indent=2))"""

env_args = {'var_functions.list_db:0': ['publicationinfo'], 'var_functions.list_db:1': ['cpc_definition'], 'var_functions.query_db:4': [{'Patents_info': 'Patent application (no. DE-102013211266-A) from DE, assigned to IBM, with publication number DE-102013211266-B4.', 'grant_date': '14th Mar 2019', 'cpc': '[\n  {\n    "code": "G06F9/45533",\n    "first": true,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "G06F9/45533",\n    "first": true,\n    "inventive": true,\n    "tree": []\n  }\n]'}, {'Patents_info': 'In RU, the patent filing (app. number RU-2017142236-A) is held by Sletov Aleksandr Anatolevich and has publication no. RU-2682615-C1.', 'grant_date': 'Mar 19th, 2019', 'cpc': '[\n  {\n    "code": "A61D1/00",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "A61B17/645",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "A61B17/6425",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "A61B17/64",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "A61B17/60",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "A61B17/58",\n    "first": true,\n    "inventive": true,\n    "tree": []\n  }\n]'}, {'Patents_info': 'The RU patent application (number RU-2018105657-A) is held by OBSHCHESTVO S OGRANICHENNOJ OTVETSTVENNOSTYU VORMKHOLS VNEDRENIE and has publication no. RU-2681783-C1.', 'grant_date': 'Mar 12th, 2019', 'cpc': '[\n  {\n    "code": "E21B33/136",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "E21B33/134",\n    "first": true,\n    "inventive": true,\n    "tree": []\n  }\n]'}, {'Patents_info': 'Patent application (number RU-2016134259-A) from RU, owned by KVINETIK LTD, with publication number RU-2681957-C2.', 'grant_date': 'on March 14th, 2019', 'cpc': '[\n  {\n    "code": "G01S19/30",\n    "first": true,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "G01S19/30",\n    "first": true,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "G01S19/30",\n    "first": true,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "G01S19/37",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "G01S19/30",\n    "first": true,\n    "inventive": true,\n    "tree": []\n  }\n]'}, {'Patents_info': 'The DK patent application (number DK-14719221-T) is held by JASKE WOLFGANG and has publication number DK-2965013-T3.', 'grant_date': 'July 8th, 2019', 'cpc': '[\n  {\n    "code": "F25B2339/047",\n    "first": false,\n    "inventive": false,\n    "tree": []\n  },\n  {\n    "code": "F24D17/02",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "F25B2400/061",\n    "first": false,\n    "inventive": false,\n    "tree": []\n  },\n  {\n    "code": "Y02B10/70",\n    "first": false,\n    "inventive": false,\n    "tree": []\n  },\n  {\n    "code": "F24D2200/20",\n    "first": false,\n    "inventive": false,\n    "tree": []\n  },\n  {\n    "code": "Y02B30/52",\n    "first": false,\n    "inventive": false,\n    "tree": []\n  },\n  {\n    "code": "F24D17/0005",\n    "first": true,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "Y02B30/18",\n    "first": false,\n    "inventive": false,\n    "tree": []\n  },\n  {\n    "code": "F24D2200/123",\n    "first": false,\n    "inventive": false,\n    "tree": []\n  }\n]'}], 'var_functions.query_db:6': 'file_storage/functions.query_db:6.json', 'var_functions.execute_python:20': {'total_patents': 50, 'first_patent_keys': ['Patents_info', 'grant_date', 'cpc', 'title_localized'], 'sample_grant_date': '14th Mar 2019', 'sample_cpc': '[\n  {\n    "code": "G06F9/45533",\n    "first": true,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "G06F9/45533",\n    "first": true,\n    "inventive": true,\n    "tree": []\n  }\n]', 'sample_extracted_cpc': ['G06F9/45533', 'G06F9/45533'], 'date_parsing_tests': {'14th Mar 2019': None, 'dated 21st November 2019': [2019, 11], 'Mar 21st, 2019': None, '5th of December, 2019': [2019, 12], '22nd of August, 2019': [2019, 8], 'July 8th, 2019': [2019, 7]}}}

exec(code, env_args)
