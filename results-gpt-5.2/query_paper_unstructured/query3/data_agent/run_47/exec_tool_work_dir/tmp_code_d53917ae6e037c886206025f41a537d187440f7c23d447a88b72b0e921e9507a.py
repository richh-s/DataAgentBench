code = """import json, re, pandas as pd

# Load full Mongo docs
mongo_src = var_call_ThTUxJeJYCknVvNemiyFDHhn
if isinstance(mongo_src, str) and mongo_src.endswith('.json'):
    with open(mongo_src, 'r', encoding='utf-8') as f:
        docs = json.load(f)
else:
    docs = mongo_src

# Load citations totals
cit_src = var_call_xXm8W2E2Sma8hAQmYX4eN1Ac
if isinstance(cit_src, str) and cit_src.endswith('.json'):
    with open(cit_src, 'r', encoding='utf-8') as f:
        cits = json.load(f)
else:
    cits = cit_src

# Parse year from text
year_patterns = [
    re.compile(r"\b(19\d{2}|20\d{2})\b"),
]

def extract_year(text):
    # Prefer year near top in first 2000 chars
    head = text[:3000]
    years = [int(y) for y in re.findall(r"\b(19\d{2}|20\d{2})\b", head)]
    # Filter plausible publication years
    years = [y for y in years if 1980 <= y <= 2026]
    if not years:
        return None
    # Heuristic: choose most frequent in head; tie -> min (often pub year appears several times)
    from collections import Counter
    cnt = Counter(years)
    maxfreq = max(cnt.values())
    candidates = [y for y,f in cnt.items() if f==maxfreq]
    return min(candidates)

def is_empirical(text):
    t = text.lower()
    # contribution may appear as metadata; fallback: look for explicit tag or common phrasing
    if 'contribution' in t and 'empirical' in t:
        return True
    if re.search(r"\bempirical\b", t):
        return True
    return False

rows = []
for d in docs:
    filename = d.get('filename','')
    title = filename[:-4] if filename.lower().endswith('.txt') else filename
    text = d.get('text','') or ''
    year = extract_year(text)
    emp = is_empirical(text)
    rows.append({'title': title, 'year': year, 'empirical': emp})

pdf = pd.DataFrame(rows)

# Filter papers published after 2016 and empirical contribution
pdf_f = pdf[(pdf['empirical']==True) & (pdf['year'].notna()) & (pdf['year']>2016)].copy()

cdf = pd.DataFrame(cits)
# ensure numeric
cdf['total_citations'] = pd.to_numeric(cdf['total_citations'], errors='coerce')

out = pdf_f.merge(cdf, on='title', how='left')
out['total_citations'] = out['total_citations'].fillna(0).astype(int)

# Select output columns
out2 = out[['title','total_citations']].sort_values(['total_citations','title'], ascending=[False, True])

result = out2.to_dict(orient='records')
print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_call_ThTUxJeJYCknVvNemiyFDHhn': 'file_storage/call_ThTUxJeJYCknVvNemiyFDHhn.json', 'var_call_xXm8W2E2Sma8hAQmYX4eN1Ac': 'file_storage/call_xXm8W2E2Sma8hAQmYX4eN1Ac.json'}

exec(code, env_args)
