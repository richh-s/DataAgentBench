code = """import json, collections

patent_records = var_functions.query_db:0

# Filter German patents in second half 2019
german_patents = []
month_indicators = ['July','August','September','October','November','December','Jul','Aug','Sep','Oct','Nov','Dec']

for record in patent_records:
    info = record['Patents_info']
    gdate = record['grant_date']
    if 'from DE' in info and '2019' in gdate:
        if any(m in gdate for m in month_indicators):
            german_patents.append(record)

print('German H2 2019 patents count:', len(german_patents))

# Process CPC codes
cpc_counts = collections.defaultdict(lambda: [0,0,0,0,0,0])

for patent in german_patents:
    cpc_str = patent['cpc']
    if len(cpc_str) < 10:
        continue
    cpc_list = json.loads(cpc_str)
    
    month = 7
    for i, m in enumerate(['July','August','September','October','November','December']):
        if m in patent['grant_date']:
            month = i + 7
            break
    if month == 7:
        for i, m in enumerate(['Jul','Aug','Sep','Oct','Nov','Dec']):
            if m in patent['grant_date']:
                month = i + 7
                break
    
    for entry in cpc_list:
        code = entry.get('code', '')
        parts = code.split('/')
        if len(parts) == 2 and len(parts[0]) >= 4 and len(parts[1]) >= 2:
            level4 = parts[0][:4] + '/' + parts[1][:2]
            cpc_counts[level4][month-7] += 1

print('Unique CPC level 4 codes:', len(cpc_counts))

# Calculate EMA (smoothing factor 0.1)
results = []
for code, counts in cpc_counts.items():
    if sum(counts) == 0:
        continue
    ema = [float(counts[0])]
    for i in range(1, len(counts)):
        ema.append(0.1 * counts[i] + 0.9 * ema[-1])
    max_ema = max(ema)
    best_month = ema.index(max_ema) + 7
    results.append({'code': code, 'max_ema': max_ema, 'best_month': best_month, 'monthly_counts': [int(x) for x in counts], 'ema_series': [round(x, 2) for x in ema]})

results.sort(key=lambda x: x['max_ema'], reverse=True)

print('\nTop 10 CPC codes by EMA:')
for i in range(min(10, len(results))):
    r = results[i]
    print(f"{r['code']}: EMA={r['max_ema']:.2f}, Best month={r['best_month']}, Counts={r['monthly_counts']}")

# Prepare output
top_10_codes = [r['code'] for r in results[:10]]
output_data = {'german_patents_count': len(german_patents), 'unique_cpc_codes': len(cpc_counts), 'top_10_codes': top_10_codes}
print('\nOutput:', output_data)"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.query_db:8': 'file_storage/functions.query_db:8.json', 'var_functions.query_db:12': [{'Patents_info': 'Patent application (no. DE-102013211266-A) from DE, assigned to IBM, with publication number DE-102013211266-B4.', 'grant_date': '14th Mar 2019'}, {'Patents_info': 'Application (no. RU-2018119076-A) from RU, assigned to FEDERALNOE GOSUDARSTVENNOE KAZENNOE VOENNOE OBRAZOVATELNOE UCHREZHDENIE VYSSHEGO OBRAZOVANIYA VOENNA, with publication no. RU-2694421-C1.', 'grant_date': '2019 on Jul 12th'}, {'Patents_info': 'GRIFOLS WORLDWIDE OPERATIONS LTD holds the AU patent filing (application no. AU-2015201496-A), with publication number AU-2015201496-B2.', 'grant_date': 'on October 31st, 2019'}, {'Patents_info': 'In US, the patent application (no. US-201314655932-A) is held by SERINPET LTDA REPRESENTACIONES Y SERVICIOS DE PETROLEOS and has pub. number US-10465517-B2.', 'grant_date': 'on November 5th, 2019'}, {'Patents_info': 'Patent application (number US-201415314902-A) from US, held by HEWLETT PACKARD ENTPR DEV LP, with publication number US-10176043-B2.', 'grant_date': '8th Jan 2019'}, {'Patents_info': 'The US patent application (ID US-201615761951-A) is held by HEWLETT PACKARD DEVELOPMENT CO and has publication no. US-10436614-B2.', 'grant_date': 'dated 8th October 2019'}, {'Patents_info': 'The US application (number US-201715791853-A) is owned by DENSO INT AMERICA INC and has pub. number US-10348153-B2.', 'grant_date': 'July the 9th, 2019'}, {'Patents_info': 'In US, the patent filing (application number US-201616068918-A) is owned by DENSO CORP and has publication no. US-10369965-B2.', 'grant_date': 'August the 6th, 2019'}, {'Patents_info': 'Application (no. US-201815940839-A) from US, held by GE VIDEO COMPRESSION LLC, with publication number US-10248966-B2.', 'grant_date': 'Apr 2nd, 2019'}, {'Patents_info': 'In DE, the application (number DE-102007032978-A) is held by HEIDELBERGER DRUCKMASCH AG and has publication number DE-102007032978-B4.', 'grant_date': 'dated 21st November 2019'}]}

exec(code, env_args)
