code = """import json

funding_path = var_call_VzgihgZ7OwHfelcmF5z1sI2X
docs_path = var_call_zyKqzSQAopIHC3ukf8gNzESM

with open(funding_path, 'r', encoding='utf-8') as f:
    funding = json.load(f)
with open(docs_path, 'r', encoding='utf-8') as f:
    docs = json.load(f)

# Collect texts that are likely to contain design-phase capital projects
design_texts = []
for doc in docs:
    text = doc.get('text','').lower()
    if 'design' in text and 'capital improvement projects' in text:
        design_texts.append(text)

# If none found, fallback: any doc with phrase 'capital improvement projects' and 'design' separately
if not design_texts:
    for doc in docs:
        text = doc.get('text','').lower()
        if 'capital improvement projects' in text and 'design' in text:
            design_texts.append(text)

all_design_text = '\n'.join(design_texts)

# Prepare funding project names (results from earlier query already filtered to Amount > 50000)
proj_names = [r.get('Project_Name','') for r in funding]

matched = set()
for name in proj_names:
    nl = name.lower()
    # remove parenthetical suffix if present
    if '(' in nl and nl.strip().endswith(')'):
        base = nl[:nl.rfind('(')].strip()
    else:
        base = nl
    if nl in all_design_text or base in all_design_text:
        matched.add(name)
    else:
        # also check if at least three-word sequence appears
        words = [w for w in base.split() if len(w)>2]
        if len(words) >= 3:
            pos = 0
            ok = True
            for w in words:
                idx = all_design_text.find(w, pos)
                if idx == -1:
                    ok = False
                    break
                pos = idx + len(w)
            if ok:
                matched.add(name)

matched_list = sorted(matched)
result = {'count': len(matched_list), 'projects': matched_list}

print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_call_w6mzZJWh1Qf1WequniXaReqc': ['civic_docs'], 'var_call_8FNlL82nAuBCB7zgbjsxnppT': ['Funding'], 'var_call_VzgihgZ7OwHfelcmF5z1sI2X': 'file_storage/call_VzgihgZ7OwHfelcmF5z1sI2X.json', 'var_call_zyKqzSQAopIHC3ukf8gNzESM': 'file_storage/call_zyKqzSQAopIHC3ukf8gNzESM.json'}

exec(code, env_args)
