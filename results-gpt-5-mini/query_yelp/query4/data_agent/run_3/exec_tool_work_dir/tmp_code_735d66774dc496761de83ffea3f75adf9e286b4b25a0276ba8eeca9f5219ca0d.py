code = """import json
import pandas as pd

# Load files
with open(var_call_S2zuCHmhggl6c0g3JVnsCV3S, 'r') as f:
    businesses = json.load(f)
with open(var_call_yro9FRCCc3lUv55SCI5jPHkG, 'r') as f:
    reviews = json.load(f)

rows = []
for b in businesses:
    bid = b.get('business_id')
    attr = b.get('attributes')
    cats = b.get('categories') if 'categories' in b else None
    accepts = False
    if isinstance(attr, dict):
        v = attr.get('BusinessAcceptsCreditCards')
        if isinstance(v, str):
            if 'true' in v.lower():
                accepts = True
        elif isinstance(v, bool):
            accepts = bool(v)
    elif isinstance(attr, str):
        low = attr.lower()
        if 'businessacceptscreditcards' in low and 'true' in low:
            accepts = True

    cats_list = []
    if cats and isinstance(cats, str):
        s = cats.strip()
        if s.startswith('[') and s.endswith(']'):
            s = s[1:-1]
        parts = [p.strip() for p in s.split(',') if p.strip()]
        cleaned = []
        for p in parts:
            if len(p) >= 2 and ((p[0] == "'" and p[-1] == "'") or (p[0] == '"' and p[-1] == '"')):
                p2 = p[1:-1]
            else:
                p2 = p
            p2 = p2.strip()
            if p2:
                cleaned.append(p2)
        cats_list = cleaned
    elif isinstance(cats, list):
        cats_list = [c for c in cats if isinstance(c, str)]

    rows.append({
        'business_id': bid,
        'business_ref': bid.replace('businessid_','businessref_') if isinstance(bid,str) else None,
        'accepts_credit': accepts,
        'categories': cats_list
    })

biz_df = pd.DataFrame(rows)
cc_biz = biz_df[biz_df['accepts_credit'] == True].copy()

from collections import defaultdict
cat_to_biz = defaultdict(set)
for _, r in cc_biz.iterrows():
    refs = r['business_ref']
    cats = r['categories']
    if not cats:
        continue
    for c in cats:
        if c and isinstance(c, str):
            cat_to_biz[c].add(refs)

rev_df = pd.DataFrame(reviews)
if not rev_df.empty:
    rev_df['rating'] = pd.to_numeric(rev_df['rating'], errors='coerce')
else:
    rev_df['rating'] = pd.Series(dtype=float)

results = []
for c, bizset in cat_to_biz.items():
    count = len(bizset)
    if count == 0:
        continue
    subset = rev_df[rev_df['business_ref'].isin(bizset)]
    if not subset.empty:
        avg_rating = float(subset['rating'].mean())
    else:
        avg_rating = None
    results.append({'category': c, 'business_count': count, 'average_rating': avg_rating})

if results:
    results_sorted = sorted(results, key=lambda x: (x['business_count'], x['category']), reverse=True)
    best = results_sorted[0]
else:
    best = {'category': None, 'business_count': 0, 'average_rating': None}

out = {
    'category': best['category'],
    'business_count': best['business_count'],
    'average_rating': round(best['average_rating'], 2) if best['average_rating'] is not None else None
}

print("__RESULT__:")
print(json.dumps(out))"""

env_args = {'var_call_d7w2bomFdJCav34AlVZstfqh': ['business', 'checkin'], 'var_call_eZ7MDOj0Zdn0YwI5SRy8qChp': ['review', 'tip', 'user'], 'var_call_S2zuCHmhggl6c0g3JVnsCV3S': 'file_storage/call_S2zuCHmhggl6c0g3JVnsCV3S.json', 'var_call_yro9FRCCc3lUv55SCI5jPHkG': 'file_storage/call_yro9FRCCc3lUv55SCI5jPHkG.json', 'var_call_dE4HJh0hciMIKYUkYYNDB6yW': {'biz_len': 100, 'rev_len': 2000}}

exec(code, env_args)
