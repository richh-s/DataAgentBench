code = """import json, re
from datetime import datetime

# Load patent data
patents_file_path = 'var_functions.query_db:0.json'
patents = json.load(open(patents_file_path))

# Define patterns for second half months
h2_patterns = ['July','August','September','October','November','December','Jul','Aug','Sep','Oct','Nov','Dec']

# Filter German patents in H2 2019
german_h2_2019 = []
for p in patents:
    info = p['Patents_info']
    date = p['grant_date']
    if 'from DE' in info and '2019' in date and any(m in date for m in h2_patterns):
        german_h2_2019.append(p)

print('German H2 2019 patents count:', len(german_h2_2019))

# Extract CPC codes at level 4
cpc_level4_data = []
for patent in german_h2_2019:
    cpc_json_str = patent['cpc']
    try:
        cpc_list = json.loads(cpc_json_str)
        for entry in cpc_list:
            code = entry.get('code', '')
            if code.count('/') == 1 and code.count(' ') == 0:
                main_class, subgroup = code.split('/')
                if len(main_class) >= 4 and len(subgroup) >= 2:
                    level4_code = f"{main_class[:4]}/{subgroup[:2]}"
                    cpc_level4_data.append({
                        'cpc_code': code,
                        'cpc_level4': level4_code,
                        'grant_date': patent['grant_date'],
                        'patent_info': patent['Patents_info']
                    })
    except:
        continue

print('Total CPC level 4 entries:', len(cpc_level4_data))
print('Unique level 4 codes:', len(set(item['cpc_level4'] for item in cpc_level4_data)))

import pandas as pd

# Group by CPC level 4 code
cpc_groups = {}
for item in cpc_level4_data:
    level4 = item['cpc_level4']
    if level4 not in cpc_groups:
        cpc_groups[level4] = []
    # Extract month from grant date
    for month_name in h2_patterns:
        if month_name in item['grant_date']:
            month_num = h2_patterns.index(month_name) % 6 + 7  # Convert to month number (7-12)
            cpc_groups[level4].append({'month': month_num, 'year': 2019})
            break

print('\nCPC Level 4 groups with data:')
for code, patents in list(cpc_groups.items())[:10]:
    print(f"{code}: {len(patents)} patents")

# Calculate exponential moving averages for each CPC level 4 code
# For 2019 second half, we have months 7-12
import numpy as np

def calculate_ema(patent_counts, smoothing=0.1):
    if not patent_counts:
        return []
    ema = []
    # Start with first value
    if len(patent_counts) > 0:
        ema.append(patent_counts[0])
        # Calculate EMA for subsequent values
        for i in range(1, len(patent_counts)):
            ema_value = smoothing * patent_counts[i] + (1 - smoothing) * ema[-1]
            ema.append(ema_value)
    return ema

# For each CPC level 4 code, count patents by month (7-12 months of 2019)
cpc_results = []

for cpc_code, patents in cpc_groups.items():
    # Count patents per month (7-12)
    monthly_counts = [0] * 6  # Index 0 = July, 1 = August, ..., 5 = December
    for patent in patents:
        month = patent['month']
        if 7 <= month <= 12:
            monthly_counts[month - 7] += 1
    
    # Calculate EMA
    ema_values = calculate_ema(monthly_counts, smoothing=0.1)
    
    # Find month with highest EMA
    if ema_values:
        max_ema = max(ema_values)
        best_month_index = ema_values.index(max_ema)
        best_month = best_month_index + 7  # Convert back to actual month (7-12)
        
        cpc_results.append({
            'cpc_level4': cpc_code,
            'monthly_counts': monthly_counts,
            'ema_values': ema_values,
            'best_month': best_month,
            'max_ema': max_ema
        })

# Sort by max EMA descending
cpc_results.sort(key=lambda x: x['max_ema'], reverse=True)

print('\nTop CPC Level 4 codes by EMA:')
for i, result in enumerate(cpc_results[:15]):
    print(f"{i+1}. {result['cpc_level4']}: Max EMA = {result['max_ema']:.2f} in month {result['best_month']}")
    print(f"   Monthly counts: {result['monthly_counts']}")
    print(f"   EMA values: {[float(f'{v:.2f}') for v in result['ema_values']]}")

# Get CPC definitions for top results
print('\nGetting CPC definitions for top codes...')

# Extract unique CPC codes to query
top_cpc_codes = [result['cpc_level4'] for result in cpc_results[:10]]
print('Top CPC codes to query:', top_cpc_codes)"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.query_db:8': 'file_storage/functions.query_db:8.json', 'var_functions.query_db:12': [{'Patents_info': 'Patent application (no. DE-102013211266-A) from DE, assigned to IBM, with publication number DE-102013211266-B4.', 'grant_date': '14th Mar 2019'}, {'Patents_info': 'Application (no. RU-2018119076-A) from RU, assigned to FEDERALNOE GOSUDARSTVENNOE KAZENNOE VOENNOE OBRAZOVATELNOE UCHREZHDENIE VYSSHEGO OBRAZOVANIYA VOENNA, with publication no. RU-2694421-C1.', 'grant_date': '2019 on Jul 12th'}, {'Patents_info': 'GRIFOLS WORLDWIDE OPERATIONS LTD holds the AU patent filing (application no. AU-2015201496-A), with publication number AU-2015201496-B2.', 'grant_date': 'on October 31st, 2019'}, {'Patents_info': 'In US, the patent application (no. US-201314655932-A) is held by SERINPET LTDA REPRESENTACIONES Y SERVICIOS DE PETROLEOS and has pub. number US-10465517-B2.', 'grant_date': 'on November 5th, 2019'}, {'Patents_info': 'Patent application (number US-201415314902-A) from US, held by HEWLETT PACKARD ENTPR DEV LP, with publication number US-10176043-B2.', 'grant_date': '8th Jan 2019'}, {'Patents_info': 'The US patent application (ID US-201615761951-A) is held by HEWLETT PACKARD DEVELOPMENT CO and has publication no. US-10436614-B2.', 'grant_date': 'dated 8th October 2019'}, {'Patents_info': 'The US application (number US-201715791853-A) is owned by DENSO INT AMERICA INC and has pub. number US-10348153-B2.', 'grant_date': 'July the 9th, 2019'}, {'Patents_info': 'In US, the patent filing (application number US-201616068918-A) is owned by DENSO CORP and has publication no. US-10369965-B2.', 'grant_date': 'August the 6th, 2019'}, {'Patents_info': 'Application (no. US-201815940839-A) from US, held by GE VIDEO COMPRESSION LLC, with publication number US-10248966-B2.', 'grant_date': 'Apr 2nd, 2019'}, {'Patents_info': 'In DE, the application (number DE-102007032978-A) is held by HEIDELBERGER DRUCKMASCH AG and has publication number DE-102007032978-B4.', 'grant_date': 'dated 21st November 2019'}]}

exec(code, env_args)
