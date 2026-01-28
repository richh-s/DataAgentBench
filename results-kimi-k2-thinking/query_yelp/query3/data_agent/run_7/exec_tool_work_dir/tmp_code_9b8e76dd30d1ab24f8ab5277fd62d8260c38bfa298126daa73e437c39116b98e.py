code = """import json

# Access the stored result
business_refs = locals()['var_functions.query_db:2']

# Extract business IDs by removing the 'businessref_' prefix
business_ids = []
for item in business_refs:
    ref = item['business_ref']
    if ref.startswith('businessref_'):
        business_id = 'businessid_' + ref.split('_')[1]
        business_ids.append(business_id)

print('__RESULT__:')
print(json.dumps(business_ids[:10]))  # Print first 10 as sample"""

env_args = {'var_functions.query_db:0': [{'date': '2018-02-19 14:12:00'}, {'date': '2018-08-12 15:51:00'}, {'date': '2018-06-02 14:52:00'}, {'date': '2018-07-09 02:34:16'}, {'date': '2018-12-08 19:50:00'}], 'var_functions.query_db:2': [{'business_ref': 'businessref_13'}, {'business_ref': 'businessref_79'}, {'business_ref': 'businessref_80'}, {'business_ref': 'businessref_82'}, {'business_ref': 'businessref_35'}, {'business_ref': 'businessref_45'}, {'business_ref': 'businessref_59'}, {'business_ref': 'businessref_77'}, {'business_ref': 'businessref_27'}, {'business_ref': 'businessref_86'}, {'business_ref': 'businessref_62'}, {'business_ref': 'businessref_8'}, {'business_ref': 'businessref_57'}, {'business_ref': 'businessref_37'}, {'business_ref': 'businessref_20'}, {'business_ref': 'businessref_22'}, {'business_ref': 'businessref_14'}, {'business_ref': 'businessref_28'}, {'business_ref': 'businessref_26'}, {'business_ref': 'businessref_4'}, {'business_ref': 'businessref_68'}, {'business_ref': 'businessref_17'}, {'business_ref': 'businessref_43'}, {'business_ref': 'businessref_99'}, {'business_ref': 'businessref_40'}, {'business_ref': 'businessref_83'}, {'business_ref': 'businessref_24'}, {'business_ref': 'businessref_36'}, {'business_ref': 'businessref_67'}, {'business_ref': 'businessref_15'}, {'business_ref': 'businessref_91'}, {'business_ref': 'businessref_46'}, {'business_ref': 'businessref_47'}, {'business_ref': 'businessref_73'}, {'business_ref': 'businessref_66'}, {'business_ref': 'businessref_25'}]}

exec(code, env_args)
