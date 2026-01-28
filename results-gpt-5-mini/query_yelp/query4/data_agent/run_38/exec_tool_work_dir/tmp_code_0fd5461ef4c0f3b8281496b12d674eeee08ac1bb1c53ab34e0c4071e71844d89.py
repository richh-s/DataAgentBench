code = """import json
import pandas as pd

# Load data
with open(var_call_5vnOh8AuoRlDoxaH2LJA4BnY, 'r') as f:
    businesses = json.load(f)
with open(var_call_VFqrAgjYogQR7lq5ElNsE2Jt, 'r') as f:
    reviews = json.load(f)

# DataFrames
df_b = pd.DataFrame(businesses)
df_r = pd.DataFrame(reviews)

# Ensure columns
if 'description' not in df_b.columns:
    df_b['description'] = None
if 'attributes' not in df_b.columns:
    df_b['attributes'] = None

# Extract categories from description
import re

def extract_cats(desc):
    if not isinstance(desc, str):
        return []
    patterns = [r'offers a range of services in (.+?)(\.|$)',
                r'offers a range of services including (.+?)(\.|$)',
                r'category of (.+?)(\.|$)',
                r'offering a range of services (?:in|including)? (.+?)(\.|$)']
    for pat in patterns:
        m = re.search(pat, desc, flags=re.IGNORECASE)
        if m:
            cats_str = m.group(1)
            parts = [p.strip() for p in re.split(r',| and | & |;|/', cats_str) if p.strip()]
            return parts
    return []

# Determine acceptance of credit cards
def accepts_cc(attr):
    if attr is None:
        return False
    if isinstance(attr, str):
        if attr.strip().lower()=='none':
            return False
        s = attr.lower()
        return 'businessacceptscreditcards' in s and 'true' in s
    if isinstance(attr, dict):
        v = attr.get('BusinessAcceptsCreditCards')
        if v is None:
            return False
        return str(v).lower().find('true')!=-1
    return False

# Apply
df_b['categories_list'] = df_b['description'].apply(extract_cats)
# Keep only businesses that accept credit cards
df_b['accepts_cc'] = df_b['attributes'].apply(accepts_cc)
cc_b = df_b[df_b['accepts_cc']].copy()

# Explode categories and clean
cc_b_expl = cc_b[['business_id','categories_list']].explode('categories_list')
# Remove empty/None/'nan' after explode
cc_b_expl['categories_list'] = cc_b_expl['categories_list'].where(cc_b_expl['categories_list'].notna(), None)
cc_b_expl = cc_b_expl[cc_b_expl['categories_list'].apply(lambda x: isinstance(x,str) and x.strip().lower() not in ('', 'none', 'nan'))]

# If a business has no extracted category (i.e., not in cc_b_expl), we cannot assign it to a category; ignore those

# Prepare reviews
if 'business_ref' not in df_r.columns:
    df_r['business_ref'] = None
if 'rating' not in df_r.columns:
    df_r['rating'] = None
else:
    df_r['rating'] = pd.to_numeric(df_r['rating'], errors='coerce')

# Map business_id to business_ref
def to_ref(bid):
    if not isinstance(bid, str):
        return None
    if '_' in bid:
        return 'businessref_' + bid.split('_',1)[1]
    return None

cc_b_expl['business_ref'] = cc_b_expl['business_id'].apply(to_ref)

# Merge with reviews
merged = pd.merge(cc_b_expl, df_r, on='business_ref', how='left')

# Compute unique business count per category
biz_counts = cc_b_expl.groupby('categories_list')['business_id'].nunique().rename('business_count')
# Compute average rating per category using merged ratings (ignoring NaN)
avg_ratings = merged.groupby('categories_list')['rating'].mean().rename('avg_rating')

summary = pd.concat([biz_counts, avg_ratings], axis=1).reset_index().rename(columns={'categories_list':'category'})
# Drop rows where category is None or empty
summary = summary[summary['category'].apply(lambda x: isinstance(x,str) and x.strip()!='')]

# If no categories found, return empty
if summary.shape[0]==0:
    result = {'category': None, 'business_count': 0, 'average_rating': None}
else:
    # Get max business_count
    max_count = int(summary['business_count'].max())
    candidates = summary[summary['business_count']==max_count].copy()
    # If multiple, choose the one with highest avg_rating (treat NaN as -inf)
    candidates['avg_fill'] = candidates['avg_rating'].fillna(-999)
    candidates = candidates.sort_values(['avg_fill','category'], ascending=[False, True])
    top = candidates.iloc[0]
    avg = None if pd.isna(top['avg_rating']) else float(round(top['avg_rating'],3))
    result = {'category': top['category'], 'business_count': int(top['business_count']), 'average_rating': avg}

print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_call_hXzUi1HOyrj3924Zuuu4nlzl': ['business', 'checkin'], 'var_call_Vx7f3xeQCmMRh0NWNG3HKaZW': ['review', 'tip', 'user'], 'var_call_O9KyZjGrIpkwN2nC1wIjqtqU': 'file_storage/call_O9KyZjGrIpkwN2nC1wIjqtqU.json', 'var_call_VFqrAgjYogQR7lq5ElNsE2Jt': 'file_storage/call_VFqrAgjYogQR7lq5ElNsE2Jt.json', 'var_call_HPQ5bAnzRSDUt6FM5hMjLm5U': {'category': None, 'business_count': 0, 'average_rating': None}, 'var_call_BDiaUSol9ihcL5p6YpXrFGSA': {'columns': ['business_id', 'name', 'attributes'], 'col_counts': {'business_id': 100, 'name': 100, 'attributes': 100}, 'categories_nonempty_count': 0, 'attributes_nonempty_count': 100, 'total_businesses': 100}, 'var_call_5vnOh8AuoRlDoxaH2LJA4BnY': 'file_storage/call_5vnOh8AuoRlDoxaH2LJA4BnY.json', 'var_call_8YD73Vi5BjJBwwICTK1ifAWM': {'total_businesses': 100, 'businesses_with_extracted_categories': 17}, 'var_call_ndlQUckcxstYi4u21USTmvcb': {'category': 'nan', 'business_count': 61, 'average_rating': 3.569}}

exec(code, env_args)
