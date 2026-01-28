code = """import json, re
path = var_call_jomEIuqLlbvcof8x2J99bnnA
with open(path, 'r', encoding='utf-8') as f:
    records = json.load(f)

candidates = []
for rec in records:
    text = rec.get('text', '')
    filename = rec.get('filename', '')
    title = filename[:-4] if filename.lower().endswith('.txt') else filename
    if 'physical activity' in text.lower() and '2016' in text:
        candidates.append(title)
# Deduplicate
candidates = sorted(list(dict.fromkeys(candidates)))

print('__RESULT__:')
print(json.dumps(candidates))"""

env_args = {'var_call_jomEIuqLlbvcof8x2J99bnnA': 'file_storage/call_jomEIuqLlbvcof8x2J99bnnA.json', 'var_call_L1VArUemkcH9MS1CPHEgycmS': []}

exec(code, env_args)
