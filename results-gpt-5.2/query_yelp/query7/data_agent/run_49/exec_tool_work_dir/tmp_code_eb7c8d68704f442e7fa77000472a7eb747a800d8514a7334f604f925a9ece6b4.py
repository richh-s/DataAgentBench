code = """import json, pandas as pd

reviews = pd.DataFrame(var_call_RwpekRE00jHYMN2rs6jKYS6Z)
# ensure numeric
reviews['review_cnt'] = reviews['review_cnt'].astype(int)
# map businessref_ -> businessid_
reviews['business_id'] = reviews['business_ref'].str.replace('businessref_', 'businessid_', regex=False)

biz = pd.DataFrame(var_call_2FkxMWLPIoxnsdbIzV5ea9KS)
# categories not present; fall back to 'Unknown'
cat_col = None
for c in ['categories','category']:
    if c in biz.columns:
        cat_col = c
        break
if cat_col is None:
    biz['category_list'] = [['Unknown'] for _ in range(len(biz))]
else:
    def to_list(v):
        if v is None or (isinstance(v,float) and pd.isna(v)):
            return ['Unknown']
        if isinstance(v,list):
            return v if v else ['Unknown']
        if isinstance(v,str):
            # split comma-separated
            parts = [p.strip() for p in v.split(',') if p.strip()]
            return parts if parts else ['Unknown']
        return ['Unknown']
    biz['category_list'] = biz[cat_col].apply(to_list)

merged = reviews.merge(biz[['business_id','category_list']], on='business_id', how='left')
merged['category_list'] = merged['category_list'].apply(lambda v: v if isinstance(v,list) else ['Unknown'])

# explode categories and sum reviews
exploded = merged.explode('category_list')
agg = exploded.groupby('category_list', as_index=False)['review_cnt'].sum().sort_values('review_cnt', ascending=False)

top5 = agg.head(5)
result = top5.to_dict(orient='records')
print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_call_AakYCUpp6D9W3XJNzvcSpr6Y': ['review', 'tip', 'user'], 'var_call_4tK9h3f5bY1PyRX4RM9jcQH0': ['business', 'checkin'], 'var_call_meQ13RxgUW9GUx2iemoHeWL9': [{'business_id': 'businessid_49', 'name': 'Steps to Learning Montessori Preschool'}, {'business_id': 'businessid_47', 'name': 'Breeze Blow Dry Bar'}, {'business_id': 'businessid_88', 'name': 'Impact Guns'}, {'business_id': 'businessid_41', 'name': 'Palms Primary Care'}, {'business_id': 'businessid_33', 'name': 'J&Q Nails'}], 'var_call_RwpekRE00jHYMN2rs6jKYS6Z': [{'business_ref': 'businessref_13', 'review_cnt': '1'}, {'business_ref': 'businessref_79', 'review_cnt': '1'}, {'business_ref': 'businessref_6', 'review_cnt': '1'}, {'business_ref': 'businessref_15', 'review_cnt': '1'}, {'business_ref': 'businessref_33', 'review_cnt': '2'}, {'business_ref': 'businessref_36', 'review_cnt': '2'}, {'business_ref': 'businessref_60', 'review_cnt': '2'}, {'business_ref': 'businessref_12', 'review_cnt': '1'}, {'business_ref': 'businessref_31', 'review_cnt': '1'}, {'business_ref': 'businessref_74', 'review_cnt': '2'}, {'business_ref': 'businessref_66', 'review_cnt': '2'}, {'business_ref': 'businessref_53', 'review_cnt': '1'}, {'business_ref': 'businessref_57', 'review_cnt': '2'}, {'business_ref': 'businessref_86', 'review_cnt': '1'}, {'business_ref': 'businessref_62', 'review_cnt': '1'}, {'business_ref': 'businessref_37', 'review_cnt': '1'}, {'business_ref': 'businessref_92', 'review_cnt': '2'}, {'business_ref': 'businessref_26', 'review_cnt': '1'}, {'business_ref': 'businessref_68', 'review_cnt': '1'}, {'business_ref': 'businessref_41', 'review_cnt': '1'}, {'business_ref': 'businessref_10', 'review_cnt': '1'}, {'business_ref': 'businessref_45', 'review_cnt': '3'}, {'business_ref': 'businessref_96', 'review_cnt': '2'}, {'business_ref': 'businessref_98', 'review_cnt': '1'}, {'business_ref': 'businessref_14', 'review_cnt': '1'}, {'business_ref': 'businessref_20', 'review_cnt': '1'}], 'var_call_H0Nx2JwFDX7kNL2FLwxAjfvc': [{'business_id': 'businessid_49'}, {'business_id': 'businessid_47'}, {'business_id': 'businessid_88'}, {'business_id': 'businessid_41'}, {'business_id': 'businessid_33'}, {'business_id': 'businessid_74'}, {'business_id': 'businessid_92'}, {'business_id': 'businessid_64'}, {'business_id': 'businessid_52'}, {'business_id': 'businessid_29'}, {'business_id': 'businessid_10'}, {'business_id': 'businessid_61'}, {'business_id': 'businessid_54'}, {'business_id': 'businessid_8'}, {'business_id': 'businessid_59'}, {'business_id': 'businessid_91'}, {'business_id': 'businessid_83'}, {'business_id': 'businessid_93'}, {'business_id': 'businessid_1'}, {'business_id': 'businessid_24'}, {'business_id': 'businessid_95'}, {'business_id': 'businessid_50'}, {'business_id': 'businessid_26'}, {'business_id': 'businessid_84'}, {'business_id': 'businessid_89'}, {'business_id': 'businessid_32'}, {'business_id': 'businessid_70'}, {'business_id': 'businessid_42'}, {'business_id': 'businessid_71'}, {'business_id': 'businessid_97'}, {'business_id': 'businessid_14'}, {'business_id': 'businessid_3'}, {'business_id': 'businessid_35'}, {'business_id': 'businessid_28'}, {'business_id': 'businessid_57'}, {'business_id': 'businessid_27'}, {'business_id': 'businessid_75'}, {'business_id': 'businessid_34'}, {'business_id': 'businessid_2'}, {'business_id': 'businessid_19'}, {'business_id': 'businessid_48'}, {'business_id': 'businessid_67'}, {'business_id': 'businessid_7'}, {'business_id': 'businessid_51'}, {'business_id': 'businessid_76'}, {'business_id': 'businessid_100'}, {'business_id': 'businessid_5'}, {'business_id': 'businessid_63'}, {'business_id': 'businessid_45'}, {'business_id': 'businessid_68'}, {'business_id': 'businessid_6'}, {'business_id': 'businessid_87'}, {'business_id': 'businessid_78'}, {'business_id': 'businessid_79'}, {'business_id': 'businessid_66'}, {'business_id': 'businessid_55'}, {'business_id': 'businessid_30'}, {'business_id': 'businessid_80'}, {'business_id': 'businessid_15'}, {'business_id': 'businessid_96'}, {'business_id': 'businessid_11'}, {'business_id': 'businessid_73'}, {'business_id': 'businessid_4'}, {'business_id': 'businessid_77'}, {'business_id': 'businessid_18'}, {'business_id': 'businessid_65'}, {'business_id': 'businessid_86'}, {'business_id': 'businessid_53'}, {'business_id': 'businessid_40'}, {'business_id': 'businessid_44'}, {'business_id': 'businessid_43'}, {'business_id': 'businessid_72'}, {'business_id': 'businessid_9'}, {'business_id': 'businessid_20'}, {'business_id': 'businessid_37'}, {'business_id': 'businessid_56'}, {'business_id': 'businessid_62'}, {'business_id': 'businessid_94'}, {'business_id': 'businessid_39'}, {'business_id': 'businessid_90'}, {'business_id': 'businessid_31'}, {'business_id': 'businessid_85'}, {'business_id': 'businessid_25'}, {'business_id': 'businessid_82'}, {'business_id': 'businessid_58'}, {'business_id': 'businessid_12'}, {'business_id': 'businessid_99'}, {'business_id': 'businessid_60'}, {'business_id': 'businessid_21'}, {'business_id': 'businessid_98'}, {'business_id': 'businessid_16'}, {'business_id': 'businessid_46'}, {'business_id': 'businessid_22'}, {'business_id': 'businessid_36'}, {'business_id': 'businessid_69'}, {'business_id': 'businessid_23'}, {'business_id': 'businessid_38'}, {'business_id': 'businessid_81'}, {'business_id': 'businessid_13'}, {'business_id': 'businessid_17'}], 'var_call_2FkxMWLPIoxnsdbIzV5ea9KS': [{'business_id': 'businessid_41'}, {'business_id': 'businessid_33'}, {'business_id': 'businessid_74'}, {'business_id': 'businessid_92'}, {'business_id': 'businessid_10'}, {'business_id': 'businessid_26'}, {'business_id': 'businessid_14'}, {'business_id': 'businessid_57'}, {'business_id': 'businessid_45'}, {'business_id': 'businessid_68'}, {'business_id': 'businessid_6'}, {'business_id': 'businessid_79'}, {'business_id': 'businessid_66'}, {'business_id': 'businessid_15'}, {'business_id': 'businessid_96'}, {'business_id': 'businessid_86'}, {'business_id': 'businessid_53'}, {'business_id': 'businessid_20'}, {'business_id': 'businessid_37'}, {'business_id': 'businessid_62'}, {'business_id': 'businessid_31'}, {'business_id': 'businessid_12'}, {'business_id': 'businessid_60'}, {'business_id': 'businessid_98'}, {'business_id': 'businessid_36'}, {'business_id': 'businessid_13'}]}

exec(code, env_args)
