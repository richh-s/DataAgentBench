code = """import json
from collections import defaultdict
p = var_call_UO8D11S4FDoOd36hCh8GDjr6
with open(p, 'r') as f:
    docs = json.load(f)
cat_to_biz = defaultdict(set)
for d in docs:
    biz_id = d.get('business_id')
    attrs = d.get('attributes')
    if not attrs or not isinstance(attrs, dict):
        continue
    val = attrs.get('BusinessAcceptsCreditCards')
    if val is None:
        continue
    sval = str(val).lower()
    if 'true' not in sval:
        continue
    cats = d.get('categories')
    if not cats:
        continue
    if isinstance(cats, list):
        parts = cats
    else:
        parts = [c.strip() for c in str(cats).split(',') if c.strip()]
    for c in parts:
        cat_to_biz[c].add(biz_id)
cat_counts = {c: len(s) for c, s in cat_to_biz.items()}
if not cat_counts:
    res = {"top_category": None, "top_count": 0, "business_ids": [], "business_refs": []}
else:
    top_category = sorted(cat_counts.items(), key=lambda x: (-x[1], x[0]))[0][0]
    top_count = cat_counts[top_category]
    biz_ids = sorted(list(cat_to_biz[top_category]))
    biz_refs = [b.replace('businessid_', 'businessref_') for b in biz_ids]
    res = {"top_category": top_category, "top_count": top_count, "business_ids": biz_ids, "business_refs": biz_refs}
print("__RESULT__:")
print(json.dumps(res))"""

env_args = {'var_call_7ZgO1JmiFzKIX0XDrSGqVpq3': ['checkin', 'business'], 'var_call_tn6yro8Bzk11NeQZGFUQjmNo': ['review', 'tip', 'user'], 'var_call_KABRrtqNUlTcXdQMb8MB38mC': 'file_storage/call_KABRrtqNUlTcXdQMb8MB38mC.json', 'var_call_ZcHJViISDWvVgJ1fdfMMnt95': {'top_category': None, 'top_count': 0, 'business_ids': [], 'business_refs': []}, 'var_call_UO8D11S4FDoOd36hCh8GDjr6': 'file_storage/call_UO8D11S4FDoOd36hCh8GDjr6.json'}

exec(code, env_args)
