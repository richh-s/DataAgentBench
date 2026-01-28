code = """import json, os, re
from pathlib import Path

# Load full Mongo result
mongo_path = var_call_XqM4EBEct83OU2WR077vMLxZ
with open(mongo_path, 'r') as f:
    mongo_records = json.load(f)

# Identify food-domain papers via heuristic: look for 'food', 'diet', 'calorie' etc. in context
food_titles = set()
for doc in mongo_records:
    text = doc.get('text', '').lower()
    if any(kw in text for kw in [' food ', ' foods ', ' diet ', ' dietary ', ' calorie', 'nutrition', 'nutritional']):
        filename = doc.get('filename', '')
        if filename.lower().endswith('.txt'):
            title = filename[:-4]
        else:
            title = filename
        if title:
            food_titles.add(title)

# Load full citations result
cites_path = var_call_9yuHbjx0se9TGksu2Pv1OztN
with open(cites_path, 'r') as f:
    cite_records = json.load(f)

# Sum citation counts for titles in food_titles
total_citations = 0
for rec in cite_records:
    title = rec.get('title', '')
    if title in food_titles:
        try:
            c = int(rec.get('citation_count', 0))
        except Exception:
            c = 0
        total_citations += c

result = json.dumps({"total_food_domain_citations": total_citations, "food_paper_count": len(food_titles)})
print("__RESULT__:")
print(result)"""

env_args = {'var_call_XqM4EBEct83OU2WR077vMLxZ': 'file_storage/call_XqM4EBEct83OU2WR077vMLxZ.json', 'var_call_9yuHbjx0se9TGksu2Pv1OztN': 'file_storage/call_9yuHbjx0se9TGksu2Pv1OztN.json'}

exec(code, env_args)
