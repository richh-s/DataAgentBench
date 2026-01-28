code = """import json
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
        biz_num = biz_id.split('_', 1)[1]
    desc = b.get('description') or ''
    text = desc.replace('\n', ' ').strip()
    low = text.lower()
    seg = ''
    if 'in the category of' in low:
        i = low.find('in the category of')
        seg = text[i + len('in the category of'):]
    elif 'offers a range of services in' in low:
        i = low.find('offers a range of services in')
        seg = text[i + len('offers a range of services in'):]
    elif 'offers a wide range of services' in low:
        i = low.find('offers a wide range of services')
        seg = text[i + len('offers a wide range of services'):]
        if 'including' in seg.lower():
            j = seg.lower().find('including')
            seg = seg[j + len('including'):]
    elif 'offers' in low:
        i = low.find('offers')
        rest = low[i:]
        if ' in ' in rest:
            j = rest.find(' in ')
            seg = text[i + j + len(' in '):]
        else:
            seg = text[i + len('offers'):]
    else:
        if ' in ' in low:
            j = low.rfind(' in ')
            seg = text[j + len(' in '):]
        else:
            seg = text
    if '.' in seg:
        seg = seg.split('.', 1)[0]
    # normalize separators to commas
    seg2 = seg.replace(';', ',').replace('/', ',').replace('|', ',')
    parts = [p.strip() for p in seg2.split(',') if p.strip()]
    cats = []
    for p in parts:
        # split by ' and ' and '&'
        subs = [p]
        if ' and ' in p:
            subs = [s.strip() for s in p.split(' and ') if s.strip()]
        if '&' in p:
            tmp = []
            for s in subs:
                tmp.extend([t.strip() for t in s.split('&') if t.strip()])
            subs = tmp
        for s in subs:
            tok = s.strip().strip("'")
            tok = tok.strip('"')
            if not tok:
                continue
            if any(ch.isdigit() for ch in tok):
                continue
            lt = tok.lower()
            if lt.startswith('located') or lt.startswith('this'):
                continue
            if len(tok) <= 1:
                continue
            if tok not in cats:
                cats.append(tok)
    rows.append({'biz_num': biz_num, 'categories': cats})

biz_df = pd.DataFrame(rows)

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
if rev_df.empty:
    biz_rating = pd.DataFrame(columns=['biz_num', 'avg_rating'])
else:
    biz_rating = rev_df.groupby('biz_num', dropna=True)['rating'].mean().reset_index().rename(columns={'rating': 'avg_rating'})

merged = biz_df.merge(biz_rating, on='biz_num', how='left')
merged['categories'] = merged['categories'].apply(lambda x: x if isinstance(x, list) else [])
exploded = merged.explode('categories')
exploded = exploded[exploded['categories'].notnull()]
exploded['category'] = exploded['categories'].astype(str).str.strip()
exploded = exploded[exploded['category'].str.len() > 0]

if exploded.empty:
    result = {'category': None, 'business_count': 0, 'average_rating': None}
else:
    cat_groups = exploded.groupby('category').agg(
        business_count=('biz_num', lambda s: int(s.nunique())),
        avg_rating=('avg_rating', lambda s: float(pd.Series(s.dropna()).mean()) if s.dropna().size > 0 else None)
    ).reset_index()
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

env_args = {'var_call_ThomBnnXqw33mhC2UcbrP9Pq': ['business', 'checkin'], 'var_call_Bt8qt7Tbvo8qIlzFI0WsTFJx': ['review', 'tip', 'user'], 'var_call_RlBzaAIrwIMVGbXZcA3U0mbp': 'file_storage/call_RlBzaAIrwIMVGbXZcA3U0mbp.json', 'var_call_K5uga7CpcssDzri9cSlPotX7': 'file_storage/call_K5uga7CpcssDzri9cSlPotX7.json', 'var_call_xCzFFIBNj6TYu1ibIoZYD2rw': {'category': None, 'business_count': 0, 'average_rating': None}, 'var_call_du7LI4MMFXCbQjsCbPs7mCjP': 'file_storage/call_du7LI4MMFXCbQjsCbPs7mCjP.json', 'var_call_uq78UAIxrbQElA5IDgHTJdzl': []}

exec(code, env_args)
