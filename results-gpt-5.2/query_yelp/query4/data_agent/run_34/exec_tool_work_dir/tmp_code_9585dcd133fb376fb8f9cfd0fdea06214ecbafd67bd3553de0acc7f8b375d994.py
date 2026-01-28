code = """import json, pandas as pd

# load biz cc flags (with attributes)
biz_cc_src = var_call_u79DblBtgt9zTxkOWnqpzGnp
if isinstance(biz_cc_src, str):
    with open(biz_cc_src,'r') as f:
        biz_cc = json.load(f)
else:
    biz_cc = biz_cc_src

# load biz categories-only
biz_cat = var_call_1MpBVT5fRSs2S2roX3TKNcpA

# load reviews
rev_src = var_call_nVPH8ykoGsk2YWKnfipQlivM
if isinstance(rev_src, str):
    with open(rev_src,'r') as f:
        rev = json.load(f)
else:
    rev = rev_src

biz_cc_df = pd.DataFrame(biz_cc)
biz_cat_df = pd.DataFrame(biz_cat)

# some documents may have categories embedded elsewhere; here categories missing entirely
# We'll treat business_id as its own 'category' placeholder so question can still be answered? No.
# Check if any categories present in dataset
has_cats = 'categories' in biz_cat_df.columns and biz_cat_df['categories'].notna().any()

# normalize accepts_cc

def accepts_cc(attrs):
    if attrs is None:
        return False
    if isinstance(attrs, float):
        return False
    if isinstance(attrs, str):
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
            return v.strip().lower()=='true'
    return False

biz_cc_df['accepts_cc'] = biz_cc_df['attributes'].apply(accepts_cc)
cc_ids = set(biz_cc_df.loc[biz_cc_df['accepts_cc'],'business_id'].dropna())

# prepare output error if no categories
if not has_cats:
    out = {
        "error": "Cannot compute business category: no 'categories' data present in business collection (field missing or all null).",
        "num_businesses_accepting_credit_cards": int(len(cc_ids))
    }
    print('__RESULT__:')
    print(json.dumps(out))
    raise SystemExit

# parse cats and compute as before

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

biz_cat_df['cat_list']=biz_cat_df['categories'].apply(parse_cats)
cc_cat_df = biz_cat_df[biz_cat_df['business_id'].isin(cc_ids)].copy()
cc_exploded = cc_cat_df[['business_id','cat_list']].explode('cat_list').rename(columns={'cat_list':'category'})
cc_exploded = cc_exploded[cc_exploded['category'].notna() & (cc_exploded['category']!='')]

cat_counts = cc_exploded.drop_duplicates().groupby('category')['business_id'].nunique().sort_values(ascending=False)
if cat_counts.empty:
    out = {"error":"No categories found among businesses accepting credit cards."}
    print('__RESULT__:')
    print(json.dumps(out))
    raise SystemExit

top_cat = cat_counts.index[0]
top_cat_n = int(cat_counts.iloc[0])

rev_df = pd.DataFrame(rev)
rev_df['rating']=pd.to_numeric(rev_df['rating'], errors='coerce')
rev_df['business_id']=rev_df['business_ref'].astype(str).str.replace('businessref_','businessid_', regex=False)

biz_ids_in_top = cc_exploded.loc[cc_exploded['category']==top_cat,'business_id'].unique().tolist()
avg_rating = float(rev_df[rev_df['business_id'].isin(biz_ids_in_top)]['rating'].mean())

out={"business_category":top_cat,"num_businesses_accepting_credit_cards":top_cat_n,"average_rating":avg_rating}
print('__RESULT__:')
print(json.dumps(out))"""

env_args = {'var_call_KiTlNpd1luNp8ySmhmptkVmV': [], 'var_call_nVPH8ykoGsk2YWKnfipQlivM': 'file_storage/call_nVPH8ykoGsk2YWKnfipQlivM.json', 'var_call_IQocTaOp77CnKEM2rqQyNEda': 'file_storage/call_IQocTaOp77CnKEM2rqQyNEda.json', 'var_call_6dabJSExEDWOJFm4NAvLzaDa': {'error': 'No businesses with credit card acceptance and categories found.'}, 'var_call_u79DblBtgt9zTxkOWnqpzGnp': 'file_storage/call_u79DblBtgt9zTxkOWnqpzGnp.json', 'var_call_1MpBVT5fRSs2S2roX3TKNcpA': [{'_id': '6859a000fe8b31cd7362e2ab', 'business_id': 'businessid_49'}, {'_id': '6859a000fe8b31cd7362e2ac', 'business_id': 'businessid_47'}, {'_id': '6859a000fe8b31cd7362e2ad', 'business_id': 'businessid_88'}, {'_id': '6859a000fe8b31cd7362e2ae', 'business_id': 'businessid_41'}, {'_id': '6859a000fe8b31cd7362e2af', 'business_id': 'businessid_33'}, {'_id': '6859a000fe8b31cd7362e2b0', 'business_id': 'businessid_74'}, {'_id': '6859a000fe8b31cd7362e2b1', 'business_id': 'businessid_92'}, {'_id': '6859a000fe8b31cd7362e2b2', 'business_id': 'businessid_64'}, {'_id': '6859a000fe8b31cd7362e2b3', 'business_id': 'businessid_52'}, {'_id': '6859a000fe8b31cd7362e2b4', 'business_id': 'businessid_29'}, {'_id': '6859a000fe8b31cd7362e2b5', 'business_id': 'businessid_10'}, {'_id': '6859a000fe8b31cd7362e2b6', 'business_id': 'businessid_61'}, {'_id': '6859a000fe8b31cd7362e2b7', 'business_id': 'businessid_54'}, {'_id': '6859a000fe8b31cd7362e2b8', 'business_id': 'businessid_8'}, {'_id': '6859a000fe8b31cd7362e2b9', 'business_id': 'businessid_59'}, {'_id': '6859a000fe8b31cd7362e2ba', 'business_id': 'businessid_91'}, {'_id': '6859a000fe8b31cd7362e2bb', 'business_id': 'businessid_83'}, {'_id': '6859a000fe8b31cd7362e2bc', 'business_id': 'businessid_93'}, {'_id': '6859a000fe8b31cd7362e2bd', 'business_id': 'businessid_1'}, {'_id': '6859a000fe8b31cd7362e2be', 'business_id': 'businessid_24'}, {'_id': '6859a000fe8b31cd7362e2bf', 'business_id': 'businessid_95'}, {'_id': '6859a000fe8b31cd7362e2c0', 'business_id': 'businessid_50'}, {'_id': '6859a000fe8b31cd7362e2c1', 'business_id': 'businessid_26'}, {'_id': '6859a000fe8b31cd7362e2c2', 'business_id': 'businessid_84'}, {'_id': '6859a000fe8b31cd7362e2c3', 'business_id': 'businessid_89'}, {'_id': '6859a000fe8b31cd7362e2c4', 'business_id': 'businessid_32'}, {'_id': '6859a000fe8b31cd7362e2c5', 'business_id': 'businessid_70'}, {'_id': '6859a000fe8b31cd7362e2c6', 'business_id': 'businessid_42'}, {'_id': '6859a000fe8b31cd7362e2c7', 'business_id': 'businessid_71'}, {'_id': '6859a000fe8b31cd7362e2c8', 'business_id': 'businessid_97'}, {'_id': '6859a000fe8b31cd7362e2c9', 'business_id': 'businessid_14'}, {'_id': '6859a000fe8b31cd7362e2ca', 'business_id': 'businessid_3'}, {'_id': '6859a000fe8b31cd7362e2cb', 'business_id': 'businessid_35'}, {'_id': '6859a000fe8b31cd7362e2cc', 'business_id': 'businessid_28'}, {'_id': '6859a000fe8b31cd7362e2cd', 'business_id': 'businessid_57'}, {'_id': '6859a000fe8b31cd7362e2ce', 'business_id': 'businessid_27'}, {'_id': '6859a000fe8b31cd7362e2cf', 'business_id': 'businessid_75'}, {'_id': '6859a000fe8b31cd7362e2d0', 'business_id': 'businessid_34'}, {'_id': '6859a000fe8b31cd7362e2d1', 'business_id': 'businessid_2'}, {'_id': '6859a000fe8b31cd7362e2d2', 'business_id': 'businessid_19'}, {'_id': '6859a000fe8b31cd7362e2d3', 'business_id': 'businessid_48'}, {'_id': '6859a000fe8b31cd7362e2d4', 'business_id': 'businessid_67'}, {'_id': '6859a000fe8b31cd7362e2d5', 'business_id': 'businessid_7'}, {'_id': '6859a000fe8b31cd7362e2d6', 'business_id': 'businessid_51'}, {'_id': '6859a000fe8b31cd7362e2d7', 'business_id': 'businessid_76'}, {'_id': '6859a000fe8b31cd7362e2d8', 'business_id': 'businessid_100'}, {'_id': '6859a000fe8b31cd7362e2d9', 'business_id': 'businessid_5'}, {'_id': '6859a000fe8b31cd7362e2da', 'business_id': 'businessid_63'}, {'_id': '6859a000fe8b31cd7362e2db', 'business_id': 'businessid_45'}, {'_id': '6859a000fe8b31cd7362e2dc', 'business_id': 'businessid_68'}, {'_id': '6859a000fe8b31cd7362e2dd', 'business_id': 'businessid_6'}, {'_id': '6859a000fe8b31cd7362e2de', 'business_id': 'businessid_87'}, {'_id': '6859a000fe8b31cd7362e2df', 'business_id': 'businessid_78'}, {'_id': '6859a000fe8b31cd7362e2e0', 'business_id': 'businessid_79'}, {'_id': '6859a000fe8b31cd7362e2e1', 'business_id': 'businessid_66'}, {'_id': '6859a000fe8b31cd7362e2e2', 'business_id': 'businessid_55'}, {'_id': '6859a000fe8b31cd7362e2e3', 'business_id': 'businessid_30'}, {'_id': '6859a000fe8b31cd7362e2e4', 'business_id': 'businessid_80'}, {'_id': '6859a000fe8b31cd7362e2e5', 'business_id': 'businessid_15'}, {'_id': '6859a000fe8b31cd7362e2e6', 'business_id': 'businessid_96'}, {'_id': '6859a000fe8b31cd7362e2e7', 'business_id': 'businessid_11'}, {'_id': '6859a000fe8b31cd7362e2e8', 'business_id': 'businessid_73'}, {'_id': '6859a000fe8b31cd7362e2e9', 'business_id': 'businessid_4'}, {'_id': '6859a000fe8b31cd7362e2ea', 'business_id': 'businessid_77'}, {'_id': '6859a000fe8b31cd7362e2eb', 'business_id': 'businessid_18'}, {'_id': '6859a000fe8b31cd7362e2ec', 'business_id': 'businessid_65'}, {'_id': '6859a000fe8b31cd7362e2ed', 'business_id': 'businessid_86'}, {'_id': '6859a000fe8b31cd7362e2ee', 'business_id': 'businessid_53'}, {'_id': '6859a000fe8b31cd7362e2ef', 'business_id': 'businessid_40'}, {'_id': '6859a000fe8b31cd7362e2f0', 'business_id': 'businessid_44'}, {'_id': '6859a000fe8b31cd7362e2f1', 'business_id': 'businessid_43'}, {'_id': '6859a000fe8b31cd7362e2f2', 'business_id': 'businessid_72'}, {'_id': '6859a000fe8b31cd7362e2f3', 'business_id': 'businessid_9'}, {'_id': '6859a000fe8b31cd7362e2f4', 'business_id': 'businessid_20'}, {'_id': '6859a000fe8b31cd7362e2f5', 'business_id': 'businessid_37'}, {'_id': '6859a000fe8b31cd7362e2f6', 'business_id': 'businessid_56'}, {'_id': '6859a000fe8b31cd7362e2f7', 'business_id': 'businessid_62'}, {'_id': '6859a000fe8b31cd7362e2f8', 'business_id': 'businessid_94'}, {'_id': '6859a000fe8b31cd7362e2f9', 'business_id': 'businessid_39'}, {'_id': '6859a000fe8b31cd7362e2fa', 'business_id': 'businessid_90'}, {'_id': '6859a000fe8b31cd7362e2fb', 'business_id': 'businessid_31'}, {'_id': '6859a000fe8b31cd7362e2fc', 'business_id': 'businessid_85'}, {'_id': '6859a000fe8b31cd7362e2fd', 'business_id': 'businessid_25'}, {'_id': '6859a000fe8b31cd7362e2fe', 'business_id': 'businessid_82'}, {'_id': '6859a000fe8b31cd7362e2ff', 'business_id': 'businessid_58'}, {'_id': '6859a000fe8b31cd7362e300', 'business_id': 'businessid_12'}, {'_id': '6859a000fe8b31cd7362e301', 'business_id': 'businessid_99'}, {'_id': '6859a000fe8b31cd7362e302', 'business_id': 'businessid_60'}, {'_id': '6859a000fe8b31cd7362e303', 'business_id': 'businessid_21'}, {'_id': '6859a000fe8b31cd7362e304', 'business_id': 'businessid_98'}, {'_id': '6859a000fe8b31cd7362e305', 'business_id': 'businessid_16'}, {'_id': '6859a000fe8b31cd7362e306', 'business_id': 'businessid_46'}, {'_id': '6859a000fe8b31cd7362e307', 'business_id': 'businessid_22'}, {'_id': '6859a000fe8b31cd7362e308', 'business_id': 'businessid_36'}, {'_id': '6859a000fe8b31cd7362e309', 'business_id': 'businessid_69'}, {'_id': '6859a000fe8b31cd7362e30a', 'business_id': 'businessid_23'}, {'_id': '6859a000fe8b31cd7362e30b', 'business_id': 'businessid_38'}, {'_id': '6859a000fe8b31cd7362e30c', 'business_id': 'businessid_81'}, {'_id': '6859a000fe8b31cd7362e30d', 'business_id': 'businessid_13'}, {'_id': '6859a000fe8b31cd7362e30e', 'business_id': 'businessid_17'}]}

exec(code, env_args)
