code = """import json

# Load stored query results
with open(var_call_FA7KkPgziK2Q90TPgVoTXk32, 'r', encoding='utf-8') as f:
    funding = json.load(f)
with open(var_call_mka5UEs3QWagkOJUBTVZMduK, 'r', encoding='utf-8') as f:
    docs = json.load(f)

# Normalize funding amounts and project names
for r in funding:
    amt = r.get('Amount', 0)
    try:
        r['Amount'] = int(amt)
    except Exception:
        s = str(amt).replace(',', '').strip()
        try:
            r['Amount'] = int(s)
        except Exception:
            r['Amount'] = 0
    r['Project_Name_norm'] = str(r.get('Project_Name', '')).strip()

# Build concatenated docs text and per-doc lowercased texts
docs_texts = [d.get('text', '') for d in docs]
docs_texts_lower = [t.lower() for t in docs_texts]

# Park-related keywords
park_keywords = ['park', 'playground', 'walkway', 'bench', 'benches', 'shade structure', 'paver', 'play area']

matched = {}

# First: direct name match with proximity check for "completed" and "2022"
for rec in funding:
    pname = rec['Project_Name_norm']
    if not pname:
        continue
    pname_l = pname.lower()
    # only consider park-related funding rows
    if not any(k in pname_l for k in park_keywords):
        continue
    for text_l in docs_texts_lower:
        idx = text_l.find(pname_l)
        if idx != -1:
            start = max(0, idx - 300)
            end = min(len(text_l), idx + 300)
            window = text_l[start:end]
            if 'completed' in window and '2022' in window:
                matched[pname] = matched.get(pname, 0) + rec['Amount']
                break
            # fallback: if document contains both words anywhere
            if 'completed' in text_l and '2022' in text_l:
                matched[pname] = matched.get(pname, 0) + rec['Amount']
                break

# Second: find doc windows that mention park + completed + 2022, then map by token overlap
for i, text_l in enumerate(docs_texts_lower):
    if 'park' in text_l and 'completed' in text_l and '2022' in text_l:
        # find lines around occurrences
        lines = docs_texts[i].splitlines()
        for j, line in enumerate(lines):
            w = line.lower()
            if 'park' in w and 'completed' in w and '2022' in w:
                # build a small window of nearby lines
                s = max(0, j-3)
                e = min(len(lines), j+4)
                window = '\n'.join(lines[s:e]).lower()
                for rec in funding:
                    pname = rec['Project_Name_norm']
                    pname_l = pname.lower()
                    if not any(k in pname_l for k in park_keywords):
                        continue
                    # tokens from project name
                    tokens = [tok for tok in pname_l.replace('-', ' ').split() if len(tok) > 4]
                    if any(tok in window for tok in tokens):
                        matched[pname] = matched.get(pname, 0) + rec['Amount']

# Prepare final aggregation
matched_list = [{'Project_Name': k, 'Amount': v} for k, v in matched.items()]
total = sum(v for v in matched.values())

result = {'total_funding': total, 'matched_projects': matched_list, 'matched_count': len(matched_list)}

print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_call_FA7KkPgziK2Q90TPgVoTXk32': 'file_storage/call_FA7KkPgziK2Q90TPgVoTXk32.json', 'var_call_mka5UEs3QWagkOJUBTVZMduK': 'file_storage/call_mka5UEs3QWagkOJUBTVZMduK.json'}

exec(code, env_args)
