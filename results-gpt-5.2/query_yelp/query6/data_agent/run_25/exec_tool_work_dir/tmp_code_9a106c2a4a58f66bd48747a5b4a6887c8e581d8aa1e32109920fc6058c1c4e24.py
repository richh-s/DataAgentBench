code = """import json, re
row = var_call_1VdRXdZ1HK2tWk4C1qnVnlEP[0]
biz = var_call_c2FZunEIM8v00qkFnEO4CTug[0]
desc = biz.get('description') or ''
# extract category-like phrase after 'featuring'
cat = None
m = re.search(r"featuring\s+([^\.]+)", desc, flags=re.IGNORECASE)
if m:
    cat = m.group(1).strip()
result = {
    "business": biz.get('name'),
    "business_id": biz.get('business_id'),
    "avg_rating": float(row['avg_rating']),
    "review_count_in_period": int(row['review_cnt']),
    "category": cat
}
print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_call_1VdRXdZ1HK2tWk4C1qnVnlEP': [{'business_ref': 'businessref_9', 'avg_rating': '4.375', 'review_cnt': '16'}], 'var_call_c2FZunEIM8v00qkFnEO4CTug': [{'business_id': 'businessid_9', 'name': 'Coffee House Too Cafe', 'description': 'Located at 501 Fairmount Ave in Philadelphia, PA, this inviting establishment offers a delightful menu featuring Restaurants, Breakfast & Brunch, American (New), Cafes, perfect for a cozy meal any time of the day.'}]}

exec(code, env_args)
