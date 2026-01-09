code = """import json, pandas as pd

# load business records
biz_src = var_call_IQocTaOp77CnKEM2rqQyNEda
if isinstance(biz_src, str):
    with open(biz_src, 'r') as f:
        biz = json.load(f)
else:
    biz = biz_src

# load reviews
rev_src = var_call_nVPH8ykoGsk2YWKnfipQlivM
if isinstance(rev_src, str):
    with open(rev_src, 'r') as f:
        rev = json.load(f)
else:
    rev = rev_src

biz_df = pd.DataFrame(biz)
if 'categories' not in biz_df.columns:
    biz_df['categories'] = None

# normalize accepts credit cards

def accepts_cc(attrs):
    if attrs is None:
        return False
    if isinstance(attrs, str):
        # many rows have "None" as string
        if attrs.strip().lower() in ['none','null','nan','']:
            return False
        return False
    if isinstance(attrs, dict):
        v = attrs.get('BusinessAcceptsCreditCards')
        if v is None:
            return False
        if isinstance(v, bool):
            return v
        if isinstance(v, str):
            return v.strip().lower() == 'true'
    return False

biz_df['accepts_cc'] = biz_df['attributes'].apply(accepts_cc)
cc_biz = biz_df[biz_df['accepts_cc']].copy()

# parse categories field into list

def parse_cats(c):
    if c is None:
        return []
    if isinstance(c, list):
        return [str(x).strip() for x in c if str(x).strip()]
    if isinstance(c, str):
        s=c.strip()
        if not s or s.lower() in ['none','null']:
            return []
        return [x.strip() for x in s.split(',') if x.strip()]
    return []

cc_biz['cat_list'] = cc_biz['categories'].apply(parse_cats)
cc_exploded = cc_biz[['business_id','cat_list']].explode('cat_list').rename(columns={'cat_list':'category'})
cc_exploded = cc_exploded[cc_exploded['category'].notna() & (cc_exploded['category']!='')]

# count businesses per category (unique businesses)
cat_counts = cc_exploded.drop_duplicates().groupby('category')['business_id'].nunique().sort_values(ascending=False)

if cat_counts.empty:
    out = {"error":"No businesses with credit card acceptance and categories found."}
    print('__RESULT__:')
    print(json.dumps(out))
    raise SystemExit

top_cat = cat_counts.index[0]
top_cat_n = int(cat_counts.iloc[0])

# compute avg rating for businesses in that category among cc-accepting
rev_df = pd.DataFrame(rev)
rev_df['rating'] = pd.to_numeric(rev_df['rating'], errors='coerce')
# map businessref_ -> businessid_
rev_df['business_id'] = rev_df['business_ref'].astype(str).str.replace('businessref_','businessid_', regex=False)

biz_ids_in_top_cat = cc_exploded.loc[cc_exploded['category']==top_cat,'business_id'].dropna().unique().tolist()
ratings = rev_df[rev_df['business_id'].isin(biz_ids_in_top_cat)]['rating'].dropna()
avg_rating = float(ratings.mean()) if len(ratings) else None

out = {"business_category": top_cat, "num_businesses_accepting_credit_cards": top_cat_n, "average_rating": avg_rating}
print('__RESULT__:')
print(json.dumps(out))"""

env_args = {'var_call_KiTlNpd1luNp8ySmhmptkVmV': [], 'var_call_nVPH8ykoGsk2YWKnfipQlivM': 'file_storage/call_nVPH8ykoGsk2YWKnfipQlivM.json', 'var_call_IQocTaOp77CnKEM2rqQyNEda': 'file_storage/call_IQocTaOp77CnKEM2rqQyNEda.json'}

exec(code, env_args)
