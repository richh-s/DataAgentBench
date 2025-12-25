code = """import json
import re

# Load Level 5 symbols
with open(locals()['var_function-call-3343180408967186434'], 'r') as f:
    l5_data = json.load(f)
    valid_l5 = set(item['symbol'] for item in l5_data)

# Load Patent Data
with open(locals()['var_function-call-18240871321988872143'], 'r') as f:
    patents = json.load(f)

# Data Structures
years_all = set()
debug_dates = []
cpc_sample = []

count_processed = 0
for p in patents:
    f_date = p.get('filing_date', '')
    if count_processed < 5:
        debug_dates.append(f_date)
    
    match = re.search(r'\b(19|20)\d{2}\b', f_date)
    if match:
        year = int(match.group(0))
        years_all.add(year)
    
    if count_processed < 5:
        cpc_sample.append(p.get('cpc', ''))
    
    count_processed += 1

print("__RESULT__:")
print(json.dumps({
    "years_found": sorted(list(years_all))[-10:], # Last 10 years
    "total_years": len(years_all),
    "sample_dates": debug_dates,
    "valid_l5_count": len(valid_l5),
    "sample_l5": list(valid_l5)[:5]
}))"""

env_args = {'var_function-call-17338831529942296706': [{'symbol': 'A01H', 'level': '5.0'}, {'symbol': 'A01F', 'level': '5.0'}, {'symbol': 'A01C', 'level': '5.0'}, {'symbol': 'A01G', 'level': '5.0'}, {'symbol': 'A23J', 'level': '5.0'}, {'symbol': 'A01N', 'level': '5.0'}, {'symbol': 'A01P', 'level': '5.0'}, {'symbol': 'A01D', 'level': '5.0'}, {'symbol': 'A01L', 'level': '5.0'}, {'symbol': 'A01K', 'level': '5.0'}], 'var_function-call-14545777970731802458': 'file_storage/function-call-14545777970731802458.json', 'var_function-call-1814896835029975198': [{'symbol': 'A01B1/00', 'level': '7.0', 'titleFull': 'Hand tools'}, {'symbol': 'A01B', 'level': '5.0', 'titleFull': 'SOIL WORKING IN AGRICULTURE OR FORESTRY; PARTS, DETAILS, OR ACCESSORIES OF AGRICULTURAL MACHINES OR IMPLEMENTS, IN GENERAL'}, {'symbol': 'A', 'level': '2.0', 'titleFull': 'HUMAN NECESSITIES'}, {'symbol': 'A01', 'level': '4.0', 'titleFull': 'AGRICULTURE; FORESTRY; ANIMAL HUSBANDRY; HUNTING; TRAPPING; FISHING'}, {'symbol': 'A01B1/02', 'level': '8.0', 'titleFull': 'Spades; Shovels'}], 'var_function-call-3343180408967186434': 'file_storage/function-call-3343180408967186434.json', 'var_function-call-7569759603939423118': [{'COUNT(*)': '277813'}], 'var_function-call-18240871321988872143': 'file_storage/function-call-18240871321988872143.json', 'var_function-call-14763584484084519735': []}

exec(code, env_args)
