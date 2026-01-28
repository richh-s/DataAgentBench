code = """import json
import pandas as pd

rev = pd.DataFrame(var_call_BaKDJ8itwx4m6IXksJbAh9uv)
if rev.empty:
    out = {"error": "No businesses found with >=5 reviews in date range."}
else:
    top = rev.iloc[0].to_dict()
    business_ref = top["business_ref"]
    bid = business_ref.replace('businessref_', 'businessid_')

    path = var_call_76KYlHYJ6dVvjtGXGzhjtvTW
    with open(path, 'r', encoding='utf-8') as f:
        biz_list = json.load(f)

    biz = next((b for b in biz_list if b.get('business_id') == bid), None)
    name = biz.get('name') if biz else None
    desc = biz.get('description') if biz else None

    # crude category extraction: take text after last 'categories' keyword if present, else None
    category = None
    if isinstance(desc, str) and 'categories' in desc.lower():
        low = desc.lower()
        idx = low.rfind('categories')
        tail = desc[idx:]
        # take after ':' if present
        if ':' in tail:
            category = tail.split(':',1)[1].strip().strip('.')
        elif 'categories of' in tail.lower():
            category = tail.split('categories of',1)[1].strip().strip(".'\"")
        else:
            category = tail

    out = {
        "business_ref": business_ref,
        "business_id": bid,
        "name": name,
        "avg_rating": float(top["avg_rating"]),
        "review_cnt": int(top["review_cnt"]),
        "category": category
    }

print('__RESULT__:')
print(json.dumps(out))"""

env_args = {'var_call_BaKDJ8itwx4m6IXksJbAh9uv': [{'business_ref': 'businessref_9', 'avg_rating': '4.0', 'review_cnt': '5'}], 'var_call_76KYlHYJ6dVvjtGXGzhjtvTW': 'file_storage/call_76KYlHYJ6dVvjtGXGzhjtvTW.json'}

exec(code, env_args)
