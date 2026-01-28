code = """import json
import pandas as pd

# Load the data
cpc_definitions = locals()['var_functions.query_db:24']
if isinstance(cpc_definitions, str) and cpc_definitions.endswith('.json'):
    with open(cpc_definitions, 'r') as f:
        cpc_defs = json.load(f)
else:
    cpc_defs = cpc_definitions

analysis_results = locals()['var_functions.query_db:14']
# This is actually the patent data from previous query
# Let's use the processed results from our Python analysis
python_results = locals()['var_functions.execute_python:20']
if isinstance(python_results, str) and python_results.endswith('.json'):
    with open(python_results, 'r') as f:
        results = json.load(f)
else:
    results = python_results

# Create a mapping of CPC symbols to full titles
cpc_title_map = {}
for def_item in cpc_defs:
    symbol = def_item.get('symbol')
    title_full = def_item.get('titleFull', 'Title not found')
    cpc_title_map[symbol] = title_full

# Prepare final results
top_cpc_groups = []
for i, item in enumerate(results.get('top_cpc_by_ema', [])):
    cpc_code = item.get('cpc_level4_code')
    count = item.get('patent_count_2019', 0)
    title = cpc_title_map.get(cpc_code, 'Title not found')
    
    top_cpc_groups.append({
        'rank': i + 1,
        'cpc_level4_code': cpc_code,
        'title_full': title,
        'patent_count_2019': count,
        'ema_value': count,
        'best_year': '2019'
    })

# Sort by EMA value (patent count) in descending order
top_cpc_groups = sorted(top_cpc_groups, key=lambda x: x['ema_value'], reverse=True)

# Format the final answer
final_output = {
    'analysis_summary': {
        'total_german_patents_2019_second_half': results.get('total_german_patents_2019_second_half', 0),
        'note': 'Exponential Moving Average calculated with smoothing factor 0.1. Since only 2019 data is available, EMA equals patent count for 2019.'
    },
    'top_cpc_technology_areas': top_cpc_groups
}

print('__RESULT__:')
print(json.dumps(final_output, indent=2))"""

env_args = {'var_functions.list_db:0': ['publicationinfo'], 'var_functions.query_db:2': [{'grant_date': '14th Mar 2019', 'Patents_info': 'Patent application (no. DE-102013211266-A) from DE, assigned to IBM, with publication number DE-102013211266-B4.', 'cpc': '[\n  {\n    "code": "G06F9/45533",\n    "first": true,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "G06F9/45533",\n    "first": true,\n    "inventive": true,\n    "tree": []\n  }\n]'}, {'grant_date': 'Mar 19th, 2019', 'Patents_info': 'In RU, the patent filing (app. number RU-2017142236-A) is held by Sletov Aleksandr Anatolevich and has publication no. RU-2682615-C1.', 'cpc': '[\n  {\n    "code": "A61D1/00",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "A61B17/645",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "A61B17/6425",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "A61B17/64",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "A61B17/60",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "A61B17/58",\n    "first": true,\n    "inventive": true,\n    "tree": []\n  }\n]'}, {'grant_date': 'Mar 12th, 2019', 'Patents_info': 'The RU patent application (number RU-2018105657-A) is held by OBSHCHESTVO S OGRANICHENNOJ OTVETSTVENNOSTYU VORMKHOLS VNEDRENIE and has publication no. RU-2681783-C1.', 'cpc': '[\n  {\n    "code": "E21B33/136",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "E21B33/134",\n    "first": true,\n    "inventive": true,\n    "tree": []\n  }\n]'}, {'grant_date': '2019 on Jul 12th', 'Patents_info': 'Application (no. RU-2018119076-A) from RU, assigned to FEDERALNOE GOSUDARSTVENNOE KAZENNOE VOENNOE OBRAZOVATELNOE UCHREZHDENIE VYSSHEGO OBRAZOVANIYA VOENNA, with publication no. RU-2694421-C1.', 'cpc': '[\n  {\n    "code": "G01S13/42",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "G01S5/18",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "F41G3/00",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "F41H13/00",\n    "first": true,\n    "inventive": true,\n    "tree": []\n  }\n]'}, {'grant_date': 'on March 14th, 2019', 'Patents_info': 'Patent application (number RU-2016134259-A) from RU, owned by KVINETIK LTD, with publication number RU-2681957-C2.', 'cpc': '[\n  {\n    "code": "G01S19/30",\n    "first": true,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "G01S19/30",\n    "first": true,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "G01S19/30",\n    "first": true,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "G01S19/37",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "G01S19/30",\n    "first": true,\n    "inventive": true,\n    "tree": []\n  }\n]'}], 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json', 'var_functions.list_db:8': ['cpc_definition'], 'var_functions.query_db:10': 'file_storage/functions.query_db:10.json', 'var_functions.query_db:12': 'file_storage/functions.query_db:12.json', 'var_functions.query_db:14': 'file_storage/functions.query_db:14.json', 'var_functions.execute_python:20': {'total_german_patents_2019_second_half': 34, 'top_cpc_by_ema': [{'rank': 1, 'cpc_level4_code': 'H04W52/02', 'patent_count_2019': 12, 'ema_2019': 12, 'best_year': '2019'}, {'rank': 2, 'cpc_level4_code': 'C04B2235/32', 'patent_count_2019': 8, 'ema_2019': 8, 'best_year': '2019'}, {'rank': 3, 'cpc_level4_code': 'B29C2049/58', 'patent_count_2019': 7, 'ema_2019': 7, 'best_year': '2019'}, {'rank': 4, 'cpc_level4_code': 'H04L1/18', 'patent_count_2019': 6, 'ema_2019': 6, 'best_year': '2019'}, {'rank': 5, 'cpc_level4_code': 'C04B2235/66', 'patent_count_2019': 6, 'ema_2019': 6, 'best_year': '2019'}, {'rank': 6, 'cpc_level4_code': 'C04B2235/65', 'patent_count_2019': 6, 'ema_2019': 6, 'best_year': '2019'}, {'rank': 7, 'cpc_level4_code': 'C04B35/64', 'patent_count_2019': 6, 'ema_2019': 6, 'best_year': '2019'}, {'rank': 8, 'cpc_level4_code': 'H01J49/04', 'patent_count_2019': 5, 'ema_2019': 5, 'best_year': '2019'}, {'rank': 9, 'cpc_level4_code': 'G02B23/24', 'patent_count_2019': 5, 'ema_2019': 5, 'best_year': '2019'}, {'rank': 10, 'cpc_level4_code': 'H04L5/00', 'patent_count_2019': 4, 'ema_2019': 4, 'best_year': '2019'}], 'note': 'Need to join with CPC definition table for full titles'}, 'var_functions.query_db:24': [{'symbol': 'C04B2235/66', 'titleFull': 'Specific sintering techniques, e.g. centrifugal sintering', 'level': '9.0', 'titlePart': '[\n  "Specific sintering techniques, e.g. centrifugal sintering"\n]'}, {'symbol': 'H04L1/18', 'titleFull': 'Automatic repetition systems, e.g. Van Duuren systems', 'level': '10.0', 'titlePart': '[\n  "Automatic repetition systems, e.g. Van Duuren systems"\n]'}, {'symbol': 'H04W52/02', 'titleFull': 'Power saving arrangements', 'level': '8.0', 'titlePart': '[\n  "Power saving arrangements"\n]'}, {'symbol': 'H04L5/00', 'titleFull': 'Arrangements affording multiple use of the transmission path', 'level': '7.0', 'titlePart': '[\n  "Arrangements affording multiple use of the transmission path"\n]'}, {'symbol': 'G02B23/24', 'titleFull': 'Instruments or systems for viewing the inside of hollow bodies, e.g. fibrescopes', 'level': '8.0', 'titlePart': '[\n  "Instruments or systems for viewing the inside of hollow bodies, e.g. fibrescopes"\n]'}, {'symbol': 'C04B2235/65', 'titleFull': 'Aspects relating to heat treatments of ceramic bodies such as green ceramics or pre-sintered ceramics, e.g. burning, sintering or melting processes', 'level': '8.0', 'titlePart': '[\n  "Aspects relating to heat treatments of ceramic bodies such as green ceramics or pre-sintered ceramics, e.g. burning, sintering or melting processes"\n]'}, {'symbol': 'H01J49/04', 'titleFull': 'Arrangements for introducing or extracting samples to be analysed, e.g. vacuum locks; Arrangements for external adjustment of electron- or ion-optical components', 'level': '9.0', 'titlePart': '[\n  "Arrangements for introducing or extracting samples to be analysed, e.g. vacuum locks",\n  "Arrangements for external adjustment of electron- or ion-optical components"\n]'}, {'symbol': 'C04B35/64', 'titleFull': 'Burning or sintering processes', 'level': '9.0', 'titlePart': '[\n  "Burning or sintering processes"\n]'}, {'symbol': 'C04B2235/32', 'titleFull': 'Metal oxides, mixed metal oxides, or oxide-forming salts thereof, e.g. carbonates, nitrates, (oxy)hydroxides, chlorides', 'level': '10.0', 'titlePart': '[\n  "Metal oxides, mixed metal oxides, or oxide-forming salts thereof, e.g. carbonates, nitrates, (oxy)hydroxides, chlorides"\n]'}]}

exec(code, env_args)
