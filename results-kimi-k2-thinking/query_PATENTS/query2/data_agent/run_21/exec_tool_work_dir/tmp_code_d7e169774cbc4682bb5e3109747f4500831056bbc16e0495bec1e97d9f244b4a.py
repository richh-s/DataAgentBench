code = """import json

# Load patent data
with open('var_functions.query_db:0.json', 'r') as f:
    patents = json.load(f)

print('Total patents:', len(patents))

# Find German patents in second half 2019
german_patents = []
for p in patents:
    if 'from DE' in p['Patents_info'] and '2019' in p['grant_date']:
        date = p['grant_date']
        if any(m in date for m in ['July','August','September','October','November','December','Jul','Aug','Sep','Oct','Nov','Dec']):
            german_patents.append(p)

print('German patents in H2 2019:', len(german_patents))

# Extract CPC level 4 codes
cpc_data = []
for patent in german_patents:
    cpc_str = patent['cpc']
    if len(cpc_str) > 10:
        cpc_list = json.loads(cpc_str)
        for entry in cpc_list:
            code = entry.get('code', '')
            if '/' in code and ' ' not in code:
                parts = code.split('/')
                if len(parts[0]) >= 4 and len(parts[1]) >= 2:
                    level4 = parts[0][:4] + '/' + parts[1][:2]
                    # Extract month from grant date
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
                    cpc_data.append({'level4': level4, 'month': month_num})

print('CPC level 4 entries:', len(cpc_data))

# Group by CPC level 4 and count per month
from collections import defaultdict
monthly_counts = defaultdict(lambda: [0,0,0,0,0,0])  # July to Dec

for item in cpc_data:
    level4 = item['level4']
    month = item['month'] if item['month'] else 7
    if 7 <= month <= 12:
        monthly_counts[level4][month-7] += 1

print('Unique CPC level 4 codes:', len(monthly_counts))

# Calculate EMA for each CPC group
result_rows = []
for level4, counts in monthly_counts.items():
    if sum(counts) == 0:
        continue
    
    # Calculate EMA (smoothing factor 0.1)
    ema = []
    if len(counts) > 0:
        ema.append(float(counts[0]))
        for i in range(1, len(counts)):
            ema_val = 0.1 * counts[i] + 0.9 * ema[-1]
            ema.append(ema_val)
    
    # Find max EMA and corresponding month
    max_ema = max(ema) if ema else 0
    best_month_index = ema.index(max_ema) if ema else 0
    best_month = best_month_index + 7
    
    result_rows.append({
        'cpc_code': level4,
        'best_month': best_month,
        'max_ema': max_ema,
        'monthly_counts': counts,
        'ema_values': [round(v,2) for v in ema]
    })

# Sort by max EMA descending
result_rows.sort(key=lambda x: x['max_ema'], reverse=True)

print('\nTop results:')
for r in result_rows[:10]:
    print(f"{r['cpc_code']}: EMA {r['max_ema']:.2f} in month {r['best_month']}, counts {r['monthly_counts']}")

# Store top codes for CPC definition query
top_codes = [r['cpc_code'] for r in result_rows[:20]]
print('\nTop CPC codes to query:', top_codes[:10])"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.query_db:8': 'file_storage/functions.query_db:8.json', 'var_functions.query_db:12': [{'Patents_info': 'Patent application (no. DE-102013211266-A) from DE, assigned to IBM, with publication number DE-102013211266-B4.', 'grant_date': '14th Mar 2019'}, {'Patents_info': 'Application (no. RU-2018119076-A) from RU, assigned to FEDERALNOE GOSUDARSTVENNOE KAZENNOE VOENNOE OBRAZOVATELNOE UCHREZHDENIE VYSSHEGO OBRAZOVANIYA VOENNA, with publication no. RU-2694421-C1.', 'grant_date': '2019 on Jul 12th'}, {'Patents_info': 'GRIFOLS WORLDWIDE OPERATIONS LTD holds the AU patent filing (application no. AU-2015201496-A), with publication number AU-2015201496-B2.', 'grant_date': 'on October 31st, 2019'}, {'Patents_info': 'In US, the patent application (no. US-201314655932-A) is held by SERINPET LTDA REPRESENTACIONES Y SERVICIOS DE PETROLEOS and has pub. number US-10465517-B2.', 'grant_date': 'on November 5th, 2019'}, {'Patents_info': 'Patent application (number US-201415314902-A) from US, held by HEWLETT PACKARD ENTPR DEV LP, with publication number US-10176043-B2.', 'grant_date': '8th Jan 2019'}, {'Patents_info': 'The US patent application (ID US-201615761951-A) is held by HEWLETT PACKARD DEVELOPMENT CO and has publication no. US-10436614-B2.', 'grant_date': 'dated 8th October 2019'}, {'Patents_info': 'The US application (number US-201715791853-A) is owned by DENSO INT AMERICA INC and has pub. number US-10348153-B2.', 'grant_date': 'July the 9th, 2019'}, {'Patents_info': 'In US, the patent filing (application number US-201616068918-A) is owned by DENSO CORP and has publication no. US-10369965-B2.', 'grant_date': 'August the 6th, 2019'}, {'Patents_info': 'Application (no. US-201815940839-A) from US, held by GE VIDEO COMPRESSION LLC, with publication number US-10248966-B2.', 'grant_date': 'Apr 2nd, 2019'}, {'Patents_info': 'In DE, the application (number DE-102007032978-A) is held by HEIDELBERGER DRUCKMASCH AG and has publication number DE-102007032978-B4.', 'grant_date': 'dated 21st November 2019'}]}

exec(code, env_args)
