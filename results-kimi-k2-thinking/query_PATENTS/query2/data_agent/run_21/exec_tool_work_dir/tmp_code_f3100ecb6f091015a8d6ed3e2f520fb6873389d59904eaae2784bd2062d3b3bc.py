code = """import json

# Load patent data from the query result
patent_data = var_functions.query_db:82

# Count total records
total_records = len(patent_data)
print('Total patents in dataset: ' + str(total_records))

# Filter German patents in second half 2019
german_h2_2019 = []

for record in patent_data:
    # Check if German patent
    is_german = 'from DE' in record['Patents_info']
    if not is_german:
        continue
    
    # Check if second half 2019
    grant_date = record['grant_date']
    if '2019' not in grant_date:
        continue
    
    has_second_half_month = ('July' in grant_date or 'August' in grant_date or 'September' in grant_date or 
                           'October' in grant_date or 'November' in grant_date or 'December' in grant_date or
                           'Jul' in grant_date or 'Aug' in grant_date or 'Sep' in grant_date or 
                           'Oct' in grant_date or 'Nov' in grant_date or 'Dec' in grant_date)
    
    if has_second_half_month:
        german_h2_2019.append(record)

print('German patents in H2 2019: ' + str(len(german_h2_2019)))

# Extract CPC level 4 codes and count by month
cpc_counts = {}
for patent in german_h2_2019:
    cpc_str = patent['cpc']
    if len(cpc_str) < 10:
        continue
    
    try:
        cpc_list = json.loads(cpc_str)
    except:
        continue
    
    # Determine month
    date_str = patent['grant_date']
    month = 7
    if 'July' in date_str or 'Jul' in date_str:
        month = 7
    elif 'August' in date_str or 'Aug' in date_str:
        month = 8
    elif 'September' in date_str or 'Sep' in date_str:
        month = 9
    elif 'October' in date_str or 'Oct' in date_str:
        month = 10
    elif 'November' in date_str or 'Nov' in date_str:
        month = 11
    elif 'December' in date_str or 'Dec' in date_str:
        month = 12
    
    for entry in cpc_list:
        code = entry.get('code', '')
        if code and '/' in code:
            parts = code.split('/')
            if len(parts) == 2 and len(parts[0]) >= 4 and len(parts[1]) >= 2:
                level4 = parts[0][:4] + '/' + parts[1][:2]
                if level4 not in cpc_counts:
                    cpc_counts[level4] = [0, 0, 0, 0, 0, 0]
                cpc_counts[level4][month - 7] += 1

print('Unique CPC level 4 codes found: ' + str(len(cpc_counts)))

# Calculate EMA
def calculate_ema(values, smoothing=0.1):
    ema = [float(values[0])]
    for i in range(1, len(values)):
        ema.append(smoothing * values[i] + (1 - smoothing) * ema[-1])
    return ema

results = []

for code, counts in cpc_counts.items():
    if sum(counts) == 0:
        continue
    
    ema_values = calculate_ema(counts, smoothing=0.1)
    max_ema = max(ema_values)
    best_month_idx = ema_values.index(max_ema)
    best_month = best_month_idx + 7
    
    results.append({
        'cpc_code': code,
        'max_ema': round(max_ema, 2),
        'best_month': best_month,
        'counts': [int(x) for x in counts],
        'ema_series': [round(x, 2) for x in ema_values]
    })

# Sort by max EMA descending
results.sort(key=lambda x: x['max_ema'], reverse=True)

print('Top 15 CPC codes by EMA:')
for i in range(min(15, len(results))):
    r = results[i]
    print(str(i+1) + ': ' + r['cpc_code'] + ' (EMA=' + str(r['max_ema']) + ', Best month=' + str(r['best_month']) + ')')

# Get top CPC codes for lookup
top_codes = [r['cpc_code'] for r in results[:20]]
print('Top 20 codes: ' + str(top_codes))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.query_db:8': 'file_storage/functions.query_db:8.json', 'var_functions.query_db:12': [{'Patents_info': 'Patent application (no. DE-102013211266-A) from DE, assigned to IBM, with publication number DE-102013211266-B4.', 'grant_date': '14th Mar 2019'}, {'Patents_info': 'Application (no. RU-2018119076-A) from RU, assigned to FEDERALNOE GOSUDARSTVENNOE KAZENNOE VOENNOE OBRAZOVATELNOE UCHREZHDENIE VYSSHEGO OBRAZOVANIYA VOENNA, with publication no. RU-2694421-C1.', 'grant_date': '2019 on Jul 12th'}, {'Patents_info': 'GRIFOLS WORLDWIDE OPERATIONS LTD holds the AU patent filing (application no. AU-2015201496-A), with publication number AU-2015201496-B2.', 'grant_date': 'on October 31st, 2019'}, {'Patents_info': 'In US, the patent application (no. US-201314655932-A) is held by SERINPET LTDA REPRESENTACIONES Y SERVICIOS DE PETROLEOS and has pub. number US-10465517-B2.', 'grant_date': 'on November 5th, 2019'}, {'Patents_info': 'Patent application (number US-201415314902-A) from US, held by HEWLETT PACKARD ENTPR DEV LP, with publication number US-10176043-B2.', 'grant_date': '8th Jan 2019'}, {'Patents_info': 'The US patent application (ID US-201615761951-A) is held by HEWLETT PACKARD DEVELOPMENT CO and has publication no. US-10436614-B2.', 'grant_date': 'dated 8th October 2019'}, {'Patents_info': 'The US application (number US-201715791853-A) is owned by DENSO INT AMERICA INC and has pub. number US-10348153-B2.', 'grant_date': 'July the 9th, 2019'}, {'Patents_info': 'In US, the patent filing (application number US-201616068918-A) is owned by DENSO CORP and has publication no. US-10369965-B2.', 'grant_date': 'August the 6th, 2019'}, {'Patents_info': 'Application (no. US-201815940839-A) from US, held by GE VIDEO COMPRESSION LLC, with publication number US-10248966-B2.', 'grant_date': 'Apr 2nd, 2019'}, {'Patents_info': 'In DE, the application (number DE-102007032978-A) is held by HEIDELBERGER DRUCKMASCH AG and has publication number DE-102007032978-B4.', 'grant_date': 'dated 21st November 2019'}], 'var_functions.query_db:58': 'file_storage/functions.query_db:58.json', 'var_functions.query_db:62': 'file_storage/functions.query_db:62.json', 'var_functions.query_db:74': 'file_storage/functions.query_db:74.json', 'var_functions.query_db:82': 'file_storage/functions.query_db:82.json'}

exec(code, env_args)
