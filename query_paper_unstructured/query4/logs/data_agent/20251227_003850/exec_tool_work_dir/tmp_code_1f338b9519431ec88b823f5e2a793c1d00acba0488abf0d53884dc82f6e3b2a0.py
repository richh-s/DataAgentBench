code = """import json

path = var_call_30lJdgJVaQJdZAMe6h3V85Ch
with open(path, 'r', encoding='utf-8') as f:
    docs = json.load(f)

titles2016 = []
for doc in docs:
    text = doc.get('text', '')
    if not text:
        continue
    if 'physical activity' not in text.lower():
        continue
    header = text[:2000]
    header_lower = header.lower()
    if ('2016' in header) or ("'16" in header) or ("’16" in header) or ('copyright 2016' in header_lower):
        fn = doc.get('filename', '')
        title = fn[:-4] if fn.lower().endswith('.txt') else fn
        if title and title not in titles2016:
            titles2016.append(title)

out = json.dumps(titles2016)
print("__RESULT__:")
print(out)"""

env_args = {'var_call_30lJdgJVaQJdZAMe6h3V85Ch': 'file_storage/call_30lJdgJVaQJdZAMe6h3V85Ch.json'}

exec(code, env_args)
