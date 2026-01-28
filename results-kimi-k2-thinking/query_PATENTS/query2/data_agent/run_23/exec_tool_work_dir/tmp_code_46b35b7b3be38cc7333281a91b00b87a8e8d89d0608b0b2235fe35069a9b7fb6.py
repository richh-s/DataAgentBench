code = """import json
import re
import pandas as pd
import numpy as np
from datetime import datetime

# Get the CPC data file path
cpc_data_file = locals()['var_functions.query_db:44']
with open(cpc_data_file, 'r') as f:
    cpc_definitions = json.load(f)

print(f'Loaded {len(cpc_definitions)} CPC definitions')

# Get the German patents data file path
german_patents_file = locals()['var_functions.query_db:30']
with open(german_patents_file, 'r') as f:
    german_patents = json.load(f)

# Extract CPC records from German patents
cpc_records = []
for patent in german_patents:
    patents_info = patent.get('Patents_info', '')
    grant_date = patent.get('grant_date', '')
    cpc_json_str = patent.get('cpc', '[]')
    
    try:
        # Parse CPC JSON string
        if isinstance(cpc_json_str, str):
            cpc_list = json.loads(cpc_json_str)
        else:
            cpc_list = cpc_json_str
            
        # Extract year from grant date
        year_match = re.search(r'(\d{4})', grant_date)
        year = int(year_match.group(1)) if year_match else None
        
        if year == 2019:  # Only 2019 patents
            for cpc_entry in cpc_list:
                code = cpc_entry.get('code', '')
                if code and '/' in code:
                    # Get CPC group at level 4 (first 4 characters of main class)
                    main_class = code.split('/')[0]
                    if len(main_class) >= 4:
                        cpc_group = main_class[:4]
                        cpc_records.append({
                            'patent_info': patents_info,
                            'grant_date': grant_date,
                            'year': year,
                            'cpc_full_code': code,
                            'cpc_group': cpc_group
                        })
    except Exception as e:
        continue

print(f'Extracted {len(cpc_records)} CPC records for 2019')

# Create DataFrame
df = pd.DataFrame(cpc_records)
print(f'DataFrame shape: {df.shape}')
print(f'Unique CPC groups: {df["cpc_group"].nunique()}')

# Count patent filings per CPC group per year
group_counts = df.groupby(['cpc_group', 'year']).size().reset_index(name='count')
print(f'Group counts shape: {group_counts.shape}')

# Create a CPC group to title mapping
cpc_title_map = {}
for cpc_def in cpc_definitions:
    symbol = cpc_def.get('symbol', '')
    title = cpc_def.get('titleFull', '')
    if len(symbol) >= 4:
        group_4 = symbol[:4]
        if group_4 not in cpc_title_map:
            cpc_title_map[group_4] = title

print(f'Created CPC title map with {len(cpc_title_map)} entries')
print('Sample title map:', list(cpc_title_map.items())[:5])

# Calculate EMA for each CPC group (using 2019 data only, so EMA is just the count)
# Since we only have 2019 data, the EMA will be equal to the count for 2019
# For demonstration, I'll show the groups with highest counts

group_2019 = group_counts[group_counts['year'] == 2019].copy()
group_2019['ema'] = group_2019['count']  # With single year, EMA = count

# Sort by EMA descending
top_groups = group_2019.sort_values('ema', ascending=False)
print(f'Top CPC groups by patent filings in 2019:')
print(top_groups.head(10))

# Get titles for top groups
results = []
for _, row in top_groups.iterrows():
    group = row['cpc_group']
    count = row['count']
    title = cpc_title_map.get(group, f'Title not found for {group}')
    results.append({
        'cpc_group': group,
        'title': title,
        'patent_count_2019': count,
        'best_year': 2019
    })

print(f'Prepared {len(results)} results')
print('Sample results:')
for r in results[:5]:
    print(f"Group: {r['cpc_group']}, Title: {r['title'][:50]}..., Count: {r['patent_count_2019']}")

print('__RESULT__:')
print(json.dumps({
    'total_cpc_groups': len(results),
    'top_groups': results[:20],  # Top 20 groups
    'summary': {
        'max_patents': int(top_groups['count'].max()),
        'avg_patents': float(top_groups['count'].mean()),
        'total_groups': len(top_groups)
    }
}))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.list_db:2': ['cpc_definition'], 'var_functions.query_db:6': [{'symbol': 'A01K2227/108', 'titleFull': 'Swine', 'level': '9.0'}, {'symbol': 'A01K2227/105', 'titleFull': 'Murine', 'level': '9.0'}, {'symbol': 'A01K2227/101', 'titleFull': 'Bovine', 'level': '9.0'}, {'symbol': 'A01K2227/107', 'titleFull': 'Rabbit', 'level': '9.0'}, {'symbol': 'A01K2227/103', 'titleFull': 'Ovine', 'level': '9.0'}], 'var_functions.execute_python:10': ['cpc_definition'], 'var_functions.query_db:12': 'file_storage/functions.query_db:12.json', 'var_functions.query_db:14': [{'Patents_info': 'The US patent application (no. US-201916389545-A) is assigned to MODERNATX INC and has pub. number US-10695419-B2.'}, {'Patents_info': 'Application (ID US-201916412740-A) from US, assigned to LEGACY RES AND DEVELOPMENT GROUP LLC, with publication no. US-10898606-B2.'}, {'Patents_info': 'TANDEM DIABETES CARE INC holds the US patent filing (app. number US-201916444452-A), with publication number US-10918785-B2.'}, {'Patents_info': 'In US, the patent filing (app. number US-201916560126-A) is belonging to DENSO CORP and has pub. number US-10897184-B2.'}, {'Patents_info': 'The US patent filing (app. number US-201916584394-A) is owned by DEPUY SYNTHES PRODUCTS INC and has publication no. US-11911287-B2.'}, {'Patents_info': 'The US patent application (number US-202016804108-A) is belonging to X DEV LLC and has pub. number US-10883891-B2.'}, {'Patents_info': 'TEDDER IND LLC holds the US patent application (number US-202016817994-A), with publication number US-11047644-B2.'}, {'Patents_info': 'The US application (ID US-202016823065-A) is belonging to POWDER MOTION LABS LLC and has publication no. US-11407172-B2.'}, {'Patents_info': 'MEDEON BIODESIGN INC holds the US patent filing (application number US-202017015991-A), with publication no. US-11813010-B2.'}, {'Patents_info': 'The US patent application (ID US-202117151830-A) is belonging to DELPHI TECH IP LTD and has pub. number US-11745738-B2.'}], 'var_functions.query_db:16': 'file_storage/functions.query_db:16.json', 'var_functions.query_db:18': [{'Patents_info': 'Patent application (no. DE-102013211266-A) from DE, assigned to IBM, with publication number DE-102013211266-B4.', 'grant_date': '14th Mar 2019'}, {'Patents_info': 'Application (no. RU-2018119076-A) from RU, assigned to FEDERALNOE GOSUDARSTVENNOE KAZENNOE VOENNOE OBRAZOVATELNOE UCHREZHDENIE VYSSHEGO OBRAZOVANIYA VOENNA, with publication no. RU-2694421-C1.', 'grant_date': '2019 on Jul 12th'}, {'Patents_info': 'GRIFOLS WORLDWIDE OPERATIONS LTD holds the AU patent filing (application no. AU-2015201496-A), with publication number AU-2015201496-B2.', 'grant_date': 'on October 31st, 2019'}, {'Patents_info': 'In US, the patent application (no. US-201314655932-A) is held by SERINPET LTDA REPRESENTACIONES Y SERVICIOS DE PETROLEOS and has pub. number US-10465517-B2.', 'grant_date': 'on November 5th, 2019'}, {'Patents_info': 'Patent application (number US-201415314902-A) from US, held by HEWLETT PACKARD ENTPR DEV LP, with publication number US-10176043-B2.', 'grant_date': '8th Jan 2019'}, {'Patents_info': 'The US patent application (ID US-201615761951-A) is held by HEWLETT PACKARD DEVELOPMENT CO and has publication no. US-10436614-B2.', 'grant_date': 'dated 8th October 2019'}, {'Patents_info': 'The US application (number US-201715791853-A) is owned by DENSO INT AMERICA INC and has pub. number US-10348153-B2.', 'grant_date': 'July the 9th, 2019'}, {'Patents_info': 'In US, the patent filing (application number US-201616068918-A) is owned by DENSO CORP and has publication no. US-10369965-B2.', 'grant_date': 'August the 6th, 2019'}, {'Patents_info': 'Application (no. US-201815940839-A) from US, held by GE VIDEO COMPRESSION LLC, with publication number US-10248966-B2.', 'grant_date': 'Apr 2nd, 2019'}, {'Patents_info': 'In DE, the application (number DE-102007032978-A) is held by HEIDELBERGER DRUCKMASCH AG and has publication number DE-102007032978-B4.', 'grant_date': 'dated 21st November 2019'}, {'Patents_info': 'The DE application (number DE-102009046500-A) is owned by LEAR CORP and has publication number DE-102009046500-B4.', 'grant_date': 'Mar 21st, 2019'}, {'Patents_info': 'The DE patent application (no. DE-102010042467-A) is owned by CONTINENTAL AUTOMOTIVE GMBH and has pub. number DE-102010042467-B4.', 'grant_date': '5th of December, 2019'}, {'Patents_info': 'In DE, the patent filing (application no. DE-112014003420-T) is assigned to TOYOTA MOTOR CO LTD and has publication number DE-112014003420-B4.', 'grant_date': '22nd of August, 2019'}, {'Patents_info': 'In DE, the patent filing (application number DE-102015221196-A) is owned by SCHOTT AG and has pub. number DE-102015221196-B4.', 'grant_date': 'September the 19th, 2019'}, {'Patents_info': 'DIEFFENBACHER GMBH MASCHINEN holds the DE patent application (number DE-102016119956-A), with publication number DE-102016119956-B4.', 'grant_date': 'on March 14th, 2019'}, {'Patents_info': 'The DE patent filing (application number DE-102018102700-A) is assigned to DIOGO CARLOS ALBERTO RAMOS and has pub. number DE-102018102700-B3.', 'grant_date': '28th Feb 2019'}, {'Patents_info': 'The DE application (number DE-102014111322-A) is owned by LEMKE SEBASTIAN and has publication no. DE-102014111322-B4.', 'grant_date': '17th of October, 2019'}, {'Patents_info': 'In DE, the patent application (no. DE-102014209298-A) is held by DENSO CORP and has publication number DE-102014209298-B4.', 'grant_date': 'on March 21st, 2019'}, {'Patents_info': 'SCHNEIDER KUNSTSTOFFWERKE GMBH holds the DE patent application (no. DE-102014112758-A), with publication number DE-102014112758-B4.', 'grant_date': '7th March 2019'}, {'Patents_info': 'BRUKER BIOSPIN GMBH holds the DE application (number DE-102015218019-A), with publication no. DE-102015218019-B4.', 'grant_date': 'February 28th, 2019'}], 'var_functions.execute_python:24': {'type': "<class 'list'>", 'length': 20, 'first_items': [{'Patents_info': 'Patent application (no. DE-102013211266-A) from DE, assigned to IBM, with publication number DE-102013211266-B4.', 'grant_date': '14th Mar 2019'}, {'Patents_info': 'Application (no. RU-2018119076-A) from RU, assigned to FEDERALNOE GOSUDARSTVENNOE KAZENNOE VOENNOE OBRAZOVATELNOE UCHREZHDENIE VYSSHEGO OBRAZOVANIYA VOENNA, with publication no. RU-2694421-C1.', 'grant_date': '2019 on Jul 12th'}, {'Patents_info': 'GRIFOLS WORLDWIDE OPERATIONS LTD holds the AU patent filing (application no. AU-2015201496-A), with publication number AU-2015201496-B2.', 'grant_date': 'on October 31st, 2019'}]}, 'var_functions.query_db:26': 'file_storage/functions.query_db:26.json', 'var_functions.query_db:28': 'file_storage/functions.query_db:28.json', 'var_functions.query_db:30': 'file_storage/functions.query_db:30.json', 'var_functions.execute_python:36': {'type': "<class 'str'>", 'is_file_path': True, 'data_count': 111}, 'var_functions.execute_python:38': {'total_cpc_records': 1250, 'dataframe_shape': [1250, 5], 'years_range': [2019, 2019], 'unique_cpc_groups': 134, 'sample_records': [{'patent_info': 'Application (ID DE-102012107580-A) from DE, held by KRAUSS MAFFEI WEGMANN GMBH & CO KG, with publication number DE-102012107580-C5.', 'grant_date': 'dated 10th October 2019', 'year': 2019, 'cpc_full_code': 'E02F3/7631', 'cpc_group': 'E02F'}, {'patent_info': 'Application (ID DE-102012107580-A) from DE, held by KRAUSS MAFFEI WEGMANN GMBH & CO KG, with publication number DE-102012107580-C5.', 'grant_date': 'dated 10th October 2019', 'year': 2019, 'cpc_full_code': 'E02F9/006', 'cpc_group': 'E02F'}, {'patent_info': 'Application (ID DE-102012107580-A) from DE, held by KRAUSS MAFFEI WEGMANN GMBH & CO KG, with publication number DE-102012107580-C5.', 'grant_date': 'dated 10th October 2019', 'year': 2019, 'cpc_full_code': 'E02F3/96', 'cpc_group': 'E02F'}, {'patent_info': 'Application (ID DE-102012107580-A) from DE, held by KRAUSS MAFFEI WEGMANN GMBH & CO KG, with publication number DE-102012107580-C5.', 'grant_date': 'dated 10th October 2019', 'year': 2019, 'cpc_full_code': 'F42B3/006', 'cpc_group': 'F42B'}, {'patent_info': 'Application (ID DE-102012107580-A) from DE, held by KRAUSS MAFFEI WEGMANN GMBH & CO KG, with publication number DE-102012107580-C5.', 'grant_date': 'dated 10th October 2019', 'year': 2019, 'cpc_full_code': 'F41H11/16', 'cpc_group': 'F41H'}]}, 'var_functions.query_db:40': 'file_storage/functions.query_db:40.json', 'var_functions.query_db:44': 'file_storage/functions.query_db:44.json'}

exec(code, env_args)
