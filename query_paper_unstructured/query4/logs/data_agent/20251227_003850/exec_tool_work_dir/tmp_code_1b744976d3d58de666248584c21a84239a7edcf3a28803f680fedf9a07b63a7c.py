code = """import json

path = var_call_30lJdgJVaQJdZAMe6h3V85Ch
with open(path, 'r', encoding='utf-8') as f:
    docs = json.load(f)

n = len(docs)
samples = []
for doc in docs[:5]:
    samples.append({
        'filename': doc.get('filename',''),
        'header': (doc.get('text','')[:500] or '')
    })

print("__RESULT__:")
print(json.dumps({'count': n, 'samples': samples}))"""

env_args = {'var_call_30lJdgJVaQJdZAMe6h3V85Ch': 'file_storage/call_30lJdgJVaQJdZAMe6h3V85Ch.json', 'var_call_kxNffj8ucVhN9ULkiBzUJqBa': [], 'var_call_UtYkYcdmqwI0XOihIyfK1u9M': [], 'var_call_Nr0aEY5y8YFEXBgXZ4cypXlu': 'file_storage/call_Nr0aEY5y8YFEXBgXZ4cypXlu.json'}

exec(code, env_args)
