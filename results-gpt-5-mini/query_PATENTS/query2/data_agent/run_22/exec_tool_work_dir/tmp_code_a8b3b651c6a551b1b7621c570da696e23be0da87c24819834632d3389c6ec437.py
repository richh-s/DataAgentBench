code = """import json
import re
from collections import defaultdict

# Load data files from storage-provided file paths
with open(var_call_Ctbh7xSwBiDEL5eLYGOJSLzr, 'r', encoding='utf-8') as f:
    records = json.load(f)
with open(var_call_qnrgzrh6Po2cYqOCX4AYJQ5X, 'r', encoding='utf-8') as f:
    cpc_defs = json.load(f)

# Build mapping from symbol to titleFull
symbol_to_title = {row.get('symbol'): row.get('titleFull') for row in cpc_defs}

# Helper to detect Germany in Patents_info
def is_germany(pi):
    if not pi:
        return False
    pi_low = pi.lower()
    # check for 'de' country code or patterns like 'from de' or 'de-'
    if re.search(r'\bde\b', pi_low):
        return True
    if 'de-' in pi or '-de' in pi_low:
        return True
    if ' from de' in pi_low:
        return True
    return False

# Helper to parse month and year from grant_date
months = {
    'january':1,'jan':1,'february':2,'feb':2,'march':3,'mar':3,'april':4,'apr':4,
    'may':5,'june':6,'jun':6,'july':7,'jul':7,'august':8,'aug':8,'september':9,'sep':9,'sept':9,
    'october':10,'oct':10,'november':11,'nov':11,'december':12,'dec':12
}

def parse_grant_date(gd):
    if not gd:
        return None, None
    gd_low = gd.lower()
    # find year
    y_match = re.search(r'(20\d{2}|19\d{2})', gd_low)
    year = int(y_match.group(0)) if y_match else None
    # find month name
    month = None
    for name, num in months.items():
        if name in gd_low:
            month = num
            break
    # numeric month
    if month is None:
        m_match = re.search(r'\b(0?[1-9]|1[0-2])\b', gd_low)
        if m_match:
            month = int(m_match.group(0))
    return year, month

# Helper to parse filing year
def parse_filing_year(fd):
    if not fd:
        return None
    m = re.search(r'(20\d{2}|19\d{2})', fd)
    return int(m.group(0)) if m else None

# Aggregate counts per CPC level-4 group per filing year for patents granted in H2 2019 in Germany
counts = defaultdict(lambda: defaultdict(int))
for rec in records:
    pi = rec.get('Patents_info') or ''
    if not is_germany(pi):
        continue
    gd = rec.get('grant_date') or ''
    g_year, g_month = parse_grant_date(gd)
    if g_year != 2019 or g_month is None or g_month < 7:
        continue
    fd = rec.get('filing_date') or ''
    f_year = parse_filing_year(fd)
    if f_year is None:
        continue
    # parse cpc codes
    cpc_field = rec.get('cpc') or ''
    cpc_list = []
    if isinstance(cpc_field, list):
        cpc_list = cpc_field
    else:
        try:
            cpc_list = json.loads(cpc_field)
        except Exception:
            try:
                import ast
                cpc_list = ast.literal_eval(cpc_field)
            except Exception:
                cpc_list = []
    for entry in cpc_list:
        if isinstance(entry, dict):
            code = entry.get('code')
        else:
            # if entry is a string like code
            code = entry
        if not code:
            continue
        code = str(code).strip()
        if len(code) < 3:
            continue
        group = code[:3]
        counts[group][f_year] += 1

# Compute EMA for each group across filing years (sorted ascending)
alpha = 0.1
results = []
for group, year_counts in counts.items():
    years = sorted(year_counts.keys())
    ema = None
    ema_by_year = {}
    for y in years:
        c = year_counts[y]
        if ema is None:
            ema = float(c)
        else:
            ema = alpha * float(c) + (1 - alpha) * ema
        ema_by_year[y] = ema
    best_year = max(ema_by_year.items(), key=lambda x: x[1])[0]
    best_ema = ema_by_year[best_year]
    title = symbol_to_title.get(group, '')
    results.append({'symbol': group, 'titleFull': title, 'best_year': int(best_year), 'best_ema': round(best_ema, 4)})

# Sort results by best_ema descending
results.sort(key=lambda x: x['best_ema'], reverse=True)

# Print result in required format as JSON-serializable string
print("__RESULT__:")
print(json.dumps(results))"""

env_args = {'var_call_rDzW7jAFtC60XL4d7FzOfcKl': ['publicationinfo'], 'var_call_KjtenStxvDRSkIeJrNS9EeBL': ['cpc_definition'], 'var_call_Ctbh7xSwBiDEL5eLYGOJSLzr': 'file_storage/call_Ctbh7xSwBiDEL5eLYGOJSLzr.json', 'var_call_qnrgzrh6Po2cYqOCX4AYJQ5X': 'file_storage/call_qnrgzrh6Po2cYqOCX4AYJQ5X.json'}

exec(code, env_args)
