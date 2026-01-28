code = """import json, re
import pandas as pd

# Load paper docs
paper_src = var_call_qlij76grcCeuq92SF3OyvQaK
if isinstance(paper_src, str) and paper_src.endswith('.json'):
    with open(paper_src, 'r', encoding='utf-8') as f:
        paper_docs = json.load(f)
else:
    paper_docs = paper_src

# Identify 'food' domain papers by substring match in full text.
# Use word boundary to reduce false positives (e.g., seafood -> counts? still food-related; keep simple word boundary on food).
food_titles = []
pat = re.compile(r"\bfood\b", re.IGNORECASE)
for d in paper_docs:
    txt = d.get('text','') or ''
    if pat.search(txt):
        fn = d.get('filename','') or ''
        title = fn[:-4] if fn.lower().endswith('.txt') else fn
        food_titles.append(title)
food_titles_set = set(food_titles)

# Load citations
cit_src = var_call_BLXzIIiiRKVAkMbcS5KNzqhC
if isinstance(cit_src, str) and cit_src.endswith('.json'):
    with open(cit_src, 'r', encoding='utf-8') as f:
        cit_rows = json.load(f)
else:
    cit_rows = cit_src

# Sum citation_count for food titles

total = 0
for r in cit_rows:
    if r.get('title') in food_titles_set:
        try:
            total += int(r.get('citation_count', 0) or 0)
        except Exception:
            pass

out = {"total_citation_count_food_domain": total, "food_paper_count": len(food_titles_set)}
print('__RESULT__:')
print(json.dumps(out))"""

env_args = {'var_call_qlij76grcCeuq92SF3OyvQaK': 'file_storage/call_qlij76grcCeuq92SF3OyvQaK.json', 'var_call_BLXzIIiiRKVAkMbcS5KNzqhC': 'file_storage/call_BLXzIIiiRKVAkMbcS5KNzqhC.json'}

exec(code, env_args)
