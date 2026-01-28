code = """import json, re

# Load the Mongo query result (full JSON file path is stored in var_call_XSYC...)
with open(var_call_XSYCXYkyEzHnvbpqCSiwmvqK, 'r', encoding='utf-8') as f:
    docs = json.load(f)

# Load the citations aggregation result
with open(var_call_HYYIfs9tJvEVZZTKL5YV42Wb, 'r', encoding='utf-8') as f:
    citations = json.load(f)

# Build a map from title to total_citations (int)
cit_map = {}
for rec in citations:
    t = rec.get('title')
    c = rec.get('total_citations')
    try:
        cit_map[t] = int(c)
    except:
        try:
            cit_map[t] = int(float(c))
        except:
            cit_map[t] = None

results = []

for d in docs:
    filename = d.get('filename','')
    title = filename[:-4] if filename.lower().endswith('.txt') else filename
    text = d.get('text','')
    # find first 4-digit year between 2000 and 2026
    years = re.findall(r'\b(20\d{2})\b', text)
    pub_year = None
    for y in years:
        iy = int(y)
        if 2000 <= iy <= 2026:
            pub_year = iy
            break
    if pub_year is None:
        # try to infer from filename if contains year
        m = re.search(r'(20\d{2})', filename)
        if m:
            pub_year = int(m.group(1))
    if pub_year is None:
        # skip if no year found
        continue
    if pub_year > 2016:
        total_cits = cit_map.get(title)
        if total_cits is None:
            # try to match with slight variations: remove punctuation
            def norm(s):
                return re.sub(r'[^A-Za-z0-9 ]','', s).strip().lower()
            found = None
            nt = norm(title)
            for k in cit_map:
                if norm(k) == nt:
                    found = cit_map[k]
                    break
            total_cits = found
        # append
        results.append({"title": title, "total_citations": total_cits if total_cits is not None else None, "year": pub_year})

# Sort by title
results = sorted(results, key=lambda x: x['title'])

import json as _json
print("__RESULT__:")
print(_json.dumps(results))"""

env_args = {'var_call_MMC0T6SATnlhtbspdcuX99Sf': ['paper_docs'], 'var_call_XSYCXYkyEzHnvbpqCSiwmvqK': 'file_storage/call_XSYCXYkyEzHnvbpqCSiwmvqK.json', 'var_call_GT4RCWgryqYG2eCHqGluJwcA': ['Citations', 'sqlite_sequence'], 'var_call_HYYIfs9tJvEVZZTKL5YV42Wb': 'file_storage/call_HYYIfs9tJvEVZZTKL5YV42Wb.json'}

exec(code, env_args)
