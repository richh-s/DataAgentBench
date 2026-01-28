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
        biz_num = biz_id.split('_', 1)[1]
    accepts = False
    attrs = b.get('attributes')
    if isinstance(attrs, dict):
        val = attrs.get('BusinessAcceptsCreditCards')
        if isinstance(val, bool):
            accepts = val
        elif isinstance(val, str):
            if 'true' in val.lower():
                accepts = True
    # gather categories
    cats = []
    # explicit categories field
    cfield = b.get('categories')
    if cfield:
        if isinstance(cfield, list):
            cats.extend([str(x).strip() for x in cfield if x])
        elif isinstance(cfield, str):
            cats.extend([x.strip() for x in cfield.split(',') if x.strip()])
    # try to extract from description
    desc = b.get('description') or ''
    if desc:
        text = desc.replace('\n', ' ').strip()
        lower = text.lower()
        cats_str = ''
        if 'in the category of' in lower:
            idx = lower.find('in the category of')
            cats_str = text[idx + len('in the category of'):]
        elif 'offers a range of services in' in lower:
            idx = lower.find('offers a range of services in')
            cats_str = text[idx + len('offers a range of services in'):]
        elif 'offers' in lower and ' in ' in lower[lower.find('offers'):]:
            start = lower.find('offers')
            inpos = lower.find(' in ', start)
            if inpos != -1:
                cats_str = text[inpos + len(' in '):]
        elif 'offers' in lower:
            idx = lower.find('offers')
            cats_str = text[idx + len('offers'):]
        elif ' this ' in lower:
            # fallback: take segment after last ' in '
            if ' in ' in lower:
                idx = lower.rfind(' in ')
                cats_str = text[idx + len(' in '):]
        # cut at first period
        if cats_str:
            if '.' in cats_str:
                cats_str = cats_str.split('.',1)[0]
            # split by common separators
            parts = re.split(r',|;|/|\|| - | and | & ', cats_str)
            for p in parts:
                tok = p.strip().strip("'\" ")
                # ignore tokens that are empty or look like addresses (contain digits) or are location phrases
                if not tok:
                    continue
                if re.search(r'\d', tok):
                    continue
                # ignore if token starts with 'located' or contains state abbreviations like 'ca' followed by comma? simple filter
                if tok.lower().startswith('located'):
                    continue
                cats.append(tok)
    # normalize unique
    uniq = []
    for x in cats:
        if x and x not in uniq:
            uniq.append(x)
    rows.append({'business_id': biz_id, 'biz_num': biz_num, 'accepts_cards': accepts, 'categories': uniq})

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
        biz_num = br.split('_', 1)[1]
    rev_rows.append({'biz_num': biz_num, 'rating': rating})
rev_df = pd.DataFrame(rev_rows)

biz_rating = rev_df.groupby('biz_num', dropna=True)['rating'].mean().reset_index().rename(columns={'rating':'avg_rating'})
merged = accept_df.merge(biz_rating, on='biz_num', how='left')

# explode categories
merged['categories'] = merged['categories'].apply(lambda x: x if isinstance(x, list) else [])
exploded = merged.explode('categories')
exploded = exploded[exploded['categories'].notnull()]
exploded['category'] = exploded['categories'].astype(str).str.strip()
exploded = exploded[exploded['category'].str.len() > 0]

# group by category
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
