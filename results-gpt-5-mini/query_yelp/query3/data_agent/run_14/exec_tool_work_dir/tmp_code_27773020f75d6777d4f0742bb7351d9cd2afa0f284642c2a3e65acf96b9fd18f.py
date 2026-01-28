code = """import json
import pandas as pd
# var_call_iuvLHx5sOSUjvF8bD4jTnBYG and var_call_fCirbofKVZnVhGFy77hLnWy5 are available
reviews_2018 = pd.DataFrame(var_call_iuvLHx5sOSUjvF8bD4jTnBYG)
businesses = pd.read_json(var_call_fCirbofKVZnVhGFy77hLnWy5)
# Normalize attributes: some are None, some are strings representing dicts
def has_parking(attrs):
    if attrs is None:
        return False
    # BikeParking field
    bike = False
    businessparking = False
    if isinstance(attrs, dict):
        # BikeParking may be 'True'/'False'
        bp = attrs.get('BikeParking')
        if bp in (True, 'True', "True", "u'True'", "u'true'", "'True'", "'true'", 'true'):
            bike = True
        if bp in ('True','true','true','u"True"'):
            bike = True
        # BusinessParking may be 'None' or a string representation of dict
        bpark = attrs.get('BusinessParking')
        if isinstance(bpark, dict):
            # if any parking True in dict
            for v in bpark.values():
                if v in (True, 'True', 'true', 'True'):
                    businessparking = True
        elif isinstance(bpark, str):
            if bpark.strip().lower()!='none':
                # check if contains 'true' or 'lot' or 'street' etc set True
                if "true" in bpark.lower() or "lot" in bpark.lower() or "garage" in bpark.lower() or "street" in bpark.lower() or "valet" in bpark.lower():
                    # but need to ensure there is a True value; in dataset strings show True/False, we'll check for "true"
                    if "true" in bpark.lower():
                        businessparking = True
                    else:
                        # sometimes lot present but marked False; look for "lot': True"
                        if "': True" in bpark or ": True" in bpark:
                            businessparking = True
        # also consider 'BikeParking' strings like 'False'
    return bike or businessparking

# Build mapping business_id -> has_parking
businesses['has_parking'] = businesses['attributes'].apply(has_parking)
# Map review business_ref to businessid by replacing prefix
reviews_2018['business_id'] = reviews_2018['business_ref'].str.replace('businessref_','businessid_')
# Merge
merged = reviews_2018.merge(businesses[['business_id','has_parking']], on='business_id', how='left')
# Count distinct businesses with has_parking True
count = int(merged[merged['has_parking']==True]['business_id'].nunique())
result = {"count_businesses_with_parking_in_2018": count}
print("__RESULT__:")
print(json.dumps(result))"""

env_args = {'var_call_iuvLHx5sOSUjvF8bD4jTnBYG': [{'business_ref': 'businessref_13'}, {'business_ref': 'businessref_79'}, {'business_ref': 'businessref_91'}, {'business_ref': 'businessref_46'}, {'business_ref': 'businessref_47'}, {'business_ref': 'businessref_73'}, {'business_ref': 'businessref_59'}, {'business_ref': 'businessref_67'}, {'business_ref': 'businessref_15'}, {'business_ref': 'businessref_24'}, {'business_ref': 'businessref_36'}, {'business_ref': 'businessref_17'}, {'business_ref': 'businessref_43'}, {'business_ref': 'businessref_99'}, {'business_ref': 'businessref_66'}, {'business_ref': 'businessref_25'}, {'business_ref': 'businessref_80'}, {'business_ref': 'businessref_86'}, {'business_ref': 'businessref_62'}, {'business_ref': 'businessref_8'}, {'business_ref': 'businessref_57'}, {'business_ref': 'businessref_37'}, {'business_ref': 'businessref_40'}, {'business_ref': 'businessref_83'}, {'business_ref': 'businessref_26'}, {'business_ref': 'businessref_4'}, {'business_ref': 'businessref_68'}, {'business_ref': 'businessref_82'}, {'business_ref': 'businessref_35'}, {'business_ref': 'businessref_45'}, {'business_ref': 'businessref_20'}, {'business_ref': 'businessref_22'}, {'business_ref': 'businessref_14'}, {'business_ref': 'businessref_28'}, {'business_ref': 'businessref_77'}, {'business_ref': 'businessref_27'}], 'var_call_fCirbofKVZnVhGFy77hLnWy5': 'file_storage/call_fCirbofKVZnVhGFy77hLnWy5.json'}

exec(code, env_args)
