code = """import json
import re
import pandas as pd

# Load data from storage variables
with open(var_call_44ZjECz4jsmP2YagpmhQJh6f, 'r') as f:
    businesses = json.load(f)
with open(var_call_JBiogo0sXTh4HbhR1iAOCGnQ, 'r') as f:
    reviews = json.load(f)

bdf = pd.DataFrame(businesses)
rdf = pd.DataFrame(reviews)

# Ensure columns
if 'attributes' not in bdf.columns:
    bdf['attributes'] = None
if 'categories' not in bdf.columns:
    bdf['categories'] = None

# Function to detect credit card acceptance
def accepts_credit(attrs):
    if attrs is None:
        return False
    # dict case
    if isinstance(attrs, dict):
        val = attrs.get('BusinessAcceptsCreditCards')
        if val is None:
            return False
        try:
            return str(val).strip().lower() == 'true'
        except:
            return False
    # string case
    s = str(attrs)
    if s.strip().lower() == 'none':
        return False
    # try regex to find explicit True/False
    m = re.search(r"BusinessAcceptsCreditCards\W*[:=]\W*'?\"?(True|False)'?\"?", s, flags=re.IGNORECASE)
    if m:
        return m.group(1).lower() == 'true'
    # fallback: check both keywords present
    if 'BusinessAcceptsCreditCards' in s and 'true' in s.lower():
        return True
    return False

# categories parsing
def parse_categories(cat):
    if cat is None:
        return []
    if isinstance(cat, list):
        return [c.strip() for c in cat if c]
    s = str(cat).strip()
    if s.lower() == 'none' or s == '':
        return []
    # split by comma
    parts = [p.strip() for p in s.split(',') if p.strip()]
    return parts

bdf['accepts_credit'] = bdf['attributes'].apply(accepts_credit)

bdf['categories_list'] = bdf['categories'].apply(parse_categories)

# map business_id to business_ref
def to_ref(bid):
    if not isinstance(bid, str):
        return None
    return bid.replace('businessid_', 'businessref_')

bdf['business_ref'] = bdf['business_id'].apply(to_ref)

# Filter credit-accepting businesses
credit_biz = bdf[bdf['accepts_credit'] == True].copy()

# Build mapping business_ref -> categories_list
biz_cat = {}
for _, row in credit_biz.iterrows():
    br = row['business_ref']
    cats = row['categories_list'] if isinstance(row['categories_list'], list) else []
    if br is not None:
        biz_cat[br] = cats

# Process reviews
rdf = rdf[rdf['business_ref'].notnull()].copy()
# rating numeric
rdf['rating'] = pd.to_numeric(rdf['rating'], errors='coerce')

# Filter reviews for businesses that accept credit cards
rdf_credit = rdf[rdf['business_ref'].isin(biz_cat.keys())].copy()

# Map categories onto reviews
rdf_credit['categories'] = rdf_credit['business_ref'].map(biz_cat)
# drop reviews where business has no categories
rdf_credit = rdf_credit[rdf_credit['categories'].map(lambda x: bool(x))].copy()

# explode categories
rdf_exploded = rdf_credit.explode('categories')
if not rdf_exploded.empty:
    rdf_exploded['categories'] = rdf_exploded['categories'].astype(str).str.strip()

# count unique businesses per category among credit-accepting
from collections import defaultdict
cat_to_bizset = defaultdict(set)
for br, cats in biz_cat.items():
    for c in cats:
        c2 = c.strip()
        if c2:
            cat_to_bizset[c2].add(br)

cat_counts = {c: len(s) for c, s in cat_to_bizset.items()}

# average rating per category from exploded reviews
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

# select best category
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
