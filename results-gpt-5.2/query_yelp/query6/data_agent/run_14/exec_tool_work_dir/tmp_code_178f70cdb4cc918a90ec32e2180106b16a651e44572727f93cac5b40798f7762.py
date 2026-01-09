code = """import json, re
import pandas as pd

# top business from reviews aggregation
rev = pd.DataFrame(var_call_BaKDJ8itwx4m6IXksJbAh9uv)
if rev.empty:
    out = {"error":"No businesses found with >=5 reviews in date range."}
else:
    top = rev.iloc[0].to_dict()
    business_ref = top["business_ref"]
    # map businessref_X -> businessid_X
    bid = business_ref.replace('businessref_', 'businessid_')

    # load businesses list from json file
    path = var_call_76KYlHYJ6dVvjtGXGzhjtvTW
    with open(path, 'r', encoding='utf-8') as f:
        biz_list = json.load(f)
    # find matching business
    biz = next((b for b in biz_list if b.get('business_id') == bid), None)

    name = biz.get('name') if biz else None
    desc = biz.get('description') if biz else None

    # extract categories from description (after 'categories of' or 'categories:' style)
    category = None
    if isinstance(desc, str):
        m = re.search(r"categories? (?:of|including|in the categories of)\s*:?\s*(.*?)(?:\.|$)", desc, flags=re.IGNORECASE|re.DOTALL)
        if m:
            category = m.group(1).strip().strip("'\"")
        else:
            # fallback: take last comma-separated chunk after 'offers' maybe; keep concise
            # try to capture tail after 'including'
            m2 = re.search(r"including\s+(.+?)(?:\.|$)", desc, flags=re.IGNORECASE|re.DOTALL)
            if m2:
                category = m2.group(1).strip()

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
