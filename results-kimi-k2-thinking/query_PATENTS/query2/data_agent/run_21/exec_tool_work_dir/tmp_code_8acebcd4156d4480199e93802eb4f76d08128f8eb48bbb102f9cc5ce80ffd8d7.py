code = """import json, os

# Load the data
patent_file = 'var_functions.query_db:0.json'
with open(patent_file) as f:
    patents = json.load(f)

print('Loaded', len(patents), 'patents')

# Filter German patents in H2 2019
german_h2 = []
for p in patents:
    info = p['Patents_info']
    date = p['grant_date']
    if 'from DE' in info and '2019' in date:
        if any(m in date for m in ['July','August','September','October','November','December','Jul','Aug','Sep','Oct','Nov','Dec']):
            german_h2.append(p)

print('German patents H2 2019:', len(german_h2))

# Parse CPC codes and extract level 4
cpc_data = []
for p in german_h2:
    cpc_str = p['cpc']
    if len(cpc_str) < 10:
        continue
    cpc_list = json.loads(cpc_str)
    
    # Get month
    month = 7
    for i,m in enumerate(['July','August','September','October','November','December']):
        if m in p['grant_date']:
            month = i + 7
            break
    
    for entry in cpc_list:
        code = entry.get('code', '')
        parts = code.split('/')
        if len(parts) == 2:
            if len(parts[0]) >= 4 and len(parts[1]) >= 2:
                level4 = parts[0][:4] + '/' + parts[1][:2]
                cpc_data.append({'code': level4, 'month': month})

print('CPC level 4 entries:', len(cpc_data))

# Count per month
from collections import defaultdict
month_counts = defaultdict(lambda: [0,0,0,0,0,0])
for item in cpc_data:
    month_counts[item['code']][item['month'] - 7] += 1

print('Unique CPC codes:', len(month_counts))

# Calculate EMA
results = []
for code, counts in month_counts.items():
    ema = []
    if sum(counts) > 0:
        ema.append(float(counts[0]))
        for i in range(1, len(counts)):
            ema.append(0.1 * counts[i] + 0.9 * ema[-1])
    
    if ema:
        max_ema = max(ema)
        best_month = ema.index(max_ema) + 7
        results.append({'code': code, 'max_ema': max_ema, 'best_month': best_month, 'counts': list(map(int, counts)), 'ema': [round(x,2) for x in ema]})

results.sort(key=lambda x: x['max_ema'], reverse=True)
print('\nTop results:')
for r in results[:15]:
    print(r['code'], 'EMA:', round(r['max_ema'],2), 'Best month:', r['best_month'], 'Counts:', r['counts'])

top_codes = [r['code'] for r in results[:20]]
print('\nTop codes:', top_codes)"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.query_db:8': 'file_storage/functions.query_db:8.json', 'var_functions.query_db:12': [{'Patents_info': 'Patent application (no. DE-102013211266-A) from DE, assigned to IBM, with publication number DE-102013211266-B4.', 'grant_date': '14th Mar 2019'}, {'Patents_info': 'Application (no. RU-2018119076-A) from RU, assigned to FEDERALNOE GOSUDARSTVENNOE KAZENNOE VOENNOE OBRAZOVATELNOE UCHREZHDENIE VYSSHEGO OBRAZOVANIYA VOENNA, with publication no. RU-2694421-C1.', 'grant_date': '2019 on Jul 12th'}, {'Patents_info': 'GRIFOLS WORLDWIDE OPERATIONS LTD holds the AU patent filing (application no. AU-2015201496-A), with publication number AU-2015201496-B2.', 'grant_date': 'on October 31st, 2019'}, {'Patents_info': 'In US, the patent application (no. US-201314655932-A) is held by SERINPET LTDA REPRESENTACIONES Y SERVICIOS DE PETROLEOS and has pub. number US-10465517-B2.', 'grant_date': 'on November 5th, 2019'}, {'Patents_info': 'Patent application (number US-201415314902-A) from US, held by HEWLETT PACKARD ENTPR DEV LP, with publication number US-10176043-B2.', 'grant_date': '8th Jan 2019'}, {'Patents_info': 'The US patent application (ID US-201615761951-A) is held by HEWLETT PACKARD DEVELOPMENT CO and has publication no. US-10436614-B2.', 'grant_date': 'dated 8th October 2019'}, {'Patents_info': 'The US application (number US-201715791853-A) is owned by DENSO INT AMERICA INC and has pub. number US-10348153-B2.', 'grant_date': 'July the 9th, 2019'}, {'Patents_info': 'In US, the patent filing (application number US-201616068918-A) is owned by DENSO CORP and has publication no. US-10369965-B2.', 'grant_date': 'August the 6th, 2019'}, {'Patents_info': 'Application (no. US-201815940839-A) from US, held by GE VIDEO COMPRESSION LLC, with publication number US-10248966-B2.', 'grant_date': 'Apr 2nd, 2019'}, {'Patents_info': 'In DE, the application (number DE-102007032978-A) is held by HEIDELBERGER DRUCKMASCH AG and has publication number DE-102007032978-B4.', 'grant_date': 'dated 21st November 2019'}]}

exec(code, env_args)
