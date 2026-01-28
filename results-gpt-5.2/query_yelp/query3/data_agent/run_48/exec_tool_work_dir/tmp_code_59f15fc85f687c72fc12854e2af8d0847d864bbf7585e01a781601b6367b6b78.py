code = """import json, pandas as pd

# load reviews businesses
df_rev = pd.DataFrame(var_call_cmPq8ApBg4Qes9jbsvRurny6)
rev_set = set(df_rev['business_ref'].dropna().tolist())

# load businesses with parking attributes (full result may be in a file)
biz_data = var_call_vIurJSzOFvslUbqwiykmemkl
if isinstance(biz_data, str):
    with open(biz_data, 'r') as f:
        biz_data = json.load(f)

df_biz = pd.DataFrame(biz_data)

# normalize to businessref_ prefix
biz_refs = set(df_biz['business_id'].dropna().str.replace('businessid_', 'businessref_', regex=False).tolist())

answer = len(rev_set.intersection(biz_refs))

print('__RESULT__:')
print(json.dumps({'count': int(answer)}))"""

env_args = {'var_call_cmPq8ApBg4Qes9jbsvRurny6': [{'business_ref': 'businessref_13'}, {'business_ref': 'businessref_79'}, {'business_ref': 'businessref_66'}, {'business_ref': 'businessref_25'}, {'business_ref': 'businessref_59'}, {'business_ref': 'businessref_67'}, {'business_ref': 'businessref_15'}, {'business_ref': 'businessref_24'}, {'business_ref': 'businessref_36'}, {'business_ref': 'businessref_91'}, {'business_ref': 'businessref_46'}, {'business_ref': 'businessref_47'}, {'business_ref': 'businessref_73'}, {'business_ref': 'businessref_17'}, {'business_ref': 'businessref_43'}, {'business_ref': 'businessref_80'}, {'business_ref': 'businessref_99'}, {'business_ref': 'businessref_86'}, {'business_ref': 'businessref_62'}, {'business_ref': 'businessref_8'}, {'business_ref': 'businessref_57'}, {'business_ref': 'businessref_37'}, {'business_ref': 'businessref_40'}, {'business_ref': 'businessref_83'}, {'business_ref': 'businessref_82'}, {'business_ref': 'businessref_35'}, {'business_ref': 'businessref_45'}, {'business_ref': 'businessref_26'}, {'business_ref': 'businessref_4'}, {'business_ref': 'businessref_68'}, {'business_ref': 'businessref_77'}, {'business_ref': 'businessref_27'}, {'business_ref': 'businessref_20'}, {'business_ref': 'businessref_22'}, {'business_ref': 'businessref_14'}, {'business_ref': 'businessref_28'}], 'var_call_vIurJSzOFvslUbqwiykmemkl': 'file_storage/call_vIurJSzOFvslUbqwiykmemkl.json'}

exec(code, env_args)
