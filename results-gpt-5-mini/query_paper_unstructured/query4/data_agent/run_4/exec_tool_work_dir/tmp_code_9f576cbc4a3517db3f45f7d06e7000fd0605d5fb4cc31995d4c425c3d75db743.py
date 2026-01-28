code = """import json, re
p = var_call_40G8suqyORvGvH2VqbbBEhkO
with open(p, 'r', encoding='utf-8') as f:
    data = json.load(f)

results = []
for rec in data:
    filename = rec.get('filename','')
    text = rec.get('text','')
    title = filename[:-4] if filename.lower().endswith('.txt') else filename
    # find first year in entire text
    m = re.search(r"\b(19[9][0-9]|20(0[0-9]|1[0-9]|2[0-5]))\b", text)
    year = int(m.group(0)) if m else None
    domain_match = 'physical activity' in text.lower()
    if domain_match:
        results.append({'title': title, 'year': year})

res2016 = [r for r in results if r['year']==2016]
print('__RESULT__:')
print(json.dumps(res2016))"""

env_args = {'var_call_UeAwGvyL4BRgCq5TsBDxPehn': 'file_storage/call_UeAwGvyL4BRgCq5TsBDxPehn.json', 'var_call_dtnwJdFJIovt8fdBMoCOC9Z5': [], 'var_call_40G8suqyORvGvH2VqbbBEhkO': 'file_storage/call_40G8suqyORvGvH2VqbbBEhkO.json', 'var_call_jokn9ejj3SySQh0YVLoqQrID': []}

exec(code, env_args)
