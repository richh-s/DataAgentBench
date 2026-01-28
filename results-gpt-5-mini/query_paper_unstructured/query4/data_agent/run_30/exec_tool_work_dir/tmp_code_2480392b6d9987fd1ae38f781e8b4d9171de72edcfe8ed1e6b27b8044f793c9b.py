code = """import json, re
path = var_call_R6gwTreaDcfvqovoD3OXntlB
with open(path, 'r', encoding='utf-8') as f:
    records = json.load(f)

out = []
for rec in records:
    filename = rec.get('filename','')
    title = filename[:-4] if filename.lower().endswith('.txt') else filename
    text = rec.get('text','')
    years = sorted(list({int(y) for y in re.findall(r'\b(20\d{2})\b', text)}))
    has_pa = bool(re.search(r'physical activity', text, flags=re.I))
    out.append({"title": title, "years": years, "has_physical_activity": has_pa})

# limit output to entries where has_pa is True
filtered = [o for o in out if o['has_physical_activity']]
# include first 100 items to keep small
result = filtered[:100]
print('__RESULT__:')
import json as _json
print(_json.dumps(result))"""

env_args = {'var_call_R6gwTreaDcfvqovoD3OXntlB': 'file_storage/call_R6gwTreaDcfvqovoD3OXntlB.json', 'var_call_SoNIw3qUMrpUQj9KJImwD4pv': []}

exec(code, env_args)
