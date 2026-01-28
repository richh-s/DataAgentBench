code = """import json
p = var_call_lGT6WoCuyWvDkZO6yDO1wveb
with open(p, 'r', encoding='utf-8') as f:
    docs = json.load(f)

keywords = ['park','playground','walkway','shade','bluffs','point dume','trancas']
found = []
for doc in docs:
    text = doc.get('text','')
    paragraphs = text.split('\n\n')
    for para in paragraphs:
        low = para.lower()
        if 'completed' in low and '2022' in low:
            if any(k in low for k in keywords):
                first_line = para.strip().split('\n')[0].strip()
                if first_line:
                    # clean common trailing word
                    if first_line.lower().endswith('project'):
                        first_line = first_line[: -len('project')].strip()
                    found.append(first_line)

# dedupe preserving order
seen = set()
unique = []
for n in found:
    if n not in seen:
        seen.add(n)
        unique.append(n)

print("__RESULT__:")
print(json.dumps(unique))"""

env_args = {'var_call_lGT6WoCuyWvDkZO6yDO1wveb': 'file_storage/call_lGT6WoCuyWvDkZO6yDO1wveb.json'}

exec(code, env_args)
