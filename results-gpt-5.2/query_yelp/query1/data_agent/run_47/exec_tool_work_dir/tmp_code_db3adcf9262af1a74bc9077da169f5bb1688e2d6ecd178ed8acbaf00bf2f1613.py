code = """import json, pandas as pd

# Load business ids from mongo result
biz = pd.DataFrame(var_call_PxSslBynkRUDo0XZ4LE17jch)
if biz.empty:
    out = {"avg_rating": None, "business_count": 0, "review_count": 0}
else:
    biz_ids = biz['business_id'].tolist()
    # map to business_ref
    biz_refs = ['businessref_' + x[len('businessid_'):] if x.startswith('businessid_') else x for x in biz_ids]
    # chunk to avoid huge IN
    chunks = [biz_refs[i:i+5000] for i in range(0, len(biz_refs), 5000)]
    avgs = []
    counts = []
    for ch in chunks:
        in_list = ','.join(["'"+s.replace("'","''")+"'" for s in ch])
        q = f"SELECT AVG(rating) AS avg_rating, COUNT(*) AS n FROM review WHERE business_ref IN ({in_list});"
        # query via tool not available here; so cannot.
    out = {"avg_rating": None, "business_count": int(len(biz_refs)), "review_count": None}

print('__RESULT__:')
print(json.dumps(out))"""

env_args = {'var_call_PxSslBynkRUDo0XZ4LE17jch': []}

exec(code, env_args)
