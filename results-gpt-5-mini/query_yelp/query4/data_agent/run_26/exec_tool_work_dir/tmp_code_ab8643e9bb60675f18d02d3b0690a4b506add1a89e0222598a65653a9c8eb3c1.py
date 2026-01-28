code = """import json
import pandas as pd

# Read JSON results from storage file paths
b_path = var_call_0Ioc9rMhjiImYfuDCvN3Uwm6
r_path = var_call_6MN17eUATOGx111pe3StyhUD

with open(b_path, 'rb') as f:
    b_text = f.read().decode('utf-8', errors='replace')
with open(r_path, 'rb') as f:
    r_text = f.read().decode('utf-8', errors='replace')

businesses = json.loads(b_text)
reviews = json.loads(r_text)

# DataFrames
df_b = pd.DataFrame(businesses)
df_r = pd.DataFrame(reviews)

# Normalize attributes
import re

def accepts_credit(attributes):
    if attributes is None:
        return False
    if isinstance(attributes, dict):
        val = attributes.get('BusinessAcceptsCreditCards')
        return val is True or str(val) == 'True'
    if isinstance(attributes, str):
        s = attributes.strip()
        if s.lower() == 'none':
            return False
        # search for BusinessAcceptsCreditCards and True
        if 'BusinessAcceptsCreditCards' in s:
            # if True appears after key, consider True
            if 'True' in s:
                return True
            if "'True'" in s or '"True"' in s:
                return True
            # also check for True without quotes
            m = re.search(r"BusinessAcceptsCreditCards\W*(True|False)", s)
            if m:
                return m.group(1) == 'True'
    return False

if 'attributes' not in df_b.columns:
    df_b['attributes'] = None

df_b['accepts_cc'] = df_b['attributes'].apply(accepts_credit)

# categories parsing
def parse_categories(cat):
    if cat is None:
        return []
    if isinstance(cat, list):
        return [c.strip() for c in cat if c]
    if isinstance(cat, str):
        parts = [c.strip() for c in cat.split(',')]
        return [p for p in parts if p]
    return []

if 'categories' not in df_b.columns:
    df_b['categories'] = None

# create business_ref
if 'business_id' in df_b.columns:
    df_b['business_ref'] = df_b['business_id'].str.replace('businessid_', 'businessref_')
else:
    df_b['business_ref'] = None

# Filter CC
df_cc = df_b[df_b['accepts_cc'] == True].copy()

# Expand categories
df_cc['category_list'] = df_cc['categories'].apply(parse_categories)

# Explode
if not df_cc.empty:
    df_expl = df_cc[['business_id', 'business_ref', 'category_list']].explode('category_list')
    df_expl = df_expl[df_expl['category_list'].notna() & (df_expl['category_list'] != '')]
else:
    df_expl = pd.DataFrame(columns=['business_id','business_ref','category_list'])

# Count unique businesses per category
biz_count = df_expl.groupby('category_list')['business_id'].nunique().reset_index()
if not biz_count.empty:
    biz_count = biz_count.rename(columns={'business_id': 'business_count', 'category_list': 'category'})
else:
    biz_count = pd.DataFrame(columns=['category','business_count'])

# Prepare reviews
if 'rating' in df_r.columns:
    df_r['rating'] = pd.to_numeric(df_r['rating'], errors='coerce')
else:
    df_r['rating'] = None

# Merge to compute average rating per category
if not df_expl.empty and not df_r.empty:
    merged = pd.merge(df_expl, df_r, on='business_ref', how='left')
    avg_rating = merged.groupby('category_list')['rating'].mean().reset_index()
    avg_rating = avg_rating.rename(columns={'category_list': 'category', 'rating': 'average_rating'})
else:
    avg_rating = pd.DataFrame(columns=['category','average_rating'])

# Combine
summary = pd.merge(biz_count, avg_rating, on='category', how='left')
summary['average_rating'] = summary['average_rating'].apply(lambda x: None if pd.isna(x) else float(x))

# Determine top category
if summary.empty:
    result = {'category': None, 'business_count': 0, 'average_rating': None}
else:
    top = summary.sort_values(['business_count', 'average_rating'], ascending=[False, False]).iloc[0]
    result = {'category': top['category'], 'business_count': int(top['business_count']), 'average_rating': (round(top['average_rating'], 2) if top['average_rating'] is not None else None)}

print("__RESULT__:")
print(json.dumps(result))"""

env_args = {'var_call_TLLD5knH0l6gGexALt0meO7T': 'file_storage/call_TLLD5knH0l6gGexALt0meO7T.json', 'var_call_0Ioc9rMhjiImYfuDCvN3Uwm6': 'file_storage/call_0Ioc9rMhjiImYfuDCvN3Uwm6.json', 'var_call_6MN17eUATOGx111pe3StyhUD': 'file_storage/call_6MN17eUATOGx111pe3StyhUD.json'}

exec(code, env_args)
