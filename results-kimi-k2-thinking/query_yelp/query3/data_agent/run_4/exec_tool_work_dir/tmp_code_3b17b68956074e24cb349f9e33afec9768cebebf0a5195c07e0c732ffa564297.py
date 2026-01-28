code = """import json

# List of business_ref values from previous query
business_refs = [
    "businessref_13", "businessref_79", "businessref_66", "businessref_25", "businessref_59",
    "businessref_67", "businessref_15", "businessref_91", "businessref_46", "businessref_47",
    "businessref_73", "businessref_99", "businessref_17", "businessref_43", "businessref_80",
    "businessref_24", "businessref_36", "businessref_40", "businessref_83", "businessref_86",
    "businessref_62", "businessref_8", "businessref_57", "businessref_37", "businessref_82",
    "businessref_35", "businessref_45", "businessref_26", "businessref_4", "businessref_68",
    "businessref_20", "businessref_22", "businessref_14", "businessref_28", "businessref_77",
    "businessref_27"
]

# Convert businessref_X to businessid_X
business_ids = []
for ref in business_refs:
    # Extract the number part
    number = ref.split('_')[1]
    business_ids.append(f"businessid_{number}")

print('__RESULT__:')
print(json.dumps(business_ids))"""

env_args = {'var_functions.query_db:0': [{'business_ref': 'businessref_13'}, {'business_ref': 'businessref_79'}, {'business_ref': 'businessref_66'}, {'business_ref': 'businessref_25'}, {'business_ref': 'businessref_59'}, {'business_ref': 'businessref_67'}, {'business_ref': 'businessref_15'}, {'business_ref': 'businessref_91'}, {'business_ref': 'businessref_46'}, {'business_ref': 'businessref_47'}, {'business_ref': 'businessref_73'}, {'business_ref': 'businessref_99'}, {'business_ref': 'businessref_17'}, {'business_ref': 'businessref_43'}, {'business_ref': 'businessref_80'}, {'business_ref': 'businessref_24'}, {'business_ref': 'businessref_36'}, {'business_ref': 'businessref_40'}, {'business_ref': 'businessref_83'}, {'business_ref': 'businessref_86'}, {'business_ref': 'businessref_62'}, {'business_ref': 'businessref_8'}, {'business_ref': 'businessref_57'}, {'business_ref': 'businessref_37'}, {'business_ref': 'businessref_82'}, {'business_ref': 'businessref_35'}, {'business_ref': 'businessref_45'}, {'business_ref': 'businessref_26'}, {'business_ref': 'businessref_4'}, {'business_ref': 'businessref_68'}, {'business_ref': 'businessref_20'}, {'business_ref': 'businessref_22'}, {'business_ref': 'businessref_14'}, {'business_ref': 'businessref_28'}, {'business_ref': 'businessref_77'}, {'business_ref': 'businessref_27'}]}

exec(code, env_args)
