code = """import json
import pandas as pd
from collections import defaultdict

file_path = 'var_functions.query_db:140.json'

with open(file_path, 'r') as f:
    patents_data = json.load(f)

print(f"Total patents loaded: {len(patents_data)}")

# Filter German patents in second half 2019
german_h2_2019 = []
second_half_months = ['July', 'August', 'September', 'October', 'November', 'December',
                       'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']

for patent in patents_data:
    patents_info = patent['Patents_info']
    grant_date = patent['grant_date']
    
    # Verify German
    if not ('from DE' in patents_info or 'In DE,' in patents_info):
        continue
    
    # Verify 2019 and second half
    if '2019' not in grant_date:
        continue
        
    has_second_half_month = any(month in grant_date for month in second_half_months)
    if not has_second_half_month:
        continue
    
    german_h2_2019.append(patent)

print(f"German patents in H2 2019: {len(german_h2_2019)}")

# Extract CPC level 4 codes and count by month
cpc_monthly = defaultdict(lambda: [0, 0, 0, 0, 0, 0])  # July(0) to Dec(5)

for patent in german_h2_2019:
    cpc_str = patent['cpc']
    if len(cpc_str) < 10:
        continue
    
    try:
        cpc_list = json.loads(cpc_str)
    except:
        continue
    
    # Determine month
    grant_date = patent['grant_date']
    month_num = 7  # Default July
    
    full_months = ['July', 'August', 'September', 'October', 'November', 'December']
    abbr_months = ['Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
    
    for i, month in enumerate(full_months):
        if month in grant_date:
            month_num = i + 7
            break
    
    if month_num == 7:  # If not found, try abbreviations
        for i, month in enumerate(abbr_months):
            if month in grant_date:
                month_num = i + 7
                break
    
    # Extract CPC level 4 codes
    for entry in cpc_list:
        code = entry.get('code', '')
        if not code or '/' not in code or ' ' in code:
            continue
        
        parts = code.split('/')
        if len(parts) != 2:
            continue
        
        main_class = parts[0]
        subgroup = parts[1]
        
        if len(main_class) >= 4 and len(subgroup) >= 2:
            level4 = main_class[:4] + '/' + subgroup[:2]
            if 7 <= month_num <= 12:
                cpc_monthly[level4][month_num - 7] += 1

print(f"Unique CPC level 4 codes: {len(cpc_monthly)}")

# Calculate EMA (smoothing factor 0.1)
ema_results = []

for cpc_code, monthly_counts in cpc_monthly.items():
    if sum(monthly_counts) == 0:
        continue
    
    # Calculate exponential moving average
    ema_values = [float(monthly_counts[0])]
    for i in range(1, len(monthly_counts)):
        ema_val = 0.1 * monthly_counts[i] + 0.9 * ema_values[-1]
        ema_values.append(ema_val)
    
    max_ema = max(ema_values)
    best_month_index = ema_values.index(max_ema)
    best_month = best_month_index + 7
    
    ema_results.append({
        'cpc_code': cpc_code,
        'max_ema': round(max_ema, 2),
        'best_month': best_month,
        'monthly_counts': [int(x) for x in monthly_counts],
        'ema_values': [round(x, 2) for x in ema_values]
    })

# Sort by max EMA descending
ema_results.sort(key=lambda x: x['max_ema'], reverse=True)

print('\nTop 10 CPC codes by EMA:')
for i in range(min(10, len(ema_results))):
    r = ema_results[i]
    print(f"{i+1}. {r['cpc_code']}: EMA={r['max_ema']}, Best month={r['best_month']}, Monthly counts={r['monthly_counts']}")

# Get top 15 codes for definition lookup
top_codes = [r['cpc_code'] for r in ema_results[:15]]
print(f"\nTop 15 CPC codes for definition lookup: {top_codes}")"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.query_db:8': 'file_storage/functions.query_db:8.json', 'var_functions.query_db:12': [{'Patents_info': 'Patent application (no. DE-102013211266-A) from DE, assigned to IBM, with publication number DE-102013211266-B4.', 'grant_date': '14th Mar 2019'}, {'Patents_info': 'Application (no. RU-2018119076-A) from RU, assigned to FEDERALNOE GOSUDARSTVENNOE KAZENNOE VOENNOE OBRAZOVATELNOE UCHREZHDENIE VYSSHEGO OBRAZOVANIYA VOENNA, with publication no. RU-2694421-C1.', 'grant_date': '2019 on Jul 12th'}, {'Patents_info': 'GRIFOLS WORLDWIDE OPERATIONS LTD holds the AU patent filing (application no. AU-2015201496-A), with publication number AU-2015201496-B2.', 'grant_date': 'on October 31st, 2019'}, {'Patents_info': 'In US, the patent application (no. US-201314655932-A) is held by SERINPET LTDA REPRESENTACIONES Y SERVICIOS DE PETROLEOS and has pub. number US-10465517-B2.', 'grant_date': 'on November 5th, 2019'}, {'Patents_info': 'Patent application (number US-201415314902-A) from US, held by HEWLETT PACKARD ENTPR DEV LP, with publication number US-10176043-B2.', 'grant_date': '8th Jan 2019'}, {'Patents_info': 'The US patent application (ID US-201615761951-A) is held by HEWLETT PACKARD DEVELOPMENT CO and has publication no. US-10436614-B2.', 'grant_date': 'dated 8th October 2019'}, {'Patents_info': 'The US application (number US-201715791853-A) is owned by DENSO INT AMERICA INC and has pub. number US-10348153-B2.', 'grant_date': 'July the 9th, 2019'}, {'Patents_info': 'In US, the patent filing (application number US-201616068918-A) is owned by DENSO CORP and has publication no. US-10369965-B2.', 'grant_date': 'August the 6th, 2019'}, {'Patents_info': 'Application (no. US-201815940839-A) from US, held by GE VIDEO COMPRESSION LLC, with publication number US-10248966-B2.', 'grant_date': 'Apr 2nd, 2019'}, {'Patents_info': 'In DE, the application (number DE-102007032978-A) is held by HEIDELBERGER DRUCKMASCH AG and has publication number DE-102007032978-B4.', 'grant_date': 'dated 21st November 2019'}], 'var_functions.query_db:58': 'file_storage/functions.query_db:58.json', 'var_functions.query_db:62': 'file_storage/functions.query_db:62.json', 'var_functions.query_db:74': 'file_storage/functions.query_db:74.json', 'var_functions.query_db:82': 'file_storage/functions.query_db:82.json', 'var_functions.query_db:94': 'file_storage/functions.query_db:94.json', 'var_functions.query_db:96': [], 'var_functions.query_db:100': 'file_storage/functions.query_db:100.json', 'var_functions.query_db:102': 'file_storage/functions.query_db:102.json', 'var_functions.query_db:104': 'file_storage/functions.query_db:104.json', 'var_functions.query_db:110': 'file_storage/functions.query_db:110.json', 'var_functions.query_db:112': 'file_storage/functions.query_db:112.json', 'var_functions.query_db:114': 'file_storage/functions.query_db:114.json', 'var_functions.query_db:116': 'file_storage/functions.query_db:116.json', 'var_functions.query_db:122': 'file_storage/functions.query_db:122.json', 'var_functions.query_db:128': 'file_storage/functions.query_db:128.json', 'var_functions.query_db:132': 'file_storage/functions.query_db:132.json', 'var_functions.query_db:134': 'file_storage/functions.query_db:134.json', 'var_functions.query_db:136': 'file_storage/functions.query_db:136.json', 'var_functions.query_db:138': 'file_storage/functions.query_db:138.json', 'var_functions.query_db:140': 'file_storage/functions.query_db:140.json', 'var_functions.query_db:142': 'file_storage/functions.query_db:142.json', 'var_functions.query_db:144': 'file_storage/functions.query_db:144.json'}

exec(code, env_args)
