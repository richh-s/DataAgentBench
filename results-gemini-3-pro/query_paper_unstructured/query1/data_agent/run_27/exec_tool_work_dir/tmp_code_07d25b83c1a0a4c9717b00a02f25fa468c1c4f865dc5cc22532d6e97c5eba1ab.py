code = """import json

with open('var_function-call-16923378931810091090.json', 'r') as f:
    papers = json.load(f)

results = []
for p in papers:
    title = p['filename'].replace('.txt', '')
    text = p.get('text', '').lower()
    has_food = 'food' in text
    has_nutrition = 'nutrition' in text
    has_eating = 'eating' in text
    # Extract first 200 chars to see if there's a domain field
    preview = text[:200].replace('\n', ' ')
    results.append({
        "title": title, 
        "has_food": has_food, 
        "has_nutrition": has_nutrition, 
        "has_eating": has_eating,
        "preview": preview
    })

print("__RESULT__:")
print(json.dumps(results))"""

env_args = {'var_function-call-4428152146119552339': 'file_storage/function-call-4428152146119552339.json', 'var_function-call-1279721563085973081': 'file_storage/function-call-1279721563085973081.json', 'var_function-call-10463220630905116945': 'file_storage/function-call-10463220630905116945.json', 'var_function-call-6853165914555926720': {'food_papers': [], 'total_citations': 0}, 'var_function-call-4486819615144744261': 'file_storage/function-call-4486819615144744261.json', 'var_function-call-16923378931810091090': 'file_storage/function-call-16923378931810091090.json', 'var_function-call-10009206756418749160': 'file_storage/function-call-10009206756418749160.json', 'var_function-call-8154133366834530525': {'food_papers': [], 'total_citations': 0}}

exec(code, env_args)
