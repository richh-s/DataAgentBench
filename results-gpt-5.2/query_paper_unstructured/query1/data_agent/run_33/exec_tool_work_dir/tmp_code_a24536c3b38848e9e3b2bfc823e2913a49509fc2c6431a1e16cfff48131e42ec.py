code = """import json, re, pandas as pd

# Load mongo docs (may be file path)
docs_src = var_call_HRdqIRfz8nWr814C6xHMvkMU
if isinstance(docs_src, str):
    with open(docs_src, 'r', encoding='utf-8') as f:
        docs = json.load(f)
else:
    docs = docs_src

# Identify 'food' domain papers by simple contains in text near a domain list or anywhere
food_titles = set()
for d in docs:
    fn = d.get('filename','')
    title = fn[:-4] if fn.lower().endswith('.txt') else fn
    text = d.get('text','') or ''
    if re.search(r'\bfood\b', text, flags=re.IGNORECASE):
        food_titles.add(title)

# Load citations (may be file path)
cit_src = var_call_dmWahoNrBrPmVOl9b8BuyXyf
if isinstance(cit_src, str):
    with open(cit_src, 'r', encoding='utf-8') as f:
        cits = json.load(f)
else:
    cits = cit_src

# Sum citation counts for titles in food_titles

total = 0
for r in cits:
    if r.get('title') in food_titles:
        try:
            total += int(r.get('citation_count') or 0)
        except Exception:
            pass

out = {"total_citation_count_food_domain": total, "food_paper_count_matched": len(food_titles)}
print('__RESULT__:')
print(json.dumps(out))"""

env_args = {'var_call_HRdqIRfz8nWr814C6xHMvkMU': 'file_storage/call_HRdqIRfz8nWr814C6xHMvkMU.json', 'var_call_dmWahoNrBrPmVOl9b8BuyXyf': 'file_storage/call_dmWahoNrBrPmVOl9b8BuyXyf.json'}

exec(code, env_args)
