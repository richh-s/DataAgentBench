code = """import json
import re

# Load data from storage file paths provided by previous tool calls
with open(var_call_Liu1vSigC9Z5tijabwYnOcGH, 'r', encoding='utf-8') as f:
    papers = json.load(f)
with open(var_call_BzrI7mKobYSyysvHGEzLXQU3, 'r', encoding='utf-8') as f:
    citations = json.load(f)

# Build a lookup for citations: normalize titles by stripping and removing surrounding quotes and lowercasing
def normalize_title(t):
    if t is None:
        return ''
    t = t.strip()
    # remove surrounding double quotes if present
    if len(t) >= 2 and ((t[0] == '"' and t[-1] == '"') or (t[0] == "'" and t[-1] == "'")):
        t = t[1:-1].strip()
    return t.lower()

cit_lookup = {}
for rec in citations:
    title = rec.get('title')
    total = rec.get('total_citations')
    try:
        total_int = int(total)
    except Exception:
        try:
            total_int = int(float(total))
        except Exception:
            total_int = None
    cit_lookup[normalize_title(title)] = total_int

# Function to extract year from text: prefer first match in first 500 chars, else anywhere
year_re = re.compile(r"(19|20)\d{2}")
results = []
for doc in papers:
    filename = doc.get('filename','')
    title = filename
    if title.lower().endswith('.txt'):
        title = title[:-4]
    text = doc.get('text','') or ''
    # extract year
    search_region = text[:1000]
    m = year_re.search(search_region)
    if not m:
        m = year_re.search(text)
    year = int(m.group(0)) if m else None
    # determine if 'empirical' contribution is present (substring match, case-insensitive)
    has_empirical = 'empirical' in text.lower()
    if has_empirical and year and year > 2016:
        norm = normalize_title(title)
        total_cits = cit_lookup.get(norm)
        results.append({
            'title': title,
            'year': year,
            'total_citations': total_cits
        })

# Prepare output: list of titles and total citations
out = [{ 'title': r['title'], 'total_citations': r['total_citations'] } for r in results]

print("__RESULT__:")
print(json.dumps(out))"""

env_args = {'var_call_BMCbEnX1Ob45VRFDVtRWfiBk': ['paper_docs'], 'var_call_KmGI9YfsVjT2T2w3ADjImlEK': ['Citations', 'sqlite_sequence'], 'var_call_Liu1vSigC9Z5tijabwYnOcGH': 'file_storage/call_Liu1vSigC9Z5tijabwYnOcGH.json', 'var_call_BzrI7mKobYSyysvHGEzLXQU3': 'file_storage/call_BzrI7mKobYSyysvHGEzLXQU3.json'}

exec(code, env_args)
