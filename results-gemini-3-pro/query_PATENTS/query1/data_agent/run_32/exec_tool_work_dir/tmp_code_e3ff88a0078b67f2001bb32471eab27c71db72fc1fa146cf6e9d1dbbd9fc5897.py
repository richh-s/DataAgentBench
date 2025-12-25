code = """import json
import re

l5_path = locals()['var_function-call-7207860585803115625']
patents_path = locals()['var_function-call-5530323500134500439']

with open(l5_path, 'r') as f:
    l5_data = json.load(f)
l5_symbols = set(item['symbol'] for item in l5_data if 'symbol' in item)

with open(patents_path, 'r') as f:
    patents = json.load(f)

total_patents = len(patents)
valid_years = 0
valid_cpc = 0
matched_l5 = 0
year_dist = {}

counts = {}

for p in patents:
    d_str = p.get('filing_date', '')
    match = re.search(r'\b(19|20)\d{2}\b', str(d_str))
    if match:
        year = int(match.group(0))
        valid_years += 1
        year_dist[year] = year_dist.get(year, 0) + 1
    else:
        continue

    cpc_str = p.get('cpc', '[]')
    try:
        cpc_list = json.loads(cpc_str)
        if cpc_list: valid_cpc += 1
    except:
        continue
    
    patent_l5s = set()
    for item in cpc_list:
        code = item.get('code', '')
        if code and len(code) >= 4:
            prefix = code[:4]
            if prefix in l5_symbols:
                patent_l5s.add(prefix)
    
    if patent_l5s:
        matched_l5 += 1
        for sym in patent_l5s:
            if sym not in counts:
                counts[sym] = {}
            counts[sym][year] = counts[sym].get(year, 0) + 1

debug_info = {
    "total": total_patents,
    "valid_years": valid_years,
    "valid_cpc": valid_cpc,
    "matched_l5": matched_l5,
    "year_min": min(year_dist.keys()) if year_dist else None,
    "year_max": max(year_dist.keys()) if year_dist else None,
    "top_years": dict(sorted(year_dist.items(), key=lambda x: x[1], reverse=True)[:5])
}

# Check EMA for top symbol
if counts:
    top_sym = max(counts, key=lambda s: sum(counts[s].values()))
    y_counts = counts[top_sym]
    min_y = min(y_counts.keys())
    max_y = max(y_counts.keys())
    ema_check = []
    
    alpha = 0.2
    curr = 0
    first = True
    max_e = -1
    max_y_e = -1
    
    for y in range(min_y, max_y + 1):
        c = y_counts.get(y, 0)
        if first:
            curr = c
            first = False
        else:
            curr = alpha * c + (1 - alpha) * curr
        ema_check.append({"year": y, "count": c, "ema": curr})
        if curr > max_e:
            max_e = curr
            max_y_e = y
            
    debug_info["example_sym"] = top_sym
    debug_info["example_ema"] = ema_check
    debug_info["example_peak"] = max_y_e

print("__RESULT__:")
print(json.dumps(debug_info))"""

env_args = {'var_function-call-16354257400330351795': 'file_storage/function-call-16354257400330351795.json', 'var_function-call-16354257400330353054': [{'symbol': 'A01H', 'level': '5.0'}, {'symbol': 'A01F', 'level': '5.0'}, {'symbol': 'A01C', 'level': '5.0'}, {'symbol': 'A01G', 'level': '5.0'}, {'symbol': 'A23J', 'level': '5.0'}], 'var_function-call-10560939620404889531': [{'symbol': 'H01M', 'level': '5.0'}, {'symbol': 'C01B33/00', 'level': '7.0'}, {'symbol': 'A01H', 'level': '5.0'}, {'symbol': 'H01M10/0565', 'level': '11.0'}], 'var_function-call-16184128629487448997': [{'len': '4', 'cnt': '677'}], 'var_function-call-4973736629774637364': [{'cnt': '277813'}], 'var_function-call-7207860585803115625': 'file_storage/function-call-7207860585803115625.json', 'var_function-call-5530323500134500439': 'file_storage/function-call-5530323500134500439.json', 'var_function-call-6282301310973396861': []}

exec(code, env_args)
