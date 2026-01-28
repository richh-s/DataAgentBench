code = """import json

# Access the stored result
review_data = locals()['var_functions.query_db:2']

# Get unique business references from 2018 reviews
business_refs_2018 = set()
for record in review_data:
    business_refs_2018.add(record['business_ref'])

print('__RESULT__:')
print(json.dumps({
    'unique_business_refs_count': len(business_refs_2018),
    'sample_business_refs': list(business_refs_2018)[:10]
}))"""

env_args = {'var_functions.list_db:0': ['checkin', 'business'], 'var_functions.query_db:2': [{'business_ref': 'businessref_77'}, {'business_ref': 'businessref_59'}, {'business_ref': 'businessref_26'}, {'business_ref': 'businessref_67'}, {'business_ref': 'businessref_15'}, {'business_ref': 'businessref_86'}, {'business_ref': 'businessref_86'}, {'business_ref': 'businessref_77'}, {'business_ref': 'businessref_13'}, {'business_ref': 'businessref_40'}, {'business_ref': 'businessref_86'}, {'business_ref': 'businessref_62'}, {'business_ref': 'businessref_86'}, {'business_ref': 'businessref_20'}, {'business_ref': 'businessref_82'}, {'business_ref': 'businessref_86'}, {'business_ref': 'businessref_24'}, {'business_ref': 'businessref_83'}, {'business_ref': 'businessref_26'}, {'business_ref': 'businessref_79'}, {'business_ref': 'businessref_91'}, {'business_ref': 'businessref_20'}, {'business_ref': 'businessref_35'}, {'business_ref': 'businessref_79'}, {'business_ref': 'businessref_67'}, {'business_ref': 'businessref_45'}, {'business_ref': 'businessref_66'}, {'business_ref': 'businessref_26'}, {'business_ref': 'businessref_13'}, {'business_ref': 'businessref_22'}, {'business_ref': 'businessref_59'}, {'business_ref': 'businessref_99'}, {'business_ref': 'businessref_25'}, {'business_ref': 'businessref_26'}, {'business_ref': 'businessref_8'}, {'business_ref': 'businessref_36'}, {'business_ref': 'businessref_79'}, {'business_ref': 'businessref_80'}, {'business_ref': 'businessref_14'}, {'business_ref': 'businessref_86'}, {'business_ref': 'businessref_15'}, {'business_ref': 'businessref_46'}, {'business_ref': 'businessref_67'}, {'business_ref': 'businessref_26'}, {'business_ref': 'businessref_13'}, {'business_ref': 'businessref_28'}, {'business_ref': 'businessref_40'}, {'business_ref': 'businessref_62'}, {'business_ref': 'businessref_67'}, {'business_ref': 'businessref_57'}, {'business_ref': 'businessref_4'}, {'business_ref': 'businessref_20'}, {'business_ref': 'businessref_86'}, {'business_ref': 'businessref_59'}, {'business_ref': 'businessref_17'}, {'business_ref': 'businessref_37'}, {'business_ref': 'businessref_68'}, {'business_ref': 'businessref_46'}, {'business_ref': 'businessref_8'}, {'business_ref': 'businessref_20'}, {'business_ref': 'businessref_47'}, {'business_ref': 'businessref_73'}, {'business_ref': 'businessref_27'}, {'business_ref': 'businessref_26'}, {'business_ref': 'businessref_43'}]}

exec(code, env_args)
