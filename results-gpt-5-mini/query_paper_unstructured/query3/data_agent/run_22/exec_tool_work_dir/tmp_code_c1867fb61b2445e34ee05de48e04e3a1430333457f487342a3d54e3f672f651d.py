code = """import json, re
path_papers = var_call_ASIUZwxdVKhBb0x0D1r1ArEE
with open(path_papers, 'r', encoding='utf-8') as f:
    papers = json.load(f)

out = []
for doc in papers:
    filename = doc.get('filename','')
    title = filename[:-4] if filename.lower().endswith('.txt') else filename
    text = doc.get('text','') or ''
    m = re.search(r"\b(19|20)\d{2}\b", text)
    year = int(m.group(0)) if m else None
    is_empirical = 'empirical' in text.lower()
    out.append({'title': title, 'year': year, 'is_empirical': is_empirical})

# filter year > 2016
filtered = [r for r in out if r['year'] and r['year']>2016]

print("__RESULT__:")
print(json.dumps({'count_after_2016': len(filtered), 'papers_after_2016_sample': filtered[:200]}))"""

env_args = {'var_call_ASIUZwxdVKhBb0x0D1r1ArEE': 'file_storage/call_ASIUZwxdVKhBb0x0D1r1ArEE.json', 'var_call_ks33GFIQt1Ru5uWUyaBQNf6y': 'file_storage/call_ks33GFIQt1Ru5uWUyaBQNf6y.json', 'var_call_Evthd1DKziWHsqlgXwjnonrR': [], 'var_call_lkVfi8bjpSmeLdoKt37z1mP5': [{'title': 'A Trip to the Moon: Personalized Animated Movies for Self-reflection', 'year': None}, {'title': 'A Wee Bit More Interaction: Designing and Evaluating an Overactive Bladder App', 'year': None}]}

exec(code, env_args)
