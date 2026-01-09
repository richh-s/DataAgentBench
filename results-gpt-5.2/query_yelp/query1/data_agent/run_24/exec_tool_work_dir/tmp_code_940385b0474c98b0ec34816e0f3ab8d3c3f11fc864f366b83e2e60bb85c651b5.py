code = """import json, pandas as pd
biz_in = pd.DataFrame(var_call_oUc4qtZq68an5uAGfrb1reJm)
# Map businessid_X -> businessref_X
biz_in['business_ref'] = biz_in['business_id'].str.replace('businessid_', 'businessref_', regex=False)
refs = biz_in['business_ref'].dropna().unique().tolist()
# Build SQL IN list safely (values are simple)
in_list = ','.join(["'"+r.replace("'","''")+"'" for r in refs])
sql = f"SELECT AVG(rating)::DOUBLE AS avg_rating, COUNT(*) AS n_reviews FROM review WHERE business_ref IN ({in_list});"
print('__RESULT__:')
print(json.dumps({'sql': sql, 'n_businesses': int(len(refs))}))"""

env_args = {'var_call_3ZCy6pxqRzuJgWRt0xD9SEg9': [], 'var_call_byhax28hmRcEdsYzesZDpbXc': [{'avg_rating': '3.515'}], 'var_call_oUc4qtZq68an5uAGfrb1reJm': [{'business_id': 'businessid_52'}, {'business_id': 'businessid_84'}, {'business_id': 'businessid_76'}, {'business_id': 'businessid_87'}, {'business_id': 'businessid_65'}, {'business_id': 'businessid_94'}, {'business_id': 'businessid_90'}, {'business_id': 'businessid_16'}]}

exec(code, env_args)
