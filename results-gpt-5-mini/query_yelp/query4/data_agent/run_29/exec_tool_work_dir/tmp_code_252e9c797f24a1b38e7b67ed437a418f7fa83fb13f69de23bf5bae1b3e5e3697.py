code = """import json
import re
import pandas as pd

# Load data files
with open(var_call_du7LI4MMFXCbQjsCbPs7mCjP, 'r') as f:
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
    desc = b.get('description') or ''
    text = desc.replace('\n', ' ').strip()
    lower = text.lower()
    cats_str = ''
    if 'in the category of' in lower:
        idx = lower.find('in the category of')
        cats_str = text[idx + len('in the category of'):]
    elif 'categories of' in lower:
        idx = lower.find('categories of')
        cats_str = text[idx + len('categories of'):]
    elif 'offers a range of services in' in lower:
        idx = lower.find('offers a range of services in')
        cats_str = text[idx + len('offers a range of services in'):]
    elif 'offers a wide range of services' in lower:
        idx = lower.find('offers a wide range of services')
        seg = text[idx + len('offers a wide range of services'):]
        if 'including' in seg.lower():
            inc_idx = seg.lower().find('including')
            cats_str = seg[inc_idx + len('including'):]
        else:
            cats_str = seg
    elif 'offers' in lower:
        idx = lower.find('offers')
        cats_str = text[idx + len('offers'):]
    elif 'this' in lower and 'offers' not in lower:
        # fallback: take last sentence
        if '.' in text:
            cats_str = text.split('.')[-1]
        else:
            cats_str = text
    # cut at first period
    if cats_str and '.' in cats_str:
        cats_str = cats_str.split('.', 1)[0]
    # split by common separators
    parts = re.split(r'[;,/|]', cats_str) if cats_str else []
    toks = []
    for p in parts:
        # further split by ' and ' or '&'
        subparts = re.split(r'\band\b|&', p, flags=re.IGNORECASE)
        for sp in subparts:
            t = sp.strip()
            # remove leading words like 'including' or 'such as'
            t = re.sub(r'^(including|such as|like)\s+', '', t, flags=re.IGNORECASE)
            if not t:
                continue
            # ignore tokens with digits (likely addresses)
            if re.search(r'\d', t):
                continue
            # ignore location-like starts
            if t.lower().startswith('located') or t.lower().startswith('this'):
                continue
            toks.append(t)
    # also consider commas directly in original if no separators found
    if not toks and cats_str:
        for p in cats_str.split(','):
            t = p.strip()
            if t and not re.search(r'\d', t) and not t.lower().startswith('located'):
                toks.append(t)
    # dedupe while preserving order
    uniq = []
    for x in toks:
        if x not in uniq:
            uniq.append(x)
    rows.append({'biz_num': biz_num, 'categories': uniq})

biz_df = pd.DataFrame(rows)

# process reviews to get per-business avg rating
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
        parts = br.split('_', 1)
        if len(parts) > 1:
            biz_num = parts[1]
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
    # pick top by business_count, then highest avg_rating, then category name
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
