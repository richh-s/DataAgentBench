code = """import json
import re
import pandas as pd

with open(var_call_RlBzaAIrwIMVGbXZcA3U0mbp, 'r') as f:
    businesses = json.load(f)
with open(var_call_K5uga7CpcssDzri9cSlPotX7, 'r') as f:
    reviews = json.load(f)

rows = []
for b in businesses:
    biz_id = b.get('business_id')
    biz_num = None
    if isinstance(biz_id, str) and '_' in biz_id:
        parts = biz_id.split('_', 1)
        if len(parts) > 1:
            biz_num = parts[1]
    attrs = b.get('attributes')
    accepts = False
    if isinstance(attrs, dict):
        val = attrs.get('BusinessAcceptsCreditCards')
        if isinstance(val, bool):
            accepts = val
        elif isinstance(val, str):
            if 'true' in val.lower() or 'True' in val:
                accepts = True
    # categories field
    cats = []
    c = b.get('categories')
    if c:
        if isinstance(c, str):
            cats = [x.strip() for x in c.split(',') if x.strip()]
        elif isinstance(c, list):
            cats = [str(x).strip() for x in c if x]
    else:
        desc = b.get('description') or ''
        desc = desc.replace('\n', ' ')
        cats_str = ''
        # try heuristics
        if 'in the category of' in desc.lower():
            m = re.search(r'in the category of ([^.]+)\.', desc, flags=re.IGNORECASE)
            if m:
                cats_str = m.group(1)
        if not cats_str and ' offers ' in desc.lower():
            # find 'offers' and then look for ' in '
            lower = desc.lower()
            idx = lower.find('offers')
            if idx >= 0:
                sub = desc[idx:]
                if ' in ' in sub.lower():
                    sub2 = sub.lower().split(' in ', 1)[1]
                    # take until period
                    if '.' in sub2:
                        cats_str = sub2.split('.',1)[0]
                    else:
                        cats_str = sub2
        if not cats_str:
            # fallback: take last 200 chars
            cats_str = desc[-200:]
        # split by common separators
        parts = re.split('[,;&]', cats_str)
        cleaned = []
        for p in parts:
            subparts = [q.strip() for q in re.split(r' and | & ', p) if q.strip()]
            for q in subparts:
                q2 = q.replace("\"", '').replace("'", '').strip()
                if q2:
                    cleaned.append(q2)
        # filter out tokens with digits (likely addresses) and very short tokens
        cats = [t for t in cleaned if not re.search(r'\d', t) and len(t) > 1]
        if not cats:
            cats = cleaned
    rows.append({'business_id': biz_id, 'biz_num': biz_num, 'accepts_cards': accepts, 'categories': cats})

biz_df = pd.DataFrame(rows)
accept_df = biz_df[biz_df['accepts_cards'] == True].copy()

# process reviews
rev_rows = []
for r in reviews:
    br = r.get('business_ref')
    rating = r.get('rating')
    try:
        rating = float(rating)
    except:
        continue
    biz_num = None
    if isinstance(br, str) and '_' in br:
        parts = br.split('_',1)
        if len(parts) > 1:
            biz_num = parts[1]
    rev_rows.append({'biz_num': biz_num, 'rating': rating})
rev_df = pd.DataFrame(rev_rows)

biz_rating = rev_df.groupby('biz_num', dropna=True)['rating'].mean().reset_index().rename(columns={'rating':'avg_rating'})
merged = accept_df.merge(biz_rating, on='biz_num', how='left')

merged['categories'] = merged['categories'].apply(lambda x: x if isinstance(x, list) else ([] if x is None else [x]))
exploded = merged.explode('categories')
exploded = exploded[exploded['categories'].notnull()]
exploded['category'] = exploded['categories'].astype(str).str.strip()
exploded = exploded[exploded['category'].str.len() > 0]

cat_groups = exploded.groupby('category').agg(
    business_count = ('biz_num', lambda s: int(s.nunique())),
    avg_rating = ('avg_rating', lambda s: float(pd.Series(s.dropna()).mean()) if s.dropna().size > 0 else None)
).reset_index()

if cat_groups.shape[0] == 0:
    result = {'category': None, 'business_count': 0, 'average_rating': None}
else:
    max_count = int(cat_groups['business_count'].max())
    top = cat_groups[cat_groups['business_count'] == max_count].copy()
    top['avg_filled'] = top['avg_rating'].fillna(-999)
    top = top.sort_values(['avg_filled', 'category'], ascending=[False, True])
    chosen = top.iloc[0]
    avg_val = chosen['avg_rating']
    if avg_val is not None:
        avg_val = float(round(avg_val, 3))
    result = {'category': chosen['category'], 'business_count': int(chosen['business_count']), 'average_rating': avg_val}

print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_call_ThomBnnXqw33mhC2UcbrP9Pq': ['business', 'checkin'], 'var_call_Bt8qt7Tbvo8qIlzFI0WsTFJx': ['review', 'tip', 'user'], 'var_call_RlBzaAIrwIMVGbXZcA3U0mbp': 'file_storage/call_RlBzaAIrwIMVGbXZcA3U0mbp.json', 'var_call_K5uga7CpcssDzri9cSlPotX7': 'file_storage/call_K5uga7CpcssDzri9cSlPotX7.json'}

exec(code, env_args)
