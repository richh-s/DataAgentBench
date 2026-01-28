code = """import json

cpc_query_path = locals()['var_functions.query_db:34']

with open(cpc_query_path, 'r') as f:
    cpc_definitions = json.load(f)

print('Loaded CPC definitions:', len(cpc_definitions))

# Create a mapping of level 4 codes to their full titles
cpc_title_map = {}
for item in cpc_definitions:
    symbol = item['symbol']
    cpc_title_map[symbol] = item['titleFull']
    print(f"{symbol}: {item['titleFull'][:80]}...")

# Now get the CPC counts from the previous analysis
second_half_patents_path = locals()['var_functions.query_db:8']

with open(second_half_patents_path, 'r') as f:
    second_half_patents = json.load(f)

# Count CPC level 4 occurrences (repeating for completeness)
def extract_cpc_codes(cpc_str):
    try:
        return json.loads(cpc_str)
    except:
        return []

def get_level4_code(full_code):
    if not full_code or '/' not in full_code:
        return None
    main, subgroup = full_code.split('/')
    if len(subgroup) >= 2:
        return f"{main}/{subgroup[:2]}"
    return f"{main}/{subgroup}"

# Count CPC level 4 occurrences
cpc_counts = {}
for patent in second_half_patents:
    cpc_items = extract_cpc_codes(patent['cpc'])
    for item in cpc_items:
        if 'code' in item:
            level4 = get_level4_code(item['code'])
            if level4:
                cpc_counts[level4] = cpc_counts.get(level4, 0) + 1

# Create final results table
results = []
for cpc_code, count in sorted(cpc_counts.items(), key=lambda x: x[1], reverse=True):
    # Get title from our map, or use default
    title = cpc_title_map.get(cpc_code, 'Title not available')
    
    # With only 2019 data available, EMA = count (alpha=0.1 with single data point)
    ema_value = float(count)
    
    results.append({
        'cpc_level4_code': cpc_code,
        'full_title': title,
        'best_year': 2019,
        'count_in_2019': count,
        'ema_value': ema_value
    })

print('\nTop 15 CPC Level 4 Technology Areas in Germany (Second Half 2019):')
print('=' * 90)
for i, result in enumerate(results[:15]):
    print(f"{i+1:2d}. {result['cpc_level4_code']} - {result['full_title'][:60]}")
    print(f"     Patents: {result['count_in_2019']}, EMA: {result['ema_value']:.2f}, Best Year: {result['best_year']}")
    print()

final_output = {
    'top_technology_areas': results[:15],
    'total_cpc_groups_analyzed': len(results),
    'total_patents_considered': len(second_half_patents)
}

print('\n__RESULT__:')
print(json.dumps(final_output, default=str))"""

env_args = {'var_functions.list_db:0': ['publicationinfo'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:5': [{'grant_date': '14th Mar 2019', 'Patents_info': 'Patent application (no. DE-102013211266-A) from DE, assigned to IBM, with publication number DE-102013211266-B4.', 'cpc': '[\n  {\n    "code": "G06F9/45533",\n    "first": true,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "G06F9/45533",\n    "first": true,\n    "inventive": true,\n    "tree": []\n  }\n]'}, {'grant_date': 'Mar 19th, 2019', 'Patents_info': 'In RU, the patent filing (app. number RU-2017142236-A) is held by Sletov Aleksandr Anatolevich and has publication no. RU-2682615-C1.', 'cpc': '[\n  {\n    "code": "A61D1/00",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "A61B17/645",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "A61B17/6425",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "A61B17/64",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "A61B17/60",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "A61B17/58",\n    "first": true,\n    "inventive": true,\n    "tree": []\n  }\n]'}, {'grant_date': 'Mar 12th, 2019', 'Patents_info': 'The RU patent application (number RU-2018105657-A) is held by OBSHCHESTVO S OGRANICHENNOJ OTVETSTVENNOSTYU VORMKHOLS VNEDRENIE and has publication no. RU-2681783-C1.', 'cpc': '[\n  {\n    "code": "E21B33/136",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "E21B33/134",\n    "first": true,\n    "inventive": true,\n    "tree": []\n  }\n]'}, {'grant_date': '2019 on Jul 12th', 'Patents_info': 'Application (no. RU-2018119076-A) from RU, assigned to FEDERALNOE GOSUDARSTVENNOE KAZENNOE VOENNOE OBRAZOVATELNOE UCHREZHDENIE VYSSHEGO OBRAZOVANIYA VOENNA, with publication no. RU-2694421-C1.', 'cpc': '[\n  {\n    "code": "G01S13/42",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "G01S5/18",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "F41G3/00",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "F41H13/00",\n    "first": true,\n    "inventive": true,\n    "tree": []\n  }\n]'}, {'grant_date': 'on March 14th, 2019', 'Patents_info': 'Patent application (number RU-2016134259-A) from RU, owned by KVINETIK LTD, with publication number RU-2681957-C2.', 'cpc': '[\n  {\n    "code": "G01S19/30",\n    "first": true,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "G01S19/30",\n    "first": true,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "G01S19/30",\n    "first": true,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "G01S19/37",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "G01S19/30",\n    "first": true,\n    "inventive": true,\n    "tree": []\n  }\n]'}, {'grant_date': 'July 8th, 2019', 'Patents_info': 'The DK patent application (number DK-14719221-T) is held by JASKE WOLFGANG and has publication number DK-2965013-T3.', 'cpc': '[\n  {\n    "code": "F25B2339/047",\n    "first": false,\n    "inventive": false,\n    "tree": []\n  },\n  {\n    "code": "F24D17/02",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "F25B2400/061",\n    "first": false,\n    "inventive": false,\n    "tree": []\n  },\n  {\n    "code": "Y02B10/70",\n    "first": false,\n    "inventive": false,\n    "tree": []\n  },\n  {\n    "code": "F24D2200/20",\n    "first": false,\n    "inventive": false,\n    "tree": []\n  },\n  {\n    "code": "Y02B30/52",\n    "first": false,\n    "inventive": false,\n    "tree": []\n  },\n  {\n    "code": "F24D17/0005",\n    "first": true,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "Y02B30/18",\n    "first": false,\n    "inventive": false,\n    "tree": []\n  },\n  {\n    "code": "F24D2200/123",\n    "first": false,\n    "inventive": false,\n    "tree": []\n  }\n]'}, {'grant_date': '8th April 2019', 'Patents_info': 'The DK patent filing (application number DK-14835716-T) is owned by UNIV OSLO HF and has pub. number DK-3069138-T3.', 'cpc': '[\n  {\n    "code": "G01N33/505",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "G01N33/56977",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "G01N33/56977",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "A61K2039/572",\n    "first": false,\n    "inventive": false,\n    "tree": []\n  },\n  {\n    "code": "A61K39/39",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "G01N2333/70539",\n    "first": false,\n    "inventive": false,\n    "tree": []\n  },\n  {\n    "code": "A61K2039/55527",\n    "first": false,\n    "inventive": false,\n    "tree": []\n  },\n  {\n    "code": "C07K14/70503",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "C07K14/70539",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "A61K2039/5158",\n    "first": false,\n    "inventive": false,\n    "tree": []\n  },\n  {\n    "code": "A61K39/0011",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "G01N33/505",\n    "first": true,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "A61K39/0011",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "A61K2039/5158",\n    "first": false,\n    "inventive": false,\n    "tree": []\n  }\n]'}, {'grant_date': '2019, May 30th', 'Patents_info': 'The RU patent application (ID RU-2018146701-U) is held by [] and has publication no. RU-189707-U1.', 'cpc': '[\n  {\n    "code": "B60P1/48",\n    "first": true,\n    "inventive": true,\n    "tree": []\n  }\n]'}, {'grant_date': '22nd May 2019', 'Patents_info': 'The ES patent application (ID ES-11727548-T) is assigned to LOHR IND and has pub. number ES-2713511-T3.', 'cpc': '[\n  {\n    "code": "B61D3/04",\n    "first": true,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "B61D3/182",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "B61D3/04",\n    "first": true,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "B61D3/16",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "Y02T30/00",\n    "first": false,\n    "inventive": false,\n    "tree": []\n  }\n]'}, {'grant_date': '2019 on Nov 14th', 'Patents_info': 'In RU, the patent filing (application no. RU-2019124341-U) is owned by [] and has pub. number RU-193787-U1.', 'cpc': '[\n  {\n    "code": "F16K17/192",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "F16L43/00",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  }\n]'}], 'var_functions.query_db:6': 'file_storage/functions.query_db:6.json', 'var_functions.query_db:8': 'file_storage/functions.query_db:8.json', 'var_functions.query_db:10': [{'grant_date': '10th Apr 1883'}, {'grant_date': '10th Apr 1888'}, {'grant_date': '10th Apr 1923'}, {'grant_date': '10th Apr 1945'}, {'grant_date': '10th Apr 1952'}, {'grant_date': '10th Apr 1969'}, {'grant_date': '10th Apr 1974'}, {'grant_date': '10th Apr 1979'}, {'grant_date': '10th Apr 1980'}, {'grant_date': '10th Apr 1984'}, {'grant_date': '10th Apr 1990'}, {'grant_date': '10th Apr 2001'}, {'grant_date': '10th Apr 2006'}, {'grant_date': '10th Apr 2008'}, {'grant_date': '10th Apr 2018'}, {'grant_date': '10th Apr 2019'}, {'grant_date': '10th Apr 2020'}, {'grant_date': '10th Apr 2023'}, {'grant_date': '10th Apr 2024'}, {'grant_date': '10th April 1956'}, {'grant_date': '10th April 1962'}, {'grant_date': '10th April 1964'}, {'grant_date': '10th April 1973'}, {'grant_date': '10th April 1979'}, {'grant_date': '10th April 1990'}, {'grant_date': '10th April 2000'}, {'grant_date': '10th April 2001'}, {'grant_date': '10th April 2002'}, {'grant_date': '10th April 2005'}, {'grant_date': '10th April 2007'}, {'grant_date': '10th April 2012'}, {'grant_date': '10th April 2013'}, {'grant_date': '10th April 2014'}, {'grant_date': '10th April 2018'}, {'grant_date': '10th April 2020'}, {'grant_date': '10th April 2023'}, {'grant_date': '10th Aug 1948'}, {'grant_date': '10th Aug 1954'}, {'grant_date': '10th Aug 1959'}, {'grant_date': '10th Aug 1970'}, {'grant_date': '10th Aug 1973'}, {'grant_date': '10th Aug 1974'}, {'grant_date': '10th Aug 1976'}, {'grant_date': '10th Aug 1993'}, {'grant_date': '10th Aug 2004'}, {'grant_date': '10th Aug 2006'}, {'grant_date': '10th Aug 2011'}, {'grant_date': '10th Aug 2014'}, {'grant_date': '10th Aug 2016'}, {'grant_date': '10th Aug 2018'}], 'var_functions.execute_python:16': {'status': 'checked'}, 'var_functions.execute_python:18': {'variables': ['json', 'var', 'var_functions.execute_python:16', 'var_functions.list_db:0', 'var_functions.query_db:10', 'var_functions.query_db:2', 'var_functions.query_db:5', 'var_functions.query_db:6', 'var_functions.query_db:8']}, 'var_functions.execute_python:26': {'total_german_2019': 20, 'second_half_german_2019': 21}, 'var_functions.execute_python:30': {'total_patents': 21, 'unique_level4': 111, 'top_level4': [['H04W52/02', 12], ['C04B2235/32', 8], ['B29C2049/58', 7], ['H04L1/18', 6], ['C04B2235/66', 6], ['C04B2235/65', 6], ['C04B35/64', 6], ['G02B23/24', 5], ['H04L5/00', 4], ['H04L1/16', 4], ['A61F5/01', 4], ['C04B2235/54', 4], ['F02D41/20', 3], ['H04W72/21', 3], ['H04W72/56', 3], ['H04W72/04', 3], ['F16C33/46', 3], ['F24B5/02', 3], ['F23L15/04', 3], ['F23L1/00', 3]]}, 'var_functions.query_db:34': [{'symbol': 'F24B5/02', 'level': '8.0', 'titleFull': 'Combustion-air or flue-gas circulation in or around stoves or ranges in or around stoves'}, {'symbol': 'H04L1/16', 'level': '9.0', 'titleFull': 'Arrangements for detecting or preventing errors in the information received by using return channel in which the return channel carries supervisory signals, e.g. repetition request signals'}, {'symbol': 'H04L1/18', 'level': '10.0', 'titleFull': 'Automatic repetition systems, e.g. Van Duuren systems'}, {'symbol': 'C04B2235/32', 'level': '10.0', 'titleFull': 'Metal oxides, mixed metal oxides, or oxide-forming salts thereof, e.g. carbonates, nitrates, (oxy)hydroxides, chlorides'}, {'symbol': 'C04B2235/54', 'level': '10.0', 'titleFull': 'Particle size related information'}, {'symbol': 'F23L1/00', 'level': '7.0', 'titleFull': 'Passages or apertures for delivering primary air for combustion\xa0'}, {'symbol': 'H04L5/00', 'level': '7.0', 'titleFull': 'Arrangements affording multiple use of the transmission path'}, {'symbol': 'A61F5/01', 'level': '8.0', 'titleFull': 'Orthopaedic devices, e.g. splints, casts or braces'}, {'symbol': 'C04B2235/65', 'level': '8.0', 'titleFull': 'Aspects relating to heat treatments of ceramic bodies such as green ceramics or pre-sintered ceramics, e.g. burning, sintering or melting processes'}, {'symbol': 'C04B2235/66', 'level': '9.0', 'titleFull': 'Specific sintering techniques, e.g. centrifugal sintering'}, {'symbol': 'F02D41/20', 'level': '8.0', 'titleFull': 'Output circuits, e.g. for controlling currents in command coils'}, {'symbol': 'F23L15/04', 'level': '8.0', 'titleFull': 'Arrangements of recuperators'}, {'symbol': 'G02B23/24', 'level': '8.0', 'titleFull': 'Instruments or systems for viewing the inside of hollow bodies, e.g. fibrescopes'}, {'symbol': 'H04W52/02', 'level': '8.0', 'titleFull': 'Power saving arrangements'}, {'symbol': 'H04W72/04', 'level': '8.0', 'titleFull': 'Wireless resource allocation'}, {'symbol': 'F16C33/46', 'level': '9.0', 'titleFull': 'Cages for rollers or needles'}, {'symbol': 'H04W72/21', 'level': '9.0', 'titleFull': 'Control channels or signalling for resource management in the uplink direction of a wireless link, i.e. towards the network'}, {'symbol': 'H04W72/56', 'level': '9.0', 'titleFull': 'Allocation or scheduling criteria for wireless resources based on priority criteria'}, {'symbol': 'C04B35/64', 'level': '9.0', 'titleFull': 'Burning or sintering processes'}]}

exec(code, env_args)
