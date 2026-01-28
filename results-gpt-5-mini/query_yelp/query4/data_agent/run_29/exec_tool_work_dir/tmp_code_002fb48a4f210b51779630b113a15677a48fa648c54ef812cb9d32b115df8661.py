code = """import json
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
    accepts = False
    attrs = b.get('attributes')
    if isinstance(attrs, dict):
        val = attrs.get('BusinessAcceptsCreditCards')
        if isinstance(val, bool):
            accepts = val
        else:
            if val is not None:
                if 'true' in str(val).lower():
                    accepts = True
    # categories: try explicit first
    cats = []
    cfield = b.get('categories')
    if cfield:
        if isinstance(cfield, list):
            cats.extend([str(x).strip() for x in cfield if x])
        elif isinstance(cfield, str):
            cats.extend([x.strip() for x in cfield.split(',') if x.strip()])
    # if no explicit categories, try to parse description
    if not cats:
        desc = b.get('description') or ''
        if desc:
            text = desc.replace('\n', ' ').strip()
            # try to find a segment likely containing categories
            seg = ''
            low = text.lower()
            # prefer phrase 'in the category of'
            key = 'in the category of'
            if key in low:
                idx = low.find(key)
                seg = text[idx + len(key):]
            else:
                key2 = 'offers a range of services in'
                if key2 in low:
                    idx = low.find(key2)
                    seg = text[idx + len(key2):]
                else:
                    # find last ' in ' occurrence
                    if ' in ' in low:
                        idx = low.rfind(' in ')
                        seg = text[idx + len(' in '):]
                    else:
                        # fallback: take last sentence
                        if '.' in text:
                            seg = text.split('.')[-1]
                        else:
                            seg = text
            # cut at period
            if '.' in seg:
                seg = seg.split('.', 1)[0]
            # split by commas
            parts = [p.strip() for p in seg.replace(';', ',').split(',') if p.strip()]
            # further split by ' and '
            final_parts = []
            for p in parts:
                if ' and ' in p:
                    for sub in p.split(' and '):
                        s = sub.strip()
                        if s:
                            final_parts.append(s)
                else:
                    final_parts.append(p)
            # clean tokens: remove those that contain digits or common address words
            for tok in final_parts:
                t = tok
                if any(ch.isdigit() for ch in t):
                    continue
                lowt = t.lower()
                if lowt.startswith('located') or lowt.startswith('this'):
                    continue
                # strip trailing words like 'this facility' etc
                t = t.strip(' -')
                if t and t not in cats:
                    cats.append(t)
    # dedupe
    uniq = []
    for x in cats:
        if x and x not in uniq:
            uniq.append(x)
    rows.append({'business_id': biz_id, 'biz_num': biz_num, 'accepts_cards': accepts, 'categories': uniq})

biz_df = pd.DataFrame(rows)
accept_df = biz_df[biz_df['accepts_cards'] == True].copy()

# reviews
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

biz_rating = rev_df.groupby('biz_num', dropna=True)['rating'].mean().reset_index().rename(columns={'rating':'avg_rating'})
merged = accept_df.merge(biz_rating, on='biz_num', how='left')

merged['categories'] = merged['categories'].apply(lambda x: x if isinstance(x, list) else [])
exploded = merged.explode('categories')
exploded = exploded[exploded['categories'].notnull()]
exploded['category'] = exploded['categories'].astype(str).str.strip()
exploded = exploded[exploded['category'].str.len() > 0]

if exploded.empty:
    result = {'category': None, 'business_count': 0, 'average_rating': None}
else:
    cat_groups = exploded.groupby('category').agg(
        business_count = ('biz_num', lambda s: int(s.nunique())),
        avg_rating = ('avg_rating', lambda s: float(pd.Series(s.dropna()).mean()) if s.dropna().size > 0 else None)
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

env_args = {'var_call_ThomBnnXqw33mhC2UcbrP9Pq': ['business', 'checkin'], 'var_call_Bt8qt7Tbvo8qIlzFI0WsTFJx': ['review', 'tip', 'user'], 'var_call_RlBzaAIrwIMVGbXZcA3U0mbp': 'file_storage/call_RlBzaAIrwIMVGbXZcA3U0mbp.json', 'var_call_K5uga7CpcssDzri9cSlPotX7': 'file_storage/call_K5uga7CpcssDzri9cSlPotX7.json', 'var_call_xCzFFIBNj6TYu1ibIoZYD2rw': {'category': None, 'business_count': 0, 'average_rating': None}}

exec(code, env_args)
