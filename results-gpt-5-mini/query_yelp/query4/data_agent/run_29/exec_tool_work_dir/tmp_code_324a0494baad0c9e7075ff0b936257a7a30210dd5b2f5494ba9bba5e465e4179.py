code = """import json
import re
import pandas as pd

# load data files
with open(var_call_RlBzaAIrwIMVGbXZcA3U0mbp, 'r') as f:
    businesses = json.load(f)
with open(var_call_K5uga7CpcssDzri9cSlPotX7, 'r') as f:
    reviews = json.load(f)

rows = []
for b in businesses:
    biz_id = b.get('business_id')
    biz_num = None
    if isinstance(biz_id, str) and '_' in biz_id:
        biz_num = biz_id.split('_', 1)[1]
    attrs = b.get('attributes')
    accepts = False
    if isinstance(attrs, dict):
        val = attrs.get('BusinessAcceptsCreditCards')
        if isinstance(val, bool):
            accepts = val
        elif isinstance(val, str):
            if 'true' in val.lower() or 'true' in val:
                accepts = True
    # categories
    cats = []
    if b.get('categories'):
        c = b.get('categories')
        if isinstance(c, str):
            cats = [x.strip() for x in c.split(',') if x.strip()]
        elif isinstance(c, list):
            cats = [str(x).strip() for x in c if x]
    else:
        desc = b.get('description') or ''
        desc = desc.replace('\n', ' ')
        m = re.search(r'in the category of ([^.]+)\.', desc, flags=re.IGNORECASE)
        if not m:
            m = re.search(r'offers[^.]* in ([^.]+)\.', desc, flags=re.IGNORECASE)
        if not m:
            m = re.search(r'offers a range of services in (.+)', desc, flags=re.IGNORECASE)
        if m:
            cats_str = m.group(1)
            parts = re.split(r',|;| and |&', cats_str)
            cleaned = [p.strip() for p in parts if p.strip()]
            cats = [p for p in cleaned if not re.search(r'\d', p)]
            if not cats:
                cats = cleaned
    rows.append({'business_id': biz_id, 'biz_num': biz_num, 'accepts_cards': accepts, 'categories': cats})

biz_df = pd.DataFrame(rows)
accept_df = biz_df[biz_df['accepts_cards'] == True].copy()

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
        biz_num = br.split('_', 1)[1]
    rev_rows.append({'biz_num': biz_num, 'rating': rating})
rev_df = pd.DataFrame(rev_rows)

biz_rating = rev_df.groupby('biz_num', dropna=True)['rating'].mean().reset_index().rename(columns={'rating':'avg_rating'})
merged = accept_df.merge(biz_rating, on='biz_num', how='left')

# explode categories
merged['categories'] = merged['categories'].apply(lambda x: x if isinstance(x, list) else ([] if x is None else [x]))
exploded = merged.explode('categories')
exploded = exploded[exploded['categories'].notnull()]
exploded['category'] = exploded['categories'].astype(str).str.strip()
exploded = exploded[exploded['category'].str.len() > 0]

# group by category
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
