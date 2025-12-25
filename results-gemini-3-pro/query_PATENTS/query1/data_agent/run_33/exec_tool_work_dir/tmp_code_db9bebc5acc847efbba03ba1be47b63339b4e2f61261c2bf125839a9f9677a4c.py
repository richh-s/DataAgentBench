code = """import json
import re

# Load Level 5 symbols
with open(locals()['var_function-call-3343180408967186434'], 'r') as f:
    l5_data = json.load(f)
    valid_l5 = set(item['symbol'] for item in l5_data)

# Load Patent Data
with open(locals()['var_function-call-18240871321988872143'], 'r') as f:
    patents = json.load(f)

counts = {} 
years_all = set()

# Process
for p in patents:
    f_date = p.get('filing_date', '')
    
    # Loose regex for year
    match = re.search(r'(19|20)\d{2}', f_date)
    if not match:
        continue
    year = int(match.group(0))
    years_all.add(year)
    
    cpc_json = p.get('cpc', '[]')
    try:
        cpc_list = json.loads(cpc_json)
    except:
        continue
        
    patent_cats = set()
    for entry in cpc_list:
        code = entry.get('code', '')
        if len(code) >= 4:
            sub = code[:4]
            if sub in valid_l5:
                patent_cats.add(sub)
    
    for c in patent_cats:
        if c not in counts:
            counts[c] = {}
        counts[c][year] = counts[c].get(year, 0) + 1

if not years_all:
    print("__RESULT__:")
    print("[]")
    exit()

min_year = min(years_all)
max_year = max(years_all)

# We must ensure we cover 2022 if it's not in the data (meaning 0 filings in 2022)
# but the user asks for best year 2022. If 2022 is not in the data range, we can't really conclude.
# But likely 2022 is in the data range if the data is recent.
# If max_year < 2022, we should probably extend range to 2022.
actual_max_year = max(max_year, 2022)

result_codes = []
alpha = 0.2

for cpc, year_counts in counts.items():
    ema_prev = None
    best_ema = -1.0
    best_y = -1
    
    # We iterate up to actual_max_year to include 2022 even if counts are 0
    # But usually patent data might have lag. 
    # If the database ends in 2020, "best year is 2022" returns nothing.
    # Let's trust the data. If data goes up to 2022 or beyond, good.
    # If not, and we extrapolate 0s, the EMA will decay, so 2022 won't be best unless it peaked then (which requires data).
    # So we stick to data range.
    
    # Wait, if 2022 is present in the data, we use it.
    
    for y in range(min_year, actual_max_year + 1):
        val = year_counts.get(y, 0)
        
        if ema_prev is None:
            ema = float(val)
            ema_prev = ema
        else:
            ema = (val * alpha) + (ema_prev * (1 - alpha))
            ema_prev = ema
            
        if ema > best_ema:
            best_ema = ema
            best_y = y
        # We don't update on tie, preserving the earliest year as 'best' in case of flat peak
        # Or should we?
        # If the peak is flat (e.g. 10, 10), EMA stays 10.
        # If EMA rises, best_y updates.
        # If EMA falls, best_y stays.
        # If EMA matches best_ema, usually we don't change.
            
    if best_y == 2022:
        result_codes.append(cpc)

print("__RESULT__:")
print(json.dumps(result_codes))"""

env_args = {'var_function-call-17338831529942296706': [{'symbol': 'A01H', 'level': '5.0'}, {'symbol': 'A01F', 'level': '5.0'}, {'symbol': 'A01C', 'level': '5.0'}, {'symbol': 'A01G', 'level': '5.0'}, {'symbol': 'A23J', 'level': '5.0'}, {'symbol': 'A01N', 'level': '5.0'}, {'symbol': 'A01P', 'level': '5.0'}, {'symbol': 'A01D', 'level': '5.0'}, {'symbol': 'A01L', 'level': '5.0'}, {'symbol': 'A01K', 'level': '5.0'}], 'var_function-call-14545777970731802458': 'file_storage/function-call-14545777970731802458.json', 'var_function-call-1814896835029975198': [{'symbol': 'A01B1/00', 'level': '7.0', 'titleFull': 'Hand tools'}, {'symbol': 'A01B', 'level': '5.0', 'titleFull': 'SOIL WORKING IN AGRICULTURE OR FORESTRY; PARTS, DETAILS, OR ACCESSORIES OF AGRICULTURAL MACHINES OR IMPLEMENTS, IN GENERAL'}, {'symbol': 'A', 'level': '2.0', 'titleFull': 'HUMAN NECESSITIES'}, {'symbol': 'A01', 'level': '4.0', 'titleFull': 'AGRICULTURE; FORESTRY; ANIMAL HUSBANDRY; HUNTING; TRAPPING; FISHING'}, {'symbol': 'A01B1/02', 'level': '8.0', 'titleFull': 'Spades; Shovels'}], 'var_function-call-3343180408967186434': 'file_storage/function-call-3343180408967186434.json', 'var_function-call-7569759603939423118': [{'COUNT(*)': '277813'}], 'var_function-call-18240871321988872143': 'file_storage/function-call-18240871321988872143.json', 'var_function-call-14763584484084519735': [], 'var_function-call-13598038491361226942': {'years_found': [], 'total_years': 0, 'sample_dates': ['dated 5th March 2019', 'March the 18th, 2019', '29th March 2019', 'on March 29th, 2019', '2nd April 2019'], 'valid_l5_count': 677, 'sample_l5': ['B08B', 'F42C', 'B60F', 'C03C', 'F25B']}}

exec(code, env_args)
