code = """import json, re
best = var_call_UVH4rqAXDGngJAwBQecqARYc[0]
biz = var_call_xmJnAP8OKDbPLB0OhLrL4Iic[0]
desc = biz.get('description') or ''
# extract categories after 'featuring'
cat = None
m = re.search(r'featuring\s+(.+?)(?:,\s*perfect|\.|$)', desc, flags=re.IGNORECASE)
if m:
    cat = m.group(1).strip()
res = {
  'business_id': biz.get('business_id'),
  'name': biz.get('name'),
  'category': cat,
  'avg_rating': float(best['avg_rating']),
  'review_count_in_period': int(best['review_cnt']),
  'period_start': '2016-01-01',
  'period_end': '2016-06-30'
}
print('__RESULT__:')
print(json.dumps(res))"""

env_args = {'var_call_UVH4rqAXDGngJAwBQecqARYc': [{'business_ref': 'businessref_9', 'avg_rating': '4.285714285714286', 'review_cnt': '7'}], 'var_call_xmJnAP8OKDbPLB0OhLrL4Iic': [{'business_id': 'businessid_9', 'name': 'Coffee House Too Cafe', 'description': 'Located at 501 Fairmount Ave in Philadelphia, PA, this inviting establishment offers a delightful menu featuring Restaurants, Breakfast & Brunch, American (New), Cafes, perfect for a cozy meal any time of the day.'}]}

exec(code, env_args)
