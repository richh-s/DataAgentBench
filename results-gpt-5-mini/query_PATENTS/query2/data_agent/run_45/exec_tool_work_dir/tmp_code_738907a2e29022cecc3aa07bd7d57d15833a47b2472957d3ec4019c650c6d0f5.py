code = """import json, re
from collections import defaultdict

# load stored query results
with open(var_call_5rHtrHNCXLAWFEXzgsUP2BJs, 'r', encoding='utf-8') as f:
    records = json.load(f)
with open(var_call_NsvNsGurGkwfOEmVn6LEFA53, 'r', encoding='utf-8') as f:
    cpc_defs = json.load(f)

# build mapping symbol->titleFull
cpc_title = {rec.get('symbol'): rec.get('titleFull') for rec in cpc_defs if rec.get('symbol')}

# month mapping
months = {m.lower(): i for i,m in enumerate(['', 'January','February','March','April','May','June','July','August','September','October','November','December'])}
shorts = {'jan':1,'feb':2,'mar':3,'apr':4,'may':5,'jun':6,'jul':7,'aug':8,'sep':9,'sept':9,'oct':10,'nov':11,'dec':12}

# helpers

def is_germany(info):
    if not info or not isinstance(info, str):
        return False
    # match whole word DE or DE- prefix
    if re.search(r'\bDE\b|\bDE-', info):
        return True
    # match patterns like 'In DE,' 'from DE'
    if re.search(r'In\s+DE\b|from\s+DE\b|The DE application|The DE patent', info):
        return True
    return False


def extract_year_month(s):
    if not s or not isinstance(s, str):
        return None, None
    y_match = re.search(r'(20\d{2})', s)
    year = int(y_match.group(1)) if y_match else None
    m = None
    mm = re.search(r'\b(January|February|March|April|May|June|July|August|September|October|November|December)\b', s)
    if mm:
        m = months[mm.group(1).lower()]
    else:
        mm2 = re.search(r'\b(Jan|Feb|Mar|Apr|May|Jun|Jul|Aug|Sep|Sept|Oct|Nov|Dec)\b', s)
        if mm2:
            m = shorts[mm2.group(1).lower()]
    return year, m


def extract_filing_year(s):
    if not s or not isinstance(s, str):
        return None
    m = re.search(r'(20\d{2})', s)
    return int(m.group(1)) if m else None


def parse_cpc_field(s):
    if not s or not isinstance(s, str):
        return []
    try:
        arr = json.loads(s)
        codes = []
        for it in arr:
            if isinstance(it, dict):
                code = it.get('code')
                if code:
                    codes.append(code)
            elif isinstance(it, str):
                codes.extend(re.findall(r'[A-Z]\d{2}[A-Z0-9]*/?\d*', it))
        return codes
    except Exception:
        # fallback regex
        return re.findall(r'[A-Z]\d{2}[A-Z0-9]*/?\d*', s)

# aggregate counts per level4 CPC group by filing year
counts = defaultdict(lambda: defaultdict(int))

for rec in records:
    info = rec.get('Patents_info') or ''
    if not is_germany(info):
        continue
    grant = rec.get('grant_date') or ''
    g_year, g_month = extract_year_month(grant)
    if g_year != 2019:
        continue
    if not g_month or g_month < 7:
        continue
    filing = rec.get('filing_date') or ''
    f_year = extract_filing_year(filing)
    if not f_year:
        # skip if no filing year
        continue
    cpc_field = rec.get('cpc') or ''
    codes = parse_cpc_field(cpc_field)
    for code in codes:
        # left of slash
        left = code.split('/')[0]
        left = left.strip()
        m = re.match(r'^([A-Z]\d{2}[A-Z])', left)
        if m:
            lvl4 = m.group(1)
        else:
            # fallback first 4 chars
            lvl4 = left[:4]
        counts[lvl4][f_year] += 1

# compute EMA with alpha=0.1 per group and find best year
alpha = 0.1
results = []
for grp, year_counts in counts.items():
    years = sorted(year_counts.keys())
    if not years:
        continue
    ema = None
    best_ema = None
    best_year = None
    for y in years:
        c = year_counts[y]
        if ema is None:
            ema = c
        else:
            ema = alpha * c + (1 - alpha) * ema
        if best_ema is None or ema > best_ema:
            best_ema = ema
            best_year = y
    title = cpc_title.get(grp)
    results.append({'cpc_group': grp, 'titleFull': title, 'best_year': best_year, 'best_ema': round(best_ema,4) if best_ema is not None else None, 'year_counts': dict(sorted(year_counts.items()))})

# sort by best_ema desc
results.sort(key=lambda x: (x['best_ema'] if x['best_ema'] is not None else -1), reverse=True)

print('__RESULT__:')
print(json.dumps(results))"""

env_args = {'var_call_aotf5Uc4J2te04vTC8sI8JrG': ['publicationinfo'], 'var_call_IVHWtrdfXTmXDR9hUhfcqliw': ['cpc_definition'], 'var_call_pmiPwWzDql1MApaUfscIR8R0': 'file_storage/call_pmiPwWzDql1MApaUfscIR8R0.json', 'var_call_96ynt5c54hdqWNWAPK3VhPur': 'file_storage/call_96ynt5c54hdqWNWAPK3VhPur.json', 'var_call_NsvNsGurGkwfOEmVn6LEFA53': 'file_storage/call_NsvNsGurGkwfOEmVn6LEFA53.json', 'var_call_5rHtrHNCXLAWFEXzgsUP2BJs': 'file_storage/call_5rHtrHNCXLAWFEXzgsUP2BJs.json', 'var_call_JfappaY2weevdUnaJZefgNUK': [], 'var_call_2XPqZhmiMIE2tG6E4kVTdTym': {'total_records': 211, 'de_candidates': 0, 'de_h2_2019': 0, 'sample': []}, 'var_call_JYMRIndR2IxmIxVTHhgbHqN8': {'total': 211, 'cnt_contains_DE': 210, 'cnt_from_DE': 14, 'examples_with_DE_dash': []}, 'var_call_ma8cV75gThAyCVwBmIrwfoZw': 'file_storage/call_ma8cV75gThAyCVwBmIrwfoZw.json'}

exec(code, env_args)
