code = """import json
import pandas as pd

# Load data
with open(var_call_44ZjECz4jsmP2YagpmhQJh6f, 'r') as f:
    businesses = json.load(f)
with open(var_call_JBiogo0sXTh4HbhR1iAOCGnQ, 'r') as f:
    reviews = json.load(f)

bdf = pd.DataFrame(businesses)
rdf = pd.DataFrame(reviews)

# Ensure columns exist
if 'attributes' not in bdf.columns:
    bdf['attributes'] = None
if 'categories' not in bdf.columns:
    bdf['categories'] = None

# Credit acceptance check
def accepts_credit(attrs):
    if attrs is None:
        return False
    if isinstance(attrs, dict):
        val = attrs.get('BusinessAcceptsCreditCards')
        if val is None:
            return False
        return str(val).strip().lower() == 'true'
    s = str(attrs)
    low = s.lower()
    if 'businessacceptscreditcards' in low:
        # look for true/false in nearby text
        idx = low.find('businessacceptscreditcards')
        snippet = low[idx: idx+80]
        if 'true' in snippet:
            return True
        if 'false' in snippet:
            return False
        # fallback: if any 'true' in whole string
        if 'true' in low:
            return True
    # fallback
    return False

# Categories parser
def parse_categories(cat):
    if cat is None:
        return []
    if isinstance(cat, list):
        return [c.strip() for c in cat if c]
    s = str(cat).strip()
    if s.lower() == 'none' or s == '':
        return []
    parts = [p.strip() for p in s.split(',') if p.strip()]
    return parts

bdf['accepts_credit'] = bdf['attributes'].apply(accepts_credit)
bdf['categories_list'] = bdf['categories'].apply(parse_categories)

# map business_id to business_ref
bdf['business_ref'] = bdf['business_id'].apply(lambda x: x.replace('businessid_', 'businessref_') if isinstance(x, str) else None)

credit_biz = bdf[bdf['accepts_credit'] == True].copy()

# build mapping
biz_cat = {}
for _, row in credit_biz.iterrows():
    br = row['business_ref']
    cats = row['categories_list'] if isinstance(row['categories_list'], list) else []
    if br is not None:
        biz_cat[br] = cats

# process reviews
rdf = rdf[rdf['business_ref'].notnull()].copy()
rdf['rating'] = pd.to_numeric(rdf['rating'], errors='coerce')

rdf_credit = rdf[rdf['business_ref'].isin(biz_cat.keys())].copy()

# map categories onto reviews
rdf_credit['categories'] = rdf_credit['business_ref'].map(biz_cat)
rdf_credit = rdf_credit[rdf_credit['categories'].map(lambda x: bool(x))].copy()

if not rdf_credit.empty:
    rdf_exploded = rdf_credit.explode('categories')
    rdf_exploded['categories'] = rdf_exploded['categories'].astype(str).str.strip()
else:
    rdf_exploded = pd.DataFrame(columns=['business_ref','rating','categories'])

# count unique businesses per category among credit-accepting
from collections import defaultdict
cat_to_bizset = defaultdict(set)
for br, cats in biz_cat.items():
    for c in cats:
        c2 = c.strip()
        if c2:
            cat_to_bizset[c2].add(br)

cat_counts = {c: len(s) for c, s in cat_to_bizset.items()}

results = []
if cat_counts:
    if not rdf_exploded.empty:
        cat_group = rdf_exploded.groupby('categories')['rating'].agg(['mean','count']).reset_index()
    else:
        cat_group = pd.DataFrame(columns=['categories','mean','count'])

    for c, cnt in cat_counts.items():
        mean_row = cat_group[cat_group['categories'] == c]
        mean = None
        review_count = 0
        if not mean_row.empty:
            mean = float(round(mean_row['mean'].iloc[0], 3))
            review_count = int(mean_row['count'].iloc[0])
        results.append({'category': c, 'business_count': int(cnt), 'avg_rating': mean, 'num_reviews': review_count})

if not results:
    out = {'category': None, 'business_count': 0, 'avg_rating': None}
else:
    res_df = pd.DataFrame(results)
    max_count = res_df['business_count'].max()
    candidates = res_df[res_df['business_count'] == max_count].copy()
    candidates['avg_rating_fill'] = candidates['avg_rating'].fillna(-1)
    best = candidates.sort_values(['avg_rating_fill','category'], ascending=[False, True]).iloc[0]
    out = {'category': best['category'], 'business_count': int(best['business_count']), 'avg_rating': None if pd.isna(best['avg_rating']) else float(best['avg_rating'])}

print("__RESULT__:")
print(json.dumps(out))"""

env_args = {'var_call_44ZjECz4jsmP2YagpmhQJh6f': 'file_storage/call_44ZjECz4jsmP2YagpmhQJh6f.json', 'var_call_JBiogo0sXTh4HbhR1iAOCGnQ': 'file_storage/call_JBiogo0sXTh4HbhR1iAOCGnQ.json'}

exec(code, env_args)
