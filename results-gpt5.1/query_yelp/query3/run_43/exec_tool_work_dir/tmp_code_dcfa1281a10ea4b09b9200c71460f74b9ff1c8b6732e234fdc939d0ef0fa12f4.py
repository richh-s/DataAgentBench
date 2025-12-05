code = """import json, pandas as pd, os

# load full business attributes file
path = var_call_hUDWLlQoANMnbt5gy5GNUewe
with open(path, 'r') as f:
    business_records = json.load(f)

business_df = pd.DataFrame(business_records)[['business_id', 'attributes']]

# parse business_ids from previous step
business_ids = json.loads(var_call_XuMHIO7mnHyAWHk3mFePu7P8)

subset = business_df[business_df['business_id'].isin(business_ids)].copy()

# function to check parking attributes
def has_parking(attrs):
    if not isinstance(attrs, dict):
        return False
    bike = attrs.get('BikeParking')
    bus = attrs.get('BusinessParking')
    cond_bike = isinstance(bike, str) and bike == 'True'
    cond_bus = isinstance(bus, str) and 'True' in bus
    return cond_bike or cond_bus

subset['has_parking'] = subset['attributes'].apply(has_parking)

count = int(subset[subset['has_parking']].shape[0])

result = json.dumps(count)

print("__RESULT__:")
print(result)"""

env_args = {'var_call_hUDWLlQoANMnbt5gy5GNUewe': 'file_storage/call_hUDWLlQoANMnbt5gy5GNUewe.json', 'var_call_O3dig3Bc62LqKNdwunqRi5YV': [{'business_ref': 'businessref_91'}, {'business_ref': 'businessref_46'}, {'business_ref': 'businessref_47'}, {'business_ref': 'businessref_73'}, {'business_ref': 'businessref_66'}, {'business_ref': 'businessref_25'}, {'business_ref': 'businessref_13'}, {'business_ref': 'businessref_79'}, {'business_ref': 'businessref_59'}, {'business_ref': 'businessref_24'}, {'business_ref': 'businessref_36'}, {'business_ref': 'businessref_17'}, {'business_ref': 'businessref_43'}, {'business_ref': 'businessref_67'}, {'business_ref': 'businessref_15'}, {'business_ref': 'businessref_80'}, {'business_ref': 'businessref_40'}, {'business_ref': 'businessref_83'}, {'business_ref': 'businessref_26'}, {'business_ref': 'businessref_4'}, {'business_ref': 'businessref_68'}, {'business_ref': 'businessref_82'}, {'business_ref': 'businessref_35'}, {'business_ref': 'businessref_45'}, {'business_ref': 'businessref_77'}, {'business_ref': 'businessref_27'}, {'business_ref': 'businessref_20'}, {'business_ref': 'businessref_22'}, {'business_ref': 'businessref_14'}, {'business_ref': 'businessref_28'}, {'business_ref': 'businessref_86'}, {'business_ref': 'businessref_62'}, {'business_ref': 'businessref_8'}, {'business_ref': 'businessref_57'}, {'business_ref': 'businessref_37'}, {'business_ref': 'businessref_99'}], 'var_call_A8Da9TJ7m6laCkPC2j4gbg9s': [{'business_ref': 'businessref_46'}, {'business_ref': 'businessref_67'}, {'business_ref': 'businessref_8'}, {'business_ref': 'businessref_20'}, {'business_ref': 'businessref_82'}], 'var_call_XuMHIO7mnHyAWHk3mFePu7P8': ['businessid_91', 'businessid_46', 'businessid_47', 'businessid_73', 'businessid_66', 'businessid_25', 'businessid_13', 'businessid_79', 'businessid_59', 'businessid_24', 'businessid_36', 'businessid_17', 'businessid_43', 'businessid_67', 'businessid_15', 'businessid_80', 'businessid_40', 'businessid_83', 'businessid_26', 'businessid_4', 'businessid_68', 'businessid_82', 'businessid_35', 'businessid_45', 'businessid_77', 'businessid_27', 'businessid_20', 'businessid_22', 'businessid_14', 'businessid_28', 'businessid_86', 'businessid_62', 'businessid_8', 'businessid_57', 'businessid_37', 'businessid_99']}

exec(code, env_args)
