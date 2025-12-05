code = """import json, pandas as pd, os

# Load full business attributes data
path = var_call_2c3fq7gcM9Ry8nKM93NbZJ2H
if os.path.isfile(path):
    with open(path, 'r') as f:
        business_attr = json.load(f)
else:
    business_attr = var_call_2c3fq7gcM9Ry8nKM93NbZJ2H

# DataFrames
rev2018 = pd.DataFrame(var_call_sOVWBzmPQY35Ldd3FfPdQfEU)
tip2018 = pd.DataFrame(var_call_Zdxb5r8tTldSg7SIUK64MyMX)

# Businesses with any review or tip in 2018
b_refs = pd.concat([rev2018['business_ref'], tip2018['business_ref']]).drop_duplicates().tolist()
# Map businessref_ -> businessid_
ids_2018 = set(['businessid_' + x.split('_',1)[1] for x in b_refs])

bdf = pd.DataFrame(business_attr)

# Keep businesses that had reviews/tips in 2018
bdf = bdf[bdf['business_id'].isin(ids_2018)].copy()

# Function to check parking
def has_parking(attrs):
    if not isinstance(attrs, dict):
        return False
    if 'BikeParking' in attrs and str(attrs['BikeParking']).strip(" u'") == 'True':
        return True
    if 'BusinessParking' in attrs and attrs['BusinessParking'] not in (None, 'None'):
        return True
    return False

bdf['has_parking'] = bdf['attributes'].apply(has_parking)
count = int(bdf[bdf['has_parking']].shape[0])

result = json.dumps(count)
print("__RESULT__:")
print(result)"""

env_args = {'var_call_2c3fq7gcM9Ry8nKM93NbZJ2H': 'file_storage/call_2c3fq7gcM9Ry8nKM93NbZJ2H.json', 'var_call_sOVWBzmPQY35Ldd3FfPdQfEU': [{'business_ref': 'businessref_13'}, {'business_ref': 'businessref_79'}, {'business_ref': 'businessref_91'}, {'business_ref': 'businessref_46'}, {'business_ref': 'businessref_47'}, {'business_ref': 'businessref_73'}, {'business_ref': 'businessref_66'}, {'business_ref': 'businessref_25'}, {'business_ref': 'businessref_67'}, {'business_ref': 'businessref_15'}, {'business_ref': 'businessref_59'}, {'business_ref': 'businessref_24'}, {'business_ref': 'businessref_36'}, {'business_ref': 'businessref_17'}, {'business_ref': 'businessref_43'}, {'business_ref': 'businessref_80'}, {'business_ref': 'businessref_99'}, {'business_ref': 'businessref_86'}, {'business_ref': 'businessref_62'}, {'business_ref': 'businessref_8'}, {'business_ref': 'businessref_57'}, {'business_ref': 'businessref_37'}, {'business_ref': 'businessref_40'}, {'business_ref': 'businessref_83'}, {'business_ref': 'businessref_26'}, {'business_ref': 'businessref_4'}, {'business_ref': 'businessref_68'}, {'business_ref': 'businessref_82'}, {'business_ref': 'businessref_35'}, {'business_ref': 'businessref_45'}, {'business_ref': 'businessref_77'}, {'business_ref': 'businessref_27'}, {'business_ref': 'businessref_20'}, {'business_ref': 'businessref_22'}, {'business_ref': 'businessref_14'}, {'business_ref': 'businessref_28'}], 'var_call_Zdxb5r8tTldSg7SIUK64MyMX': [{'business_ref': 'businessref_46'}, {'business_ref': 'businessref_67'}, {'business_ref': 'businessref_82'}, {'business_ref': 'businessref_8'}, {'business_ref': 'businessref_20'}]}

exec(code, env_args)
