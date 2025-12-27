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

YEAR_MIN = 1990
YEAR_MAX = 2030

def extract_year(text):
    head = text[:3000]
    m = re.search("\\b(19\\d{2}|20\\d{2})\\b", head)
    if m:
        y = int(m.group(1))
        if YEAR_MIN <= y <= YEAR_MAX:
            return y
    return None

results = []
for doc in paper_docs:
    filename = doc.get('filename') or ''
    text = doc.get('text') or ''
    if not filename or not text:
        continue
    # Title from filename without .txt
    title = filename.strip()
    if title.lower().endswith('.txt'):
        title = title[:-4]
    year = extract_year(text)
    if year is None or year <= 2016:
        continue
    tl = text.lower()
    fl = filename.lower()
    if 'empirical' not in tl and 'empirical' not in fl:
        continue
    total_citations = citation_map.get(title)
    if total_citations is None:
        alt = title.strip().strip('"')
        total_citations = citation_map.get(alt)
    if total_citations is None:
        # try case-insensitive match
        for k, v in citation_map.items():
            if k.lower() == title.lower():
                total_citations = v
                break
    if total_citations is None:
        continue
    results.append({'title': title, 'total_citations': total_citations, 'year': year})

results.sort(key=lambda x: (-x['total_citations'], x['title']))

final_out = [{'title': r['title'], 'total_citations': r['total_citations']} for r in results]

print("__RESULT__:")
print(json.dumps(final_out))"""

env_args = {'var_call_WPw67wgXaskTYVaZBay2hrci': 'file_storage/call_WPw67wgXaskTYVaZBay2hrci.json', 'var_call_1ntqvKIgCKBFjh2PBN0ocFX8': 'file_storage/call_1ntqvKIgCKBFjh2PBN0ocFX8.json', 'var_call_mYMhTkK3uSl7cJInG6UsluoL': []}

exec(code, env_args)
