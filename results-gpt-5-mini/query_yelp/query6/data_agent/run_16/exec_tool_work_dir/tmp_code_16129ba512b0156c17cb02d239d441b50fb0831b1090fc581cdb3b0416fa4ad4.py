code = """import json
# access the stored query results
reviews = var_call_CrLTXY6glqpMKi9mumkBa6qA
business_docs = var_call_sP45l6fznaD9MURwY1r7G80n

# extract values
rev = reviews[0]
biz = business_docs[0]

business_ref = rev.get('business_ref')
avg_rating = float(rev.get('avg_rating'))
count = int(rev.get('cnt'))
name = biz.get('name')
description = biz.get('description','')

# parse categories from description if possible
categories = []
if 'featuring ' in description:
    s = description.split('featuring ',1)[1]
    if ', perfect' in s:
        s = s.split(', perfect',1)[0]
    else:
        s = s.split('.',1)[0]
    categories = [c.strip() for c in s.split(',') if c.strip()]
else:
    # fallback to any categories field
    cats_field = biz.get('categories')
    if cats_field:
        categories = cats_field if isinstance(cats_field, list) else [cats_field]

# build final answer string
ans = f"{name} — Categories: {', '.join(categories)} — Average rating: {avg_rating:.1f} ({count} reviews) between 2016-01-01 and 2016-06-30."

print("__RESULT__:")
print(json.dumps(ans))"""

env_args = {'var_call_CrLTXY6glqpMKi9mumkBa6qA': [{'business_ref': 'businessref_9', 'avg_rating': '4.0', 'cnt': '5'}], 'var_call_sP45l6fznaD9MURwY1r7G80n': [{'_id': '6859a000fe8b31cd7362e2f3', 'business_id': 'businessid_9', 'name': 'Coffee House Too Cafe', 'description': 'Located at 501 Fairmount Ave in Philadelphia, PA, this inviting establishment offers a delightful menu featuring Restaurants, Breakfast & Brunch, American (New), Cafes, perfect for a cozy meal any time of the day.'}]}

exec(code, env_args)
