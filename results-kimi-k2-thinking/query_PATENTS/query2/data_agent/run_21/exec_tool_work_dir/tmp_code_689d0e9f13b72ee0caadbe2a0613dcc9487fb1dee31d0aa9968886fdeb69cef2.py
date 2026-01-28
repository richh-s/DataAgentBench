code = """import json

# Get the file path from the tool result
file_path = var_functions.query_db:0

# Load the patent data
with open(file_path, 'r') as f:
    patents = json.load(f)

print('Total patents loaded:', len(patents))

# Filter for German patents in second half 2019
german_h2_2019 = []
for p in patents:
    # Check if German patent
    if 'from DE' not in p['Patents_info']:
        continue
    
    # Check if 2019
    grant_date = p['grant_date']
    if '2019' not in grant_date:
        continue
    
    # Check if second half (July-December)
    date_upper = grant_date.upper()
    is_second_half = any(m in date_upper for m in ['JUL','AUG','SEP','OCT','NOV','DEC'])
    
    # Also check full month names
    if not is_second_half:
        is_second_half = any(m in grant_date for m in ['July','August','September','October','November','December'])
    
    if is_second_half:
        german_h2_2019.append(p)

print('German patents in H2 2019:', len(german_h2_2019))

# Extract CPC statistics
from collections import defaultdict
import numpy as np

# Count CPC codes at level 4
monthly_counts = defaultdict(lambda: np.zeros(6))  # 6 months: July-Dec

for patent in german_h2_2019:
    cpc_str = patent['cpc']
    if len(cpc_str) <= 10:
        continue
    
    cpc_list = json.loads(cpc_str)
    
    # Find month from grant date
    month_num = None
    for i, m in enumerate(['July','August','September','October','November','December']):
        if m in patent['grant_date']:
            month_num = i + 7
            break
    if month_num is None:
        for i, m in enumerate(['Jul','Aug','Sep','Oct','Nov','Dec']):
            if m in patent['grant_date']:
                month_num = i + 7
                break
    
    if month_num is None:
        month_num = 7  # Default to July
    
    for entry in cpc_list:
        code = entry.get('code', '')
        parts = code.split('/')
        if len(parts) == 2 and parts[0] and parts[1]:
            level4_code = parts[0][:4] + '/' + parts[1][:2]
            monthly_counts[level4_code][month_num - 7] += 1

print('Unique CPC level 4 codes found:', len(monthly_counts))

# Calculate exponential moving averages (smoothing factor 0.1)
results = []
for cpc_code, counts in monthly_counts.items():
    if sum(counts) == 0:
        continue
    
    ema_values = []
    if len(counts) > 0:
        ema_values.append(float(counts[0]))
        for i in range(1, len(counts)):
            ema_val = 0.1 * counts[i] + 0.9 * ema_values[-1]
            ema_values.append(ema_val)
    
    max_ema = max(ema_values) if ema_values else 0
    best_month_idx = ema_values.index(max_ema) if ema_values else 0
    best_month = best_month_idx + 7
    
    results.append({
        'cpc_level4': cpc_code,
        'max_ema': max_ema,
        'best_month': best_month,
        'monthly_counts': [int(x) for x in counts],
        'ema_values': [round(x, 2) for x in ema_values]
    })

# Sort by max EMA descending
results.sort(key=lambda x: x['max_ema'], reverse=True)

print('\nTop 10 CPC codes by EMA:')
for i in range(min(10, len(results))):
    r = results[i]
    print(f"{r['cpc_level4']}: Max EMA={r['max_ema']:.2f} in month {r['best_month']}")

# Get top CPC codes for definition lookup
top_cpc_codes = [r['cpc_level4'] for r in results[:20]]
print('\nTop CPC codes to get definitions:', top_cpc_codes)"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.query_db:8': 'file_storage/functions.query_db:8.json', 'var_functions.query_db:12': [{'Patents_info': 'Patent application (no. DE-102013211266-A) from DE, assigned to IBM, with publication number DE-102013211266-B4.', 'grant_date': '14th Mar 2019'}, {'Patents_info': 'Application (no. RU-2018119076-A) from RU, assigned to FEDERALNOE GOSUDARSTVENNOE KAZENNOE VOENNOE OBRAZOVATELNOE UCHREZHDENIE VYSSHEGO OBRAZOVANIYA VOENNA, with publication no. RU-2694421-C1.', 'grant_date': '2019 on Jul 12th'}, {'Patents_info': 'GRIFOLS WORLDWIDE OPERATIONS LTD holds the AU patent filing (application no. AU-2015201496-A), with publication number AU-2015201496-B2.', 'grant_date': 'on October 31st, 2019'}, {'Patents_info': 'In US, the patent application (no. US-201314655932-A) is held by SERINPET LTDA REPRESENTACIONES Y SERVICIOS DE PETROLEOS and has pub. number US-10465517-B2.', 'grant_date': 'on November 5th, 2019'}, {'Patents_info': 'Patent application (number US-201415314902-A) from US, held by HEWLETT PACKARD ENTPR DEV LP, with publication number US-10176043-B2.', 'grant_date': '8th Jan 2019'}, {'Patents_info': 'The US patent application (ID US-201615761951-A) is held by HEWLETT PACKARD DEVELOPMENT CO and has publication no. US-10436614-B2.', 'grant_date': 'dated 8th October 2019'}, {'Patents_info': 'The US application (number US-201715791853-A) is owned by DENSO INT AMERICA INC and has pub. number US-10348153-B2.', 'grant_date': 'July the 9th, 2019'}, {'Patents_info': 'In US, the patent filing (application number US-201616068918-A) is owned by DENSO CORP and has publication no. US-10369965-B2.', 'grant_date': 'August the 6th, 2019'}, {'Patents_info': 'Application (no. US-201815940839-A) from US, held by GE VIDEO COMPRESSION LLC, with publication number US-10248966-B2.', 'grant_date': 'Apr 2nd, 2019'}, {'Patents_info': 'In DE, the application (number DE-102007032978-A) is held by HEIDELBERGER DRUCKMASCH AG and has publication number DE-102007032978-B4.', 'grant_date': 'dated 21st November 2019'}]}

exec(code, env_args)
