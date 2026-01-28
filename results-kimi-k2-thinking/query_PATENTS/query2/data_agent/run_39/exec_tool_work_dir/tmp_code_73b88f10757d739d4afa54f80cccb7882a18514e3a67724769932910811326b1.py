code = """import json
from collections import defaultdict

# Load data
patent_file = locals()['var_functions.query_db:6']
with open(patent_file, 'r') as f:
    patents_data = json.load(f)

cpc_titles_data = locals()['var_functions.query_db:32']

# Helper functions
def extract_level4_cpc(cpc_field):
    try:
        if isinstance(cpc_field, str):
            cpc_list = json.loads(cpc_field)
        else:
            cpc_list = cpc_field
        codes = []
        for item in cpc_list:
            code = item.get('code')
            if code and '/' in code:
                parts = code.split('/')
                if len(parts) == 2 and len(parts[1]) == 2:
                    codes.append(code)
        return codes
    except:
        return []

def parse_date(date_str):
    if not date_str or '2019' not in str(date_str).lower():
        return None
    ds = str(date_str).lower()
    months = {
        'jul': 7, 'july': 7, 'aug': 8, 'august': 8,
        'sep': 9, 'september': 9, 'oct': 10, 'october': 10,
        'nov': 11, 'november': 11, 'dec': 12, 'december': 12
    }
    for name, num in months.items():
        if name in ds:
            return 2019, num
    return None

# Filter German patents from July-Dec 2019
filtered = []
for p in patents_data:
    if 'DE-' in p.get('Patents_info', ''):
        date_parsed = parse_date(p.get('grant_date'))
        if date_parsed and date_parsed[1] >= 7:
            cpc_codes = extract_level4_cpc(p.get('cpc', '[]'))
            if cpc_codes:
                filtered.append({'month': date_parsed[1], 'cpc_codes': cpc_codes})

# Count by CPC and month
counts = defaultdict(lambda: defaultdict(int))
months = [7, 8, 9, 10, 11, 12]

for item in filtered:
    m = item['month']
    for cpc in item['cpc_codes']:
        counts[cpc][m] += 1

# Calculate EMA
alpha = 0.1
ema = {}
for cpc in counts:
    values = [counts[cpc][m] for m in months]
    avg = None
    for v in values:
        if avg is None:
            avg = v
        else:
            avg = alpha * v + (1 - alpha) * avg
    ema[cpc] = avg if avg is not None else 0

# Sort by EMA
sorted_cpc = sorted(ema.items(), key=lambda x: x[1], reverse=True)

# Build title lookup
title_lookup = {}
for item in cpc_titles_data:
    title_lookup[item['symbol']] = item['titleFull']

# Prepare final result
result = []
for cpc, ema_value in sorted_cpc:
    if ema_value > 0:
        title = title_lookup.get(cpc, 'Title not available')
        result.append({
            'cpc_group': cpc,
            'exponential_moving_average': round(ema_value, 3),
            'full_title': title
        })

print('__RESULT__:')
print(json.dumps({
    'top_cpc_groups': result[:10],
    'total_analyzed': len(filtered),
    'unique_cpc_groups': len(sorted_cpc)
}))"""

env_args = {'var_functions.list_db:0': ['publicationinfo'], 'var_functions.list_db:1': ['cpc_definition'], 'var_functions.query_db:4': [{'Patents_info': 'Patent application (no. DE-102013211266-A) from DE, assigned to IBM, with publication number DE-102013211266-B4.', 'grant_date': '14th Mar 2019', 'cpc': '[\n  {\n    "code": "G06F9/45533",\n    "first": true,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "G06F9/45533",\n    "first": true,\n    "inventive": true,\n    "tree": []\n  }\n]'}, {'Patents_info': 'In RU, the patent filing (app. number RU-2017142236-A) is held by Sletov Aleksandr Anatolevich and has publication no. RU-2682615-C1.', 'grant_date': 'Mar 19th, 2019', 'cpc': '[\n  {\n    "code": "A61D1/00",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "A61B17/645",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "A61B17/6425",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "A61B17/64",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "A61B17/60",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "A61B17/58",\n    "first": true,\n    "inventive": true,\n    "tree": []\n  }\n]'}, {'Patents_info': 'The RU patent application (number RU-2018105657-A) is held by OBSHCHESTVO S OGRANICHENNOJ OTVETSTVENNOSTYU VORMKHOLS VNEDRENIE and has publication no. RU-2681783-C1.', 'grant_date': 'Mar 12th, 2019', 'cpc': '[\n  {\n    "code": "E21B33/136",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "E21B33/134",\n    "first": true,\n    "inventive": true,\n    "tree": []\n  }\n]'}, {'Patents_info': 'Patent application (number RU-2016134259-A) from RU, owned by KVINETIK LTD, with publication number RU-2681957-C2.', 'grant_date': 'on March 14th, 2019', 'cpc': '[\n  {\n    "code": "G01S19/30",\n    "first": true,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "G01S19/30",\n    "first": true,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "G01S19/30",\n    "first": true,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "G01S19/37",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "G01S19/30",\n    "first": true,\n    "inventive": true,\n    "tree": []\n  }\n]'}, {'Patents_info': 'The DK patent application (number DK-14719221-T) is held by JASKE WOLFGANG and has publication number DK-2965013-T3.', 'grant_date': 'July 8th, 2019', 'cpc': '[\n  {\n    "code": "F25B2339/047",\n    "first": false,\n    "inventive": false,\n    "tree": []\n  },\n  {\n    "code": "F24D17/02",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "F25B2400/061",\n    "first": false,\n    "inventive": false,\n    "tree": []\n  },\n  {\n    "code": "Y02B10/70",\n    "first": false,\n    "inventive": false,\n    "tree": []\n  },\n  {\n    "code": "F24D2200/20",\n    "first": false,\n    "inventive": false,\n    "tree": []\n  },\n  {\n    "code": "Y02B30/52",\n    "first": false,\n    "inventive": false,\n    "tree": []\n  },\n  {\n    "code": "F24D17/0005",\n    "first": true,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "Y02B30/18",\n    "first": false,\n    "inventive": false,\n    "tree": []\n  },\n  {\n    "code": "F24D2200/123",\n    "first": false,\n    "inventive": false,\n    "tree": []\n  }\n]'}], 'var_functions.query_db:6': 'file_storage/functions.query_db:6.json', 'var_functions.execute_python:20': {'total_patents': 50, 'first_patent_keys': ['Patents_info', 'grant_date', 'cpc', 'title_localized'], 'sample_grant_date': '14th Mar 2019', 'sample_cpc': '[\n  {\n    "code": "G06F9/45533",\n    "first": true,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "G06F9/45533",\n    "first": true,\n    "inventive": true,\n    "tree": []\n  }\n]', 'sample_extracted_cpc': ['G06F9/45533', 'G06F9/45533'], 'date_parsing_tests': {'14th Mar 2019': None, 'dated 21st November 2019': [2019, 11], 'Mar 21st, 2019': None, '5th of December, 2019': [2019, 12], '22nd of August, 2019': [2019, 8], 'July 8th, 2019': [2019, 7]}}, 'var_functions.execute_python:22': {'total_filtered': 21, 'sample_patents': [{'patent_info': 'In DE, the application (number DE-102007032978-A) is held by HEIDELBERGER DRUCKMASCH AG and has publication number DE-102007032978-B4.', 'grant_date': 'dated 21st November 2019', 'year': 2019, 'month': 11, 'cpc_level4': ['B41F22/00', 'B41F21/00'], 'title_localized': '[\n  {\n    "language": "de",\n    "text": "Trommel zum Fördern eines Bogens",\n    "truncated": false\n  }\n]'}, {'patent_info': 'The DE patent application (no. DE-102010042467-A) is owned by CONTINENTAL AUTOMOTIVE GMBH and has pub. number DE-102010042467-B4.', 'grant_date': '5th of December, 2019', 'year': 2019, 'month': 12, 'cpc_level4': ['F02D41/20', 'F02D41/00'], 'title_localized': '[\n  {\n    "language": "de",\n    "text": "Ermittlung des Öffnungszeitpunkts eines Steuerventils eines indirekt angetriebenen Kraftstoffinjektors",\n    "truncated": false\n  }\n]'}, {'patent_info': 'In DE, the patent filing (application no. DE-112014003420-T) is assigned to TOYOTA MOTOR CO LTD and has publication number DE-112014003420-B4.', 'grant_date': '22nd of August, 2019', 'year': 2019, 'month': 8, 'cpc_level4': ['F02M59/44', 'F02M59/06', 'F02M55/04'], 'title_localized': '[\n  {\n    "language": "de",\n    "text": "Pulsationsdämpfer und Hochdruckkraftstoffpumpe",\n    "truncated": false\n  }\n]'}, {'patent_info': 'In DE, the patent filing (application number DE-102015221196-A) is owned by SCHOTT AG and has pub. number DE-102015221196-B4.', 'grant_date': 'September the 19th, 2019', 'year': 2019, 'month': 9, 'cpc_level4': ['G01D11/24'], 'title_localized': '[\n  {\n    "language": "de",\n    "text": "Verfahren zur Herstellung eines Bauteiles, Bauteil und Drucksensor",\n    "truncated": false\n  }\n]'}, {'patent_info': 'The DE application (number DE-102014111322-A) is owned by LEMKE SEBASTIAN and has publication no. DE-102014111322-B4.', 'grant_date': '17th of October, 2019', 'year': 2019, 'month': 10, 'cpc_level4': ['B63B21/50'], 'title_localized': '[\n  {\n    "language": "de",\n    "text": "Wasserkraftwerk",\n    "truncated": false\n  }\n]'}]}, 'var_functions.execute_python:26': {'total_filtered_patents': 21, 'total_cpc_groups': 57, 'top_cpc_by_ema': [['G02B15/15', 1.1809800000000004], ['B66C23/80', 0.5904900000000002], ['B60S9/10', 0.5904900000000002], ['G02B13/02', 0.5904900000000002], ['G02B23/24', 0.5904900000000002], ['A61B1/00', 0.5904900000000002], ['G02B13/18', 0.5904900000000002], ['F02D41/20', 0.30000000000000004], ['A61F5/14', 0.2], ['A43B17/00', 0.2], ['A43B7/20', 0.2], ['H01R2201/26', 0.2], ['C04B2235/77', 0.2], ['C04B2235/72', 0.2], ['C04B35/64', 0.2]], 'month_order': [7, 8, 9, 10, 11, 12]}, 'var_functions.query_db:32': [{'symbol': 'A43B17/00', 'titleFull': 'Insoles for insertion, e.g. footbeds or inlays, for attachment to the shoe after the upper has been joined'}, {'symbol': 'A61B1/00', 'titleFull': 'Instruments for performing medical examinations of the interior of cavities or tubes of the body by visual or photographical inspection, e.g. endoscopes; Illuminating arrangements therefor'}, {'symbol': 'A61F5/14', 'titleFull': 'Special medical insertions for shoes for flat-feet, club-feet or the like'}, {'symbol': 'B60S9/10', 'titleFull': 'Ground-engaging vehicle fittings for supporting, lifting, or manoeuvring the vehicle, wholly or in part, e.g. built-in jacks for only lifting or supporting by fluid pressure'}, {'symbol': 'B66C23/80', 'titleFull': 'Supports, e.g. outriggers, for mobile cranes hydraulically actuated'}, {'symbol': 'F02D41/20', 'titleFull': 'Output circuits, e.g. for controlling currents in command coils'}, {'symbol': 'G02B13/02', 'titleFull': 'Telephoto objectives, i.e. systems of the type + - in which the distance from the front vertex to the image plane is less than the equivalent focal length'}, {'symbol': 'G02B13/18', 'titleFull': 'Optical objectives specially designed for the purposes specified below with lenses having one or more non-spherical faces, e.g. for reducing geometrical aberration'}, {'symbol': 'G02B15/15', 'titleFull': 'Optical objectives with means for varying the magnification by axial movement of one or more lenses or groups of lenses relative to the image plane for continuously varying the equivalent focal length of the objective compensation by means of only one movement or by means of only linearly related movements, e.g. optical compensation'}, {'symbol': 'G02B23/24', 'titleFull': 'Instruments or systems for viewing the inside of hollow bodies, e.g. fibrescopes'}]}

exec(code, env_args)
