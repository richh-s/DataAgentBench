code = """import json, pandas as pd
reviews_2018 = pd.DataFrame(var_call_Kl6rRrIhc8efMyfXJrwyi79w)
reviews_2018['business_id'] = reviews_2018['business_ref'].str.replace('businessref_','businessid_', regex=False)
with open(var_call_TruYCcYBj5BU5q3HEAiDTE75, 'r') as f:
    business_data = json.load(f)
business_df = pd.DataFrame(business_data)[['business_id','attributes']]
# filter businesses to those that received reviews in 2018
merged = business_df.merge(reviews_2018[['business_id']].drop_duplicates(), on='business_id')
# normalize attributes
def has_parking_or_bike(attrs):
    if attrs is None or attrs == 'None':
        return False
    if isinstance(attrs, dict):
        bp = attrs.get('BusinessParking')
        bk = attrs.get('BikeParking')
    else:
        return False
    has_parking = False
    if isinstance(bp, str):
        if bp != 'None':
            has_parking = True
    elif bp:
        has_parking = True
    has_bike = False
    if isinstance(bk, str):
        if bk.lower() == 'true':
            has_bike = True
    elif bk:
        has_bike = True
    return has_parking or has_bike
merged['has_parking_or_bike'] = merged['attributes'].apply(has_parking_or_bike)
count = int(merged['has_parking_or_bike'].sum())
import json as _j
result = _j.dumps(count)
print("__RESULT__:")
print(result)"""

env_args = {'var_call_zdYk2ouQfu7ozfEfWkTLZcT6': ['checkin', 'business'], 'var_call_Kl6rRrIhc8efMyfXJrwyi79w': [{'business_ref': 'businessref_13'}, {'business_ref': 'businessref_79'}, {'business_ref': 'businessref_66'}, {'business_ref': 'businessref_25'}, {'business_ref': 'businessref_91'}, {'business_ref': 'businessref_46'}, {'business_ref': 'businessref_47'}, {'business_ref': 'businessref_73'}, {'business_ref': 'businessref_59'}, {'business_ref': 'businessref_67'}, {'business_ref': 'businessref_15'}, {'business_ref': 'businessref_24'}, {'business_ref': 'businessref_36'}, {'business_ref': 'businessref_17'}, {'business_ref': 'businessref_43'}, {'business_ref': 'businessref_99'}, {'business_ref': 'businessref_80'}, {'business_ref': 'businessref_86'}, {'business_ref': 'businessref_62'}, {'business_ref': 'businessref_8'}, {'business_ref': 'businessref_57'}, {'business_ref': 'businessref_37'}, {'business_ref': 'businessref_40'}, {'business_ref': 'businessref_83'}, {'business_ref': 'businessref_26'}, {'business_ref': 'businessref_4'}, {'business_ref': 'businessref_68'}, {'business_ref': 'businessref_82'}, {'business_ref': 'businessref_35'}, {'business_ref': 'businessref_45'}, {'business_ref': 'businessref_77'}, {'business_ref': 'businessref_27'}, {'business_ref': 'businessref_20'}, {'business_ref': 'businessref_22'}, {'business_ref': 'businessref_14'}, {'business_ref': 'businessref_28'}], 'var_call_TruYCcYBj5BU5q3HEAiDTE75': 'file_storage/call_TruYCcYBj5BU5q3HEAiDTE75.json'}

exec(code, env_args)
