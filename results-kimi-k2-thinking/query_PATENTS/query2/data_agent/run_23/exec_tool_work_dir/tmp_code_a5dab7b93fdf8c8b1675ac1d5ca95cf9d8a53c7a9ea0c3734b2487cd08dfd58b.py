code = """import json
import re
import pandas as pd
import numpy as np
from collections import defaultdict

# Get the CPC definitions for level 4 groups
cpc_defs_file = locals()['var_functions.query_db:52']
with open(cpc_defs_file, 'r') as f:
    cpc_level4 = json.load(f)

# Create CPC group to title mapping
cpc_title_map = {item['symbol']: item['titleFull'] for item in cpc_level4}

# Get the multi-year German patents data
german_multi_file = locals()['var_functions.query_db:54']
with open(german_multi_file, 'r') as f:
    german_patents_multi = json.load(f)

print(f'Loaded {len(german_patents_multi)} German patents from multiple years')

# Extract CPC records for all available years
cpc_records = []
years_available = set()

for patent in german_patents_multi:
    patents_info = patent.get('Patents_info', '')
    grant_date = patent.get('grant_date', '')
    cpc_json_str = patent.get('cpc', '[]')
    
    try:
        if isinstance(cpc_json_str, str):
            cpc_list = json.loads(cpc_json_str)
        else:
            cpc_list = cpc_json_str
            
        year_match = re.search(r'(\d{4})', grant_date)
        year = int(year_match.group(1)) if year_match else None
        
        if year and 2017 <= year <= 2020:  # Focus on 2017-2020
            years_available.add(year)
            for cpc_entry in cpc_list:
                code = cpc_entry.get('code', '')
                if code and '/' in code:
                    main_class = code.split('/')[0]
                    if len(main_class) >= 4:
                        cpc_group = main_class[:4]
                        cpc_records.append({
                            'cpc_group': cpc_group,
                            'year': year
                        })
    except:
        continue

print(f'Years available: {sorted(years_available)}')
print(f'Total CPC records: {len(cpc_records)}')

# Count patents per CPC group per year
group_year_counts = defaultdict(lambda: defaultdict(int))
for record in cpc_records:
    group_year_counts[record['cpc_group']][record['year']] += 1

# Calculate exponential moving average for each group
# Formula: EMA_t = α * value_t + (1-α) * EMA_{t-1}
# With α = 0.1 (smoothing factor)
alpha = 0.1
results = []

for group, year_counts in group_year_counts.items():
    # Sort years
    sorted_years = sorted(year_counts.items())
    
    # Calculate EMA over the years
    ema = 0
    for i, (year, count) in enumerate(sorted_years):
        if i == 0:
            ema = count  # Initialize with first value
        else:
            ema = alpha * count + (1 - alpha) * ema
    
    # Find best year (highest count)
    best_year, max_count = max(year_counts.items(), key=lambda x: x[1])
    
    # Get title for this CPC group
    title = cpc_title_map.get(group, f'Title not available for {group}')
    
    results.append({
        'cpc_group': group,
        'full_title': title,
        'exponential_moving_average': round(ema, 2),
        'patent_count_best_year': max_count,
        'best_year': best_year
    })

# Sort by EMA descending
results.sort(key=lambda x: x['exponential_moving_average'], reverse=True)

print(f'Found {len(results)} CPC technology areas with EMA calculated')
print('\\nTop 10 by EMA:')
for i, r in enumerate(results[:10]):
    print(f"{i+1}. {r['cpc_group']}: EMA={r['exponential_moving_average']}, Best Year={r['best_year']} ({r['patent_count_best_year']} patents)")
    print(f"   {r['full_title'][:80]}...")

print('\\nResults focused on 2019 (patents granted in second half):')
# Filter for groups that have 2019 data (second half of 2019 was our original filter)
groups_with_2019 = [r for r in results if any(y == 2019 for y in group_year_counts[r['cpc_group']].keys())]
print(f'Groups with 2019 patents: {len(groups_with_2019)}')

print('__RESULT__:')
print(json.dumps(groups_with_2019[:15]))  # Top 15 groups with 2019 data"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.list_db:2': ['cpc_definition'], 'var_functions.query_db:6': [{'symbol': 'A01K2227/108', 'titleFull': 'Swine', 'level': '9.0'}, {'symbol': 'A01K2227/105', 'titleFull': 'Murine', 'level': '9.0'}, {'symbol': 'A01K2227/101', 'titleFull': 'Bovine', 'level': '9.0'}, {'symbol': 'A01K2227/107', 'titleFull': 'Rabbit', 'level': '9.0'}, {'symbol': 'A01K2227/103', 'titleFull': 'Ovine', 'level': '9.0'}], 'var_functions.execute_python:10': ['cpc_definition'], 'var_functions.query_db:12': 'file_storage/functions.query_db:12.json', 'var_functions.query_db:14': [{'Patents_info': 'The US patent application (no. US-201916389545-A) is assigned to MODERNATX INC and has pub. number US-10695419-B2.'}, {'Patents_info': 'Application (ID US-201916412740-A) from US, assigned to LEGACY RES AND DEVELOPMENT GROUP LLC, with publication no. US-10898606-B2.'}, {'Patents_info': 'TANDEM DIABETES CARE INC holds the US patent filing (app. number US-201916444452-A), with publication number US-10918785-B2.'}, {'Patents_info': 'In US, the patent filing (app. number US-201916560126-A) is belonging to DENSO CORP and has pub. number US-10897184-B2.'}, {'Patents_info': 'The US patent filing (app. number US-201916584394-A) is owned by DEPUY SYNTHES PRODUCTS INC and has publication no. US-11911287-B2.'}, {'Patents_info': 'The US patent application (number US-202016804108-A) is belonging to X DEV LLC and has pub. number US-10883891-B2.'}, {'Patents_info': 'TEDDER IND LLC holds the US patent application (number US-202016817994-A), with publication number US-11047644-B2.'}, {'Patents_info': 'The US application (ID US-202016823065-A) is belonging to POWDER MOTION LABS LLC and has publication no. US-11407172-B2.'}, {'Patents_info': 'MEDEON BIODESIGN INC holds the US patent filing (application number US-202017015991-A), with publication no. US-11813010-B2.'}, {'Patents_info': 'The US patent application (ID US-202117151830-A) is belonging to DELPHI TECH IP LTD and has pub. number US-11745738-B2.'}], 'var_functions.query_db:16': 'file_storage/functions.query_db:16.json', 'var_functions.query_db:18': [{'Patents_info': 'Patent application (no. DE-102013211266-A) from DE, assigned to IBM, with publication number DE-102013211266-B4.', 'grant_date': '14th Mar 2019'}, {'Patents_info': 'Application (no. RU-2018119076-A) from RU, assigned to FEDERALNOE GOSUDARSTVENNOE KAZENNOE VOENNOE OBRAZOVATELNOE UCHREZHDENIE VYSSHEGO OBRAZOVANIYA VOENNA, with publication no. RU-2694421-C1.', 'grant_date': '2019 on Jul 12th'}, {'Patents_info': 'GRIFOLS WORLDWIDE OPERATIONS LTD holds the AU patent filing (application no. AU-2015201496-A), with publication number AU-2015201496-B2.', 'grant_date': 'on October 31st, 2019'}, {'Patents_info': 'In US, the patent application (no. US-201314655932-A) is held by SERINPET LTDA REPRESENTACIONES Y SERVICIOS DE PETROLEOS and has pub. number US-10465517-B2.', 'grant_date': 'on November 5th, 2019'}, {'Patents_info': 'Patent application (number US-201415314902-A) from US, held by HEWLETT PACKARD ENTPR DEV LP, with publication number US-10176043-B2.', 'grant_date': '8th Jan 2019'}, {'Patents_info': 'The US patent application (ID US-201615761951-A) is held by HEWLETT PACKARD DEVELOPMENT CO and has publication no. US-10436614-B2.', 'grant_date': 'dated 8th October 2019'}, {'Patents_info': 'The US application (number US-201715791853-A) is owned by DENSO INT AMERICA INC and has pub. number US-10348153-B2.', 'grant_date': 'July the 9th, 2019'}, {'Patents_info': 'In US, the patent filing (application number US-201616068918-A) is owned by DENSO CORP and has publication no. US-10369965-B2.', 'grant_date': 'August the 6th, 2019'}, {'Patents_info': 'Application (no. US-201815940839-A) from US, held by GE VIDEO COMPRESSION LLC, with publication number US-10248966-B2.', 'grant_date': 'Apr 2nd, 2019'}, {'Patents_info': 'In DE, the application (number DE-102007032978-A) is held by HEIDELBERGER DRUCKMASCH AG and has publication number DE-102007032978-B4.', 'grant_date': 'dated 21st November 2019'}, {'Patents_info': 'The DE application (number DE-102009046500-A) is owned by LEAR CORP and has publication number DE-102009046500-B4.', 'grant_date': 'Mar 21st, 2019'}, {'Patents_info': 'The DE patent application (no. DE-102010042467-A) is owned by CONTINENTAL AUTOMOTIVE GMBH and has pub. number DE-102010042467-B4.', 'grant_date': '5th of December, 2019'}, {'Patents_info': 'In DE, the patent filing (application no. DE-112014003420-T) is assigned to TOYOTA MOTOR CO LTD and has publication number DE-112014003420-B4.', 'grant_date': '22nd of August, 2019'}, {'Patents_info': 'In DE, the patent filing (application number DE-102015221196-A) is owned by SCHOTT AG and has pub. number DE-102015221196-B4.', 'grant_date': 'September the 19th, 2019'}, {'Patents_info': 'DIEFFENBACHER GMBH MASCHINEN holds the DE patent application (number DE-102016119956-A), with publication number DE-102016119956-B4.', 'grant_date': 'on March 14th, 2019'}, {'Patents_info': 'The DE patent filing (application number DE-102018102700-A) is assigned to DIOGO CARLOS ALBERTO RAMOS and has pub. number DE-102018102700-B3.', 'grant_date': '28th Feb 2019'}, {'Patents_info': 'The DE application (number DE-102014111322-A) is owned by LEMKE SEBASTIAN and has publication no. DE-102014111322-B4.', 'grant_date': '17th of October, 2019'}, {'Patents_info': 'In DE, the patent application (no. DE-102014209298-A) is held by DENSO CORP and has publication number DE-102014209298-B4.', 'grant_date': 'on March 21st, 2019'}, {'Patents_info': 'SCHNEIDER KUNSTSTOFFWERKE GMBH holds the DE patent application (no. DE-102014112758-A), with publication number DE-102014112758-B4.', 'grant_date': '7th March 2019'}, {'Patents_info': 'BRUKER BIOSPIN GMBH holds the DE application (number DE-102015218019-A), with publication no. DE-102015218019-B4.', 'grant_date': 'February 28th, 2019'}], 'var_functions.execute_python:24': {'type': "<class 'list'>", 'length': 20, 'first_items': [{'Patents_info': 'Patent application (no. DE-102013211266-A) from DE, assigned to IBM, with publication number DE-102013211266-B4.', 'grant_date': '14th Mar 2019'}, {'Patents_info': 'Application (no. RU-2018119076-A) from RU, assigned to FEDERALNOE GOSUDARSTVENNOE KAZENNOE VOENNOE OBRAZOVATELNOE UCHREZHDENIE VYSSHEGO OBRAZOVANIYA VOENNA, with publication no. RU-2694421-C1.', 'grant_date': '2019 on Jul 12th'}, {'Patents_info': 'GRIFOLS WORLDWIDE OPERATIONS LTD holds the AU patent filing (application no. AU-2015201496-A), with publication number AU-2015201496-B2.', 'grant_date': 'on October 31st, 2019'}]}, 'var_functions.query_db:26': 'file_storage/functions.query_db:26.json', 'var_functions.query_db:28': 'file_storage/functions.query_db:28.json', 'var_functions.query_db:30': 'file_storage/functions.query_db:30.json', 'var_functions.execute_python:36': {'type': "<class 'str'>", 'is_file_path': True, 'data_count': 111}, 'var_functions.execute_python:38': {'total_cpc_records': 1250, 'dataframe_shape': [1250, 5], 'years_range': [2019, 2019], 'unique_cpc_groups': 134, 'sample_records': [{'patent_info': 'Application (ID DE-102012107580-A) from DE, held by KRAUSS MAFFEI WEGMANN GMBH & CO KG, with publication number DE-102012107580-C5.', 'grant_date': 'dated 10th October 2019', 'year': 2019, 'cpc_full_code': 'E02F3/7631', 'cpc_group': 'E02F'}, {'patent_info': 'Application (ID DE-102012107580-A) from DE, held by KRAUSS MAFFEI WEGMANN GMBH & CO KG, with publication number DE-102012107580-C5.', 'grant_date': 'dated 10th October 2019', 'year': 2019, 'cpc_full_code': 'E02F9/006', 'cpc_group': 'E02F'}, {'patent_info': 'Application (ID DE-102012107580-A) from DE, held by KRAUSS MAFFEI WEGMANN GMBH & CO KG, with publication number DE-102012107580-C5.', 'grant_date': 'dated 10th October 2019', 'year': 2019, 'cpc_full_code': 'E02F3/96', 'cpc_group': 'E02F'}, {'patent_info': 'Application (ID DE-102012107580-A) from DE, held by KRAUSS MAFFEI WEGMANN GMBH & CO KG, with publication number DE-102012107580-C5.', 'grant_date': 'dated 10th October 2019', 'year': 2019, 'cpc_full_code': 'F42B3/006', 'cpc_group': 'F42B'}, {'patent_info': 'Application (ID DE-102012107580-A) from DE, held by KRAUSS MAFFEI WEGMANN GMBH & CO KG, with publication number DE-102012107580-C5.', 'grant_date': 'dated 10th October 2019', 'year': 2019, 'cpc_full_code': 'F41H11/16', 'cpc_group': 'F41H'}]}, 'var_functions.query_db:40': 'file_storage/functions.query_db:40.json', 'var_functions.query_db:44': 'file_storage/functions.query_db:44.json', 'var_functions.execute_python:46': {'total_cpc_groups': 134, 'top_groups': [{'cpc_group': 'G06F', 'title': 'Title not found for G06F', 'patent_count_2019': 89, 'best_year': 2019}, {'cpc_group': 'B60K', 'title': 'ARRANGEMENT OR MOUNTING OF PROPULSION UNITS OR OF TRANSMISSIONS IN VEHICLES; ARRANGEMENT OR MOUNTING OF PLURAL DIVERSE PRIME-MOVERS IN VEHICLES; AUXILIARY DRIVES FOR VEHICLES; INSTRUMENTATION OR DASHBOARDS FOR VEHICLES; ARRANGEMENTS IN CONNECTION WITH COOLING, AIR INTAKE, GAS EXHAUST OR FUEL SUPPLY OF PROPULSION UNITS IN VEHICLES', 'patent_count_2019': 80, 'best_year': 2019}, {'cpc_group': 'C04B', 'title': 'LIME, MAGNESIA; SLAG; CEMENTS; COMPOSITIONS THEREOF, e.g. MORTARS, CONCRETE OR LIKE BUILDING MATERIALS; ARTIFICIAL STONE; CERAMICS; REFRACTORIES; TREATMENT OF NATURAL STONE', 'patent_count_2019': 58, 'best_year': 2019}, {'cpc_group': 'A61M', 'title': 'DEVICES FOR INTRODUCING MEDIA INTO, OR ONTO, THE BODY; DEVICES FOR TRANSDUCING BODY MEDIA OR FOR TAKING MEDIA FROM THE BODY; DEVICES FOR PRODUCING OR ENDING SLEEP OR STUPOR', 'patent_count_2019': 54, 'best_year': 2019}, {'cpc_group': 'H04L', 'title': 'Title not found for H04L', 'patent_count_2019': 53, 'best_year': 2019}, {'cpc_group': 'B29C', 'title': 'SHAPING OR JOINING OF PLASTICS; SHAPING OF MATERIAL IN A PLASTIC STATE, NOT OTHERWISE PROVIDED FOR; AFTER-TREATMENT OF THE SHAPED PRODUCTS, e.g. REPAIRING', 'patent_count_2019': 46, 'best_year': 2019}, {'cpc_group': 'B60N', 'title': 'SEATS SPECIALLY ADAPTED FOR VEHICLES; VEHICLE PASSENGER ACCOMMODATION NOT OTHERWISE PROVIDED FOR', 'patent_count_2019': 46, 'best_year': 2019}, {'cpc_group': 'B01L', 'title': 'CHEMICAL OR PHYSICAL LABORATORY APPARATUS FOR GENERAL USE', 'patent_count_2019': 42, 'best_year': 2019}, {'cpc_group': 'G02B', 'title': 'Title not found for G02B', 'patent_count_2019': 38, 'best_year': 2019}, {'cpc_group': 'G01N', 'title': 'Title not found for G01N', 'patent_count_2019': 38, 'best_year': 2019}, {'cpc_group': 'H04W', 'title': 'Title not found for H04W', 'patent_count_2019': 35, 'best_year': 2019}, {'cpc_group': 'B01J', 'title': 'CHEMICAL OR PHYSICAL PROCESSES, e.g. CATALYSIS OR COLLOID CHEMISTRY; THEIR RELEVANT APPARATUS', 'patent_count_2019': 32, 'best_year': 2019}, {'cpc_group': 'A61B', 'title': 'DIAGNOSIS; SURGERY; IDENTIFICATION', 'patent_count_2019': 31, 'best_year': 2019}, {'cpc_group': 'F17C', 'title': 'VESSELS FOR CONTAINING OR STORING COMPRESSED, LIQUEFIED OR SOLIDIFIED GASES; FIXED-CAPACITY GAS-HOLDERS; FILLING VESSELS WITH, OR DISCHARGING FROM VESSELS, COMPRESSED, LIQUEFIED, OR SOLIDIFIED GASES', 'patent_count_2019': 30, 'best_year': 2019}, {'cpc_group': 'B42D', 'title': 'BOOKS; BOOK COVERS; LOOSE LEAVES; PRINTED MATTER CHARACTERISED BY IDENTIFICATION OR SECURITY FEATURES; PRINTED MATTER OF SPECIAL FORMAT OR STYLE NOT OTHERWISE PROVIDED FOR; DEVICES FOR USE THEREWITH AND NOT OTHERWISE PROVIDED FOR; MOVABLE-STRIP WRITING OR READING APPARATUS', 'patent_count_2019': 18, 'best_year': 2019}, {'cpc_group': 'H02K', 'title': 'Title not found for H02K', 'patent_count_2019': 16, 'best_year': 2019}, {'cpc_group': 'H01L', 'title': 'Title not found for H01L', 'patent_count_2019': 16, 'best_year': 2019}, {'cpc_group': 'F02D', 'title': 'CONTROLLING COMBUSTION ENGINES', 'patent_count_2019': 16, 'best_year': 2019}, {'cpc_group': 'A61K', 'title': 'PREPARATIONS FOR MEDICAL, DENTAL OR TOILETRY PURPOSES', 'patent_count_2019': 15, 'best_year': 2019}, {'cpc_group': 'F21V', 'title': 'FUNCTIONAL FEATURES OR DETAILS OF LIGHTING DEVICES OR SYSTEMS THEREOF; STRUCTURAL COMBINATIONS OF LIGHTING DEVICES WITH OTHER ARTICLES, NOT OTHERWISE PROVIDED FOR', 'patent_count_2019': 14, 'best_year': 2019}], 'summary': {'max_patents': 89, 'avg_patents': 9.328358208955224, 'total_groups': 134}}, 'var_functions.query_db:48': 'file_storage/functions.query_db:48.json', 'var_functions.execute_python:50': [{'cpc_group': 'G06F', 'full_title': 'Title not available for G06F', 'patent_count_2019': 89, 'exponential_moving_average': 89.0, 'best_year': 2019}, {'cpc_group': 'B60K', 'full_title': 'ARRANGEMENT OR MOUNTING OF PROPULSION UNITS OR OF TRANSMISSIONS IN VEHICLES; ARRANGEMENT OR MOUNTING OF PLURAL DIVERSE PRIME-MOVERS IN VEHICLES; AUXILIARY DRIVES FOR VEHICLES; INSTRUMENTATION OR DASHBOARDS FOR VEHICLES; ARRANGEMENTS IN CONNECTION WITH COOLING, AIR INTAKE, GAS EXHAUST OR FUEL SUPPLY OF PROPULSION UNITS IN VEHICLES', 'patent_count_2019': 80, 'exponential_moving_average': 80.0, 'best_year': 2019}, {'cpc_group': 'C04B', 'full_title': 'LIME, MAGNESIA; SLAG; CEMENTS; COMPOSITIONS THEREOF, e.g. MORTARS, CONCRETE OR LIKE BUILDING MATERIALS; ARTIFICIAL STONE; CERAMICS; REFRACTORIES; TREATMENT OF NATURAL STONE', 'patent_count_2019': 58, 'exponential_moving_average': 58.0, 'best_year': 2019}, {'cpc_group': 'A61M', 'full_title': 'DEVICES FOR INTRODUCING MEDIA INTO, OR ONTO, THE BODY; DEVICES FOR TRANSDUCING BODY MEDIA OR FOR TAKING MEDIA FROM THE BODY; DEVICES FOR PRODUCING OR ENDING SLEEP OR STUPOR', 'patent_count_2019': 54, 'exponential_moving_average': 54.0, 'best_year': 2019}, {'cpc_group': 'H04L', 'full_title': 'Title not available for H04L', 'patent_count_2019': 53, 'exponential_moving_average': 53.0, 'best_year': 2019}, {'cpc_group': 'B29C', 'full_title': 'SHAPING OR JOINING OF PLASTICS; SHAPING OF MATERIAL IN A PLASTIC STATE, NOT OTHERWISE PROVIDED FOR; AFTER-TREATMENT OF THE SHAPED PRODUCTS, e.g. REPAIRING', 'patent_count_2019': 46, 'exponential_moving_average': 46.0, 'best_year': 2019}, {'cpc_group': 'B60N', 'full_title': 'SEATS SPECIALLY ADAPTED FOR VEHICLES; VEHICLE PASSENGER ACCOMMODATION NOT OTHERWISE PROVIDED FOR', 'patent_count_2019': 46, 'exponential_moving_average': 46.0, 'best_year': 2019}, {'cpc_group': 'B01L', 'full_title': 'CHEMICAL OR PHYSICAL LABORATORY APPARATUS FOR GENERAL USE', 'patent_count_2019': 42, 'exponential_moving_average': 42.0, 'best_year': 2019}, {'cpc_group': 'G01N', 'full_title': 'Title not available for G01N', 'patent_count_2019': 38, 'exponential_moving_average': 38.0, 'best_year': 2019}, {'cpc_group': 'G02B', 'full_title': 'Title not available for G02B', 'patent_count_2019': 38, 'exponential_moving_average': 38.0, 'best_year': 2019}, {'cpc_group': 'H04W', 'full_title': 'Title not available for H04W', 'patent_count_2019': 35, 'exponential_moving_average': 35.0, 'best_year': 2019}, {'cpc_group': 'B01J', 'full_title': 'CHEMICAL OR PHYSICAL PROCESSES, e.g. CATALYSIS OR COLLOID CHEMISTRY; THEIR RELEVANT APPARATUS', 'patent_count_2019': 32, 'exponential_moving_average': 32.0, 'best_year': 2019}, {'cpc_group': 'A61B', 'full_title': 'DIAGNOSIS; SURGERY; IDENTIFICATION', 'patent_count_2019': 31, 'exponential_moving_average': 31.0, 'best_year': 2019}, {'cpc_group': 'F17C', 'full_title': 'VESSELS FOR CONTAINING OR STORING COMPRESSED, LIQUEFIED OR SOLIDIFIED GASES; FIXED-CAPACITY GAS-HOLDERS; FILLING VESSELS WITH, OR DISCHARGING FROM VESSELS, COMPRESSED, LIQUEFIED, OR SOLIDIFIED GASES', 'patent_count_2019': 30, 'exponential_moving_average': 30.0, 'best_year': 2019}, {'cpc_group': 'B42D', 'full_title': 'BOOKS; BOOK COVERS; LOOSE LEAVES; PRINTED MATTER CHARACTERISED BY IDENTIFICATION OR SECURITY FEATURES; PRINTED MATTER OF SPECIAL FORMAT OR STYLE NOT OTHERWISE PROVIDED FOR; DEVICES FOR USE THEREWITH AND NOT OTHERWISE PROVIDED FOR; MOVABLE-STRIP WRITING OR READING APPARATUS', 'patent_count_2019': 18, 'exponential_moving_average': 18.0, 'best_year': 2019}], 'var_functions.query_db:52': [{'symbol': 'G01N', 'titleFull': 'INVESTIGATING OR ANALYSING MATERIALS BY DETERMINING THEIR CHEMICAL OR PHYSICAL PROPERTIES'}, {'symbol': 'H04L', 'titleFull': 'TRANSMISSION OF DIGITAL INFORMATION, e.g. TELEGRAPHIC COMMUNICATION'}, {'symbol': 'G02B', 'titleFull': 'OPTICAL ELEMENTS, SYSTEMS OR APPARATUS'}, {'symbol': 'G06F', 'titleFull': 'ELECTRIC DIGITAL DATA PROCESSING'}, {'symbol': 'H01L', 'titleFull': 'SEMICONDUCTOR DEVICES NOT COVERED BY CLASS H10'}, {'symbol': 'H02K', 'titleFull': 'DYNAMO-ELECTRIC MACHINES'}, {'symbol': 'H04W', 'titleFull': 'WIRELESS COMMUNICATION NETWORKS'}], 'var_functions.query_db:54': 'file_storage/functions.query_db:54.json'}

exec(code, env_args)
