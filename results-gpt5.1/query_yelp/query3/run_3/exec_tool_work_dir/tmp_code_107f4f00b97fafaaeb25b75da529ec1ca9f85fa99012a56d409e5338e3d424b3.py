code = """import json, pandas as pd

reviews_2018 = pd.DataFrame(var_call_kTXPOogz9Za4kWVNAIikJQLR)
tips_2018 = pd.DataFrame(var_call_x7Tq9AkH8T95ZJd3Ccqc8dM4)

# union of businesses with reviews or tips in 2018
all_refs = pd.unique(pd.concat([reviews_2018['business_ref'], tips_2018['business_ref']]))

# map business_ref -> business_id
business_ids = pd.Series(all_refs).str.replace('businessref_', 'businessid_', regex=False)

result = pd.DataFrame({'business_ref': all_refs, 'business_id': business_ids})

result_json = result.to_dict(orient='records')

print('__RESULT__:')
print(json.dumps(result_json))"""

env_args = {'var_call_0yqnO07shNdFJHQaNm53nwum': 'file_storage/call_0yqnO07shNdFJHQaNm53nwum.json', 'var_call_kTXPOogz9Za4kWVNAIikJQLR': [{'business_ref': 'businessref_79'}, {'business_ref': 'businessref_13'}, {'business_ref': 'businessref_44'}, {'business_ref': 'businessref_67'}, {'business_ref': 'businessref_15'}, {'business_ref': 'businessref_81'}, {'business_ref': 'businessref_33'}, {'business_ref': 'businessref_24'}, {'business_ref': 'businessref_52'}, {'business_ref': 'businessref_89'}, {'business_ref': 'businessref_36'}, {'business_ref': 'businessref_60'}, {'business_ref': 'businessref_12'}, {'business_ref': 'businessref_43'}, {'business_ref': 'businessref_17'}, {'business_ref': 'businessref_25'}, {'business_ref': 'businessref_66'}, {'business_ref': 'businessref_99'}, {'business_ref': 'businessref_31'}, {'business_ref': 'businessref_40'}, {'business_ref': 'businessref_92'}, {'business_ref': 'businessref_83'}, {'business_ref': 'businessref_95'}, {'business_ref': 'businessref_61'}, {'business_ref': 'businessref_26'}, {'business_ref': 'businessref_68'}, {'business_ref': 'businessref_34'}, {'business_ref': 'businessref_21'}, {'business_ref': 'businessref_4'}, {'business_ref': 'businessref_49'}, {'business_ref': 'businessref_10'}, {'business_ref': 'businessref_23'}, {'business_ref': 'businessref_80'}, {'business_ref': 'businessref_51'}, {'business_ref': 'businessref_45'}, {'business_ref': 'businessref_82'}, {'business_ref': 'businessref_35'}, {'business_ref': 'businessref_77'}, {'business_ref': 'businessref_50'}, {'business_ref': 'businessref_76'}, {'business_ref': 'businessref_27'}, {'business_ref': 'businessref_3'}, {'business_ref': 'businessref_20'}, {'business_ref': 'businessref_28'}, {'business_ref': 'businessref_22'}, {'business_ref': 'businessref_69'}, {'business_ref': 'businessref_14'}, {'business_ref': 'businessref_70'}, {'business_ref': 'businessref_18'}, {'business_ref': 'businessref_6'}, {'business_ref': 'businessref_47'}, {'business_ref': 'businessref_91'}, {'business_ref': 'businessref_71'}, {'business_ref': 'businessref_46'}, {'business_ref': 'businessref_73'}, {'business_ref': 'businessref_59'}, {'business_ref': 'businessref_29'}, {'business_ref': 'businessref_86'}, {'business_ref': 'businessref_8'}, {'business_ref': 'businessref_72'}, {'business_ref': 'businessref_62'}, {'business_ref': 'businessref_85'}, {'business_ref': 'businessref_57'}, {'business_ref': 'businessref_56'}, {'business_ref': 'businessref_90'}, {'business_ref': 'businessref_97'}, {'business_ref': 'businessref_37'}], 'var_call_x7Tq9AkH8T95ZJd3Ccqc8dM4': [{'business_ref': 'businessref_46'}, {'business_ref': 'businessref_6'}, {'business_ref': 'businessref_67'}, {'business_ref': 'businessref_99'}, {'business_ref': 'businessref_8'}, {'business_ref': 'businessref_86'}, {'business_ref': 'businessref_85'}, {'business_ref': 'businessref_21'}, {'business_ref': 'businessref_27'}, {'business_ref': 'businessref_20'}, {'business_ref': 'businessref_69'}, {'business_ref': 'businessref_18'}, {'business_ref': 'businessref_36'}, {'business_ref': 'businessref_24'}, {'business_ref': 'businessref_45'}, {'business_ref': 'businessref_82'}]}

exec(code, env_args)
