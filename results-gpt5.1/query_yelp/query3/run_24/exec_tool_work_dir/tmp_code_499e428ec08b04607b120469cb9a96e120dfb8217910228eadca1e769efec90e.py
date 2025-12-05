code = """import json
recs = var_call_nVZMKz81n3XVSJSfXrKVgylN
ids = []
for r in recs:
    bid = r['business_ref']
    if bid.startswith('businessref_'):
        num = bid.split('_',1)[1]
        ids.append('businessid_' + num)
    else:
        ids.append(bid)
result = json.dumps(ids)
print("__RESULT__:")
print(result)"""

env_args = {'var_call_hGycpu3AouqjWWh7ZbW4xXSP': ['checkin', 'business'], 'var_call_nVZMKz81n3XVSJSfXrKVgylN': [{'business_ref': 'businessref_13'}, {'business_ref': 'businessref_79'}, {'business_ref': 'businessref_66'}, {'business_ref': 'businessref_25'}, {'business_ref': 'businessref_91'}, {'business_ref': 'businessref_46'}, {'business_ref': 'businessref_47'}, {'business_ref': 'businessref_73'}, {'business_ref': 'businessref_59'}, {'business_ref': 'businessref_24'}, {'business_ref': 'businessref_36'}, {'business_ref': 'businessref_17'}, {'business_ref': 'businessref_43'}, {'business_ref': 'businessref_99'}, {'business_ref': 'businessref_86'}, {'business_ref': 'businessref_62'}, {'business_ref': 'businessref_8'}, {'business_ref': 'businessref_57'}, {'business_ref': 'businessref_37'}, {'business_ref': 'businessref_40'}, {'business_ref': 'businessref_83'}, {'business_ref': 'businessref_26'}, {'business_ref': 'businessref_4'}, {'business_ref': 'businessref_68'}, {'business_ref': 'businessref_82'}, {'business_ref': 'businessref_35'}, {'business_ref': 'businessref_45'}, {'business_ref': 'businessref_80'}, {'business_ref': 'businessref_77'}, {'business_ref': 'businessref_27'}, {'business_ref': 'businessref_20'}, {'business_ref': 'businessref_22'}, {'business_ref': 'businessref_14'}, {'business_ref': 'businessref_28'}, {'business_ref': 'businessref_67'}, {'business_ref': 'businessref_15'}]}

exec(code, env_args)
