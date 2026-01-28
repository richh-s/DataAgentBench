code = """import json
import pandas as pd
with open(var_call_5vnOh8AuoRlDoxaH2LJA4BnY,'r') as f:
    businesses = json.load(f)
with open(var_call_VFqrAgjYogQR7lq5ElNsE2Jt,'r') as f:
    reviews = json.load(f)

# Dataframes
df_b = pd.DataFrame(businesses)
# Extract categories from description as before
import re

def extract_cats(desc):
    if not isinstance(desc, str):
        return []
    m = re.search(r'offers a range of services in (.+?)(\.|$)', desc, flags=re.IGNORECASE)
    if not m:
        m = re.search(r'offers a range of services including (.+?)(\.|$)', desc, flags=re.IGNORECASE)
    if not m:
        m = re.search(r'category of (.+?)(\.|$)', desc, flags=re.IGNORECASE)
    if not m:
        m = re.search(r'offering a range of services (?:in|including)? (.+?)(\.|$)', desc, flags=re.IGNORECASE)
    if not m:
        return []
    cats_str = m.group(1)
    parts = [p.strip() for p in re.split(r',| and | & |;|/', cats_str) if p.strip()]
    return parts

# attributes accept cc

def accepts_cc(attr):
    if attr is None:
        return False
    if isinstance(attr, str):
        if attr.lower() == 'none':
            return False
        return 'businessacceptscreditcards' in attr.lower() and 'true' in attr.lower()
    if isinstance(attr, dict):
        v = attr.get('BusinessAcceptsCreditCards')
        return str(v).lower().find('true')!=-1 if v is not None else False
    return False

# process
df_b['categories_list'] = df_b['description'].apply(extract_cats)
# explode

df_b_expl = df_b[['business_id','attributes','categories_list','name','description']].explode('categories_list')
# clean categories
if 'categories_list' in df_b_expl.columns:
    df_b_expl['categories_list'] = df_b_expl['categories_list'].astype(str).str.strip()
    df_b_expl = df_b_expl[df_b_expl['categories_list'].notna() & (df_b_expl['categories_list']!='')]

# accepts cc

df_b_expl['accepts_cc'] = df_b_expl['attributes'].apply(accepts_cc)

# Filter accept cc
cc_biz = df_b_expl[df_b_expl['accepts_cc']]

# Load reviews
df_r = pd.DataFrame(reviews)
df_r['rating'] = pd.to_numeric(df_r['rating'], errors='coerce')

# Map business_id to business_ref
cc_biz['business_ref'] = cc_biz['business_id'].apply(lambda x: 'businessref_'+x.split('_',1)[1] if isinstance(x,str) and '_' in x else None)

# Merge
merged = pd.merge(cc_biz, df_r, left_on='business_ref', right_on='business_ref', how='left')

# Compute unique business count per category
biz_counts = cc_biz.groupby('categories_list')['business_id'].nunique().rename('business_count')
avg_ratings = merged.groupby('categories_list')['rating'].mean().rename('avg_rating')
summary = pd.concat([biz_counts, avg_ratings], axis=1).reset_index().rename(columns={'categories_list':'category'})

# sort
summary = summary.sort_values('business_count', ascending=False)

# Prepare top
if summary.shape[0]==0:
    result = {}
else:
    top = summary.iloc[0]
    result = {'category': top['category'], 'business_count': int(top['business_count']), 'average_rating': None if pd.isna(top['avg_rating']) else float(round(top['avg_rating'],3))}

print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_call_hXzUi1HOyrj3924Zuuu4nlzl': ['business', 'checkin'], 'var_call_Vx7f3xeQCmMRh0NWNG3HKaZW': ['review', 'tip', 'user'], 'var_call_O9KyZjGrIpkwN2nC1wIjqtqU': 'file_storage/call_O9KyZjGrIpkwN2nC1wIjqtqU.json', 'var_call_VFqrAgjYogQR7lq5ElNsE2Jt': 'file_storage/call_VFqrAgjYogQR7lq5ElNsE2Jt.json', 'var_call_HPQ5bAnzRSDUt6FM5hMjLm5U': {'category': None, 'business_count': 0, 'average_rating': None}, 'var_call_BDiaUSol9ihcL5p6YpXrFGSA': {'columns': ['business_id', 'name', 'attributes'], 'col_counts': {'business_id': 100, 'name': 100, 'attributes': 100}, 'categories_nonempty_count': 0, 'attributes_nonempty_count': 100, 'total_businesses': 100}, 'var_call_5vnOh8AuoRlDoxaH2LJA4BnY': 'file_storage/call_5vnOh8AuoRlDoxaH2LJA4BnY.json', 'var_call_8YD73Vi5BjJBwwICTK1ifAWM': {'total_businesses': 100, 'businesses_with_extracted_categories': 17}}

exec(code, env_args)
