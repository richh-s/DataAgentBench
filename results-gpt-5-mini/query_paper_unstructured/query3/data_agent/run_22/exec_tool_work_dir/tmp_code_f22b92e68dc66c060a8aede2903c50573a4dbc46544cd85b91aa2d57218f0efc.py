code = """import json
import re

path_papers = var_call_ASIUZwxdVKhBb0x0D1r1ArEE
with open(path_papers, 'r', encoding='utf-8') as f:
    papers = json.load(f)

result = []
for doc in papers:
    filename = doc.get('filename','')
    title = filename[:-4] if filename.lower().endswith('.txt') else filename
    text = doc.get('text','') or ''
    m = re.search(r"\b(19|20)\d{2}\b", text)
    year = int(m.group(0)) if m else None
    is_empirical = 'empirical' in text.lower()
    if is_empirical:
        result.append({'title': title, 'year': year})

print("__RESULT__:")
print(json.dumps(result))"""

env_args = {'var_call_ASIUZwxdVKhBb0x0D1r1ArEE': 'file_storage/call_ASIUZwxdVKhBb0x0D1r1ArEE.json', 'var_call_ks33GFIQt1Ru5uWUyaBQNf6y': 'file_storage/call_ks33GFIQt1Ru5uWUyaBQNf6y.json', 'var_call_Evthd1DKziWHsqlgXwjnonrR': []}

exec(code, env_args)
