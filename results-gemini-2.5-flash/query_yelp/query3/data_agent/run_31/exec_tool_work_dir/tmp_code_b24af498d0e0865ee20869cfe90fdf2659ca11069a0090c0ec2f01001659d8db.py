code = """import pandas as pd
import json

business_refs_2018 = locals()['var_function-call-12937857947461596871']
df_business_refs = pd.DataFrame(business_refs_2018)
df_business_refs['business_id'] = df_business_refs['business_ref'].apply(lambda x: x.replace('businessref_', 'businessid_'))

business_ids_2018 = df_business_refs['business_id'].tolist()

print("__RESULT__:")
print(json.dumps(business_ids_2018))"""

env_args = {'var_function-call-12937857947461596871': [{'business_ref': 'businessref_44'}, {'business_ref': 'businessref_13'}, {'business_ref': 'businessref_47'}, {'business_ref': 'businessref_6'}, {'business_ref': 'businessref_91'}, {'business_ref': 'businessref_71'}, {'business_ref': 'businessref_46'}, {'business_ref': 'businessref_59'}, {'business_ref': 'businessref_29'}, {'business_ref': 'businessref_81'}, {'business_ref': 'businessref_33'}, {'business_ref': 'businessref_67'}, {'business_ref': 'businessref_15'}, {'business_ref': 'businessref_24'}, {'business_ref': 'businessref_60'}, {'business_ref': 'businessref_36'}, {'business_ref': 'businessref_43'}, {'business_ref': 'businessref_25'}, {'business_ref': 'businessref_66'}, {'business_ref': 'businessref_99'}, {'business_ref': 'businessref_80'}, {'business_ref': 'businessref_8'}, {'business_ref': 'businessref_85'}, {'business_ref': 'businessref_86'}, {'business_ref': 'businessref_56'}, {'business_ref': 'businessref_57'}, {'business_ref': 'businessref_90'}, {'business_ref': 'businessref_92'}, {'business_ref': 'businessref_95'}, {'business_ref': 'businessref_61'}, {'business_ref': 'businessref_68'}, {'business_ref': 'businessref_34'}, {'business_ref': 'businessref_21'}, {'business_ref': 'businessref_10'}, {'business_ref': 'businessref_45'}, {'business_ref': 'businessref_50'}, {'business_ref': 'businessref_76'}, {'business_ref': 'businessref_27'}, {'business_ref': 'businessref_28'}, {'business_ref': 'businessref_69'}, {'business_ref': 'businessref_14'}, {'business_ref': 'businessref_18'}, {'business_ref': 'businessref_22'}]}

exec(code, env_args)
