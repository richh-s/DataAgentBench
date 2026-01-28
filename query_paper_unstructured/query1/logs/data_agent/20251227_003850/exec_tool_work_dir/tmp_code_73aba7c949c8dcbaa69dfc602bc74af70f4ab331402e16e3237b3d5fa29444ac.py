code = """import json, re

# Load full results from stored file paths
with open(var_call_KOAb1xgHNfb3JOSVlpr2sxoD, 'r') as f:
    docs = json.load(f)
with open(var_call_XFFPJlFw3TBBuuRwIfyp1MXj, 'r') as f:
    cites = json.load(f)

# Prepare regex for detecting 'food' domain mentions
food_patterns = [r"\bfood\b", r"\bdiet\b", r"\bnutrition\b", r"\beating\b", r"\bmeal\b", r"\bcalorie\b"]
compiled_patterns = [re.compile(p, re.IGNORECASE) for p in food_patterns]

# Extract titles from docs that match 'food' domain
food_titles = set()
for doc in docs:
    filename = doc.get('filename')
    text = doc.get('text') or ''
    if not filename:
        continue
    title = filename.replace('.txt', '')
    if any(p.search(text) for p in compiled_patterns):
        food_titles.add(title)

# Sum citation counts for titles in food_titles
total_citations = 0
for row in cites:
    title = row.get('title')
    cc = row.get('citation_count')
    if title in food_titles:
        try:
            total_citations += int(cc)
        except (TypeError, ValueError):
            # Skip non-integer citation counts
            pass

result = json.dumps({"total_citations_food_domain": total_citations})
print("__RESULT__:")
print(result)"""

env_args = {'var_call_KOAb1xgHNfb3JOSVlpr2sxoD': 'file_storage/call_KOAb1xgHNfb3JOSVlpr2sxoD.json', 'var_call_XFFPJlFw3TBBuuRwIfyp1MXj': 'file_storage/call_XFFPJlFw3TBBuuRwIfyp1MXj.json'}

exec(code, env_args)
