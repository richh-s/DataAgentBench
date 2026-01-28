code = """import json
import re
import pandas as pd

with open(var_call_du7LI4MMFXCbQjsCbPs7mCjP, 'r') as f:
    businesses = json.load(f)
with open(var_call_K5uga7CpcssDzri9cSlPotX7, 'r') as f:
    reviews = json.load(f)

rows = []
for b in businesses:
    biz_id = b.get('business_id')
    biz_num = None
    if isinstance(biz_id, str) and '_' in biz_id:
        biz_num = biz_id.split('_',1)[1]
    # assume BusinessAcceptsCreditCards True by query
    accepts = True
    desc = b.get('description') or ''
    # extract categories from description or categories field
    cats = []
    if b.get('categories'):
        c = b.get('categories')
        if isinstance(c, str):
            cats = [x.strip() for x in c.split(',') if x.strip()]
        elif isinstance(c, list):
            cats = [str(x).strip() for x in c if x]
    else:
        text = desc.replace('\n',' ').strip()
        m = re.search(r'in the category of ([^.]+)\.', text, flags=re.IGNORECASE)
        if not m:
            m = re.search(r'offers[^.]* in ([^.]+)\.', text, flags=re.IGNORECASE)
        if not m:
            # fallback: take after last ' in '
            low = text.lower()
            if ' in ' in low:
                seg = text[low.rfind(' in ')+4:]
            else:
                seg = text
            m = re.match(r'(.+)', seg)
        if m:
            cats_str = m.group(1)
            # split
            parts = re.split(r',|;| and |&', cats_str)
            cats = [p.strip().strip("'\"") for p in parts if p.strip()]
    rows.append({'business_id': biz_id, 'biz_num': biz_num, 'categories': cats})

biz_df = pd.DataFrame(rows)

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
        biz_num = br.split('_',1)[1]
    rev_rows.append({'biz_num': biz_num, 'rating': rating})
rev_df = pd.DataFrame(rev_rows)

biz_rating = rev_df.groupby('biz_num', dropna=True)['rating'].mean().reset_index().rename(columns={'rating':'avg_rating'})

# merge
merged = biz_df.merge(biz_rating, on='biz_num', how='left')
merged['categories'] = merged['categories'].apply(lambda x: x if isinstance(x, list) else ([] if x is None else [x]))
exploded = merged.explode('categories')
exploded['category'] = exploded['categories'].astype(str).str.strip()
exploded = exploded[exploded['category'].str.len() > 0]

cat_groups = exploded.groupby('category').agg(
    business_count = ('biz_num', lambda s: int(s.nunique())),
    avg_rating = ('avg_rating', lambda s: float(pd.Series(s.dropna()).mean()) if s.dropna().size>0 else None)
).reset_index()

cat_groups = cat_groups.sort_values('business_count', ascending=False)

print('__RESULT__:')
print(json.dumps({'top_categories_sample': cat_groups.head(20).to_dict(orient='records')}))"""

env_args = {'var_call_ThomBnnXqw33mhC2UcbrP9Pq': ['business', 'checkin'], 'var_call_Bt8qt7Tbvo8qIlzFI0WsTFJx': ['review', 'tip', 'user'], 'var_call_RlBzaAIrwIMVGbXZcA3U0mbp': 'file_storage/call_RlBzaAIrwIMVGbXZcA3U0mbp.json', 'var_call_K5uga7CpcssDzri9cSlPotX7': 'file_storage/call_K5uga7CpcssDzri9cSlPotX7.json', 'var_call_xCzFFIBNj6TYu1ibIoZYD2rw': {'category': None, 'business_count': 0, 'average_rating': None}, 'var_call_du7LI4MMFXCbQjsCbPs7mCjP': 'file_storage/call_du7LI4MMFXCbQjsCbPs7mCjP.json'}

exec(code, env_args)
