code = """import json

# Access variables by string keys
german_patents_data = locals()['var_functions.query_db:6']
second_half_data = locals()['var_functions.query_db:8']

print('=== German patents in 2019 ===')
print('Type of data:', type(german_patents_data))
if isinstance(german_patents_data, str) and '.json' in german_patents_data:
    with open(german_patents_data, 'r') as f:
        german_patents = json.load(f)
        print('Count:', len(german_patents))
        print('Sample record:', german_patents[0] if german_patents else 'None')

print('\\n=== German patents in second half 2019 ===')  
print('Type of data:', type(second_half_data))
if isinstance(second_half_data, str) and '.json' in second_half_data:
    with open(second_half_data, 'r') as f:
        second_half_patents = json.load(f)
        print('Count:', len(second_half_patents))
        print('Sample record:', second_half_patents[0] if second_half_patents else 'None')

# Now process the CPC data to extract CPC codes at level 4
def extract_cpc_codes(cpc_json_str):
    try:
        cpc_list = json.loads(cpc_json_str)
        return [item['code'] for item in cpc_list if 'code' in item]
    except:
        return []

def get_cpc_level4(code):
    """Extract CPC code up to level 4 (e.g., G06F9/45533 -> G06F9/45)"""
    if not code or '/' not in code:
        return None
    parts = code.split('/')
    main_class = parts[0]
    subgroup = parts[1]
    if len(subgroup) >= 2:
        return f"{main_class}/{subgroup[:2]}"
    return None

# Process second half German patents
cpc_level4_counts = {}
all_years = []

for patent in second_half_patents:
    grant_date = patent['grant_date']
    year = None
    # Extract year from grant_date string
    if '2019' in str(grant_date):
        year = 2019
    
    if year:
        all_years.append(year)
        cpc_codes = extract_cpc_codes(patent['cpc'])
        for code in cpc_codes:
            level4 = get_cpc_level4(code)
            if level4:
                if level4 not in cpc_level4_counts:
                    cpc_level4_counts[level4] = {}
                if year not in cpc_level4_counts[level4]:
                    cpc_level4_counts[level4][year] = 0
                cpc_level4_counts[level4][year] += 1

print('\\n=== CPC Level 4 counts ===')
print('Unique CPC Level 4 codes:', len(cpc_level4_counts))
print('Sample CPC counts:', {k: v for k, v in list(cpc_level4_counts.items())[:5]})

# Calculate exponential moving average for each CPC group
def calculate_ema(values, alpha=0.1):
    """Calculate exponential moving average"""
    if not values:
        return []
    ema = [values[0]]
    for i in range(1, len(values)):
        ema.append(alpha * values[i] + (1 - alpha) * ema[i - 1])
    return ema

# Since we only have one year (2019) in this dataset, EMA will just be the same as the count
results = []
for cpc_code, year_counts in cpc_level4_counts.items():
    if 2019 in year_counts:
        ema_value = calculate_ema([year_counts[2019]])[0]
        results.append({
            'cpc_level4_code': cpc_code,
            'year': 2019,
            'count': year_counts[2019],
            'ema_value': ema_value
        })

# Sort by EMA (which is just count for single year)
results.sort(key=lambda x: x['ema_value'], reverse=True)

print('\\n=== Top 15 CPC Level 4 codes by EMA ===')
for r in results[:15]:
    print(f"{r['cpc_level4_code']}: count={r['count']}, ema={r['ema_value']:.2f}")

print('\\n__RESULT__:')
print(json.dumps({
    'total_german_patents': len(german_patents),
    'second_half_patents': len(second_half_patents),
    'unique_level4_codes': len(cpc_level4_counts),
    'top_results': results[:20]
}))"""

env_args = {'var_functions.list_db:0': ['publicationinfo'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:5': [{'grant_date': '14th Mar 2019', 'Patents_info': 'Patent application (no. DE-102013211266-A) from DE, assigned to IBM, with publication number DE-102013211266-B4.', 'cpc': '[\n  {\n    "code": "G06F9/45533",\n    "first": true,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "G06F9/45533",\n    "first": true,\n    "inventive": true,\n    "tree": []\n  }\n]'}, {'grant_date': 'Mar 19th, 2019', 'Patents_info': 'In RU, the patent filing (app. number RU-2017142236-A) is held by Sletov Aleksandr Anatolevich and has publication no. RU-2682615-C1.', 'cpc': '[\n  {\n    "code": "A61D1/00",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "A61B17/645",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "A61B17/6425",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "A61B17/64",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "A61B17/60",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "A61B17/58",\n    "first": true,\n    "inventive": true,\n    "tree": []\n  }\n]'}, {'grant_date': 'Mar 12th, 2019', 'Patents_info': 'The RU patent application (number RU-2018105657-A) is held by OBSHCHESTVO S OGRANICHENNOJ OTVETSTVENNOSTYU VORMKHOLS VNEDRENIE and has publication no. RU-2681783-C1.', 'cpc': '[\n  {\n    "code": "E21B33/136",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "E21B33/134",\n    "first": true,\n    "inventive": true,\n    "tree": []\n  }\n]'}, {'grant_date': '2019 on Jul 12th', 'Patents_info': 'Application (no. RU-2018119076-A) from RU, assigned to FEDERALNOE GOSUDARSTVENNOE KAZENNOE VOENNOE OBRAZOVATELNOE UCHREZHDENIE VYSSHEGO OBRAZOVANIYA VOENNA, with publication no. RU-2694421-C1.', 'cpc': '[\n  {\n    "code": "G01S13/42",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "G01S5/18",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "F41G3/00",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "F41H13/00",\n    "first": true,\n    "inventive": true,\n    "tree": []\n  }\n]'}, {'grant_date': 'on March 14th, 2019', 'Patents_info': 'Patent application (number RU-2016134259-A) from RU, owned by KVINETIK LTD, with publication number RU-2681957-C2.', 'cpc': '[\n  {\n    "code": "G01S19/30",\n    "first": true,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "G01S19/30",\n    "first": true,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "G01S19/30",\n    "first": true,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "G01S19/37",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "G01S19/30",\n    "first": true,\n    "inventive": true,\n    "tree": []\n  }\n]'}, {'grant_date': 'July 8th, 2019', 'Patents_info': 'The DK patent application (number DK-14719221-T) is held by JASKE WOLFGANG and has publication number DK-2965013-T3.', 'cpc': '[\n  {\n    "code": "F25B2339/047",\n    "first": false,\n    "inventive": false,\n    "tree": []\n  },\n  {\n    "code": "F24D17/02",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "F25B2400/061",\n    "first": false,\n    "inventive": false,\n    "tree": []\n  },\n  {\n    "code": "Y02B10/70",\n    "first": false,\n    "inventive": false,\n    "tree": []\n  },\n  {\n    "code": "F24D2200/20",\n    "first": false,\n    "inventive": false,\n    "tree": []\n  },\n  {\n    "code": "Y02B30/52",\n    "first": false,\n    "inventive": false,\n    "tree": []\n  },\n  {\n    "code": "F24D17/0005",\n    "first": true,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "Y02B30/18",\n    "first": false,\n    "inventive": false,\n    "tree": []\n  },\n  {\n    "code": "F24D2200/123",\n    "first": false,\n    "inventive": false,\n    "tree": []\n  }\n]'}, {'grant_date': '8th April 2019', 'Patents_info': 'The DK patent filing (application number DK-14835716-T) is owned by UNIV OSLO HF and has pub. number DK-3069138-T3.', 'cpc': '[\n  {\n    "code": "G01N33/505",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "G01N33/56977",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "G01N33/56977",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "A61K2039/572",\n    "first": false,\n    "inventive": false,\n    "tree": []\n  },\n  {\n    "code": "A61K39/39",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "G01N2333/70539",\n    "first": false,\n    "inventive": false,\n    "tree": []\n  },\n  {\n    "code": "A61K2039/55527",\n    "first": false,\n    "inventive": false,\n    "tree": []\n  },\n  {\n    "code": "C07K14/70503",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "C07K14/70539",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "A61K2039/5158",\n    "first": false,\n    "inventive": false,\n    "tree": []\n  },\n  {\n    "code": "A61K39/0011",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "G01N33/505",\n    "first": true,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "A61K39/0011",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "A61K2039/5158",\n    "first": false,\n    "inventive": false,\n    "tree": []\n  }\n]'}, {'grant_date': '2019, May 30th', 'Patents_info': 'The RU patent application (ID RU-2018146701-U) is held by [] and has publication no. RU-189707-U1.', 'cpc': '[\n  {\n    "code": "B60P1/48",\n    "first": true,\n    "inventive": true,\n    "tree": []\n  }\n]'}, {'grant_date': '22nd May 2019', 'Patents_info': 'The ES patent application (ID ES-11727548-T) is assigned to LOHR IND and has pub. number ES-2713511-T3.', 'cpc': '[\n  {\n    "code": "B61D3/04",\n    "first": true,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "B61D3/182",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "B61D3/04",\n    "first": true,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "B61D3/16",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "Y02T30/00",\n    "first": false,\n    "inventive": false,\n    "tree": []\n  }\n]'}, {'grant_date': '2019 on Nov 14th', 'Patents_info': 'In RU, the patent filing (application no. RU-2019124341-U) is owned by [] and has pub. number RU-193787-U1.', 'cpc': '[\n  {\n    "code": "F16K17/192",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "F16L43/00",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  }\n]'}], 'var_functions.query_db:6': 'file_storage/functions.query_db:6.json', 'var_functions.query_db:8': 'file_storage/functions.query_db:8.json', 'var_functions.query_db:10': [{'grant_date': '10th Apr 1883'}, {'grant_date': '10th Apr 1888'}, {'grant_date': '10th Apr 1923'}, {'grant_date': '10th Apr 1945'}, {'grant_date': '10th Apr 1952'}, {'grant_date': '10th Apr 1969'}, {'grant_date': '10th Apr 1974'}, {'grant_date': '10th Apr 1979'}, {'grant_date': '10th Apr 1980'}, {'grant_date': '10th Apr 1984'}, {'grant_date': '10th Apr 1990'}, {'grant_date': '10th Apr 2001'}, {'grant_date': '10th Apr 2006'}, {'grant_date': '10th Apr 2008'}, {'grant_date': '10th Apr 2018'}, {'grant_date': '10th Apr 2019'}, {'grant_date': '10th Apr 2020'}, {'grant_date': '10th Apr 2023'}, {'grant_date': '10th Apr 2024'}, {'grant_date': '10th April 1956'}, {'grant_date': '10th April 1962'}, {'grant_date': '10th April 1964'}, {'grant_date': '10th April 1973'}, {'grant_date': '10th April 1979'}, {'grant_date': '10th April 1990'}, {'grant_date': '10th April 2000'}, {'grant_date': '10th April 2001'}, {'grant_date': '10th April 2002'}, {'grant_date': '10th April 2005'}, {'grant_date': '10th April 2007'}, {'grant_date': '10th April 2012'}, {'grant_date': '10th April 2013'}, {'grant_date': '10th April 2014'}, {'grant_date': '10th April 2018'}, {'grant_date': '10th April 2020'}, {'grant_date': '10th April 2023'}, {'grant_date': '10th Aug 1948'}, {'grant_date': '10th Aug 1954'}, {'grant_date': '10th Aug 1959'}, {'grant_date': '10th Aug 1970'}, {'grant_date': '10th Aug 1973'}, {'grant_date': '10th Aug 1974'}, {'grant_date': '10th Aug 1976'}, {'grant_date': '10th Aug 1993'}, {'grant_date': '10th Aug 2004'}, {'grant_date': '10th Aug 2006'}, {'grant_date': '10th Aug 2011'}, {'grant_date': '10th Aug 2014'}, {'grant_date': '10th Aug 2016'}, {'grant_date': '10th Aug 2018'}], 'var_functions.execute_python:16': {'status': 'checked'}, 'var_functions.execute_python:18': {'variables': ['json', 'var', 'var_functions.execute_python:16', 'var_functions.list_db:0', 'var_functions.query_db:10', 'var_functions.query_db:2', 'var_functions.query_db:5', 'var_functions.query_db:6', 'var_functions.query_db:8']}}

exec(code, env_args)
