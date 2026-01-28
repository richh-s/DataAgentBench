code = """import json

# Load file paths from storage variables
funding_path = var_call_VzgihgZ7OwHfelcmF5z1sI2X
docs_path = var_call_zyKqzSQAopIHC3ukf8gNzESM

with open(funding_path, 'r', encoding='utf-8') as f:
    funding = json.load(f)
with open(docs_path, 'r', encoding='utf-8') as f:
    docs = json.load(f)

# Combine all text and find sections that mention 'capital improvement projects (design)'
combined_design_text = ''
for doc in docs:
    text = doc.get('text', '')
    lower = text.lower()
    marker = 'capital improvement projects (design)'
    if marker in lower:
        # take from marker to a reasonable length (e.g., 5000 chars) to include project list
        start = lower.find(marker) + len(marker)
        snippet = lower[start:start+20000]
        combined_design_text += '\n' + snippet

# If no explicit marker, also try to include any lines under 'capital improvement projects' that contain 'design'
if not combined_design_text:
    for doc in docs:
        lower = doc.get('text','').lower()
        if 'capital improvement projects' in lower and 'design' in lower:
            combined_design_text += '\n' + lower

# Prepare project names from funding results (these results already filtered to Amount > 50000)
proj_names = [r.get('Project_Name','') for r in funding]

matched = set()
for name in proj_names:
    name_low = name.lower()
    name_strip = name_low
    # remove parenthetical suffix
    if '(' in name_low and name_low.endswith(')'):
        name_strip = name_low[:name_low.rfind('(')].strip()
    # direct substring check
    if name_low in combined_design_text or name_strip in combined_design_text:
        matched.add(name)
    else:
        # check if all significant words (length>2) appear in order
        import re
        words = [w for w in re.findall(r"[a-z0-9]+", name_strip) if len(w)>2]
        pos = 0
        ok = True
        for w in words:
            idx = combined_design_text.find(w, pos)
            if idx == -1:
                ok = False
                break
            pos = idx + len(w)
        if ok and words:
            matched.add(name)

matched_list = sorted(matched)
result = {'count': len(matched_list), 'projects': matched_list}

print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_call_w6mzZJWh1Qf1WequniXaReqc': ['civic_docs'], 'var_call_8FNlL82nAuBCB7zgbjsxnppT': ['Funding'], 'var_call_VzgihgZ7OwHfelcmF5z1sI2X': 'file_storage/call_VzgihgZ7OwHfelcmF5z1sI2X.json', 'var_call_zyKqzSQAopIHC3ukf8gNzESM': 'file_storage/call_zyKqzSQAopIHC3ukf8gNzESM.json'}

exec(code, env_args)
