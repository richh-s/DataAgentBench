code = """import json, re

# Load subset of docs that contain 'empirical'
with open(var_call_A4dO1XSE2oNscPIdA44yQl9j, 'r', encoding='utf-8') as f:
    empirical_docs = json.load(f)

# Load aggregated citation totals
with open(var_call_1ntqvKIgCKBFjh2PBN0ocFX8, 'r', encoding='utf-8') as f:
    citations = json.load(f)

# Build citation map
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

# Helper to extract publication year from header
YEAR_MIN = 2017
YEAR_MAX = 2030

def extract_year(text):
    head = text[:6000]
    years = re.findall("\\b(19\\d{2}|20\\d{2})\\b", head)
    cand = []
    for ystr in years:
        try:
            y = int(ystr)
            if YEAR_MIN <= y <= YEAR_MAX:
                cand.append(y)
        except Exception:
            pass
    if cand:
        return max(cand)
    return None

results = []
for doc in empirical_docs:
    fn = doc.get('filename') or ''
    text = doc.get('text') or ''
    if not fn or not text:
        continue
    title = fn.strip()
    if title.lower().endswith('.txt'):
        title = title[:-4]
    year = extract_year(text)
    if year is None:
        continue
    # After 2016
    if year <= 2016:
        continue
    # Join citations
    tc = citation_map.get(title)
    if tc is None:
        # Try alternative without surrounding quotes
        alt = title.strip().strip('"')
        tc = citation_map.get(alt)
    if tc is None:
        # Case-insensitive exact match
        low_title = title.lower()
        for k, v in citation_map.items():
            if isinstance(k, str) and k.lower() == low_title:
                tc = v
                break
    if tc is None:
        continue
    results.append({'title': title, 'total_citations': tc})

# Sort results
results.sort(key=lambda x: (-x['total_citations'], x['title']))

print("__RESULT__:")
print(json.dumps(results))"""

env_args = {'var_call_WPw67wgXaskTYVaZBay2hrci': 'file_storage/call_WPw67wgXaskTYVaZBay2hrci.json', 'var_call_1ntqvKIgCKBFjh2PBN0ocFX8': 'file_storage/call_1ntqvKIgCKBFjh2PBN0ocFX8.json', 'var_call_mYMhTkK3uSl7cJInG6UsluoL': [], 'var_call_lk7wSCfnHF8Qhr71426NHQZw': [], 'var_call_B6tTsBXqGYIrbqBYA3iowVR1': [], 'var_call_rHchAtTQ45xNOeRMELsaL42l': [], 'var_call_A4dO1XSE2oNscPIdA44yQl9j': 'file_storage/call_A4dO1XSE2oNscPIdA44yQl9j.json'}

exec(code, env_args)
