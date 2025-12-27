code = """import json

path = var_call_30lJdgJVaQJdZAMe6h3V85Ch
with open(path, 'r', encoding='utf-8') as f:
    docs = json.load(f)

substrs = [
    '2016',
    "chi '16",
    "ubicomp '16",
    "cscw '16",
    "dis '16",
    'pervasivehealth 2016',
    'www 2016',
    "iui '16",
    'ozchi 2016',
    "tei '16",
    'ah 2016',
    'copyright 2016'
]

def is_2016(text):
    if not text:
        return False
    header = text[:8000].lower()
    for s in substrs:
        if s in header:
            return True
    return False

titles2016 = []
for doc in docs:
    text = doc.get('text', '')
    if not text:
        continue
    if 'physical activity' not in text.lower():
        continue
    if is_2016(text):
        fn = doc.get('filename', '')
        title = fn[:-4] if fn.lower().endswith('.txt') else fn
        if title and title not in titles2016:
            titles2016.append(title)

print("__RESULT__:")
print(json.dumps(titles2016))"""

env_args = {'var_call_30lJdgJVaQJdZAMe6h3V85Ch': 'file_storage/call_30lJdgJVaQJdZAMe6h3V85Ch.json', 'var_call_kxNffj8ucVhN9ULkiBzUJqBa': []}

exec(code, env_args)
