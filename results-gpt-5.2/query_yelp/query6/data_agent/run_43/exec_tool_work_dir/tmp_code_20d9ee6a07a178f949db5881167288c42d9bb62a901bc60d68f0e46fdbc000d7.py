code = """import json, re
rec = var_call_CHgeI45hs5J4wykT1kGTVr3T[0]
desc = rec.get('description') or ''
# Extract categories after 'featuring'
cat = None
m = re.search(r"featuring\s+(.+?)(?:,\s*perfect|\.|$)", desc, flags=re.IGNORECASE)
if m:
    cat = m.group(1).strip()
# Fallback: take last sentence after 'menu featuring'
if not cat:
    cat = desc
out = {
    "business_id": rec.get('business_id'),
    "name": rec.get('name'),
    "category": cat
}
print('__RESULT__:')
print(json.dumps(out))"""

env_args = {'var_call_Xvm9n76uQZxO3tATNdV96feQ': [{'business_ref': 'businessref_9', 'review_cnt': '5', 'avg_rating': '4.0'}], 'var_call_CHgeI45hs5J4wykT1kGTVr3T': [{'business_id': 'businessid_9', 'name': 'Coffee House Too Cafe', 'description': 'Located at 501 Fairmount Ave in Philadelphia, PA, this inviting establishment offers a delightful menu featuring Restaurants, Breakfast & Brunch, American (New), Cafes, perfect for a cozy meal any time of the day.'}]}

exec(code, env_args)
