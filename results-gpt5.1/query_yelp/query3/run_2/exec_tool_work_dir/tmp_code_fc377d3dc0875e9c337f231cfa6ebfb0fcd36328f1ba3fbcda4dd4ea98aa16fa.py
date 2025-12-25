code = """import json
import pandas as pd

# Load business attributes data from file
file_path = var_call_PmbUu7bhndsCfGjRstKyGMBq
with open(file_path, 'r') as f:
    business_attr = json.load(f)

# Dataframes from review and tip distinct business_ref
review_df = pd.DataFrame(var_call_sxGl4Xm4zoVQDXlT7vJcjat6)
tip_df = pd.DataFrame(var_call_gS79oJYH0XTadu7C6zLDdWyl)

# Union of business_ref that received reviews or tips in 2018
all_refs = pd.concat([review_df, tip_df]).drop_duplicates().reset_index(drop=True)

# Convert business_ref (businessref_X) to business_id (businessid_X)
all_refs['business_id'] = all_refs['business_ref'].str.replace('businessref_', 'businessid_', regex=False)

# Business attributes dataframe
biz_df = pd.DataFrame(business_attr)

# Keep only businesses that received reviews/tips in 2018
merged = pd.merge(all_refs, biz_df, on='business_id', how='inner')

# Function to check if business offers parking or bike parking

def offers_parking(attrs):
    if not isinstance(attrs, dict):
        return False
    # Direct BikeParking flag
    if 'BikeParking' in attrs and str(attrs['BikeParking']).strip().lower() == 'true':
        return True
    # BusinessParking: treat anything non-null and not 'None' as offering some kind of parking
    bp = attrs.get('BusinessParking')
    if bp is None:
        return False
    s = str(bp).strip().lower()
    if s == 'none' or s == 'false' or s == '':
        return False
    return True

merged['offers_parking'] = merged['attributes'].apply(offers_parking)

count = int(merged[merged['offers_parking']].shape[0])

result = json.dumps({"business_count": count})
print("__RESULT__:")
print(result)"""

env_args = {'var_call_PmbUu7bhndsCfGjRstKyGMBq': 'file_storage/call_PmbUu7bhndsCfGjRstKyGMBq.json', 'var_call_sxGl4Xm4zoVQDXlT7vJcjat6': [{'business_ref': 'businessref_13'}, {'business_ref': 'businessref_79'}, {'business_ref': 'businessref_91'}, {'business_ref': 'businessref_46'}, {'business_ref': 'businessref_47'}, {'business_ref': 'businessref_73'}, {'business_ref': 'businessref_66'}, {'business_ref': 'businessref_25'}, {'business_ref': 'businessref_59'}, {'business_ref': 'businessref_67'}, {'business_ref': 'businessref_15'}, {'business_ref': 'businessref_24'}, {'business_ref': 'businessref_36'}, {'business_ref': 'businessref_17'}, {'business_ref': 'businessref_43'}, {'business_ref': 'businessref_99'}, {'business_ref': 'businessref_80'}, {'business_ref': 'businessref_40'}, {'business_ref': 'businessref_83'}, {'business_ref': 'businessref_26'}, {'business_ref': 'businessref_4'}, {'business_ref': 'businessref_68'}, {'business_ref': 'businessref_82'}, {'business_ref': 'businessref_35'}, {'business_ref': 'businessref_45'}, {'business_ref': 'businessref_77'}, {'business_ref': 'businessref_27'}, {'business_ref': 'businessref_20'}, {'business_ref': 'businessref_22'}, {'business_ref': 'businessref_14'}, {'business_ref': 'businessref_28'}, {'business_ref': 'businessref_86'}, {'business_ref': 'businessref_62'}, {'business_ref': 'businessref_8'}, {'business_ref': 'businessref_57'}, {'business_ref': 'businessref_37'}], 'var_call_gS79oJYH0XTadu7C6zLDdWyl': [{'business_ref': 'businessref_67'}, {'business_ref': 'businessref_8'}, {'business_ref': 'businessref_82'}, {'business_ref': 'businessref_20'}, {'business_ref': 'businessref_46'}]}

exec(code, env_args)
