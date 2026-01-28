code = """import json
import re

# Load data
with open(var_call_imMVVH4ydlnQiLitue5achAa, 'r') as f:
    funding = json.load(f)
with open(var_call_LsS5gYiobVLdbl1d1c1xS3Ye, 'r') as f:
    civic_docs = json.load(f)

# Normalize amounts and names
for r in funding:
    try:
        r['Amount'] = int(r.get('Amount', 0))
    except Exception:
        try:
            r['Amount'] = int(float(r.get('Amount', 0)))
        except Exception:
            r['Amount'] = 0
    pname = r.get('Project_Name', '')
    r['Project_Name_norm'] = pname.split('(')[0].strip().lower()

# keywords for park-related
park_keywords = ['park', 'playground', 'walkway', 'shade', 'bench', 'benches', 'bluffs', 'point dume', 'legacy park']

# combine civic text
texts = [doc.get('text','').lower() for doc in civic_docs]
full_text = '\n'.join(texts)

completion_keywords = ['construction was completed', 'construction was completed,', 'construction was completed.', 'completed', 'notice of completion', 'completion filed', 'filed january 2023', 'filed january 2023', 'filed january']

matched = []

for r in funding:
    name = r.get('Project_Name','').lower()
    name_norm = r.get('Project_Name_norm','')
    # determine if park-related by keyword in name
    is_park = any(kw in name for kw in park_keywords) or any(kw in name_norm for kw in park_keywords)
    if not is_park:
        continue
    found = False
    # search occurrences of normalized name or name in full_text
    search_terms = [name_norm] if name_norm else []
    if name and name not in search_terms:
        search_terms.append(name)
    for term in search_terms:
        if not term:
            continue
        idx = full_text.find(term)
        while idx != -1:
            start = max(0, idx-200)
            end = min(len(full_text), idx+500)
            window = full_text[start:end]
            if '2022' in window and any(k in window for k in completion_keywords):
                found = True
                break
            idx = full_text.find(term, idx+1)
        if found:
            break
    if found:
        matched.append({'Project_Name': r.get('Project_Name',''), 'Amount': r['Amount']})

total = sum(m['Amount'] for m in matched)
result = {'total_funding': total, 'projects': matched}

print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_call_NnUo40dHHTLYgcQTqlojtfqg': ['civic_docs'], 'var_call_UjP3tQXtgm9tRd9gDjbiDPvo': ['Funding'], 'var_call_LsS5gYiobVLdbl1d1c1xS3Ye': 'file_storage/call_LsS5gYiobVLdbl1d1c1xS3Ye.json', 'var_call_imMVVH4ydlnQiLitue5achAa': 'file_storage/call_imMVVH4ydlnQiLitue5achAa.json', 'var_call_jTbIoLYTmACc319xO44IBupV': {'funding_count': 500}}

exec(code, env_args)
