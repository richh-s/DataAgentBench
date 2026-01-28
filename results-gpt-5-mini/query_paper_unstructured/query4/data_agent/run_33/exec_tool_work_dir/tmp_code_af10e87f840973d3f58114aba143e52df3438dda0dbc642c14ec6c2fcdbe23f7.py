code = """import json, re
with open(var_call_MofUK2m03WbBxbNaWInNuQUc, 'r', encoding='utf-8') as f:
    docs = json.load(f)

candidates = []
for d in docs:
    filename = d.get('filename','')
    text = (d.get('text') or '')
    title = filename.rsplit('.txt',1)[0]
    lower = text.lower()
    if 'physical' in lower and 'activity' in lower:
        years = re.findall(r"\b(19|20)\d{2}\b", text)
        # re.findall returns just the leading part due to group; fix
        years = re.findall(r"\b(19|20)\d{2}\b", text)
        years_full = re.findall(r"\b(?:19|20)\d{2}\b", text)
        # two-digit year patterns like '16 or ’16
        twod = re.findall(r"\b'?(?:’)?(\d{2})\b", text)
        # collect context
        idx = lower.find('physical')
        snippet = text[max(0, idx-50):idx+200]
        candidates.append({'title': title, 'filename': filename, 'years_found': years_full, 'two_digit_years': twod, 'snippet': snippet[:500]})

# Also search filenames containing physical or activity
for d in docs:
    filename = d.get('filename','')
    text = (d.get('text') or '')
    title = filename.rsplit('.txt',1)[0]
    if 'physical' in filename.lower() or 'activity' in filename.lower():
        if not any(c['title']==title for c in candidates):
            years_full = re.findall(r"\b(?:19|20)\d{2}\b", text)
            twod = re.findall(r"\b'?(?:’)?(\d{2})\b", text)
            candidates.append({'title': title, 'filename': filename, 'years_found': years_full, 'two_digit_years': twod, 'snippet': ''})

import json
print('__RESULT__:')
print(json.dumps(candidates))"""

env_args = {'var_call_MofUK2m03WbBxbNaWInNuQUc': 'file_storage/call_MofUK2m03WbBxbNaWInNuQUc.json', 'var_call_CVUkhUcAwiQzAT1X9ezOtb8s': []}

exec(code, env_args)
