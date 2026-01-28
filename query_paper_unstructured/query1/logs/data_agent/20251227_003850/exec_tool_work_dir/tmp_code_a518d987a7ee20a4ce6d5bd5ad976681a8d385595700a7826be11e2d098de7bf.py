code = """import json, re

with open(var_call_KOAb1xgHNfb3JOSVlpr2sxoD, 'r') as f:
    docs = json.load(f)
with open(var_call_XFFPJlFw3TBBuuRwIfyp1MXj, 'r') as f:
    cites = json.load(f)

food_patterns = [r"\bfood\b", r"\bdiet\b", r"\bnutrition\b", r"\beating\b", r"\bmeal\b", r"\bcalorie\b"]
compiled_patterns = [re.compile(p, re.IGNORECASE) for p in food_patterns]

food_titles = set()
for doc in docs:
    filename = doc.get('filename')
    text = doc.get('text') or ''
    if not filename:
        continue
    title = filename.replace('.txt', '')
    if any(p.search(text) for p in compiled_patterns):
        food_titles.add(title)

citation_titles = set(row.get('title') for row in cites if row.get('title'))
intersect = sorted(list(food_titles.intersection(citation_titles)))

result = {
    "food_titles_count": len(food_titles),
    "food_titles_sample": sorted(list(food_titles))[:20],
    "citation_titles_count": len(citation_titles),
    "intersection_count": len(intersect),
    "intersection_sample": intersect[:20]
}

import json as _json
print("__RESULT__:")
print(_json.dumps(result))"""

env_args = {'var_call_KOAb1xgHNfb3JOSVlpr2sxoD': 'file_storage/call_KOAb1xgHNfb3JOSVlpr2sxoD.json', 'var_call_XFFPJlFw3TBBuuRwIfyp1MXj': 'file_storage/call_XFFPJlFw3TBBuuRwIfyp1MXj.json', 'var_call_7x4P0KBQEa1dlWFV6BOGAVaZ': {'total_citations_food_domain': 0}}

exec(code, env_args)
