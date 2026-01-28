code = """import json
# var_call_aEPnqKEpCB5ZyHSMQjaQbNUx is provided by previous query
data = var_call_aEPnqKEpCB5ZyHSMQjaQbNUx
lst = ["businessid_" + item['business_ref'].split('_',1)[1] for item in data]
print("__RESULT__:")
print(json.dumps(lst))"""

env_args = {'var_call_N3LoAZwhmoTehv9CSP6C8LCP': ['business', 'checkin'], 'var_call_9jrPHdOoxE6DYvbugLssYmfH': ['review', 'tip', 'user'], 'var_call_aEPnqKEpCB5ZyHSMQjaQbNUx': [{'business_ref': 'businessref_13'}, {'business_ref': 'businessref_79'}, {'business_ref': 'businessref_66'}, {'business_ref': 'businessref_25'}, {'business_ref': 'businessref_91'}, {'business_ref': 'businessref_46'}, {'business_ref': 'businessref_47'}, {'business_ref': 'businessref_73'}, {'business_ref': 'businessref_59'}, {'business_ref': 'businessref_67'}, {'business_ref': 'businessref_15'}, {'business_ref': 'businessref_24'}, {'business_ref': 'businessref_36'}, {'business_ref': 'businessref_17'}, {'business_ref': 'businessref_43'}, {'business_ref': 'businessref_99'}, {'business_ref': 'businessref_80'}, {'business_ref': 'businessref_40'}, {'business_ref': 'businessref_83'}, {'business_ref': 'businessref_26'}, {'business_ref': 'businessref_4'}, {'business_ref': 'businessref_68'}, {'business_ref': 'businessref_82'}, {'business_ref': 'businessref_35'}, {'business_ref': 'businessref_45'}, {'business_ref': 'businessref_77'}, {'business_ref': 'businessref_27'}, {'business_ref': 'businessref_20'}, {'business_ref': 'businessref_22'}, {'business_ref': 'businessref_14'}, {'business_ref': 'businessref_28'}, {'business_ref': 'businessref_86'}, {'business_ref': 'businessref_62'}, {'business_ref': 'businessref_8'}, {'business_ref': 'businessref_57'}, {'business_ref': 'businessref_37'}]}

exec(code, env_args)
