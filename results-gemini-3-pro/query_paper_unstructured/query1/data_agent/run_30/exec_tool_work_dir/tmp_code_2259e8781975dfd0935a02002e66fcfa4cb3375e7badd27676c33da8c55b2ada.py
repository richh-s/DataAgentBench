code = """import json

with open(locals()['var_function-call-8395827407536305276'], 'r') as f:
    papers = json.load(f)

food_papers = []

for p in papers:
    text = p.get('text', '').lower()
    title = p.get('filename', '').replace('.txt', '')
    
    # Title check
    if 'food' in title.lower():
        food_papers.append(title)
        continue
    
    # Keyword check
    # Check for 'keywords' string and then 'food' nearby
    idx = text.find('keywords')
    if idx != -1:
        # Check next 500 chars
        snippet = text[idx:idx+500]
        if 'food' in snippet:
            food_papers.append(title)

print('__RESULT__:')
print(json.dumps(food_papers))"""

env_args = {'var_function-call-3709648201764099351': 'file_storage/function-call-3709648201764099351.json', 'var_function-call-12009379333761153785': 'file_storage/function-call-12009379333761153785.json', 'var_function-call-8395827407536305276': 'file_storage/function-call-8395827407536305276.json'}

exec(code, env_args)
