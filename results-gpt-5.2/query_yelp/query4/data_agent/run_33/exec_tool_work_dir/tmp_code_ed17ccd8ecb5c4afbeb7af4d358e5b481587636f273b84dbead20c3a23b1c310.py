code = """import json, pandas as pd

path = var_call_WTf2y4JsqToZXWWhzgz2bk09
with open(path,'r') as f:
    rows = json.load(f)

df = pd.DataFrame(rows)

def extract_categories(desc):
    if not isinstance(desc,str):
        return []
    marker = 'categories of '
    if marker in desc:
        after = desc.split(marker,1)[1]
        # remove surrounding quotes and trailing punctuation
        after = after.strip()
        if after.startswith("'") and after.endswith("'."):
            after = after[1:-2]
        elif after.startswith("'") and after.endswith("'"):
            after = after[1:-1]
        after = after.strip().rstrip('.')
        return [c.strip() for c in after.split(',') if c.strip()]
    # otherwise look for 'including ...' list after 'including'
    if 'including' in desc:
        after = desc.split('including',1)[1]
        # truncate at 'and' phrase end
        after = after.replace('and',',')
        # stop at 'offering'
        if 'offering' in after:
            after = after.split('offering',1)[0]
        # remove trailing text
        after = after.strip().rstrip('.')
        # split by commas
        return [c.strip() for c in after.split(',') if c.strip()]
    return []

df['categories'] = df['description'].apply(extract_categories)
exp = df[['business_id','categories']].explode('categories')
exp = exp[exp['categories'].notna()]
exp['category']=exp['categories'].astype(str).str.strip()
exp=exp[exp['category']!='']

counts = exp.drop_duplicates(['business_id','category']).groupby('category')['business_id'].nunique().reset_index(name='business_count')
maxc = counts['business_count'].max() if not counts.empty else 0
top = counts[counts.business_count==maxc].sort_values('category').head(1)

rev_df = pd.DataFrame(var_call_HqCxWQSch4DVvkGjJzb49Gh8)
rev_df['avg_rating']=rev_df['avg_rating'].astype(float)

exp['business_ref']=exp['business_id'].str.replace('businessid_','businessref_', regex=False)
merged = exp.merge(rev_df[['business_ref','avg_rating']], on='business_ref', how='left')
cat_avg = merged.dropna(subset=['avg_rating']).drop_duplicates(['category','business_ref']).groupby('category')['avg_rating'].mean().reset_index(name='avg_rating')

if len(top)==0:
    res = {"category": None, "business_count": 0, "avg_rating": None}
else:
    cat = top.iloc[0]['category']
    bc = int(top.iloc[0]['business_count'])
    ar = cat_avg[cat_avg['category']==cat]['avg_rating']
    ar = None if ar.empty else float(ar.iloc[0])
    res = {"category": cat, "business_count": bc, "avg_rating": ar}

print('__RESULT__:')
print(json.dumps(res))"""

env_args = {'var_call_zbKv8dS6GctzwthY0shGYOqe': 'file_storage/call_zbKv8dS6GctzwthY0shGYOqe.json', 'var_call_HqCxWQSch4DVvkGjJzb49Gh8': [{'business_ref': 'businessref_47', 'avg_rating': '3.9047619047619047', 'review_cnt': '42'}, {'business_ref': 'businessref_16', 'avg_rating': '3.024390243902439', 'review_cnt': '41'}, {'business_ref': 'businessref_46', 'avg_rating': '4.181818181818182', 'review_cnt': '44'}, {'business_ref': 'businessref_91', 'avg_rating': '4.911111111111111', 'review_cnt': '45'}, {'business_ref': 'businessref_1', 'avg_rating': '4.333333333333333', 'review_cnt': '6'}, {'business_ref': 'businessref_55', 'avg_rating': '4.918918918918919', 'review_cnt': '37'}, {'business_ref': 'businessref_73', 'avg_rating': '5.0', 'review_cnt': '5'}, {'business_ref': 'businessref_6', 'avg_rating': '4.0', 'review_cnt': '37'}, {'business_ref': 'businessref_71', 'avg_rating': '3.268292682926829', 'review_cnt': '41'}, {'business_ref': 'businessref_38', 'avg_rating': '3.1176470588235294', 'review_cnt': '17'}, {'business_ref': 'businessref_32', 'avg_rating': '3.4285714285714284', 'review_cnt': '7'}, {'business_ref': 'businessref_30', 'avg_rating': '3.6', 'review_cnt': '5'}, {'business_ref': 'businessref_66', 'avg_rating': '2.1818181818181817', 'review_cnt': '44'}, {'business_ref': 'businessref_9', 'avg_rating': '4.435897435897436', 'review_cnt': '39'}, {'business_ref': 'businessref_25', 'avg_rating': '4.444444444444445', 'review_cnt': '36'}, {'business_ref': 'businessref_2', 'avg_rating': '4.769230769230769', 'review_cnt': '13'}, {'business_ref': 'businessref_74', 'avg_rating': '2.8333333333333335', 'review_cnt': '6'}, {'business_ref': 'businessref_59', 'avg_rating': '4.6', 'review_cnt': '30'}, {'business_ref': 'businessref_5', 'avg_rating': '1.6', 'review_cnt': '5'}, {'business_ref': 'businessref_29', 'avg_rating': '3.9047619047619047', 'review_cnt': '21'}, {'business_ref': 'businessref_58', 'avg_rating': '4.166666666666667', 'review_cnt': '6'}, {'business_ref': 'businessref_39', 'avg_rating': '4.125', 'review_cnt': '8'}, {'business_ref': 'businessref_100', 'avg_rating': '4.0', 'review_cnt': '4'}, {'business_ref': 'businessref_81', 'avg_rating': '3.6666666666666665', 'review_cnt': '6'}, {'business_ref': 'businessref_93', 'avg_rating': '2.857142857142857', 'review_cnt': '7'}, {'business_ref': 'businessref_67', 'avg_rating': '3.3260869565217392', 'review_cnt': '46'}, {'business_ref': 'businessref_15', 'avg_rating': '3.5294117647058822', 'review_cnt': '17'}, {'business_ref': 'businessref_54', 'avg_rating': '3.5', 'review_cnt': '10'}, {'business_ref': 'businessref_33', 'avg_rating': '3.5217391304347827', 'review_cnt': '23'}, {'business_ref': 'businessref_89', 'avg_rating': '3.04', 'review_cnt': '25'}, {'business_ref': 'businessref_24', 'avg_rating': '3.289473684210526', 'review_cnt': '38'}, {'business_ref': 'businessref_36', 'avg_rating': '4.090909090909091', 'review_cnt': '44'}, {'business_ref': 'businessref_12', 'avg_rating': '3.730769230769231', 'review_cnt': '26'}, {'business_ref': 'businessref_60', 'avg_rating': '2.0', 'review_cnt': '32'}, {'business_ref': 'businessref_52', 'avg_rating': '4.166666666666667', 'review_cnt': '6'}, {'business_ref': 'businessref_31', 'avg_rating': '1.5', 'review_cnt': '14'}, {'business_ref': 'businessref_78', 'avg_rating': '5.0', 'review_cnt': '6'}, {'business_ref': 'businessref_99', 'avg_rating': '3.2', 'review_cnt': '5'}, {'business_ref': 'businessref_51', 'avg_rating': '3.9714285714285715', 'review_cnt': '35'}, {'business_ref': 'businessref_53', 'avg_rating': '3.7142857142857144', 'review_cnt': '7'}, {'business_ref': 'businessref_80', 'avg_rating': '1.8888888888888888', 'review_cnt': '9'}, {'business_ref': 'businessref_19', 'avg_rating': '3.3333333333333335', 'review_cnt': '6'}, {'business_ref': 'businessref_57', 'avg_rating': '1.9047619047619047', 'review_cnt': '42'}, {'business_ref': 'businessref_85', 'avg_rating': '3.3863636363636362', 'review_cnt': '44'}, {'business_ref': 'businessref_86', 'avg_rating': '3.739130434782609', 'review_cnt': '46'}, {'business_ref': 'businessref_37', 'avg_rating': '3.2083333333333335', 'review_cnt': '24'}, {'business_ref': 'businessref_42', 'avg_rating': '4.083333333333333', 'review_cnt': '12'}, {'business_ref': 'businessref_97', 'avg_rating': '4.294117647058823', 'review_cnt': '17'}, {'business_ref': 'businessref_8', 'avg_rating': '2.8222222222222224', 'review_cnt': '45'}, {'business_ref': 'businessref_90', 'avg_rating': '1.0', 'review_cnt': '3'}, {'business_ref': 'businessref_72', 'avg_rating': '4.6', 'review_cnt': '5'}, {'business_ref': 'businessref_56', 'avg_rating': '2.3333333333333335', 'review_cnt': '6'}, {'business_ref': 'businessref_62', 'avg_rating': '3.0', 'review_cnt': '7'}, {'business_ref': 'businessref_95', 'avg_rating': '2.1666666666666665', 'review_cnt': '6'}, {'business_ref': 'businessref_40', 'avg_rating': '4.476190476190476', 'review_cnt': '21'}, {'business_ref': 'businessref_61', 'avg_rating': '2.4705882352941178', 'review_cnt': '17'}, {'business_ref': 'businessref_92', 'avg_rating': '4.575757575757576', 'review_cnt': '33'}, {'business_ref': 'businessref_94', 'avg_rating': '4.066666666666666', 'review_cnt': '30'}, {'business_ref': 'businessref_7', 'avg_rating': '3.75', 'review_cnt': '16'}, {'business_ref': 'businessref_63', 'avg_rating': '2.8333333333333335', 'review_cnt': '6'}, {'business_ref': 'businessref_83', 'avg_rating': '4.833333333333333', 'review_cnt': '6'}, {'business_ref': 'businessref_34', 'avg_rating': '3.3333333333333335', 'review_cnt': '9'}, {'business_ref': 'businessref_21', 'avg_rating': '2.0285714285714285', 'review_cnt': '35'}, {'business_ref': 'businessref_26', 'avg_rating': '1.7083333333333333', 'review_cnt': '24'}, {'business_ref': 'businessref_68', 'avg_rating': '1.7619047619047619', 'review_cnt': '21'}, {'business_ref': 'businessref_88', 'avg_rating': '3.212121212121212', 'review_cnt': '33'}, {'business_ref': 'businessref_65', 'avg_rating': '3.8333333333333335', 'review_cnt': '18'}, {'business_ref': 'businessref_4', 'avg_rating': '5.0', 'review_cnt': '7'}, {'business_ref': 'businessref_43', 'avg_rating': '3.0476190476190474', 'review_cnt': '21'}, {'business_ref': 'businessref_48', 'avg_rating': '3.3846153846153846', 'review_cnt': '13'}, {'business_ref': 'businessref_17', 'avg_rating': '3.9', 'review_cnt': '10'}, {'business_ref': 'businessref_64', 'avg_rating': '3.7142857142857144', 'review_cnt': '7'}, {'business_ref': 'businessref_10', 'avg_rating': '4.1875', 'review_cnt': '16'}, {'business_ref': 'businessref_23', 'avg_rating': '3.4444444444444446', 'review_cnt': '9'}, {'business_ref': 'businessref_49', 'avg_rating': '4.166666666666667', 'review_cnt': '6'}, {'business_ref': 'businessref_84', 'avg_rating': '5.0', 'review_cnt': '4'}, {'business_ref': 'businessref_11', 'avg_rating': '4.2', 'review_cnt': '10'}, {'business_ref': 'businessref_41', 'avg_rating': '4.0', 'review_cnt': '4'}, {'business_ref': 'businessref_77', 'avg_rating': '2.5476190476190474', 'review_cnt': '42'}, {'business_ref': 'businessref_27', 'avg_rating': '3.3214285714285716', 'review_cnt': '28'}, {'business_ref': 'businessref_50', 'avg_rating': '2.4285714285714284', 'review_cnt': '7'}, {'business_ref': 'businessref_76', 'avg_rating': '3.5555555555555554', 'review_cnt': '9'}, {'business_ref': 'businessref_75', 'avg_rating': '4.0', 'review_cnt': '5'}, {'business_ref': 'businessref_82', 'avg_rating': '4.309523809523809', 'review_cnt': '42'}, {'business_ref': 'businessref_35', 'avg_rating': '4.125', 'review_cnt': '8'}, {'business_ref': 'businessref_45', 'avg_rating': '3.3863636363636362', 'review_cnt': '44'}, {'business_ref': 'businessref_96', 'avg_rating': '3.8863636363636362', 'review_cnt': '44'}, {'business_ref': 'businessref_22', 'avg_rating': '2.8181818181818183', 'review_cnt': '11'}, {'business_ref': 'businessref_20', 'avg_rating': '3.2142857142857144', 'review_cnt': '42'}, {'business_ref': 'businessref_18', 'avg_rating': '1.8181818181818181', 'review_cnt': '11'}, {'business_ref': 'businessref_14', 'avg_rating': '3.4', 'review_cnt': '25'}, {'business_ref': 'businessref_3', 'avg_rating': '2.0', 'review_cnt': '4'}, {'business_ref': 'businessref_69', 'avg_rating': '4.222222222222222', 'review_cnt': '9'}, {'business_ref': 'businessref_98', 'avg_rating': '1.2', 'review_cnt': '5'}, {'business_ref': 'businessref_28', 'avg_rating': '4.055555555555555', 'review_cnt': '18'}, {'business_ref': 'businessref_70', 'avg_rating': '4.777777777777778', 'review_cnt': '9'}, {'business_ref': 'businessref_79', 'avg_rating': '4.627906976744186', 'review_cnt': '43'}, {'business_ref': 'businessref_44', 'avg_rating': '2.9285714285714284', 'review_cnt': '42'}, {'business_ref': 'businessref_13', 'avg_rating': '3.9166666666666665', 'review_cnt': '12'}, {'business_ref': 'businessref_87', 'avg_rating': '3.3333333333333335', 'review_cnt': '6'}], 'var_call_MVerqjXWBw1Kl1Jb2hL7SCBL': {'category': None, 'business_count': 0, 'avg_rating': None}, 'var_call_WTf2y4JsqToZXWWhzgz2bk09': 'file_storage/call_WTf2y4JsqToZXWWhzgz2bk09.json'}

exec(code, env_args)
