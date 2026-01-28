code = """import json
import re
import os

# Load patent data
patent_file = 'var_functions.query_db:0.json'
if not os.path.exists(patent_file):
    print('File does not exist:', patent_file)
else:
    with open(patent_file, 'r') as f:
        patents = json.load(f)
    
    print(f'Loaded {len(patents)} patents successfully')

# Filter for German patents in second half 2019
german_h2_2019 = []
month_indicators = ['July', 'August', 'September', 'October', 'November', 'December',
                    'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']

for p in patents:
    # Check German
    if 'from DE' not in p['Patents_info']:
        continue
    
    # Check 2019
    if '2019' not in p['grant_date']:
        continue
    
    # Check second half
    date_str = p['grant_date']
    has_second_half_month = any(m in date_str for m in month_indicators)
    
    if has_second_half_month:
        german_h2_2019.append(p)

print('German patents in second half 2019:', len(german_h2_2019))

# Extract CPC at level 4 and count by month
cpc_month_data = []
for patent in german_h2_2019:
    cpc_str = patent['cpc']
    if len(cpc_str) <= 10:
        continue
    
    try:
        cpc_list = json.loads(cpc_str)
        
        # Determine month (7-12)
        date_str = patent['grant_date']
        month_num = None
        for i, m in enumerate(['July', 'August', 'September', 'October', 'November', 'December']):
            if m in date_str:
                month_num = i + 7
                break
        if month_num is None:
            for i, m in enumerate(['Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']):
                if m in date_str:
                    month_num = i + 7
                    break
        if month_num is None:
            month_num = 7
        
        # Extract level 4 CPC codes
        for entry in cpc_list:
            code = entry.get('code', '')
            if code and '/' in code and ' ' not in code:
                parts = code.split('/')
                if len(parts[0]) >= 4 and len(parts[1]) >= 2:
                    level4 = parts[0][:4] + '/' + parts[1][:2]
                    cpc_month_data.append({'code': level4, 'month': month_num})
    except:
        continue

print('CPC level 4 entries:', len(cpc_month_data))

# Group by CPC code and month
from collections import defaultdict
cpc_groups = defaultdict(lambda: [0,0,0,0,0,0])  # July (7) to December (12)
for item in cpc_month_data:
    cpc_groups[item['code']][item['month']-7] += 1

print('Unique CPC level 4 codes:', len(cpc_groups))

# Calculate EMA for each CPC code
ema_results = []
for cpc_code, monthly_counts in cpc_groups.items():
    if sum(monthly_counts) == 0:
        continue
    
    # EMA calculation with smoothing factor 0.1
    ema = []
    if len(monthly_counts) > 0:
        ema.append(float(monthly_counts[0]))
        for i in range(1, len(monthly_counts)):
            new_ema = 0.1 * monthly_counts[i] + 0.9 * ema[-1]
            ema.append(new_ema)
    
    # Find best month (highest EMA)
    if ema:
        max_ema = max(ema)
        best_month_idx = ema.index(max_ema)
        best_month = best_month_idx + 7
        
        ema_results.append({
            'cpc_code': cpc_code,
            'monthly_counts': [int(x) for x in monthly_counts],
            'ema_values': [round(x, 2) for x in ema],
            'max_ema': max_ema,
            'best_month': best_month
        })

# Sort by max EMA descending
ema_results.sort(key=lambda x: x['max_ema'], reverse=True)

print('\nTop 10 CPC codes by Exponential Moving Average:')
for i in range(min(10, len(ema_results))):
    r = ema_results[i]
    print(f"{i+1}. {r['cpc_code']}: Max EMA = {r['max_ema']:.2f} in month {r['best_month']}")

# Prepare for CPC definition lookup
top_cpc_codes = [r['cpc_code'] for r in ema_results[:20]]
print('\nTop CPC codes to lookup:', top_cpc_codes[:10])

# Save results for later use
with open('german_patents_analysis.json', 'w') as f:
    json.dump({
        'german_h2_2019_total': len(german_h2_2019),
        'cpc_level4_entries': len(cpc_month_data),
        'unique_cpc_codes': len(cpc_groups),
        'top_cpc_codes': top_cpc_codes,
        'ema_results': ema_results[:20]
    }, f)"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.query_db:8': 'file_storage/functions.query_db:8.json', 'var_functions.query_db:12': [{'Patents_info': 'Patent application (no. DE-102013211266-A) from DE, assigned to IBM, with publication number DE-102013211266-B4.', 'grant_date': '14th Mar 2019'}, {'Patents_info': 'Application (no. RU-2018119076-A) from RU, assigned to FEDERALNOE GOSUDARSTVENNOE KAZENNOE VOENNOE OBRAZOVATELNOE UCHREZHDENIE VYSSHEGO OBRAZOVANIYA VOENNA, with publication no. RU-2694421-C1.', 'grant_date': '2019 on Jul 12th'}, {'Patents_info': 'GRIFOLS WORLDWIDE OPERATIONS LTD holds the AU patent filing (application no. AU-2015201496-A), with publication number AU-2015201496-B2.', 'grant_date': 'on October 31st, 2019'}, {'Patents_info': 'In US, the patent application (no. US-201314655932-A) is held by SERINPET LTDA REPRESENTACIONES Y SERVICIOS DE PETROLEOS and has pub. number US-10465517-B2.', 'grant_date': 'on November 5th, 2019'}, {'Patents_info': 'Patent application (number US-201415314902-A) from US, held by HEWLETT PACKARD ENTPR DEV LP, with publication number US-10176043-B2.', 'grant_date': '8th Jan 2019'}, {'Patents_info': 'The US patent application (ID US-201615761951-A) is held by HEWLETT PACKARD DEVELOPMENT CO and has publication no. US-10436614-B2.', 'grant_date': 'dated 8th October 2019'}, {'Patents_info': 'The US application (number US-201715791853-A) is owned by DENSO INT AMERICA INC and has pub. number US-10348153-B2.', 'grant_date': 'July the 9th, 2019'}, {'Patents_info': 'In US, the patent filing (application number US-201616068918-A) is owned by DENSO CORP and has publication no. US-10369965-B2.', 'grant_date': 'August the 6th, 2019'}, {'Patents_info': 'Application (no. US-201815940839-A) from US, held by GE VIDEO COMPRESSION LLC, with publication number US-10248966-B2.', 'grant_date': 'Apr 2nd, 2019'}, {'Patents_info': 'In DE, the application (number DE-102007032978-A) is held by HEIDELBERGER DRUCKMASCH AG and has publication number DE-102007032978-B4.', 'grant_date': 'dated 21st November 2019'}]}

exec(code, env_args)
