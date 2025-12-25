code = """import json
import re

# Load data
patents_path = locals()['var_function-call-12692344048836219409']
cpc_def_path = locals()['var_function-call-11616478013038593955']

with open(patents_path, 'r') as f:
    patents_data = json.load(f)

with open(cpc_def_path, 'r') as f:
    cpc_defs = json.load(f)

# Map symbol -> title
cpc_titles = {d['symbol']: d['titleFull'] for d in cpc_defs}

# Filter H2 2019
h2_months = ['Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
def is_h2_2019(date_str):
    if not isinstance(date_str, str): return False
    if '2019' not in date_str: return False
    # Check month
    for m in h2_months:
        if m in date_str or m.upper() in date_str.upper() or m.lower() in date_str.lower(): # Case insensitive check
            return True
    # Full names
    full_months = ['July', 'August', 'September', 'October', 'November', 'December']
    for m in full_months:
        if m in date_str or m.lower() in date_str.lower():
            return True
    return False

filtered_patents = [p for p in patents_data if is_h2_2019(p.get('grant_date', ''))]

# Process filings
cpc_counts = {}

for p in filtered_patents:
    # Filing Year
    f_date = p.get('filing_date', '')
    match = re.search(r'\d{4}', f_date)
    if not match: continue
    year = int(match.group(0))
    
    # CPC Codes
    cpc_json = p.get('cpc', '[]')
    try:
        cpc_list = json.loads(cpc_json)
    except:
        continue
    
    # Extract Level 4 (Class - 3 chars)
    codes = set()
    for item in cpc_list:
        code = item.get('code', '')
        if len(code) >= 3:
            class_code = code[:3]
            codes.add(class_code)
            
    for code in codes:
        if code not in cpc_counts:
            cpc_counts[code] = {}
        cpc_counts[code][year] = cpc_counts[code].get(year, 0) + 1

# Calculate EMA
results = []
alpha = 0.1

for code, year_counts in cpc_counts.items():
    if not year_counts: continue
    years = sorted(year_counts.keys())
    if not years: continue
    min_year = years[0]
    max_year = years[-1]
    
    # Need to cover range from min_year to max_year?
    # Or max_year of the whole dataset?
    # Usually for comparing, we might stop at 2019 (since patents are granted in 2019).
    # But filings could be earlier.
    # I'll run up to the last year present for that code.
    
    current_ema = year_counts[min_year]
    max_ema = current_ema
    best_year = min_year
    
    for y in range(min_year + 1, max_year + 1):
        count = year_counts.get(y, 0)
        current_ema = alpha * count + (1 - alpha) * current_ema
        if current_ema > max_ema:
            max_ema = current_ema
            best_year = y
            
    results.append({
        "full_title": cpc_titles.get(code, "N/A"),
        "cpc_group_code": code,
        "best_year": best_year,
        "max_ema": max_ema
    })

# Sort by max_ema
results.sort(key=lambda x: x['max_ema'], reverse=True)

print("__RESULT__:")
print(json.dumps(results))"""

env_args = {'var_function-call-12347039294743270016': 'file_storage/function-call-12347039294743270016.json', 'var_function-call-10181815232966794860': [{'symbol': 'B04', 'level': '4.0', 'titleFull': 'CENTRIFUGAL APPARATUS OR MACHINES FOR CARRYING-OUT PHYSICAL OR CHEMICAL PROCESSES'}, {'symbol': 'B23', 'level': '4.0', 'titleFull': 'MACHINE TOOLS; METAL-WORKING NOT OTHERWISE PROVIDED FOR'}, {'symbol': 'B30', 'level': '4.0', 'titleFull': 'PRESSES'}, {'symbol': 'B21', 'level': '4.0', 'titleFull': 'MECHANICAL METAL-WORKING WITHOUT ESSENTIALLY REMOVING MATERIAL; PUNCHING METAL'}, {'symbol': 'B25', 'level': '4.0', 'titleFull': 'HAND TOOLS; PORTABLE POWER-DRIVEN TOOLS; MANIPULATORS'}], 'var_function-call-7851907252641243452': [{'symbol': 'B', 'level': '2.0', 'titleFull': 'PERFORMING OPERATIONS; TRANSPORTING'}, {'symbol': 'B04B', 'level': '5.0', 'titleFull': 'CENTRIFUGES'}, {'symbol': 'B04B1/00', 'level': '7.0', 'titleFull': 'Centrifuges with rotary bowls provided with solid jackets for separating predominantly liquid mixtures with or without solid particles'}, {'symbol': 'B04', 'level': '4.0', 'titleFull': 'CENTRIFUGAL APPARATUS OR MACHINES FOR CARRYING-OUT PHYSICAL OR CHEMICAL PROCESSES'}], 'var_function-call-12692344048836219409': 'file_storage/function-call-12692344048836219409.json', 'var_function-call-11616478013038593955': 'file_storage/function-call-11616478013038593955.json'}

exec(code, env_args)
