code = """import json
import pandas as pd
import re

# Access file paths from storage
cpc_def_path = locals()['var_function-call-12113266246292229848']
pub_info_path = locals()['var_function-call-12113266246292228993']

# Load CPC Definitions (Level 4)
with open(cpc_def_path, 'r') as f:
    cpc_defs = json.load(f)

# Map symbol -> titleFull
cpc_titles = {item['symbol']: item['titleFull'] for item in cpc_defs}

# Load Publication Info
with open(pub_info_path, 'r') as f:
    pub_data = json.load(f)

# Date Parser
month_map = {
    'january': 1, 'february': 2, 'march': 3, 'april': 4, 'may': 5, 'june': 6,
    'july': 7, 'august': 8, 'september': 9, 'october': 10, 'november': 11, 'december': 12,
    'jan': 1, 'feb': 2, 'mar': 3, 'apr': 4, 'jun': 6, 'jul': 7, 'aug': 8, 'sep': 9, 'oct': 10, 'nov': 11, 'dec': 12,
    'sept': 9
}

def parse_date(date_str):
    if not date_str:
        return None
    s = str(date_str).lower()
    # Find year (4 digits)
    year_match = re.search(r'\d{4}', s)
    if not year_match:
        return None
    year = int(year_match.group(0))
    
    # Find month
    month = 0
    for m, v in month_map.items():
        if m in s:
            month = v
            break
    if month == 0:
        # Try to see if there's a numeric date like YYYY-MM-DD or similar if regex fails
        # But for now, if month name not found, ignore?
        # Maybe "dated 5th March 2019" -> March found.
        return None 
        
    return pd.Timestamp(year=year, month=month, day=1)

def is_h2_2019(date_obj):
    if date_obj is None:
        return False
    return (date_obj.year == 2019) and (date_obj.month >= 7)

# Processing
cpc_filing_counts = {} # cpc -> year -> count

for record in pub_data:
    # 1. Check Germany
    p_info = record.get('Patents_info', '')
    if 'DE-' not in p_info and 'Germany' not in p_info and 'from DE' not in p_info and 'In DE' not in p_info:
        continue
        
    # 2. Check Grant Date
    g_date = parse_date(record.get('grant_date'))
    if not is_h2_2019(g_date):
        continue
        
    # 3. Get Filing Year
    f_date = parse_date(record.get('filing_date'))
    if not f_date:
        continue
    f_year = f_date.year
    
    # 4. Extract CPCs
    cpc_json = record.get('cpc')
    if not cpc_json:
        continue
    try:
        cpcs = json.loads(cpc_json)
        # Extract unique Level 4 codes (Classes) for this patent
        patent_codes = set()
        for item in cpcs:
            code = item.get('code', '')
            if len(code) >= 3:
                l4 = code[:3]
                if l4 in cpc_titles:
                    patent_codes.add(l4)
        
        # Add to aggregate
        for c in patent_codes:
            if c not in cpc_filing_counts:
                cpc_filing_counts[c] = {}
            cpc_filing_counts[c][f_year] = cpc_filing_counts[c].get(f_year, 0) + 1
            
    except:
        continue

# EMA Calculation
all_years = set()
for c in cpc_filing_counts:
    all_years.update(cpc_filing_counts[c].keys())

if not all_years:
    print("__RESULT__:")
    print("[]")
else:
    min_year = min(all_years)
    max_year = max(all_years)
    year_range = sorted(list(range(min_year, max_year + 1)))
    
    ema_results = {} # cpc -> {year: ema}
    alpha = 0.1
    
    for c, counts in cpc_filing_counts.items():
        ema_series = {}
        prev_ema = None
        
        # Init with first year
        prev_ema = counts.get(min_year, 0)
        ema_series[min_year] = prev_ema
        
        for y in year_range[1:]:
            val = counts.get(y, 0)
            cur_ema = (val * alpha) + (prev_ema * (1 - alpha))
            ema_series[y] = cur_ema
            prev_ema = cur_ema
            
        ema_results[c] = ema_series

    # Identify Winners (Highest EMA each year)
    winners = set()
    for y in year_range:
        best_c = None
        max_val = -1
        for c in ema_results:
            val = ema_results[c].get(y, 0)
            if val > max_val:
                max_val = val
                best_c = c
        if best_c:
            winners.add(best_c)
            
    # Format Result
    final_output = []
    for c in winners:
        series = ema_results[c]
        # Find best year
        best_y = max(series, key=series.get)
        
        final_output.append({
            "CPC Group Code": c,
            "Title": cpc_titles.get(c, "Unknown"),
            "Best Year": best_y
        })

    print("__RESULT__:")
    print(json.dumps(final_output))"""

env_args = {'var_function-call-502300787869230635': 'file_storage/function-call-502300787869230635.json', 'var_function-call-502300787869229232': [{'symbol': 'B04', 'level': '4.0', 'titleFull': 'CENTRIFUGAL APPARATUS OR MACHINES FOR CARRYING-OUT PHYSICAL OR CHEMICAL PROCESSES'}, {'symbol': 'B23', 'level': '4.0', 'titleFull': 'MACHINE TOOLS; METAL-WORKING NOT OTHERWISE PROVIDED FOR'}, {'symbol': 'B30', 'level': '4.0', 'titleFull': 'PRESSES'}, {'symbol': 'B21', 'level': '4.0', 'titleFull': 'MECHANICAL METAL-WORKING WITHOUT ESSENTIALLY REMOVING MATERIAL; PUNCHING METAL'}, {'symbol': 'B25', 'level': '4.0', 'titleFull': 'HAND TOOLS; PORTABLE POWER-DRIVEN TOOLS; MANIPULATORS'}], 'var_function-call-5341567489112971283': [{'symbol': 'C01B', 'level': '5.0', 'titleFull': 'NON-METALLIC ELEMENTS; COMPOUNDS THEREOF; METALLOIDS OR COMPOUNDS THEREOF NOT COVERED BY SUBCLASS C01C'}, {'symbol': 'C01B33/00', 'level': '7.0', 'titleFull': 'Silicon; Compounds thereof'}], 'var_function-call-5341567489112970574': [{'COUNT(*)': '277813'}], 'var_function-call-5341567489112969865': [{'Patents_info': 'Patent application (number DE-10317286-A) from DE, belonging to NICOLAY VERWALTUNGS GMBH, with publication no. DE-10317286-B3.'}, {'Patents_info': 'MIELE & CIE holds the DE patent filing (app. number DE-102005018015-A), with publication number DE-102005018015-B3.'}, {'Patents_info': 'UHLMANN PAC SYSTEME GMBH & CO holds the DE patent filing (app. number DE-102006022262-A), with publication number DE-102006022262-B3.'}, {'Patents_info': 'The DE patent filing (application no. DE-102007030491-A) is belonging to HEINRICH GEORG GMBH MASCHINENF and has pub. number DE-102007030491-B3.'}, {'Patents_info': 'In DE, the patent filing (application no. DE-102009032362-A) is owned by MARTOR KG and has pub. number DE-102009032362-B3.'}], 'var_function-call-8485550721636509159': [{'level': '2.0', 'symbol': 'A'}, {'level': '2.0', 'symbol': 'B'}, {'level': '2.0', 'symbol': 'C'}, {'level': '2.0', 'symbol': 'D'}, {'level': '2.0', 'symbol': 'E'}, {'level': '2.0', 'symbol': 'F'}, {'level': '2.0', 'symbol': 'G'}, {'level': '2.0', 'symbol': 'H'}, {'level': '2.0', 'symbol': 'Y'}, {'level': '4.0', 'symbol': 'A01'}], 'var_function-call-12113266246292228993': 'file_storage/function-call-12113266246292228993.json', 'var_function-call-12113266246292229848': 'file_storage/function-call-12113266246292229848.json'}

exec(code, env_args)
