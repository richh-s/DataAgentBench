code = """import pandas as pd
# var_call_tLtpdGNnuIAaJiawGQBvGsGV contains the list of business_ref values from reviews in 2018
df_reviews_2018 = pd.DataFrame(var_call_tLtpdGNnuIAaJiawGQBvGsGV)
# Convert business_ref to business_id by replacing prefix

def ref_to_id(x):
    if pd.isna(x):
        return x
    return x.replace('businessref_', 'businessid_')

df_reviews_2018['business_id'] = df_reviews_2018['business_ref'].apply(ref_to_id)

# Prepare list of unique business_ids
business_ids = df_reviews_2018['business_id'].unique().tolist()

# Output as JSON-serializable structure
import json
result = json.dumps({'business_ids': business_ids})
print('__RESULT__:')
print(result)"""

env_args = {'var_call_tLtpdGNnuIAaJiawGQBvGsGV': [{'business_ref': 'businessref_13'}, {'business_ref': 'businessref_79'}, {'business_ref': 'businessref_66'}, {'business_ref': 'businessref_25'}, {'business_ref': 'businessref_91'}, {'business_ref': 'businessref_46'}, {'business_ref': 'businessref_47'}, {'business_ref': 'businessref_73'}, {'business_ref': 'businessref_67'}, {'business_ref': 'businessref_15'}, {'business_ref': 'businessref_24'}, {'business_ref': 'businessref_36'}, {'business_ref': 'businessref_17'}, {'business_ref': 'businessref_43'}, {'business_ref': 'businessref_99'}, {'business_ref': 'businessref_86'}, {'business_ref': 'businessref_62'}, {'business_ref': 'businessref_8'}, {'business_ref': 'businessref_57'}, {'business_ref': 'businessref_37'}, {'business_ref': 'businessref_40'}, {'business_ref': 'businessref_83'}, {'business_ref': 'businessref_26'}, {'business_ref': 'businessref_4'}, {'business_ref': 'businessref_68'}, {'business_ref': 'businessref_82'}, {'business_ref': 'businessref_35'}, {'business_ref': 'businessref_45'}, {'business_ref': 'businessref_80'}, {'business_ref': 'businessref_77'}, {'business_ref': 'businessref_27'}, {'business_ref': 'businessref_20'}, {'business_ref': 'businessref_22'}, {'business_ref': 'businessref_14'}, {'business_ref': 'businessref_28'}, {'business_ref': 'businessref_59'}]}

exec(code, env_args)
