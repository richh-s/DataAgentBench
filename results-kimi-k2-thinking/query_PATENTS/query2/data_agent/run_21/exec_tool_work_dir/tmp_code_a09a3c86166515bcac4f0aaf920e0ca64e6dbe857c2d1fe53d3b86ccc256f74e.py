code = """import json
import os
from collections import defaultdict

# Load patent data from the file
patent_file = 'var_functions.query_db:74.json'
with open(patent_file, 'r') as f:
    patents_data = json.load(f)

print('Total patents loaded: ' + str(len(patents_data)))

# Filter German patents in second half 2019
german_h2_2019 = []
month_indicators = ['July', 'August', 'September', 'October', 'November', 'December']
month_abbrs = ['Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']

for patent in patents_data:
    patents_info = patent['Patents_info']
    grant_date = patent['grant_date']
    
    # Check if German patent
    is_german = False
    german_markers = ['from DE', 'In DE,', 'DE application', 'DE patent', 'DE-']
    for marker in german_markers:
        if marker in patents_info:
            is_german = True
            break
    
    if not is_german:
        continue
    
    # Check if 2019
    if '2019' not in grant_date:
        continue
    
    # Check if second half (July-December)
    is_second_half = False
    for month in month_indicators:
        if month in grant_date:
            is_second_half = True
            break
    
    if not is_second_half:
        for month in month_abbrs:
            if month in grant_date:
                is_second_half = True
                break
    
    if is_second_half:
        german_h2_2019.append(patent)

print('German patents in H2 2019: ' + str(len(german_h2_2019)))

# Now extract CPC levels and calculate EMA
cpc_monthly_data = defaultdict(lambda: [0, 0, 0, 0, 0, 0])  # July(7) to Dec(12)

for patent in german_h2_2019:
    cpc_str = patent['cpc']
    if len(cpc_str) < 10:
        continue
    
    try:
        cpc_list = json.loads(cpc_str)
    except:
        continue
    
    # Determine grant month
    month_num = 7
    for i, month in enumerate(month_indicators):
        if month in patent['grant_date']:
            month_num = i + 7
            break
    
    if month_num == 7:
        for i, month in enumerate(month_abbrs):
            if month in patent['grant_date']:
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
                cpc_monthly_data[level4_code][month_num - 7] += 1

print('Unique CPC level 4 codes: ' + str(len(cpc_monthly_data)))

# Calculate exponential moving average (smoothing factor 0.1)
ema_results = []

for cpc_code, monthly_counts in cpc_monthly_data.items():
    total_patents = sum(monthly_counts)
    if total_patents == 0:
        continue
    
    # Calculate EMA
    ema_values = []
    if len(monthly_counts) > 0:
        ema_values.append(float(monthly_counts[0]))
        for i in range(1, len(monthly_counts)):
            ema_val = 0.1 * monthly_counts[i] + 0.9 * ema_values[-1]
            ema_values.append(ema_val)
    
    # Find best month (highest EMA)
    max_ema = max(ema_values) if ema_values else 0
    best_month_index = ema_values.index(max_ema) if ema_values else 0
    best_month = best_month_index + 7
    
    ema_results.append({
        'cpc_code': cpc_code,
        'monthly_counts': monthly_counts,
        'ema_values': [round(x, 2) for x in ema_values],
        'max_ema': round(max_ema, 2),
        'best_month': best_month
    })

# Sort by max EMA descending
ema_results.sort(key=lambda x: x['max_ema'], reverse=True)

print('Total CPC groups with data: ' + str(len(ema_results)))
print('\nTop 15 CPC groups by EMA:')
for i in range(min(15, len(ema_results))):
    r = ema_results[i]
    print('  ' + str(i+1) + '. ' + r['cpc_code'] + ': EMA=' + str(r['max_ema']) + ', Best month=' + str(r['best_month']) + ', Monthly counts=' + str(r['monthly_counts']))

# Get top CPC codes for definition lookup
top_cpc_codes = [r['cpc_code'] for r in ema_results[:20]]
print('\nTop 20 CPC codes to lookup definitions: ' + str(top_cpc_codes))

# Save results for next step
with open('ema_analysis_results.json', 'w') as f:
    json.dump({
        'german_patents_count': len(german_h2_2019),
        'unique_cpc_codes': len(cpc_monthly_data),
        'top_cpc_codes': top_cpc_codes,
        'detailed_results': ema_results[:20]
    }, f)"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.query_db:8': 'file_storage/functions.query_db:8.json', 'var_functions.query_db:12': [{'Patents_info': 'Patent application (no. DE-102013211266-A) from DE, assigned to IBM, with publication number DE-102013211266-B4.', 'grant_date': '14th Mar 2019'}, {'Patents_info': 'Application (no. RU-2018119076-A) from RU, assigned to FEDERALNOE GOSUDARSTVENNOE KAZENNOE VOENNOE OBRAZOVATELNOE UCHREZHDENIE VYSSHEGO OBRAZOVANIYA VOENNA, with publication no. RU-2694421-C1.', 'grant_date': '2019 on Jul 12th'}, {'Patents_info': 'GRIFOLS WORLDWIDE OPERATIONS LTD holds the AU patent filing (application no. AU-2015201496-A), with publication number AU-2015201496-B2.', 'grant_date': 'on October 31st, 2019'}, {'Patents_info': 'In US, the patent application (no. US-201314655932-A) is held by SERINPET LTDA REPRESENTACIONES Y SERVICIOS DE PETROLEOS and has pub. number US-10465517-B2.', 'grant_date': 'on November 5th, 2019'}, {'Patents_info': 'Patent application (number US-201415314902-A) from US, held by HEWLETT PACKARD ENTPR DEV LP, with publication number US-10176043-B2.', 'grant_date': '8th Jan 2019'}, {'Patents_info': 'The US patent application (ID US-201615761951-A) is held by HEWLETT PACKARD DEVELOPMENT CO and has publication no. US-10436614-B2.', 'grant_date': 'dated 8th October 2019'}, {'Patents_info': 'The US application (number US-201715791853-A) is owned by DENSO INT AMERICA INC and has pub. number US-10348153-B2.', 'grant_date': 'July the 9th, 2019'}, {'Patents_info': 'In US, the patent filing (application number US-201616068918-A) is owned by DENSO CORP and has publication no. US-10369965-B2.', 'grant_date': 'August the 6th, 2019'}, {'Patents_info': 'Application (no. US-201815940839-A) from US, held by GE VIDEO COMPRESSION LLC, with publication number US-10248966-B2.', 'grant_date': 'Apr 2nd, 2019'}, {'Patents_info': 'In DE, the application (number DE-102007032978-A) is held by HEIDELBERGER DRUCKMASCH AG and has publication number DE-102007032978-B4.', 'grant_date': 'dated 21st November 2019'}], 'var_functions.query_db:58': 'file_storage/functions.query_db:58.json', 'var_functions.query_db:62': 'file_storage/functions.query_db:62.json', 'var_functions.query_db:74': 'file_storage/functions.query_db:74.json'}

exec(code, env_args)
