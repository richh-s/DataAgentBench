code = """import json, pandas as pd

# Load businesses with credit cards
biz_src = var_call_zcSBwm7rtW8L1n12hIzeoziz
if isinstance(biz_src, str):
    with open(biz_src, 'r') as f:
        biz = json.load(f)
else:
    biz = biz_src

# Load reviews
rev_src = var_call_6DIOdi4zSqwTnNdtRHIRCVD6
if isinstance(rev_src, str):
    with open(rev_src, 'r') as f:
        reviews = json.load(f)
else:
    reviews = rev_src

biz_df = pd.DataFrame(biz)
# categories may be missing; ignore null
if 'categories' in biz_df.columns:
    cats = biz_df[['business_id','categories']].copy()
else:
    cats = biz_df[['business_id']].copy()
    cats['categories'] = None

# explode categories: assume comma-separated string
cats['categories'] = cats['categories'].fillna('')
cats['category_list'] = cats['categories'].apply(lambda x: [c.strip() for c in x.split(',') if c.strip()])
expl = cats[['business_id','category_list']].explode('category_list')
expl = expl.rename(columns={'category_list':'category'})
expl = expl[expl['category'].notna() & (expl['category']!='')]

# Count businesses per category (unique businesses)
cat_counts = expl.drop_duplicates(['business_id','category']).groupby('category')['business_id'].nunique().reset_index(name='business_count')

# Determine max category
if len(cat_counts)==0:
    result = {"category": None, "business_count": 0, "average_rating": None}
else:
    top_row = cat_counts.sort_values(['business_count','category'], ascending=[False, True]).iloc[0]
    top_cat = top_row['category']

    # Map businessid_ -> businessref_
    top_biz_ids = expl.loc[expl['category']==top_cat, 'business_id'].dropna().unique().tolist()
    top_biz_refs = ['businessref_' + bid.split('businessid_',1)[1] if bid.startswith('businessid_') else bid for bid in top_biz_ids]

    rev_df = pd.DataFrame(reviews)
    rev_df['rating'] = pd.to_numeric(rev_df['rating'], errors='coerce')
    avg_rating = rev_df[rev_df['business_ref'].isin(top_biz_refs)]['rating'].mean()
    avg_rating = None if pd.isna(avg_rating) else float(avg_rating)

    result = {"category": top_cat, "business_count": int(top_row['business_count']), "average_rating": avg_rating}

print("__RESULT__:")
print(json.dumps(result))"""

env_args = {'var_call_KwykIv3Zn3OEIYXXtvoTsYCf': [], 'var_call_6DIOdi4zSqwTnNdtRHIRCVD6': 'file_storage/call_6DIOdi4zSqwTnNdtRHIRCVD6.json', 'var_call_zcSBwm7rtW8L1n12hIzeoziz': 'file_storage/call_zcSBwm7rtW8L1n12hIzeoziz.json'}

exec(code, env_args)
