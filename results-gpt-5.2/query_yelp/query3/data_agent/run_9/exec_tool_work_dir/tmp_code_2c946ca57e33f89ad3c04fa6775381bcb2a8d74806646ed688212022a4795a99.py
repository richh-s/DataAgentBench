code = """import json, pandas as pd

reviews = pd.DataFrame(var_call_rcD989qnQqLxuKpT43Az2koI)
refs = set(reviews['business_ref'].tolist())

# load full mongo result
path = var_call_UtQFjsyho25mMjZcpUmuD69D
with open(path, 'r') as f:
    biz_recs = json.load(f)

biz_df = pd.DataFrame(biz_recs)
# Map businessid_X -> businessref_X
biz_df['business_ref'] = biz_df['business_id'].str.replace('businessid_', 'businessref_', regex=False)

count = int(biz_df[biz_df['business_ref'].isin(refs)]['business_ref'].nunique())

out = json.dumps({'count': count})
print('__RESULT__:')
print(out)"""

env_args = {'var_call_rcD989qnQqLxuKpT43Az2koI': [{'business_ref': 'businessref_91'}, {'business_ref': 'businessref_46'}, {'business_ref': 'businessref_47'}, {'business_ref': 'businessref_73'}, {'business_ref': 'businessref_59'}, {'business_ref': 'businessref_13'}, {'business_ref': 'businessref_79'}, {'business_ref': 'businessref_67'}, {'business_ref': 'businessref_15'}, {'business_ref': 'businessref_17'}, {'business_ref': 'businessref_43'}, {'business_ref': 'businessref_66'}, {'business_ref': 'businessref_25'}, {'business_ref': 'businessref_99'}, {'business_ref': 'businessref_80'}, {'business_ref': 'businessref_86'}, {'business_ref': 'businessref_62'}, {'business_ref': 'businessref_8'}, {'business_ref': 'businessref_57'}, {'business_ref': 'businessref_37'}, {'business_ref': 'businessref_82'}, {'business_ref': 'businessref_35'}, {'business_ref': 'businessref_45'}, {'business_ref': 'businessref_77'}, {'business_ref': 'businessref_27'}, {'business_ref': 'businessref_20'}, {'business_ref': 'businessref_22'}, {'business_ref': 'businessref_14'}, {'business_ref': 'businessref_28'}, {'business_ref': 'businessref_24'}, {'business_ref': 'businessref_36'}, {'business_ref': 'businessref_40'}, {'business_ref': 'businessref_83'}, {'business_ref': 'businessref_26'}, {'business_ref': 'businessref_4'}, {'business_ref': 'businessref_68'}], 'var_call_UtQFjsyho25mMjZcpUmuD69D': 'file_storage/call_UtQFjsyho25mMjZcpUmuD69D.json'}

exec(code, env_args)
