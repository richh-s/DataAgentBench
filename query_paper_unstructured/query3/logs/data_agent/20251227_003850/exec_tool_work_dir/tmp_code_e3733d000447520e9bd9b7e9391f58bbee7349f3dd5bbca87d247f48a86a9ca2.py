code = """import json, re

# Load MongoDB paper documents
with open(var_call_WPw67wgXaskTYVaZBay2hrci, 'r', encoding='utf-8') as f:
    paper_docs = json.load(f)

# Load aggregated citation totals
with open(var_call_1ntqvKIgCKBFjh2PBN0ocFX8, 'r', encoding='utf-8') as f:
    citations = json.load(f)

# Build mapping from title to total citations (int)
citation_map = {}
for rec in citations:
    title = rec.get('title')
    tc = rec.get('total_citations')
    try:
        citation_map[title] = int(tc)
    except Exception:
        try:
            citation_map[title] = int(float(tc))
        except Exception:
            citation_map[title] = None

# Helper to get publication year as the max of years 2017-2030 appearing in header
YEAR_MIN = 2017
YEAR_MAX = 2030

year_pattern = re.compile(r"\b(19\d{2}|20\d{2})\b")


def get_pub_year(text):
    head = text[:4000]
    years = []
    for m in year_pattern.finditer(head):
        y = int(m.group(1))
        if YEAR_MIN <= y <= YEAR_MAX:
            years.append(y)
    if years:
        return max(years)
    return None

results = []
for doc in paper_docs:
    filename = doc.get('filename') or ''
    text = doc.get('text') or ''
    if not filename or not text:
        continue
    title = filename.strip()
    if title.lower().endswith('.txt'):
        title = title[:-4]
    year = get_pub_year(text)
    if year is None:
        continue
    # Published after 2016
    if year <= 2016:
        continue
    # Empirical contribution: substring match
    if 'empirical' not in text.lower() and 'empirical' not in title.lower():
        continue
    total_citations = citation_map.get(title)
    if total_citations is None:
        alt = title.strip().strip('"')
        total_citations = citation_map.get(alt)
    if total_citations is None:
        # case-insensitive exact match
        for k, v in citation_map.items():
            if isinstance(k, str) and k.lower() == title.lower():
                total_citations = v
                break
    if total_citations is None:
        continue
    results.append({'title': title, 'total_citations': total_citations})

# Sort by total citations desc then title
results.sort(key=lambda x: (-x['total_citations'], x['title']))

print("__RESULT__:")
print(json.dumps(results))"""

env_args = {'var_call_WPw67wgXaskTYVaZBay2hrci': 'file_storage/call_WPw67wgXaskTYVaZBay2hrci.json', 'var_call_1ntqvKIgCKBFjh2PBN0ocFX8': 'file_storage/call_1ntqvKIgCKBFjh2PBN0ocFX8.json', 'var_call_mYMhTkK3uSl7cJInG6UsluoL': [], 'var_call_lk7wSCfnHF8Qhr71426NHQZw': []}

exec(code, env_args)
