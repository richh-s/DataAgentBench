code = """import json
import os
from collections import defaultdict

# Load the patent data
patent_file = 'var_functions.query_db:82.json'
with open(patent_file, 'r') as f:
    patents = json.load(f)

print('Loaded', len(patents), 'patent records')

# Filter for German patents in second half of 2019
german_h2_2019 = []

for patent in patents:
    patents_info = patent['Patents_info']
    grant_date = patent['grant_date']
    
    # Check if German patent
    is_german = False
    if 'from DE' in patents_info or 'In DE,' in patents_info:
        is_german = True
    
    if not is_german:
        continue
    
    # Check if 2019
    if '2019' not in grant_date:
        continue
    
    # Check if in second half (July-December)
    second_half_months = ['July', 'August', 'September', 'October', 'November', 'December']
    second_half_abbrs = ['Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
    
    in_second_half = False
    for month in second_half_months:
        if month in grant_date:
            in_second_half = True
            break
    
    if not in_second_half:
        for month in second_half_abbrs:
            if month in grant_date:
                in_second_half = True
                break
    
    if in_second_half:
        german_h2_2019.append(patent)

print('German patents in second half 2019: ' + str(len(german_h2_2019)))

# Extract CPC level 4 codes and count by month
cpc_monthly_counts = defaultdict(lambda: [0, 0, 0, 0, 0, 0])  # July to December (6 months)

for patent in german_h2_2019:
    cpc_str = patent['cpc']
    if len(cpc_str) < 10:
        continue
    
    try:
        cpc_list = json.loads(cpc_str)
    except:
        continue
    
    # Determine month
    month_num = 7  # Default to July
    date_str = patent['grant_date']
    
    for i, month in enumerate(['July', 'August', 'September', 'October', 'November', 'December']):
        if month in date_str:
            month_num = i + 7
            break
    
    if month_num == 7:  # If not found, try abbreviations
        for i, month in enumerate(['Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']):
            if month in date_str:
                month_num = i + 7
                break
    
    # Extract level 4 CPC codes
    for entry in cpc_list:
        code = entry.get('code', '')
        if not code or '/' not in code:
            continue
        
        parts = code.split('/')
        if len(parts) != 2:
            continue
        
        main_class = parts[0]
        subgroup = parts[1]
        
        if len(main_class) >= 4 and len(subgroup) >= 2:
            level4_code = main_class[:4] + '/' + subgroup[:2]
            if 7 <= month_num <= 12:
                cpc_monthly_counts[level4_code][month_num - 7] += 1

print('Unique CPC level 4 codes found: ' + str(len(cpc_monthly_counts)))

# Calculate Exponential Moving Average (EMA) with smoothing factor 0.1
ema_results = []

for cpc_code, monthly_counts in cpc_monthly_counts.items():
    if sum(monthly_counts) == 0:
        continue
    
    # Calculate EMA
    ema_values = []
    if len(monthly_counts) > 0:
        ema_values.append(float(monthly_counts[0]))
        for i in range(1, len(monthly_counts)):
            ema_val = 0.1 * monthly_counts[i] + 0.9 * ema_values[-1]
            ema_values.append(ema_val)
    
    # Find month with highest EMA
    if ema_values:
        max_ema = max(ema_values)
        best_month_index = ema_values.index(max_ema)
        best_month = best_month_index + 7  # Convert to actual month (7-12)
        
        ema_results.append({
            'cpc_level4_code': cpc_code,
            'monthly_counts': monthly_counts,
            'ema_values': [round(x, 2) for x in ema_values],
            'max_ema': round(max_ema, 2),
            'best_month': best_month
        })

# Sort by max EMA descending
ema_results.sort(key=lambda x: x['max_ema'], reverse=True)

print('\nTop 10 CPC codes by EMA:')
for i in range(min(10, len(ema_results))):
    r = ema_results[i]
    print(str(i+1) + '. ' + r['cpc_level4_code'] + ': Max EMA=' + str(r['max_ema']) + ', Best month=' + str(r['best_month']) + ', Monthly counts=' + str(r['monthly_counts']))

# Get top CPC codes for definition lookup
top_cpc_codes = [r['cpc_level4_code'] for r in ema_results[:20]]
print('\nTop 20 CPC codes to lookup: ' + str(top_cpc_codes))

# Save results for next step
with open('ema_analysis_results.json', 'w') as f:
    json.dump({
        'total_german_patents_h2_2019': len(german_h2_2019),
        'unique_cpc_level4_codes': len(cpc_monthly_counts),
        'top_cpc_codes': top_cpc_codes,
        'ema_results': ema_results[:20]
    }, f, indent=2)"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.query_db:8': 'file_storage/functions.query_db:8.json', 'var_functions.query_db:12': [{'Patents_info': 'Patent application (no. DE-102013211266-A) from DE, assigned to IBM, with publication number DE-102013211266-B4.', 'grant_date': '14th Mar 2019'}, {'Patents_info': 'Application (no. RU-2018119076-A) from RU, assigned to FEDERALNOE GOSUDARSTVENNOE KAZENNOE VOENNOE OBRAZOVATELNOE UCHREZHDENIE VYSSHEGO OBRAZOVANIYA VOENNA, with publication no. RU-2694421-C1.', 'grant_date': '2019 on Jul 12th'}, {'Patents_info': 'GRIFOLS WORLDWIDE OPERATIONS LTD holds the AU patent filing (application no. AU-2015201496-A), with publication number AU-2015201496-B2.', 'grant_date': 'on October 31st, 2019'}, {'Patents_info': 'In US, the patent application (no. US-201314655932-A) is held by SERINPET LTDA REPRESENTACIONES Y SERVICIOS DE PETROLEOS and has pub. number US-10465517-B2.', 'grant_date': 'on November 5th, 2019'}, {'Patents_info': 'Patent application (number US-201415314902-A) from US, held by HEWLETT PACKARD ENTPR DEV LP, with publication number US-10176043-B2.', 'grant_date': '8th Jan 2019'}, {'Patents_info': 'The US patent application (ID US-201615761951-A) is held by HEWLETT PACKARD DEVELOPMENT CO and has publication no. US-10436614-B2.', 'grant_date': 'dated 8th October 2019'}, {'Patents_info': 'The US application (number US-201715791853-A) is owned by DENSO INT AMERICA INC and has pub. number US-10348153-B2.', 'grant_date': 'July the 9th, 2019'}, {'Patents_info': 'In US, the patent filing (application number US-201616068918-A) is owned by DENSO CORP and has publication no. US-10369965-B2.', 'grant_date': 'August the 6th, 2019'}, {'Patents_info': 'Application (no. US-201815940839-A) from US, held by GE VIDEO COMPRESSION LLC, with publication number US-10248966-B2.', 'grant_date': 'Apr 2nd, 2019'}, {'Patents_info': 'In DE, the application (number DE-102007032978-A) is held by HEIDELBERGER DRUCKMASCH AG and has publication number DE-102007032978-B4.', 'grant_date': 'dated 21st November 2019'}], 'var_functions.query_db:58': 'file_storage/functions.query_db:58.json', 'var_functions.query_db:62': 'file_storage/functions.query_db:62.json', 'var_functions.query_db:74': 'file_storage/functions.query_db:74.json', 'var_functions.query_db:82': 'file_storage/functions.query_db:82.json'}

exec(code, env_args)
