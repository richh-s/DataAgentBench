code = """import json, pandas as pd

business_credit = pd.DataFrame(var_call_PloZwB1AwpVDfo86e3xYrnP6)

with open(var_call_QQcX970zjv8tIHp6Hl9laqUF, 'r') as f:
    reviews = pd.DataFrame(json.load(f))

business_credit['category'] = 'All Categories'

business_credit['business_ref'] = business_credit['business_id'].str.replace('businessid_', 'businessref_', False)

reviews_subset = reviews.merge(business_credit[['business_ref', 'category']], on='business_ref', how='inner')

if reviews_subset.empty:
    result = {'business_category': None, 'num_businesses': 0, 'average_rating': None}
else:
    reviews_subset['rating'] = pd.to_numeric(reviews_subset['rating'])
    agg = reviews_subset.groupby('category').agg(num_businesses=('business_ref', 'nunique'), avg_rating=('rating', 'mean')).reset_index()
    max_row = agg.sort_values('num_businesses', ascending=False).iloc[0]
    result = {'business_category': max_row['category'], 'num_businesses': int(max_row['num_businesses']), 'average_rating': round(float(max_row['avg_rating']), 3)}

out = json.dumps(result)
print("__RESULT__:")
print(out)"""

env_args = {'var_call_LwiZdCbu04usohmm35vmIASB': [{'business_id': 'businessid_49'}, {'business_id': 'businessid_47'}, {'business_id': 'businessid_88'}, {'business_id': 'businessid_33'}, {'business_id': 'businessid_92'}], 'var_call_QQcX970zjv8tIHp6Hl9laqUF': 'file_storage/call_QQcX970zjv8tIHp6Hl9laqUF.json', 'var_call_PloZwB1AwpVDfo86e3xYrnP6': [{'business_id': 'businessid_49'}, {'business_id': 'businessid_47'}, {'business_id': 'businessid_88'}, {'business_id': 'businessid_33'}, {'business_id': 'businessid_92'}, {'business_id': 'businessid_64'}, {'business_id': 'businessid_52'}, {'business_id': 'businessid_29'}, {'business_id': 'businessid_10'}, {'business_id': 'businessid_61'}, {'business_id': 'businessid_54'}, {'business_id': 'businessid_8'}, {'business_id': 'businessid_91'}, {'business_id': 'businessid_83'}, {'business_id': 'businessid_93'}, {'business_id': 'businessid_24'}, {'business_id': 'businessid_95'}, {'business_id': 'businessid_26'}, {'business_id': 'businessid_84'}, {'business_id': 'businessid_89'}, {'business_id': 'businessid_32'}, {'business_id': 'businessid_71'}, {'business_id': 'businessid_97'}, {'business_id': 'businessid_14'}, {'business_id': 'businessid_3'}, {'business_id': 'businessid_27'}, {'business_id': 'businessid_75'}, {'business_id': 'businessid_2'}, {'business_id': 'businessid_48'}, {'business_id': 'businessid_67'}, {'business_id': 'businessid_76'}, {'business_id': 'businessid_100'}, {'business_id': 'businessid_63'}, {'business_id': 'businessid_45'}, {'business_id': 'businessid_68'}, {'business_id': 'businessid_6'}, {'business_id': 'businessid_87'}, {'business_id': 'businessid_66'}, {'business_id': 'businessid_55'}, {'business_id': 'businessid_30'}, {'business_id': 'businessid_15'}, {'business_id': 'businessid_96'}, {'business_id': 'businessid_11'}, {'business_id': 'businessid_73'}, {'business_id': 'businessid_4'}, {'business_id': 'businessid_77'}, {'business_id': 'businessid_18'}, {'business_id': 'businessid_65'}, {'business_id': 'businessid_86'}, {'business_id': 'businessid_53'}, {'business_id': 'businessid_40'}, {'business_id': 'businessid_44'}, {'business_id': 'businessid_43'}, {'business_id': 'businessid_9'}, {'business_id': 'businessid_20'}, {'business_id': 'businessid_37'}, {'business_id': 'businessid_62'}, {'business_id': 'businessid_94'}, {'business_id': 'businessid_90'}, {'business_id': 'businessid_31'}, {'business_id': 'businessid_85'}, {'business_id': 'businessid_25'}, {'business_id': 'businessid_82'}, {'business_id': 'businessid_58'}, {'business_id': 'businessid_60'}, {'business_id': 'businessid_21'}, {'business_id': 'businessid_98'}, {'business_id': 'businessid_16'}, {'business_id': 'businessid_46'}, {'business_id': 'businessid_22'}, {'business_id': 'businessid_36'}, {'business_id': 'businessid_38'}, {'business_id': 'businessid_81'}, {'business_id': 'businessid_13'}, {'business_id': 'businessid_17'}]}

exec(code, env_args)
