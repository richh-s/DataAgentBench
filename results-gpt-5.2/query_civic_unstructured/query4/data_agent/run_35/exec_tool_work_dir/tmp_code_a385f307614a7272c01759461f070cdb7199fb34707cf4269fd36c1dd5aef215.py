code = """import json, re

civic_src = var_call_2t22R3UaX4Znxt0xz8fGYIAP
if isinstance(civic_src, str):
    with open(civic_src, 'r', encoding='utf-8') as f:
        civic_docs = json.load(f)
else:
    civic_docs = civic_src

spring_any = []
for doc in civic_docs:
    text = doc.get('text','')
    if re.search(r"Spring\s*,?\s*2022", text, flags=re.IGNORECASE):
        spring_any.append(doc['filename'])

print('__RESULT__:')
print(json.dumps({"docs_with_spring_2022": spring_any[:50], "count": len(spring_any)}))"""

env_args = {'var_call_KGer4GH8D7ZnCWgfNaReubzl': ['Funding'], 'var_call_2t22R3UaX4Znxt0xz8fGYIAP': 'file_storage/call_2t22R3UaX4Znxt0xz8fGYIAP.json', 'var_call_CAVbt0EfwT8uPhTQKJt2uLzX': 'file_storage/call_CAVbt0EfwT8uPhTQKJt2uLzX.json', 'var_call_gqCYwIbXiadWD03lxJ9pO1c8': {'projects_started_spring_2022_count': 0, 'projects_started_spring_2022_total_funding': 0, 'projects': []}}

exec(code, env_args)
