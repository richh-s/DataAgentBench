code = """import json, re

# Load the Mongo query result (stored as a JSON file path)
with open(var_call_eqVpDzSJ4eJnf2cjjmc0mqok, 'r', encoding='utf-8') as f:
    papers = json.load(f)

# Load the citations query result
with open(var_call_pHoBui3CDBVkbmtrFLlBSEXR, 'r', encoding='utf-8') as f:
    citations = json.load(f)

# Helper to extract year from text: find first 4-digit year between 2000 and 2026
year_regex = re.compile(r"\b(20\d{2})\b")

def extract_year(text):
    m = year_regex.search(text)
    if m:
        try:
            y = int(m.group(1))
            return y
        except:
            return None
    return None

# Build set of titles that are empirical and published after 2016
selected_titles = set()
for doc in papers:
    filename = doc.get('filename','')
    text = doc.get('text','') or ''
    title = filename[:-4] if filename.lower().endswith('.txt') else filename
    year = extract_year(text)
    if year and year > 2016 and re.search(r"\bempirical\b", text, re.IGNORECASE):
        selected_titles.add(title)

# Sum citations per title
citation_sums = {}
for rec in citations:
    t = rec.get('title')
    cnt = rec.get('citation_count', 0)
    try:
        cnt_int = int(cnt)
    except:
        try:
            cnt_int = int(float(cnt))
        except:
            cnt_int = 0
    citation_sums[t] = citation_sums.get(t, 0) + cnt_int

# Build result list
result = []
for t in sorted(selected_titles):
    total = citation_sums.get(t, 0)
    result.append({'title': t, 'total_citations': total})

import json
print("__RESULT__:")
print(json.dumps(result))"""

env_args = {'var_call_1TXxaCavn8Z9lCOvKK9Pehmr': ['paper_docs'], 'var_call_eqVpDzSJ4eJnf2cjjmc0mqok': 'file_storage/call_eqVpDzSJ4eJnf2cjjmc0mqok.json', 'var_call_pHoBui3CDBVkbmtrFLlBSEXR': 'file_storage/call_pHoBui3CDBVkbmtrFLlBSEXR.json'}

exec(code, env_args)
