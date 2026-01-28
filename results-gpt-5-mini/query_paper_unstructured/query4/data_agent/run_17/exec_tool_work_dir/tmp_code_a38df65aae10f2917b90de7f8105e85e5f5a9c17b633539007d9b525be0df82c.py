code = """import json, re
path = var_call_557VZrPhqUrgO6CAofXjAEsq
with open(path, 'r', encoding='utf-8') as f:
    docs = json.load(f)

out = {}
for doc in docs:
    filename = doc.get('filename','')
    title = filename[:-4] if filename.lower().endswith('.txt') else filename
    text = doc.get('text','') or ''
    if not re.search(r'physical\W*activity', text, re.I) and not re.search(r'\bexercise\b', text, re.I):
        continue
    years = sorted(list({int(y.group(0)) for y in re.finditer(r'\b(19|20)\d{2}\b', text)}))
    # collect contexts for each year occurrence
    contexts = {}
    for m in re.finditer(r'\b(19|20)\d{2}\b', text):
        y = m.group(0)
        start = max(0, m.start()-40)
        end = m.end()+40
        contexts.setdefault(y, []).append(text[start:end])
    out[title] = {'years': years, 'contexts': contexts}

print('__RESULT__:')
print(json.dumps(out))"""

env_args = {'var_call_VNEvq032PXm1hSsPWSIEbAc4': 'file_storage/call_VNEvq032PXm1hSsPWSIEbAc4.json', 'var_call_VAXyipWQI6VX8cowdguGGkry': [], 'var_call_557VZrPhqUrgO6CAofXjAEsq': 'file_storage/call_557VZrPhqUrgO6CAofXjAEsq.json', 'var_call_cOaf4DkuMvSAPShkJlA1MB3v': [], 'var_call_TvxTlwyBcM7agVRIdBv7mCMq': []}

exec(code, env_args)
