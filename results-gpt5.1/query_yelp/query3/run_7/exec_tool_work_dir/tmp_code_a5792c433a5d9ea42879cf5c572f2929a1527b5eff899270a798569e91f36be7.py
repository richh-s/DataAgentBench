code = """import json
import pandas as pd

# Load business attributes
path = var_call_l3tTOLoLgIINX7tHYIZzMLcr
with open(path, 'r') as f:
    biz_attr = json.load(f)

biz_df = pd.DataFrame(biz_attr)

# Filter businesses that offer either BusinessParking (not None) or BikeParking == 'True'

def has_parking(attrs):
    if not isinstance(attrs, dict):
        return False
    if 'BusinessParking' in attrs and attrs['BusinessParking'] not in (None, "None"):
        return True
    if 'BikeParking' in attrs and str(attrs['BikeParking']) == 'True':
        return True
    return False

biz_df['has_parking'] = biz_df['attributes'].apply(has_parking)

parking_biz_ids = set(biz_df.loc[biz_df['has_parking'], 'business_id'])

# Load distinct reviewed businesses in 2018
review_df = pd.DataFrame(var_call_XRiz8AxKiKI3Z98cNCFM6HuN)

# Map businessref_X to businessid_X
review_df['business_id'] = review_df['business_ref'].str.replace('businessref_', 'businessid_', regex=False)

reviewed_biz_ids = set(review_df['business_id'])

# Intersection: businesses that got reviews in 2018 and have parking/bike parking
result_count = len(parking_biz_ids.intersection(reviewed_biz_ids))

out = json.dumps(result_count)
print("__RESULT__:")
print(out)"""

env_args = {'var_call_l3tTOLoLgIINX7tHYIZzMLcr': 'file_storage/call_l3tTOLoLgIINX7tHYIZzMLcr.json', 'var_call_XRiz8AxKiKI3Z98cNCFM6HuN': [{'business_ref': 'businessref_13'}, {'business_ref': 'businessref_79'}, {'business_ref': 'businessref_91'}, {'business_ref': 'businessref_46'}, {'business_ref': 'businessref_47'}, {'business_ref': 'businessref_73'}, {'business_ref': 'businessref_59'}, {'business_ref': 'businessref_67'}, {'business_ref': 'businessref_15'}, {'business_ref': 'businessref_24'}, {'business_ref': 'businessref_36'}, {'business_ref': 'businessref_66'}, {'business_ref': 'businessref_25'}, {'business_ref': 'businessref_17'}, {'business_ref': 'businessref_43'}, {'business_ref': 'businessref_99'}, {'business_ref': 'businessref_80'}, {'business_ref': 'businessref_86'}, {'business_ref': 'businessref_62'}, {'business_ref': 'businessref_8'}, {'business_ref': 'businessref_57'}, {'business_ref': 'businessref_37'}, {'business_ref': 'businessref_40'}, {'business_ref': 'businessref_83'}, {'business_ref': 'businessref_26'}, {'business_ref': 'businessref_4'}, {'business_ref': 'businessref_68'}, {'business_ref': 'businessref_82'}, {'business_ref': 'businessref_35'}, {'business_ref': 'businessref_45'}, {'business_ref': 'businessref_20'}, {'business_ref': 'businessref_22'}, {'business_ref': 'businessref_14'}, {'business_ref': 'businessref_28'}, {'business_ref': 'businessref_77'}, {'business_ref': 'businessref_27'}]}

exec(code, env_args)
