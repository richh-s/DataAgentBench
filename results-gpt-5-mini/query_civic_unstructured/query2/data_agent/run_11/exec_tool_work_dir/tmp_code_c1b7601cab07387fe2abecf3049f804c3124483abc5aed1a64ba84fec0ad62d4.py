code = """import json

with open(var_call_FA7KkPgziK2Q90TPgVoTXk32, 'r', encoding='utf-8') as f:
    funding = json.load(f)
with open(var_call_mka5UEs3QWagkOJUBTVZMduK, 'r', encoding='utf-8') as f:
    docs = json.load(f)

# Normalize amounts
for r in funding:
    try:
        r['Amount'] = int(r.get('Amount') if r.get('Amount') is not None else 0)
    except Exception:
        amt = str(r.get('Amount','0')).replace(',','').strip()
        try:
            r['Amount'] = int(amt)
        except Exception:
            r['Amount'] = 0
    r['Project_Name_norm'] = str(r.get('Project_Name','')).strip()

park_keywords = ['park', 'playground', 'walkway', 'bench', 'shade structure', 'paver', 'benches']

# Build a concatenated lowercased text of all docs for simple searching
all_docs_text = "\n".join([d.get('text','') for d in docs]).lower()

matched = {}
for rec in funding:
    pname = rec['Project_Name_norm']
    pname_l = pname.lower()
    if not any(kw in pname_l for kw in park_keywords):
        continue
    # check if pname appears in docs and docs mention completed and 2022
    if pname_l in all_docs_text and 'completed' in all_docs_text and '2022' in all_docs_text:
        # More strict: ensure that both words appear (they do globally)
        matched[pname] = matched.get(pname, 0) + rec['Amount']

# Also, find any lines in docs that mention 'park' and 'completed' and '2022', and then try to match funding records by substring overlap
lines = all_docs_text.splitlines()
for i,line in enumerate(lines):
    if 'park' in line and 'completed' in line and '2022' in line:
        # check nearby lines
        window = '\n'.join(lines[max(0,i-2):i+3])
        for rec in funding:
            pname = rec['Project_Name_norm']
            pname_l = pname.lower()
            if not any(kw in pname_l for kw in park_keywords):
                continue
            # if any long token from project name in window
            tokens = [t for t in pname_l.replace('-', ' ').split() if len(t)>4]
            if any(tok in window for tok in tokens):
                matched[pname] = matched.get(pname, 0) + rec['Amount']

# Prepare result
matched_list = [{'Project_Name': k, 'Amount': v} for k,v in matched.items()]
total = sum(v for v in matched.values())

result = {'total_funding': total, 'matched_projects': matched_list, 'matched_count': len(matched_list)}

print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_call_FA7KkPgziK2Q90TPgVoTXk32': 'file_storage/call_FA7KkPgziK2Q90TPgVoTXk32.json', 'var_call_mka5UEs3QWagkOJUBTVZMduK': 'file_storage/call_mka5UEs3QWagkOJUBTVZMduK.json'}

exec(code, env_args)
