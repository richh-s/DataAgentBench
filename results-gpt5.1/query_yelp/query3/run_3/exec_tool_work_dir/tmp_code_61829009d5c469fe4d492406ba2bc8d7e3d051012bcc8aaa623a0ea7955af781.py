code = """import json, pandas as pd, os

# load full business attributes from file
path = var_call_0yqnO07shNdFJHQaNm53nwum
with open(path, 'r') as f:
    business_records = json.load(f)

biz_df = pd.DataFrame(business_records)[['business_id', 'attributes']]

refs_map = pd.DataFrame(var_call_dZVENeYTBNPkj9VsWwpOhdEM)

# keep only businesses that received review or tip in 2018
merged = refs_map.merge(biz_df, on='business_id', how='left')

# function to check parking
def has_parking(attrs):
    if attrs is None or attrs == 'None':
        return False
    if not isinstance(attrs, dict):
        return False
    bike = attrs.get('BikeParking')
    if isinstance(bike, str):
        if bike.strip(" '") == 'True':
            return True
    elif bike is True:
        return True
    bp = attrs.get('BusinessParking')
    if isinstance(bp, str):
        s = bp.lower()
        if 'true' in s:
            return True
    elif isinstance(bp, dict):
        if any(bool(v) for v in bp.values()):
            return True
    return False

merged['has_parking'] = merged['attributes'].apply(has_parking)

count = int(merged[merged['has_parking']].shape[0])

print('__RESULT__:')
print(json.dumps(count))"""

env_args = {'var_call_0yqnO07shNdFJHQaNm53nwum': 'file_storage/call_0yqnO07shNdFJHQaNm53nwum.json', 'var_call_kTXPOogz9Za4kWVNAIikJQLR': [{'business_ref': 'businessref_79'}, {'business_ref': 'businessref_13'}, {'business_ref': 'businessref_44'}, {'business_ref': 'businessref_67'}, {'business_ref': 'businessref_15'}, {'business_ref': 'businessref_81'}, {'business_ref': 'businessref_33'}, {'business_ref': 'businessref_24'}, {'business_ref': 'businessref_52'}, {'business_ref': 'businessref_89'}, {'business_ref': 'businessref_36'}, {'business_ref': 'businessref_60'}, {'business_ref': 'businessref_12'}, {'business_ref': 'businessref_43'}, {'business_ref': 'businessref_17'}, {'business_ref': 'businessref_25'}, {'business_ref': 'businessref_66'}, {'business_ref': 'businessref_99'}, {'business_ref': 'businessref_31'}, {'business_ref': 'businessref_40'}, {'business_ref': 'businessref_92'}, {'business_ref': 'businessref_83'}, {'business_ref': 'businessref_95'}, {'business_ref': 'businessref_61'}, {'business_ref': 'businessref_26'}, {'business_ref': 'businessref_68'}, {'business_ref': 'businessref_34'}, {'business_ref': 'businessref_21'}, {'business_ref': 'businessref_4'}, {'business_ref': 'businessref_49'}, {'business_ref': 'businessref_10'}, {'business_ref': 'businessref_23'}, {'business_ref': 'businessref_80'}, {'business_ref': 'businessref_51'}, {'business_ref': 'businessref_45'}, {'business_ref': 'businessref_82'}, {'business_ref': 'businessref_35'}, {'business_ref': 'businessref_77'}, {'business_ref': 'businessref_50'}, {'business_ref': 'businessref_76'}, {'business_ref': 'businessref_27'}, {'business_ref': 'businessref_3'}, {'business_ref': 'businessref_20'}, {'business_ref': 'businessref_28'}, {'business_ref': 'businessref_22'}, {'business_ref': 'businessref_69'}, {'business_ref': 'businessref_14'}, {'business_ref': 'businessref_70'}, {'business_ref': 'businessref_18'}, {'business_ref': 'businessref_6'}, {'business_ref': 'businessref_47'}, {'business_ref': 'businessref_91'}, {'business_ref': 'businessref_71'}, {'business_ref': 'businessref_46'}, {'business_ref': 'businessref_73'}, {'business_ref': 'businessref_59'}, {'business_ref': 'businessref_29'}, {'business_ref': 'businessref_86'}, {'business_ref': 'businessref_8'}, {'business_ref': 'businessref_72'}, {'business_ref': 'businessref_62'}, {'business_ref': 'businessref_85'}, {'business_ref': 'businessref_57'}, {'business_ref': 'businessref_56'}, {'business_ref': 'businessref_90'}, {'business_ref': 'businessref_97'}, {'business_ref': 'businessref_37'}], 'var_call_x7Tq9AkH8T95ZJd3Ccqc8dM4': [{'business_ref': 'businessref_46'}, {'business_ref': 'businessref_6'}, {'business_ref': 'businessref_67'}, {'business_ref': 'businessref_99'}, {'business_ref': 'businessref_8'}, {'business_ref': 'businessref_86'}, {'business_ref': 'businessref_85'}, {'business_ref': 'businessref_21'}, {'business_ref': 'businessref_27'}, {'business_ref': 'businessref_20'}, {'business_ref': 'businessref_69'}, {'business_ref': 'businessref_18'}, {'business_ref': 'businessref_36'}, {'business_ref': 'businessref_24'}, {'business_ref': 'businessref_45'}, {'business_ref': 'businessref_82'}], 'var_call_dZVENeYTBNPkj9VsWwpOhdEM': [{'business_ref': 'businessref_79', 'business_id': 'businessid_79'}, {'business_ref': 'businessref_13', 'business_id': 'businessid_13'}, {'business_ref': 'businessref_44', 'business_id': 'businessid_44'}, {'business_ref': 'businessref_67', 'business_id': 'businessid_67'}, {'business_ref': 'businessref_15', 'business_id': 'businessid_15'}, {'business_ref': 'businessref_81', 'business_id': 'businessid_81'}, {'business_ref': 'businessref_33', 'business_id': 'businessid_33'}, {'business_ref': 'businessref_24', 'business_id': 'businessid_24'}, {'business_ref': 'businessref_52', 'business_id': 'businessid_52'}, {'business_ref': 'businessref_89', 'business_id': 'businessid_89'}, {'business_ref': 'businessref_36', 'business_id': 'businessid_36'}, {'business_ref': 'businessref_60', 'business_id': 'businessid_60'}, {'business_ref': 'businessref_12', 'business_id': 'businessid_12'}, {'business_ref': 'businessref_43', 'business_id': 'businessid_43'}, {'business_ref': 'businessref_17', 'business_id': 'businessid_17'}, {'business_ref': 'businessref_25', 'business_id': 'businessid_25'}, {'business_ref': 'businessref_66', 'business_id': 'businessid_66'}, {'business_ref': 'businessref_99', 'business_id': 'businessid_99'}, {'business_ref': 'businessref_31', 'business_id': 'businessid_31'}, {'business_ref': 'businessref_40', 'business_id': 'businessid_40'}, {'business_ref': 'businessref_92', 'business_id': 'businessid_92'}, {'business_ref': 'businessref_83', 'business_id': 'businessid_83'}, {'business_ref': 'businessref_95', 'business_id': 'businessid_95'}, {'business_ref': 'businessref_61', 'business_id': 'businessid_61'}, {'business_ref': 'businessref_26', 'business_id': 'businessid_26'}, {'business_ref': 'businessref_68', 'business_id': 'businessid_68'}, {'business_ref': 'businessref_34', 'business_id': 'businessid_34'}, {'business_ref': 'businessref_21', 'business_id': 'businessid_21'}, {'business_ref': 'businessref_4', 'business_id': 'businessid_4'}, {'business_ref': 'businessref_49', 'business_id': 'businessid_49'}, {'business_ref': 'businessref_10', 'business_id': 'businessid_10'}, {'business_ref': 'businessref_23', 'business_id': 'businessid_23'}, {'business_ref': 'businessref_80', 'business_id': 'businessid_80'}, {'business_ref': 'businessref_51', 'business_id': 'businessid_51'}, {'business_ref': 'businessref_45', 'business_id': 'businessid_45'}, {'business_ref': 'businessref_82', 'business_id': 'businessid_82'}, {'business_ref': 'businessref_35', 'business_id': 'businessid_35'}, {'business_ref': 'businessref_77', 'business_id': 'businessid_77'}, {'business_ref': 'businessref_50', 'business_id': 'businessid_50'}, {'business_ref': 'businessref_76', 'business_id': 'businessid_76'}, {'business_ref': 'businessref_27', 'business_id': 'businessid_27'}, {'business_ref': 'businessref_3', 'business_id': 'businessid_3'}, {'business_ref': 'businessref_20', 'business_id': 'businessid_20'}, {'business_ref': 'businessref_28', 'business_id': 'businessid_28'}, {'business_ref': 'businessref_22', 'business_id': 'businessid_22'}, {'business_ref': 'businessref_69', 'business_id': 'businessid_69'}, {'business_ref': 'businessref_14', 'business_id': 'businessid_14'}, {'business_ref': 'businessref_70', 'business_id': 'businessid_70'}, {'business_ref': 'businessref_18', 'business_id': 'businessid_18'}, {'business_ref': 'businessref_6', 'business_id': 'businessid_6'}, {'business_ref': 'businessref_47', 'business_id': 'businessid_47'}, {'business_ref': 'businessref_91', 'business_id': 'businessid_91'}, {'business_ref': 'businessref_71', 'business_id': 'businessid_71'}, {'business_ref': 'businessref_46', 'business_id': 'businessid_46'}, {'business_ref': 'businessref_73', 'business_id': 'businessid_73'}, {'business_ref': 'businessref_59', 'business_id': 'businessid_59'}, {'business_ref': 'businessref_29', 'business_id': 'businessid_29'}, {'business_ref': 'businessref_86', 'business_id': 'businessid_86'}, {'business_ref': 'businessref_8', 'business_id': 'businessid_8'}, {'business_ref': 'businessref_72', 'business_id': 'businessid_72'}, {'business_ref': 'businessref_62', 'business_id': 'businessid_62'}, {'business_ref': 'businessref_85', 'business_id': 'businessid_85'}, {'business_ref': 'businessref_57', 'business_id': 'businessid_57'}, {'business_ref': 'businessref_56', 'business_id': 'businessid_56'}, {'business_ref': 'businessref_90', 'business_id': 'businessid_90'}, {'business_ref': 'businessref_97', 'business_id': 'businessid_97'}, {'business_ref': 'businessref_37', 'business_id': 'businessid_37'}]}

exec(code, env_args)
