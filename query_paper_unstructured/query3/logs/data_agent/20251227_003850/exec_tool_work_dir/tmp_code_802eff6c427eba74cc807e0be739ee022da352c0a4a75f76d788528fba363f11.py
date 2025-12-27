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

# Simple year extraction: find the first 4-digit year in the first 3000 chars
YEAR_MIN = 1990
YEAR_MAX = 2030

def extract_year(text):
    head = text[:3000]
    m = re.search(r"\b(19\d{2}|20\d{2})\b", head)
    if m:
        y = int(m.group(1))
        if YEAR_MIN <= y <= YEAR_MAX:
            return y
    return None

# Empirical contribution check: substring match

def has_empirical_contribution(text):
    return bool(re.search(r"\bempirical\b", text.lower()))

results = []
for doc in paper_docs:
    filename = doc.get('filename')
    text = doc.get('text') or ''
    if not filename or not text:
        continue
    # Title from filename without .txt
    title = filename.strip()
    if title.lower().endswith('.txt'):
        title = title[:-4]
    year = extract_year(text)
    if year is None:
        continue
    if year <= 2016:
        continue
    if not has_empirical_contribution(text):
        continue
    total_citations = citation_map.get(title)
    if total_citations is None:
        alt = title.strip().strip('"')
        total_citations = citation_map.get(alt)
    if total_citations is None:
        continue
    results.append({'title': title, 'total_citations': total_citations})

# Sort by total citations descending, then title
results.sort(key=lambda x: (-x['total_citations'], x['title']))

print("__RESULT__:")
print(json.dumps(results))"""

env_args = {'var_call_WPw67wgXaskTYVaZBay2hrci': 'file_storage/call_WPw67wgXaskTYVaZBay2hrci.json', 'var_call_1ntqvKIgCKBFjh2PBN0ocFX8': 'file_storage/call_1ntqvKIgCKBFjh2PBN0ocFX8.json'}

exec(code, env_args)
