code = """import json
import re

with open(var_call_Mg8jcZD7OFnFitGEUSuW0mxV, 'r', encoding='utf-8') as f:
    records = json.load(f)
with open(var_call_VXK5JBkY21k0gFoUIiz5HJB3, 'r', encoding='utf-8') as f:
    cpc_defs = json.load(f)

# build title map
title_map = {r['symbol']: r.get('titleFull') for r in cpc_defs}

months = {
    'jan':1,'january':1,
    'feb':2,'february':2,
    'mar':3,'march':3,
    'apr':4,'april':4,
    'may':5,
    'jun':6,'june':6,
    'jul':7,'july':7,
    'aug':8,'august':8,
    'sep':9,'sept':9,'september':9,
    'oct':10,'october':10,
    'nov':11,'november':11,
    'dec':12,'december':12
}

def is_grant_in_h2_2019(grant_date_str):
    if not grant_date_str:
        return False
    s = grant_date_str.lower()
    if '2019' not in s:
        return False
    for mname, mnum in months.items():
        if mname in s:
            return (7 <= mnum <= 12)
    return False

def extract_year(datestr):
    if not datestr:
        return None
    # find any 4-digit number between 1900 and 2099
    found = re.findall(r"\d{4}", datestr)
    for f in found:
        y = int(f)
        if 1900 <= y <= 2099:
            return y
    return None

def parse_cpc_field(cpc_field_str):
    if not cpc_field_str:
        return []
    try:
        lst = json.loads(cpc_field_str)
        codes = []
        for item in lst:
            if isinstance(item, dict):
                code = item.get('code')
                if code:
                    codes.append(code)
        return codes
    except Exception:
        # fallback simple extraction: uppercase letter + two digits and optional letter
        return re.findall(r"[A-Z][0-9]{2}[A-Z]?", cpc_field_str.upper())

counts = {}
for rec in records:
    pinfo = rec.get('Patents_info','') or ''
    if 'germany' not in pinfo.lower():
        continue
    grant = rec.get('grant_date','') or ''
    if not is_grant_in_h2_2019(grant):
        continue
    filing = rec.get('filing_date','') or ''
    fy = extract_year(filing)
    if fy is None:
        fy = extract_year(rec.get('publication_date','') or '')
        if fy is None:
            continue
    cpcs = parse_cpc_field(rec.get('cpc',''))
    for code in cpcs:
        if len(code) < 3:
            continue
        lvl4 = code[:3].upper()
        counts.setdefault(lvl4, {}).setdefault(fy, 0)
        counts[lvl4][fy] += 1

alpha = 0.1
results = []
for lvl, year_counts in counts.items():
    years = sorted(year_counts.keys())
    if not years:
        continue
    prev_ema = None
    ema_by_year = {}
    for y in years:
        cnt = year_counts.get(y, 0)
        if prev_ema is None:
            ema = cnt
        else:
            ema = alpha * cnt + (1 - alpha) * prev_ema
        ema_by_year[y] = ema
        prev_ema = ema
    best_year = max(ema_by_year.items(), key=lambda x: x[1])[0]
    peak_ema = ema_by_year[best_year]
    title = title_map.get(lvl)
    results.append({'cpc_group': lvl, 'titleFull': title, 'best_year': int(best_year), 'peak_ema': float(round(peak_ema,6)), 'year_counts': {str(k): v for k,v in year_counts.items()}})

results_sorted = sorted(results, key=lambda x: x['peak_ema'], reverse=True)
out = results_sorted[:50]

print("__RESULT__:")
print(json.dumps(out))"""

env_args = {'var_call_nIXHvvymMvZLu038dQFL9QE8': ['publicationinfo'], 'var_call_InMp5BUYkZMmtbN4Dvtz46KF': ['cpc_definition'], 'var_call_F7Gp5tyJWrCLK3TamHbJQxcy': [], 'var_call_gZP35ibEUH7SgdGEv3tHyHQJ': 'file_storage/call_gZP35ibEUH7SgdGEv3tHyHQJ.json', 'var_call_Mg8jcZD7OFnFitGEUSuW0mxV': 'file_storage/call_Mg8jcZD7OFnFitGEUSuW0mxV.json', 'var_call_VXK5JBkY21k0gFoUIiz5HJB3': 'file_storage/call_VXK5JBkY21k0gFoUIiz5HJB3.json'}

exec(code, env_args)
