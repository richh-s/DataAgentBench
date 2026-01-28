code = """import json
import re
from collections import defaultdict, OrderedDict

# Load stored results from previous tool calls
pub_path = var_call_bw5fdoDnIu059RTr23gOMQyC
cpc_def_path = var_call_chi0ECWXARfCqqTpfRLWbUyi

with open(pub_path, 'r', encoding='utf-8') as f:
    pubs = json.load(f)
with open(cpc_def_path, 'r', encoding='utf-8') as f:
    cpc_defs = json.load(f)

# Helper: parse month and year from grant_date
months = {m.lower(): i+1 for i,m in enumerate(['January','February','March','April','May','June','July','August','September','October','November','December'])}
month_abbr = {m[:3].lower():v for m,v in months.items()}

def parse_month_year(s):
    if not s or not isinstance(s, str):
        return None, None
    s_clean = s.replace('.', '').replace(',', ' ').lower()
    ymatch = re.search(r'(20\d{2}|19\d{2})', s)
    year = int(ymatch.group(0)) if ymatch else None
    mon = None
    for name, num in months.items():
        if name.lower() in s_clean:
            mon = num
            break
    if mon is None:
        for abbr, num in month_abbr.items():
            if re.search(r'\b'+re.escape(abbr)+r'\b', s_clean):
                mon = num
                break
    return mon, year

# Helper: determine if patent is Germany-related via Patents_info
def is_germany(s):
    if not s or not isinstance(s, str):
        return False
    s_up = s.upper()
    if re.search(r'\bDE\b', s_up):
        return True
    if 'DE-' in s_up:
        return True
    return False

# Parse CPC JSON-like field
import ast

def parse_cpc_field(s):
    if not s or not isinstance(s, str):
        return []
    try:
        return json.loads(s)
    except Exception:
        try:
            return ast.literal_eval(s)
        except Exception:
            codes = re.findall(r'"code":\s*"([A-Z0-9/\\]+)"', s)
            return [{'code': c} for c in codes]

# Build records for Germany patents granted in H2 2019
records = []
for rec in pubs:
    grant = rec.get('grant_date')
    mon, yr = parse_month_year(grant)
    if yr != 2019 or mon is None or mon < 7:
        continue
    if not is_germany(rec.get('Patents_info','')):
        continue
    filing = rec.get('filing_date','')
    fmatch = re.search(r'(20\d{2}|19\d{2})', filing)
    if not fmatch:
        continue
    filing_year = int(fmatch.group(0))
    entries = parse_cpc_field(rec.get('cpc',''))
    codes = set()
    for e in entries:
        code = None
        if isinstance(e, dict):
            code = e.get('code')
        elif isinstance(e, str):
            code = e
        if not code or len(code) < 3:
            continue
        group = code[:3].upper()
        codes.add(group)
    if not codes:
        continue
    for g in codes:
        records.append({'rowid': rec.get('rowid'), 'group': g, 'filing_year': filing_year})

# Aggregate counts per group per filing year (unique patents)
group_year_counts = defaultdict(lambda: defaultdict(set))
for r in records:
    group_year_counts[r['group']][r['filing_year']].add(r['rowid'])

# Convert to counts
group_year_counts_num = {}
for g, years in group_year_counts.items():
    group_year_counts_num[g] = {yr: len(rowids) for yr, rowids in years.items()}

# EMA computation per group across sorted years
alpha = 0.1
results = []
for g, ycounts in group_year_counts_num.items():
    years = sorted(ycounts.keys())
    if not years:
        continue
    ema_by_year = OrderedDict()
    ema = None
    for y in years:
        x = ycounts[y]
        if ema is None:
            ema = x
        else:
            ema = alpha * x + (1-alpha) * ema
        ema_by_year[y] = ema
    best_year = max(ema_by_year.items(), key=lambda kv: kv[1])[0]
    peak_ema = ema_by_year[best_year]
    results.append({'cpc_group': g, 'best_year': int(best_year), 'peak_ema': float(peak_ema), 'ema_by_year': {str(k): v for k,v in ema_by_year.items()}})

# Attach titleFull from CPC definitions (level 4)
cpc_title_map = {item.get('symbol'): item.get('titleFull') for item in cpc_defs}
for r in results:
    title = cpc_title_map.get(r['cpc_group']) or cpc_title_map.get(r['cpc_group'].upper()) or ''
    r['titleFull'] = title

# Keep only groups that exist in level 4 definitions (non-empty title)
filtered_results = [r for r in results if r['titleFull']]
# Sort by peak_ema desc and take top 10
top_results = sorted(filtered_results, key=lambda x: x['peak_ema'], reverse=True)[:10]

lines = []
for r in top_results:
    lines.append(f"{r['cpc_group']} - {r['titleFull']} - Best year: {r['best_year']} (peak EMA: {r['peak_ema']:.2f})")
plain_text = '\n'.join(lines) if lines else 'No results found.'

output = {'top_results': top_results, 'plain_text': plain_text}

print("__RESULT__:")
print(json.dumps(output))"""

env_args = {'var_call_JIcWp4aOobxVTcnSOux2y8l1': 'file_storage/call_JIcWp4aOobxVTcnSOux2y8l1.json', 'var_call_bw5fdoDnIu059RTr23gOMQyC': 'file_storage/call_bw5fdoDnIu059RTr23gOMQyC.json', 'var_call_chi0ECWXARfCqqTpfRLWbUyi': 'file_storage/call_chi0ECWXARfCqqTpfRLWbUyi.json'}

exec(code, env_args)
