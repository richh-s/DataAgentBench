code = """import json, pandas as pd

reviews = pd.DataFrame(var_call_O3dig3Bc62LqKNdwunqRi5YV)
tips = pd.DataFrame(var_call_A8Da9TJ7m6laCkPC2j4gbg9s)

all_refs = pd.concat([reviews['business_ref'], tips['business_ref']]).drop_duplicates().tolist()

# convert to corresponding business_id values
business_ids = [ref.replace('businessref_', 'businessid_') for ref in all_refs]

result = json.dumps(business_ids)

print("__RESULT__:")
print(result)"""

env_args = {'var_call_hUDWLlQoANMnbt5gy5GNUewe': 'file_storage/call_hUDWLlQoANMnbt5gy5GNUewe.json', 'var_call_O3dig3Bc62LqKNdwunqRi5YV': [{'business_ref': 'businessref_91'}, {'business_ref': 'businessref_46'}, {'business_ref': 'businessref_47'}, {'business_ref': 'businessref_73'}, {'business_ref': 'businessref_66'}, {'business_ref': 'businessref_25'}, {'business_ref': 'businessref_13'}, {'business_ref': 'businessref_79'}, {'business_ref': 'businessref_59'}, {'business_ref': 'businessref_24'}, {'business_ref': 'businessref_36'}, {'business_ref': 'businessref_17'}, {'business_ref': 'businessref_43'}, {'business_ref': 'businessref_67'}, {'business_ref': 'businessref_15'}, {'business_ref': 'businessref_80'}, {'business_ref': 'businessref_40'}, {'business_ref': 'businessref_83'}, {'business_ref': 'businessref_26'}, {'business_ref': 'businessref_4'}, {'business_ref': 'businessref_68'}, {'business_ref': 'businessref_82'}, {'business_ref': 'businessref_35'}, {'business_ref': 'businessref_45'}, {'business_ref': 'businessref_77'}, {'business_ref': 'businessref_27'}, {'business_ref': 'businessref_20'}, {'business_ref': 'businessref_22'}, {'business_ref': 'businessref_14'}, {'business_ref': 'businessref_28'}, {'business_ref': 'businessref_86'}, {'business_ref': 'businessref_62'}, {'business_ref': 'businessref_8'}, {'business_ref': 'businessref_57'}, {'business_ref': 'businessref_37'}, {'business_ref': 'businessref_99'}], 'var_call_A8Da9TJ7m6laCkPC2j4gbg9s': [{'business_ref': 'businessref_46'}, {'business_ref': 'businessref_67'}, {'business_ref': 'businessref_8'}, {'business_ref': 'businessref_20'}, {'business_ref': 'businessref_82'}]}

exec(code, env_args)
