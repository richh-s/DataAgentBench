code = """import json, pandas as pd

def load_records(x):
    if isinstance(x, str):
        with open(x, 'r', encoding='utf-8') as f:
            return json.load(f)
    return x

biz_cc = load_records(var_call_zFqYe8IgQAOsB0c13wdNksBr)
rev = load_records(var_call_NEyKRqrdCnyirx61N25lLFTi)

biz_df = pd.DataFrame(biz_cc)
# infer category from attributes: use key "categories" if present else "Restaurants" if any Restaurants* keys else "Other"
attr = biz_df['attributes'].apply(lambda d: d if isinstance(d, dict) else {})

def infer_category(d):
    if not isinstance(d, dict):
        return 'Other'
    if 'categories' in d and d['categories'] not in (None, '', 'None'):
        return str(d['categories'])
    if any(str(k).startswith('Restaurants') for k in d.keys()):
        return 'Restaurants'
    if any(k in d for k in ['AcceptsInsurance','ByAppointmentOnly']):
        return 'Services'
    return 'Other'

biz_df['category'] = attr.apply(infer_category)

# map businessid_ -> businessref_
biz_df['business_ref'] = biz_df['business_id'].astype(str).str.replace('businessid_','businessref_', regex=False)

rev_df = pd.DataFrame(rev)
rev_df['rating'] = pd.to_numeric(rev_df['rating'], errors='coerce')

# only businesses that accept credit cards
cc_refs = set(biz_df['business_ref'].dropna().unique())
rev_df = rev_df[rev_df['business_ref'].isin(cc_refs)]

# counts of businesses per category among cc
cat_counts = biz_df.groupby('category')['business_id'].nunique().reset_index(name='business_count')

df = biz_df[['business_ref','category']].drop_duplicates()
merged = rev_df.merge(df, on='business_ref', how='inner')
cat_rating = merged.groupby('category')['rating'].mean().reset_index(name='avg_rating')

out = cat_counts.merge(cat_rating, on='category', how='left')
out = out.sort_values(['business_count','avg_rating'], ascending=[False, False])
row = out.iloc[0].to_dict()
row['avg_rating'] = None if pd.isna(row['avg_rating']) else float(row['avg_rating'])
row['business_count'] = int(row['business_count'])

result = json.dumps(row)
print('__RESULT__:')
print(result)"""

env_args = {'var_call_zFqYe8IgQAOsB0c13wdNksBr': 'file_storage/call_zFqYe8IgQAOsB0c13wdNksBr.json', 'var_call_NEyKRqrdCnyirx61N25lLFTi': 'file_storage/call_NEyKRqrdCnyirx61N25lLFTi.json'}

exec(code, env_args)
