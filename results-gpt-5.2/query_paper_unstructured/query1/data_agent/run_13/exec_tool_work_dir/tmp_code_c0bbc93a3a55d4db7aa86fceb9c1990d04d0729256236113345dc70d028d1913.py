code = """import json, re

mongo_src = var_call_Yp9yrBbnHB65oy2iNj2UNcqe
if isinstance(mongo_src, str) and mongo_src.endswith('.json'):
    with open(mongo_src, 'r', encoding='utf-8') as f:
        paper_docs = json.load(f)
else:
    paper_docs = mongo_src

cit_src = var_call_0YVbp3PbxQIrQYqAYWhjzYoI
if isinstance(cit_src, str) and cit_src.endswith('.json'):
    with open(cit_src, 'r', encoding='utf-8') as f:
        citations = json.load(f)
else:
    citations = cit_src

food_titles = set()
# domain: food  OR domain = [..]
pat = re.compile(r"\bdomain\b\s*[:=]\s*(\[[^\]]*\]|[^\n\r,;]+)", re.IGNORECASE)
for d in paper_docs:
    fn = d.get('filename','')
    title = fn[:-4] if fn.lower().endswith('.txt') else fn
    text = d.get('text','') or ''
    m = pat.search(text)
    if m and ('food' in m.group(1).lower()):
        food_titles.add(title)

food_cit_total = 0
for r in citations:
    if r.get('title') in food_titles:
        try:
            food_cit_total += int(r.get('citation_count') or 0)
        except Exception:
            food_cit_total += 0

out = {"food_domain_paper_count": len(food_titles), "total_citation_count": food_cit_total}
print('__RESULT__:')
print(json.dumps(out))"""

env_args = {'var_call_Yp9yrBbnHB65oy2iNj2UNcqe': 'file_storage/call_Yp9yrBbnHB65oy2iNj2UNcqe.json', 'var_call_0YVbp3PbxQIrQYqAYWhjzYoI': 'file_storage/call_0YVbp3PbxQIrQYqAYWhjzYoI.json'}

exec(code, env_args)
