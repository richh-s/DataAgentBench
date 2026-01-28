code = """import json
import re
import pandas as pd

# load data from storage file paths
with open(var_call_RlBzaAIrwIMVGbXZcA3U0mbp, 'r') as f:
    businesses = json.load(f)

with open(var_call_K5uga7CpcssDzri9cSlPotX7, 'r') as f:
    reviews = json.load(f)

# normalize businesses
rows = []
for b in businesses:
    biz_id = b.get('business_id')
    # extract numeric id after underscore
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
            if val.lower() == 'true' or "True" in val:
                accepts = True
    # extract categories
    cats = None
    if 'categories' in b and b.get('categories'):
        cats = b.get('categories')
        # ensure list
        if isinstance(cats, str):
            cats = [c.strip() for c in cats.split(',') if c.strip()]
        elif isinstance(cats, list):
            cats = [str(c).strip() for c in cats if c]
    else:
        desc = b.get('description') or ''
        desc = desc.replace('\n', ' ')
        cats = []
        # try to find categories in description with some heuristics
        m = re.search(r'offers[^.]* in ([^.]+)\.', desc, re.IGNORECASE)
        if not m:
            m = re.search(r'in the category of ([^.]+)\.', desc, re.IGNORECASE)
        if not m:
            m = re.search(r'offers[^.]* ([A-Za-z &/,]+)$', desc)
        if m:
            cats_str = m.group(1)
            # split by common separators
            cats_list = [c.strip(' "\'') for c in re.split(r',|;| and |&', cats_str) if c.strip()]
            # filter out tokens that look like addresses (contain digits)
            cats = [c for c in cats_list if not re.search(r'\d', c) and len(c) > 1]
            if not cats:
                cats = cats_list
    rows.append({'business_id': biz_id, 'biz_num': biz_num, 'accepts_cards': accepts, 'categories': cats})

biz_df = pd.DataFrame(rows)
# filter accepting credit cards
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
        biz_num = br.split('_',1)[1]
    rev_rows.append({'business_ref': br, 'biz_num': biz_num, 'rating': rating})
rev_df = pd.DataFrame(rev_rows)

# compute per-business average rating
biz_rating = rev_df.groupby('biz_num', dropna=True)['rating'].mean().reset_index().rename(columns={'rating':'avg_rating'})

# merge with accepting businesses
merged = accept_df.merge(biz_rating, on='biz_num', how='left')

# explode categories
merged['categories'] = merged['categories'].apply(lambda x: x if isinstance(x, list) else ([] if x is None else [x]))
exploded = merged.explode('categories')
exploded = exploded[exploded['categories'].notnull()]
exploded['category'] = exploded['categories'].astype(str).str.strip()
# filter out empty
exploded = exploded[exploded['category'].str.len() > 0]

# For each category, get unique businesses count and average of per-business avg_rating (ignoring businesses with no rating)
cat_groups = exploded.groupby('category').agg(
    business_count = ('biz_num', lambda s: int(s.nunique())),
    avg_rating = ('avg_rating', lambda s: float(pd.Series(s.dropna()).mean()) if s.dropna().size>0 else None)
).reset_index()

# find category with max business_count
if cat_groups.shape[0] == 0:
    result = {"category": None, "business_count": 0, "average_rating": None}
else:
    max_count = cat_groups['business_count'].max()
    top = cat_groups[cat_groups['business_count'] == max_count].copy()
    # if multiple, choose the one with highest avg_rating (treat None as very small)
    top['avg_rating_filled'] = top['avg_rating'].fillna(-999)
    top = top.sort_values(['avg_rating_filled','category'], ascending=[False, True])
    chosen = top.iloc[0]
    avg_rating_val = chosen['avg_rating']
    if avg_rating_val is None:
        avg_rating_val = None
    else:
        avg_rating_val = float(round(avg_rating_val,3))
    result = {"category": chosen['category'], "business_count": int(chosen['business_count']), "average_rating": avg_rating_val}

print("__RESULT__:")
print(json.dumps(result))"""

env_args = {'var_call_ThomBnnXqw33mhC2UcbrP9Pq': ['business', 'checkin'], 'var_call_Bt8qt7Tbvo8qIlzFI0WsTFJx': ['review', 'tip', 'user'], 'var_call_RlBzaAIrwIMVGbXZcA3U0mbp': 'file_storage/call_RlBzaAIrwIMVGbXZcA3U0mbp.json', 'var_call_K5uga7CpcssDzri9cSlPotX7': 'file_storage/call_K5uga7CpcssDzri9cSlPotX7.json'}

exec(code, env_args)
