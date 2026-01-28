code = """import json, re
with open(var_call_KOAb1xgHNfb3JOSVlpr2sxoD, 'r') as f:
    docs = json.load(f)

count_docs = len(docs)
food_docs = []
for doc in docs:
    text = (doc.get('text') or '')
    fn = doc.get('filename')
    if not fn:
        continue
    if 'food' in text.lower() or 'diet' in text.lower() or 'nutrition' in text.lower() or 'eating' in text.lower() or 'meal' in text.lower() or 'calorie' in text.lower():
        food_docs.append(fn)

result = {"count_docs": count_docs, "food_docs_count": len(food_docs), "food_docs_sample": food_docs[:10]}
print("__RESULT__:")
print(json.dumps(result))"""

env_args = {'var_call_KOAb1xgHNfb3JOSVlpr2sxoD': 'file_storage/call_KOAb1xgHNfb3JOSVlpr2sxoD.json', 'var_call_XFFPJlFw3TBBuuRwIfyp1MXj': 'file_storage/call_XFFPJlFw3TBBuuRwIfyp1MXj.json', 'var_call_7x4P0KBQEa1dlWFV6BOGAVaZ': {'total_citations_food_domain': 0}, 'var_call_VMUHIoAr4PWJyDnTWS33EepV': {'food_titles_count': 0, 'food_titles_sample': [], 'citation_titles_count': 259, 'intersection_count': 0, 'intersection_sample': []}}

exec(code, env_args)
