code = """import json, pandas as pd, os

# Load business refs with 2018 reviews
business_refs_2018 = pd.DataFrame(var_call_jewODiokip1l3xPGJ7AGvGWF)
# Map to business_id by replacing prefix
business_refs_2018['business_id'] = business_refs_2018['business_ref'].str.replace('businessref_', 'businessid_', regex=False)

# Load full business attributes from file
with open(var_call_qxamF9uygqP4Yux6KAugERbY, 'r') as f:
    business_attr = json.load(f)

biz_df = pd.DataFrame(business_attr)[['business_id','attributes']]

# Normalize attributes to detect parking

def has_parking(attrs):
    if attrs is None or attrs == 'None':
        return False
    # attrs expected as dict
    if isinstance(attrs, dict):
        bp = attrs.get('BusinessParking')
        bike = attrs.get('BikeParking')
        has_bp = False
        if isinstance(bp, str):
            if 'True' in bp or 'true' in bp:
                has_bp = True
        elif isinstance(bp, dict):
            has_bp = any(bool(v) for v in bp.values())
        has_bike = False
        if isinstance(bike, str):
            if 'True' in bike or 'true' in bike:
                has_bike = True
        elif isinstance(bike, bool):
            has_bike = bike
        return has_bp or has_bike
    return False

biz_df['has_parking_or_bike'] = biz_df['attributes'].apply(has_parking)

# Filter businesses with 2018 reviews
merged = pd.merge(business_refs_2018[['business_id']], biz_df, on='business_id', how='left')

result_count = int(merged[merged['has_parking_or_bike']].drop_duplicates('business_id').shape[0])

out = json.dumps(result_count)
print("__RESULT__:")
print(out)"""

env_args = {'var_call_GQPTcihVUbBsSPIRxa42Xuv4': ['checkin', 'business'], 'var_call_jewODiokip1l3xPGJ7AGvGWF': [{'business_ref': 'businessref_79'}, {'business_ref': 'businessref_13'}, {'business_ref': 'businessref_44'}, {'business_ref': 'businessref_6'}, {'business_ref': 'businessref_47'}, {'business_ref': 'businessref_91'}, {'business_ref': 'businessref_71'}, {'business_ref': 'businessref_46'}, {'business_ref': 'businessref_73'}, {'business_ref': 'businessref_25'}, {'business_ref': 'businessref_66'}, {'business_ref': 'businessref_59'}, {'business_ref': 'businessref_29'}, {'business_ref': 'businessref_67'}, {'business_ref': 'businessref_15'}, {'business_ref': 'businessref_81'}, {'business_ref': 'businessref_33'}, {'business_ref': 'businessref_43'}, {'business_ref': 'businessref_17'}, {'business_ref': 'businessref_80'}, {'business_ref': 'businessref_51'}, {'business_ref': 'businessref_86'}, {'business_ref': 'businessref_8'}, {'business_ref': 'businessref_72'}, {'business_ref': 'businessref_62'}, {'business_ref': 'businessref_85'}, {'business_ref': 'businessref_57'}, {'business_ref': 'businessref_56'}, {'business_ref': 'businessref_90'}, {'business_ref': 'businessref_97'}, {'business_ref': 'businessref_37'}, {'business_ref': 'businessref_40'}, {'business_ref': 'businessref_92'}, {'business_ref': 'businessref_83'}, {'business_ref': 'businessref_95'}, {'business_ref': 'businessref_61'}, {'business_ref': 'businessref_99'}, {'business_ref': 'businessref_31'}, {'business_ref': 'businessref_26'}, {'business_ref': 'businessref_68'}, {'business_ref': 'businessref_34'}, {'business_ref': 'businessref_21'}, {'business_ref': 'businessref_4'}, {'business_ref': 'businessref_49'}, {'business_ref': 'businessref_10'}, {'business_ref': 'businessref_23'}, {'business_ref': 'businessref_45'}, {'business_ref': 'businessref_82'}, {'business_ref': 'businessref_35'}, {'business_ref': 'businessref_77'}, {'business_ref': 'businessref_50'}, {'business_ref': 'businessref_76'}, {'business_ref': 'businessref_27'}, {'business_ref': 'businessref_3'}, {'business_ref': 'businessref_20'}, {'business_ref': 'businessref_28'}, {'business_ref': 'businessref_22'}, {'business_ref': 'businessref_69'}, {'business_ref': 'businessref_14'}, {'business_ref': 'businessref_70'}, {'business_ref': 'businessref_18'}, {'business_ref': 'businessref_24'}, {'business_ref': 'businessref_52'}, {'business_ref': 'businessref_89'}, {'business_ref': 'businessref_36'}, {'business_ref': 'businessref_60'}, {'business_ref': 'businessref_12'}], 'var_call_qxamF9uygqP4Yux6KAugERbY': 'file_storage/call_qxamF9uygqP4Yux6KAugERbY.json'}

exec(code, env_args)
