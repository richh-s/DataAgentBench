code = """import json, re
with open(var_call_MofUK2m03WbBxbNaWInNuQUc, 'r', encoding='utf-8') as f:
    docs = json.load(f)

matches = []
for d in docs:
    filename = d.get('filename','')
    title = filename.rsplit('.txt',1)[0]
    text = (d.get('text') or '')
    lower = text.lower()
    if 'physical' in lower and 'activity' in lower:
        # search for 2016 in the first 400 chars (likely header) or anywhere
        found2016 = False
        if re.search(r"\b2016\b", text):
            found2016 = True
        # also check for patterns like "CHI '16" or "'16" near venue lines
        if not found2016:
            if re.search(r"'16\b|’16\b|\b2016\b", text):
                found2016 = True
        if found2016:
            matches.append({'title': title})

print('__RESULT__:')
print(json.dumps(matches))"""

env_args = {'var_call_MofUK2m03WbBxbNaWInNuQUc': 'file_storage/call_MofUK2m03WbBxbNaWInNuQUc.json', 'var_call_CVUkhUcAwiQzAT1X9ezOtb8s': [], 'var_call_8e2mPHQzlupulgcMsl5j9Fx8': 'file_storage/call_8e2mPHQzlupulgcMsl5j9Fx8.json'}

exec(code, env_args)
