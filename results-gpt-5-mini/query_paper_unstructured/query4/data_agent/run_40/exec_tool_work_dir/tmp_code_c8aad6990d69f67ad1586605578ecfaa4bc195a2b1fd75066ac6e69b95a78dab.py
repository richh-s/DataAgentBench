code = """import json, re
path = var_call_uDJDEG1WUDDBdEQCbx5fId9d
with open(path, 'r', encoding='utf-8') as f:
    docs = json.load(f)

results = []
for d in docs:
    text = d.get('text','')
    filename = d.get('filename','')
    title = filename[:-4] if filename.lower().endswith('.txt') else filename
    # Find year in the first 1000 chars
    header = text[:2000]
    years = re.findall(r'\b(20\d{2})\b', header)
    year = None
    if years:
        # choose the first occurrence
        year = int(years[0])
    else:
        # search whole text
        years_all = re.findall(r'\b(20\d{2})\b', text)
        if years_all:
            year = int(years_all[0])
    # check domain mention
    if year == 2016 and re.search(r'physical activity', text, re.IGNORECASE):
        results.append({'title': title, 'year': year})

# deduplicate
unique = {r['title']: r for r in results}
out = list(unique.values())
print('__RESULT__:')
print(json.dumps(out))"""

env_args = {'var_call_dZcb7oiZgAHY4QVK8xj1Nin6': 'file_storage/call_dZcb7oiZgAHY4QVK8xj1Nin6.json', 'var_call_jX3aMtn3six7yGSA1qsFYicb': [], 'var_call_ArPkaigkLlJbnG0DtleLJDpz': ['paper_docs'], 'var_call_uDJDEG1WUDDBdEQCbx5fId9d': 'file_storage/call_uDJDEG1WUDDBdEQCbx5fId9d.json'}

exec(code, env_args)
