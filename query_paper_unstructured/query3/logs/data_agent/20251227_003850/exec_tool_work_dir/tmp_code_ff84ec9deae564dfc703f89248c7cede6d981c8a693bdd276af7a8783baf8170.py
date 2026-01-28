code = """import json, re

# Load storage results
with open(var_call_WPw67wgXaskTYVaZBay2hrci, 'r', encoding='utf-8') as f:
    paper_docs = json.load(f)
with open(var_call_1ntqvKIgCKBFjh2PBN0ocFX8, 'r', encoding='utf-8') as f:
    citations = json.load(f)

# Build docs map: title -> text
docs_map = {}
for d in paper_docs:
    fn = d.get('filename') or ''
    text = d.get('text') or ''
    if not fn or not text:
        continue
    title = fn.strip()
    if title.lower().endswith('.txt'):
        title = title[:-4]
    docs_map[title] = text

# Build citation totals map
citation_map = {}
for rec in citations:
    t = rec.get('title')
    tc = rec.get('total_citations')
    try:
        citation_map[t] = int(tc)
    except Exception:
        try:
            citation_map[t] = int(float(tc))
        except Exception:
            citation_map[t] = None

VENUES = ['chi', 'cscw', 'ubicomp', 'dis', 'pervasivehealth', 'www', 'iui', 'ozchi', 'tei', 'ah']
YEAR_MIN = 2000
YEAR_MAX = 2030

# Helper to extract year from header

def extract_year(text):
    head = text[:6000]
    lines = head.split('\n')[:80]
    years_found = []
    # Venue lines
    for line in lines:
        low = line.lower()
        if any(v in low for v in VENUES):
            years = re.findall("\b(19\d{2}|20\d{2})\b", line)
            years_int = []
            for y in years:
                try:
                    yi = int(y)
                    if YEAR_MIN <= yi <= YEAR_MAX:
                        years_int.append(yi)
                except Exception:
                    pass
            if years_int:
                years_found.extend(years_int)
    if years_found:
        return max(years_found)
    # Copyright lines
    for line in lines:
        low = line.lower()
        if 'copyright' in low or '©' in line or '(c)' in low:
            years = re.findall("\b(19\d{2}|20\d{2})\b", line)
            years_int = []
            for y in years:
                try:
                    yi = int(y)
                    if YEAR_MIN <= yi <= YEAR_MAX:
                        years_int.append(yi)
                except Exception:
                    pass
            if years_int:
                return max(years_int)
    # Fallback: any year in head between bounds, take max
    years = re.findall("\b(19\d{2}|20\d{2})\b", head)
    cand = []
    for y in years:
        try:
            yi = int(y)
            if YEAR_MIN <= yi <= YEAR_MAX:
                cand.append(yi)
        except Exception:
            pass
    if cand:
        return max(cand)
    return None

# Filter citations for titles containing 'empirical'
empirical_titles = [rec['title'] for rec in citations if isinstance(rec.get('title'), str) and ('empirical' in rec['title'].lower())]

results = []
for title in empirical_titles:
    text = docs_map.get(title)
    if not text:
        # try relaxed lookup stripping quotes
        t2 = title.strip().strip('"')
        text = docs_map.get(t2)
    if not text:
        continue
    year = extract_year(text)
    if year is None or year <= 2016:
        continue
    tc = citation_map.get(title)
    if tc is None:
        tc = citation_map.get(title.strip().strip('"'))
    if tc is None:
        # case-insensitive exact match against docs_map keys
        for k in citation_map.keys():
            if isinstance(k, str) and k.lower() == title.lower():
                tc = citation_map[k]
                break
    if tc is None:
        continue
    results.append({'title': title, 'total_citations': tc})

# Sort results by citations desc then title
results.sort(key=lambda x: (-x['total_citations'], x['title']))

print("__RESULT__:")
print(json.dumps(results))"""

env_args = {'var_call_WPw67wgXaskTYVaZBay2hrci': 'file_storage/call_WPw67wgXaskTYVaZBay2hrci.json', 'var_call_1ntqvKIgCKBFjh2PBN0ocFX8': 'file_storage/call_1ntqvKIgCKBFjh2PBN0ocFX8.json', 'var_call_mYMhTkK3uSl7cJInG6UsluoL': [], 'var_call_lk7wSCfnHF8Qhr71426NHQZw': [], 'var_call_B6tTsBXqGYIrbqBYA3iowVR1': [], 'var_call_rHchAtTQ45xNOeRMELsaL42l': []}

exec(code, env_args)
