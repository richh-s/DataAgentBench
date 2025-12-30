code = """import json, re, os

# Load full Mongo result
path_mongo = var_call_YLMxdSjEmcP0ytsY1AENDsnI
with open(path_mongo, 'r') as f:
    mongo_records = json.load(f)

# Load full citations result
path_cit = var_call_7dxv9eUsWZ2yEq4kc9hR5tx5
with open(path_cit, 'r') as f:
    cit_records = json.load(f)

# Build set of titles for food-domain papers by simple heuristic on full text
food_titles = set()
food_keywords = [' food ', ' foods ', ' diet ', ' dietary ', ' eating ', ' nutrition ', 'meal', 'meals']

for doc in mongo_records:
    text = doc.get('text', '').lower()
    if any(kw.strip() in text for kw in food_keywords):
        filename = doc.get('filename', '')
        if filename.lower().endswith('.txt'):
            title = filename[:-4]
        else:
            title = filename
        food_titles.add(title)

# Sum citations for those titles
total_citations_food = 0
for rec in cit_records:
    title = rec.get('title', '')
    # Titles in citations should match exactly title
    if title in food_titles:
        try:
            total_citations_food += int(rec.get('total_citations', 0))
        except ValueError:
            pass

result = total_citations_food

print("__RESULT__:")
print(json.dumps(result))"""

env_args = {'var_call_YLMxdSjEmcP0ytsY1AENDsnI': 'file_storage/call_YLMxdSjEmcP0ytsY1AENDsnI.json', 'var_call_7dxv9eUsWZ2yEq4kc9hR5tx5': 'file_storage/call_7dxv9eUsWZ2yEq4kc9hR5tx5.json'}

exec(code, env_args)
