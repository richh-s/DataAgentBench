code = """import json, pandas as pd

reviews_2018 = pd.DataFrame(var_call_Dvrw4TRqcldCy3xBNYsMZeZj)
reviews_2018['business_id'] = reviews_2018['business_ref'].str.replace('businessref_', 'businessid_', regex=False)

import os
with open(var_call_U42pWNraRMY73pAqHafdnTnp, 'r') as f:
    business_attr = json.load(f)

business_attr_df = pd.DataFrame(business_attr)

business_attr_df['has_parking_or_bike'] = business_attr_df['attributes'].apply(lambda attrs: bool(attrs) and (('BikeParking' in attrs and attrs['BikeParking'] == 'True') or ('BusinessParking' in attrs and attrs['BusinessParking'] not in [None, "None", "{'garage': False, 'street': False, 'validated': False, 'lot': False, 'valet': False}"])) )

merged = pd.merge(reviews_2018, business_attr_df[['business_id', 'has_parking_or_bike']], on='business_id', how='left')

count_businesses = merged[merged['has_parking_or_bike'] == True]['business_id'].nunique()

result = json.dumps(int(count_businesses))
print("__RESULT__:")
print(result)"""

env_args = {'var_call_U42pWNraRMY73pAqHafdnTnp': 'file_storage/call_U42pWNraRMY73pAqHafdnTnp.json', 'var_call_Dvrw4TRqcldCy3xBNYsMZeZj': [{'business_ref': 'businessref_79'}, {'business_ref': 'businessref_13'}, {'business_ref': 'businessref_44'}, {'business_ref': 'businessref_25'}, {'business_ref': 'businessref_66'}, {'business_ref': 'businessref_59'}, {'business_ref': 'businessref_29'}, {'business_ref': 'businessref_67'}, {'business_ref': 'businessref_15'}, {'business_ref': 'businessref_81'}, {'business_ref': 'businessref_33'}, {'business_ref': 'businessref_24'}, {'business_ref': 'businessref_52'}, {'business_ref': 'businessref_89'}, {'business_ref': 'businessref_36'}, {'business_ref': 'businessref_60'}, {'business_ref': 'businessref_12'}, {'business_ref': 'businessref_43'}, {'business_ref': 'businessref_17'}, {'business_ref': 'businessref_6'}, {'business_ref': 'businessref_47'}, {'business_ref': 'businessref_91'}, {'business_ref': 'businessref_71'}, {'business_ref': 'businessref_46'}, {'business_ref': 'businessref_73'}, {'business_ref': 'businessref_99'}, {'business_ref': 'businessref_31'}, {'business_ref': 'businessref_80'}, {'business_ref': 'businessref_51'}, {'business_ref': 'businessref_40'}, {'business_ref': 'businessref_92'}, {'business_ref': 'businessref_83'}, {'business_ref': 'businessref_95'}, {'business_ref': 'businessref_61'}, {'business_ref': 'businessref_26'}, {'business_ref': 'businessref_68'}, {'business_ref': 'businessref_34'}, {'business_ref': 'businessref_21'}, {'business_ref': 'businessref_4'}, {'business_ref': 'businessref_49'}, {'business_ref': 'businessref_10'}, {'business_ref': 'businessref_23'}, {'business_ref': 'businessref_45'}, {'business_ref': 'businessref_82'}, {'business_ref': 'businessref_35'}, {'business_ref': 'businessref_77'}, {'business_ref': 'businessref_50'}, {'business_ref': 'businessref_76'}, {'business_ref': 'businessref_27'}, {'business_ref': 'businessref_3'}, {'business_ref': 'businessref_20'}, {'business_ref': 'businessref_28'}, {'business_ref': 'businessref_22'}, {'business_ref': 'businessref_69'}, {'business_ref': 'businessref_14'}, {'business_ref': 'businessref_70'}, {'business_ref': 'businessref_18'}, {'business_ref': 'businessref_86'}, {'business_ref': 'businessref_8'}, {'business_ref': 'businessref_72'}, {'business_ref': 'businessref_62'}, {'business_ref': 'businessref_85'}, {'business_ref': 'businessref_57'}, {'business_ref': 'businessref_56'}, {'business_ref': 'businessref_90'}, {'business_ref': 'businessref_97'}, {'business_ref': 'businessref_37'}]}

exec(code, env_args)
