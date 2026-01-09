code = """import json, pandas as pd

reviews = pd.DataFrame(var_call_9cicD5w3Nv2LUfvRQAPNpGYs)
biz = pd.DataFrame(var_call_B1R36VBe2H1lBhEviQkeiv0s)

if reviews.empty:
    out = []
else:
    reviews['n_reviews'] = reviews['n_reviews'].astype(int)
    # map businessref_ -> businessid_
    reviews['business_id'] = reviews['business_ref'].str.replace('businessref_', 'businessid_', regex=False)

    # categories field may be missing; treat as unknown
    if 'categories' not in biz.columns:
        biz['categories'] = None

    merged = reviews.merge(biz[['business_id','categories']], on='business_id', how='left')

    def to_cats(x):
        if x is None or (isinstance(x, float) and pd.isna(x)):
            return []
        if isinstance(x, list):
            return [str(c).strip() for c in x if str(c).strip()]
        # sometimes stored as comma-separated string
        s = str(x)
        return [c.strip() for c in s.split(',') if c.strip()]

    merged['cat_list'] = merged['categories'].apply(to_cats)
    exploded = merged.explode('cat_list')
    exploded = exploded[exploded['cat_list'].notna() & (exploded['cat_list']!='')]

    cat_counts = exploded.groupby('cat_list', as_index=False)['n_reviews'].sum().sort_values('n_reviews', ascending=False)
    out = cat_counts.head(5).to_dict(orient='records')

print('__RESULT__:')
print(json.dumps(out))"""

env_args = {'var_call_9cicD5w3Nv2LUfvRQAPNpGYs': [{'business_ref': 'businessref_13', 'n_reviews': '1'}, {'business_ref': 'businessref_79', 'n_reviews': '1'}, {'business_ref': 'businessref_74', 'n_reviews': '2'}, {'business_ref': 'businessref_66', 'n_reviews': '2'}, {'business_ref': 'businessref_15', 'n_reviews': '1'}, {'business_ref': 'businessref_33', 'n_reviews': '2'}, {'business_ref': 'businessref_6', 'n_reviews': '1'}, {'business_ref': 'businessref_31', 'n_reviews': '1'}, {'business_ref': 'businessref_53', 'n_reviews': '1'}, {'business_ref': 'businessref_57', 'n_reviews': '2'}, {'business_ref': 'businessref_86', 'n_reviews': '1'}, {'business_ref': 'businessref_62', 'n_reviews': '1'}, {'business_ref': 'businessref_37', 'n_reviews': '1'}, {'business_ref': 'businessref_26', 'n_reviews': '1'}, {'business_ref': 'businessref_68', 'n_reviews': '1'}, {'business_ref': 'businessref_41', 'n_reviews': '1'}, {'business_ref': 'businessref_10', 'n_reviews': '1'}, {'business_ref': 'businessref_45', 'n_reviews': '3'}, {'business_ref': 'businessref_92', 'n_reviews': '2'}, {'business_ref': 'businessref_36', 'n_reviews': '2'}, {'business_ref': 'businessref_60', 'n_reviews': '2'}, {'business_ref': 'businessref_12', 'n_reviews': '1'}, {'business_ref': 'businessref_96', 'n_reviews': '2'}, {'business_ref': 'businessref_98', 'n_reviews': '1'}, {'business_ref': 'businessref_14', 'n_reviews': '1'}, {'business_ref': 'businessref_20', 'n_reviews': '1'}], 'var_call_B1R36VBe2H1lBhEviQkeiv0s': [{'business_id': 'businessid_49'}, {'business_id': 'businessid_47'}, {'business_id': 'businessid_88'}, {'business_id': 'businessid_41'}, {'business_id': 'businessid_33'}, {'business_id': 'businessid_74'}, {'business_id': 'businessid_92'}, {'business_id': 'businessid_64'}, {'business_id': 'businessid_52'}, {'business_id': 'businessid_29'}, {'business_id': 'businessid_10'}, {'business_id': 'businessid_61'}, {'business_id': 'businessid_54'}, {'business_id': 'businessid_8'}, {'business_id': 'businessid_59'}, {'business_id': 'businessid_91'}, {'business_id': 'businessid_83'}, {'business_id': 'businessid_93'}, {'business_id': 'businessid_1'}, {'business_id': 'businessid_24'}, {'business_id': 'businessid_95'}, {'business_id': 'businessid_50'}, {'business_id': 'businessid_26'}, {'business_id': 'businessid_84'}, {'business_id': 'businessid_89'}, {'business_id': 'businessid_32'}, {'business_id': 'businessid_70'}, {'business_id': 'businessid_42'}, {'business_id': 'businessid_71'}, {'business_id': 'businessid_97'}, {'business_id': 'businessid_14'}, {'business_id': 'businessid_3'}, {'business_id': 'businessid_35'}, {'business_id': 'businessid_28'}, {'business_id': 'businessid_57'}, {'business_id': 'businessid_27'}, {'business_id': 'businessid_75'}, {'business_id': 'businessid_34'}, {'business_id': 'businessid_2'}, {'business_id': 'businessid_19'}, {'business_id': 'businessid_48'}, {'business_id': 'businessid_67'}, {'business_id': 'businessid_7'}, {'business_id': 'businessid_51'}, {'business_id': 'businessid_76'}, {'business_id': 'businessid_100'}, {'business_id': 'businessid_5'}, {'business_id': 'businessid_63'}, {'business_id': 'businessid_45'}, {'business_id': 'businessid_68'}, {'business_id': 'businessid_6'}, {'business_id': 'businessid_87'}, {'business_id': 'businessid_78'}, {'business_id': 'businessid_79'}, {'business_id': 'businessid_66'}, {'business_id': 'businessid_55'}, {'business_id': 'businessid_30'}, {'business_id': 'businessid_80'}, {'business_id': 'businessid_15'}, {'business_id': 'businessid_96'}, {'business_id': 'businessid_11'}, {'business_id': 'businessid_73'}, {'business_id': 'businessid_4'}, {'business_id': 'businessid_77'}, {'business_id': 'businessid_18'}, {'business_id': 'businessid_65'}, {'business_id': 'businessid_86'}, {'business_id': 'businessid_53'}, {'business_id': 'businessid_40'}, {'business_id': 'businessid_44'}, {'business_id': 'businessid_43'}, {'business_id': 'businessid_72'}, {'business_id': 'businessid_9'}, {'business_id': 'businessid_20'}, {'business_id': 'businessid_37'}, {'business_id': 'businessid_56'}, {'business_id': 'businessid_62'}, {'business_id': 'businessid_94'}, {'business_id': 'businessid_39'}, {'business_id': 'businessid_90'}, {'business_id': 'businessid_31'}, {'business_id': 'businessid_85'}, {'business_id': 'businessid_25'}, {'business_id': 'businessid_82'}, {'business_id': 'businessid_58'}, {'business_id': 'businessid_12'}, {'business_id': 'businessid_99'}, {'business_id': 'businessid_60'}, {'business_id': 'businessid_21'}, {'business_id': 'businessid_98'}, {'business_id': 'businessid_16'}, {'business_id': 'businessid_46'}, {'business_id': 'businessid_22'}, {'business_id': 'businessid_36'}, {'business_id': 'businessid_69'}, {'business_id': 'businessid_23'}, {'business_id': 'businessid_38'}, {'business_id': 'businessid_81'}, {'business_id': 'businessid_13'}, {'business_id': 'businessid_17'}]}

exec(code, env_args)
