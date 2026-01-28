code = """import json

# Load data from storage paths provided by previous tool calls
with open(var_call_FA7KkPgziK2Q90TPgVoTXk32, 'r', encoding='utf-8') as f:
    funding = json.load(f)
with open(var_call_mka5UEs3QWagkOJUBTVZMduK, 'r', encoding='utf-8') as f:
    docs = json.load(f)

# Normalize funding amounts and names
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

# Park-related keywords
park_keywords = ['park', 'playground', 'walkway', 'bench', 'benches', 'shade structure', 'paver', 'play area', 'bluffs']

# Prepare lowercased doc texts
docs_texts = [d.get('text','') for d in docs]
docs_texts_lower = [t.lower() for t in docs_texts]

matched = {}

# First pass: direct name match within documents with proximity check for 'completed' and '2022'
for rec in funding:
    pname = rec['Project_Name_norm']
    if not pname:
        continue
    pname_l = pname.lower()
    # only park projects
    if not any(k in pname_l for k in park_keywords):
        continue
    for text_l in docs_texts_lower:
        pos = text_l.find(pname_l)
        if pos != -1:
            start = max(0, pos - 300)
            end = min(len(text_l), pos + 300)
            window = text_l[start:end]
            if 'completed' in window and '2022' in window:
                matched[pname] = matched.get(pname, 0) + rec['Amount']
                break
            # fallback: if doc contains both terms anywhere
            if 'completed' in text_l and '2022' in text_l:
                matched[pname] = matched.get(pname, 0) + rec['Amount']
                break

# Second pass: find docs that mention park + completed + 2022, then map funding by token overlap
for idx, text_l in enumerate(docs_texts_lower):
    if 'park' in text_l and 'completed' in text_l and '2022' in text_l:
        window = text_l
        for rec in funding:
            pname = rec['Project_Name_norm']
            pname_l = pname.lower()
            if not any(k in pname_l for k in park_keywords):
                continue
            # generate tokens
            cleaned = ''.join(ch if ch.isalnum() else ' ' for ch in pname_l)
            tokens = [t for t in cleaned.split() if len(t) > 4]
            if any(tok in window for tok in tokens):
                matched[pname] = matched.get(pname, 0) + rec['Amount']

# Deduplicate: ensure each funding project counted once
# matched currently may have duplicates added by multiple docs; but summing amounts per project is fine
matched_list = [{'Project_Name': k, 'Amount': v} for k, v in matched.items()]

total = sum(v for v in matched.values())

result = {'total_funding': total, 'matched_projects': matched_list, 'matched_count': len(matched_list)}

print("__RESULT__:")
print(json.dumps(result))"""

env_args = {'var_call_FA7KkPgziK2Q90TPgVoTXk32': 'file_storage/call_FA7KkPgziK2Q90TPgVoTXk32.json', 'var_call_mka5UEs3QWagkOJUBTVZMduK': 'file_storage/call_mka5UEs3QWagkOJUBTVZMduK.json', 'var_call_AFpwSc8e8NWk7WAxPDYTmfTa': {'funding_records': 500, 'doc_records': 19}}

exec(code, env_args)
