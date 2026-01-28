code = """import json
import re

with open('var_function-call-1279721563085973081.json', 'r') as f:
    papers = json.load(f)

print("__RESULT__:")
results = []
for p in papers:
    title = p['filename'].replace('.txt', '')
    text = p.get('text', '')
    has_food = 'food' in text.lower()
    snippet = ""
    if has_food:
        idx = text.lower().find('food')
        start = max(0, idx - 50)
        end = min(len(text), idx + 50)
        snippet = text[start:end]
    results.append({"title": title, "has_food": has_food, "snippet": snippet})

print(json.dumps(results))"""

env_args = {'var_function-call-4428152146119552339': 'file_storage/function-call-4428152146119552339.json', 'var_function-call-1279721563085973081': 'file_storage/function-call-1279721563085973081.json', 'var_function-call-10463220630905116945': 'file_storage/function-call-10463220630905116945.json', 'var_function-call-6853165914555926720': {'food_papers': [], 'total_citations': 0}}

exec(code, env_args)
