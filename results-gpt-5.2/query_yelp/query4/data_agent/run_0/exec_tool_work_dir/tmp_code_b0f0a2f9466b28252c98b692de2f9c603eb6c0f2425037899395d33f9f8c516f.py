code = """import json, pandas as pd

biz = pd.DataFrame(var_call_znkVZ5adAl6McDvkRUlcp6a0)
# normalize attributes

def accepts(v):
    if v is None or (isinstance(v,float) and pd.isna(v)):
        return False
    if isinstance(v, dict):
        v = v.get('BusinessAcceptsCreditCards')
    if v is None:
        return False
    if isinstance(v, bool):
        return v
    if isinstance(v, (int, float)):
        return v == 1
    if isinstance(v, str):
        return v.strip().lower() in {'true','1','yes','y','t'}
    return False

biz['accepts_cc'] = biz['attributes'].apply(accepts)
# categories may be missing in sample; treat missing as 'Unknown'
biz['categories'] = biz.get('categories', pd.Series([None]*len(biz)))

cc_biz = biz[biz['accepts_cc']].copy()

# explode categories

def split_cats(x):
    if x is None or (isinstance(x,float) and pd.isna(x)):
        return ['Unknown']
    if isinstance(x, list):
        return [str(i).strip() for i in x if str(i).strip()] or ['Unknown']
    if isinstance(x, str):
        # common yelp format: comma-separated
        parts = [p.strip() for p in x.split(',')]
        parts = [p for p in parts if p]
        return parts or ['Unknown']
    return ['Unknown']

cc_biz['category'] = cc_biz['categories'].apply(split_cats)
cc_exploded = cc_biz[['business_id','category']].explode('category')

# counts per category
counts = cc_exploded.groupby('category', as_index=False).agg(business_count=('business_id','nunique'))
# pick max count; tie-breaker alphabetical
max_count = counts['business_count'].max() if len(counts) else 0
cands = counts[counts['business_count']==max_count].sort_values('category')
if len(cands)==0:
    out = {'category': None, 'business_count': 0, 'average_rating': None}
else:
    top_cat = cands.iloc[0]['category']
    top_biz_ids = cc_exploded[cc_exploded['category']==top_cat]['business_id'].unique().tolist()
    # map businessid_ -> businessref_
    top_biz_refs = [bid.replace('businessid_','businessref_') for bid in top_biz_ids]
    ratings = pd.DataFrame(var_call_2sdD1NxrA3LDaY0NezQkEojb)
    ratings['avg_rating'] = ratings['avg_rating'].astype(float)
    cat_ratings = ratings[ratings['business_ref'].isin(top_biz_refs)]
    avg_rating = float(cat_ratings['avg_rating'].mean()) if len(cat_ratings) else None
    out = {'category': top_cat, 'business_count': int(max_count), 'average_rating': avg_rating}

print('__RESULT__:')
print(json.dumps(out))"""

env_args = {'var_call_WHWIQd6I5hnhRJAMKbwWGt1i': [{'business_id': 'businessid_49'}, {'business_id': 'businessid_47'}, {'business_id': 'businessid_88'}, {'business_id': 'businessid_33'}, {'business_id': 'businessid_92'}], 'var_call_znkVZ5adAl6McDvkRUlcp6a0': [{'business_id': 'businessid_49', 'attributes': {'BusinessAcceptsCreditCards': 'True'}}, {'business_id': 'businessid_47', 'attributes': {'BusinessAcceptsCreditCards': 'True'}}, {'business_id': 'businessid_88', 'attributes': {'BusinessAcceptsCreditCards': 'True'}}, {'business_id': 'businessid_41', 'attributes': 'nan'}, {'business_id': 'businessid_33', 'attributes': {'BusinessAcceptsCreditCards': 'True'}}], 'var_call_2sdD1NxrA3LDaY0NezQkEojb': [{'business_ref': 'businessref_47', 'avg_rating': '3.9047619047619047'}, {'business_ref': 'businessref_16', 'avg_rating': '3.024390243902439'}, {'business_ref': 'businessref_46', 'avg_rating': '4.181818181818182'}, {'business_ref': 'businessref_91', 'avg_rating': '4.911111111111111'}, {'business_ref': 'businessref_1', 'avg_rating': '4.333333333333333'}, {'business_ref': 'businessref_55', 'avg_rating': '4.918918918918919'}, {'business_ref': 'businessref_73', 'avg_rating': '5.0'}, {'business_ref': 'businessref_6', 'avg_rating': '4.0'}, {'business_ref': 'businessref_71', 'avg_rating': '3.268292682926829'}, {'business_ref': 'businessref_38', 'avg_rating': '3.1176470588235294'}, {'business_ref': 'businessref_32', 'avg_rating': '3.4285714285714284'}, {'business_ref': 'businessref_30', 'avg_rating': '3.6'}, {'business_ref': 'businessref_66', 'avg_rating': '2.1818181818181817'}, {'business_ref': 'businessref_9', 'avg_rating': '4.435897435897436'}, {'business_ref': 'businessref_25', 'avg_rating': '4.444444444444445'}, {'business_ref': 'businessref_2', 'avg_rating': '4.769230769230769'}, {'business_ref': 'businessref_74', 'avg_rating': '2.8333333333333335'}, {'business_ref': 'businessref_59', 'avg_rating': '4.6'}, {'business_ref': 'businessref_5', 'avg_rating': '1.6'}, {'business_ref': 'businessref_29', 'avg_rating': '3.9047619047619047'}, {'business_ref': 'businessref_58', 'avg_rating': '4.166666666666667'}, {'business_ref': 'businessref_39', 'avg_rating': '4.125'}, {'business_ref': 'businessref_100', 'avg_rating': '4.0'}, {'business_ref': 'businessref_81', 'avg_rating': '3.6666666666666665'}, {'business_ref': 'businessref_93', 'avg_rating': '2.857142857142857'}, {'business_ref': 'businessref_67', 'avg_rating': '3.3260869565217392'}, {'business_ref': 'businessref_15', 'avg_rating': '3.5294117647058822'}, {'business_ref': 'businessref_54', 'avg_rating': '3.5'}, {'business_ref': 'businessref_33', 'avg_rating': '3.5217391304347827'}, {'business_ref': 'businessref_89', 'avg_rating': '3.04'}, {'business_ref': 'businessref_24', 'avg_rating': '3.289473684210526'}, {'business_ref': 'businessref_36', 'avg_rating': '4.090909090909091'}, {'business_ref': 'businessref_12', 'avg_rating': '3.730769230769231'}, {'business_ref': 'businessref_60', 'avg_rating': '2.0'}, {'business_ref': 'businessref_52', 'avg_rating': '4.166666666666667'}, {'business_ref': 'businessref_43', 'avg_rating': '3.0476190476190474'}, {'business_ref': 'businessref_48', 'avg_rating': '3.3846153846153846'}, {'business_ref': 'businessref_17', 'avg_rating': '3.9'}, {'business_ref': 'businessref_31', 'avg_rating': '1.5'}, {'business_ref': 'businessref_78', 'avg_rating': '5.0'}, {'business_ref': 'businessref_99', 'avg_rating': '3.2'}, {'business_ref': 'businessref_51', 'avg_rating': '3.9714285714285715'}, {'business_ref': 'businessref_53', 'avg_rating': '3.7142857142857144'}, {'business_ref': 'businessref_80', 'avg_rating': '1.8888888888888888'}, {'business_ref': 'businessref_19', 'avg_rating': '3.3333333333333335'}, {'business_ref': 'businessref_57', 'avg_rating': '1.9047619047619047'}, {'business_ref': 'businessref_85', 'avg_rating': '3.3863636363636362'}, {'business_ref': 'businessref_86', 'avg_rating': '3.739130434782609'}, {'business_ref': 'businessref_37', 'avg_rating': '3.2083333333333335'}, {'business_ref': 'businessref_42', 'avg_rating': '4.083333333333333'}, {'business_ref': 'businessref_97', 'avg_rating': '4.294117647058823'}, {'business_ref': 'businessref_8', 'avg_rating': '2.8222222222222224'}, {'business_ref': 'businessref_90', 'avg_rating': '1.0'}, {'business_ref': 'businessref_72', 'avg_rating': '4.6'}, {'business_ref': 'businessref_56', 'avg_rating': '2.3333333333333335'}, {'business_ref': 'businessref_62', 'avg_rating': '3.0'}, {'business_ref': 'businessref_95', 'avg_rating': '2.1666666666666665'}, {'business_ref': 'businessref_40', 'avg_rating': '4.476190476190476'}, {'business_ref': 'businessref_61', 'avg_rating': '2.4705882352941178'}, {'business_ref': 'businessref_92', 'avg_rating': '4.575757575757576'}, {'business_ref': 'businessref_94', 'avg_rating': '4.066666666666666'}, {'business_ref': 'businessref_7', 'avg_rating': '3.75'}, {'business_ref': 'businessref_63', 'avg_rating': '2.8333333333333335'}, {'business_ref': 'businessref_83', 'avg_rating': '4.833333333333333'}, {'business_ref': 'businessref_34', 'avg_rating': '3.3333333333333335'}, {'business_ref': 'businessref_21', 'avg_rating': '2.0285714285714285'}, {'business_ref': 'businessref_26', 'avg_rating': '1.7083333333333333'}, {'business_ref': 'businessref_68', 'avg_rating': '1.7619047619047619'}, {'business_ref': 'businessref_88', 'avg_rating': '3.212121212121212'}, {'business_ref': 'businessref_65', 'avg_rating': '3.8333333333333335'}, {'business_ref': 'businessref_4', 'avg_rating': '5.0'}, {'business_ref': 'businessref_64', 'avg_rating': '3.7142857142857144'}, {'business_ref': 'businessref_10', 'avg_rating': '4.1875'}, {'business_ref': 'businessref_23', 'avg_rating': '3.4444444444444446'}, {'business_ref': 'businessref_49', 'avg_rating': '4.166666666666667'}, {'business_ref': 'businessref_84', 'avg_rating': '5.0'}, {'business_ref': 'businessref_11', 'avg_rating': '4.2'}, {'business_ref': 'businessref_41', 'avg_rating': '4.0'}, {'business_ref': 'businessref_82', 'avg_rating': '4.309523809523809'}, {'business_ref': 'businessref_35', 'avg_rating': '4.125'}, {'business_ref': 'businessref_45', 'avg_rating': '3.3863636363636362'}, {'business_ref': 'businessref_77', 'avg_rating': '2.5476190476190474'}, {'business_ref': 'businessref_27', 'avg_rating': '3.3214285714285716'}, {'business_ref': 'businessref_50', 'avg_rating': '2.4285714285714284'}, {'business_ref': 'businessref_76', 'avg_rating': '3.5555555555555554'}, {'business_ref': 'businessref_75', 'avg_rating': '4.0'}, {'business_ref': 'businessref_96', 'avg_rating': '3.8863636363636362'}, {'business_ref': 'businessref_22', 'avg_rating': '2.8181818181818183'}, {'business_ref': 'businessref_20', 'avg_rating': '3.2142857142857144'}, {'business_ref': 'businessref_18', 'avg_rating': '1.8181818181818181'}, {'business_ref': 'businessref_14', 'avg_rating': '3.4'}, {'business_ref': 'businessref_3', 'avg_rating': '2.0'}, {'business_ref': 'businessref_69', 'avg_rating': '4.222222222222222'}, {'business_ref': 'businessref_98', 'avg_rating': '1.2'}, {'business_ref': 'businessref_28', 'avg_rating': '4.055555555555555'}, {'business_ref': 'businessref_70', 'avg_rating': '4.777777777777778'}, {'business_ref': 'businessref_79', 'avg_rating': '4.627906976744186'}, {'business_ref': 'businessref_44', 'avg_rating': '2.9285714285714284'}, {'business_ref': 'businessref_13', 'avg_rating': '3.9166666666666665'}, {'business_ref': 'businessref_87', 'avg_rating': '3.3333333333333335'}]}

exec(code, env_args)
