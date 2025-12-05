code = """import json
import pandas as pd

# load full business query result
with open(var_call_BjwboPeKOzPLU18IiPiW3TYC, 'r') as f:
    data = json.load(f)

df = pd.DataFrame(data)

count = 0
for attrs in df['attributes']:
    if attrs is None or attrs == "None":
        continue
    # attrs is a dict
    has_bike = False
    has_parking = False
    if isinstance(attrs, dict):
        if 'BikeParking' in attrs and attrs['BikeParking'] is not None and attrs['BikeParking'] != "False":
            has_bike = True
        if 'BusinessParking' in attrs and attrs['BusinessParking'] is not None and attrs['BusinessParking'] != "None":
            has_parking = True
    if has_bike or has_parking:
        count += 1

result = json.dumps(count)
print('__RESULT__:')
print(result)"""

env_args = {'var_call_8OV662A59X2rVWoFH4gwxWEG': ['checkin', 'business'], 'var_call_psty2J59j1z2KXSgg0h7MgnR': [{'business_ref': 'businessref_13'}, {'business_ref': 'businessref_79'}, {'business_ref': 'businessref_66'}, {'business_ref': 'businessref_25'}, {'business_ref': 'businessref_59'}, {'business_ref': 'businessref_67'}, {'business_ref': 'businessref_15'}, {'business_ref': 'businessref_91'}, {'business_ref': 'businessref_46'}, {'business_ref': 'businessref_47'}, {'business_ref': 'businessref_73'}, {'business_ref': 'businessref_24'}, {'business_ref': 'businessref_36'}, {'business_ref': 'businessref_17'}, {'business_ref': 'businessref_43'}, {'business_ref': 'businessref_80'}, {'business_ref': 'businessref_86'}, {'business_ref': 'businessref_62'}, {'business_ref': 'businessref_8'}, {'business_ref': 'businessref_57'}, {'business_ref': 'businessref_37'}, {'business_ref': 'businessref_40'}, {'business_ref': 'businessref_83'}, {'business_ref': 'businessref_26'}, {'business_ref': 'businessref_4'}, {'business_ref': 'businessref_68'}, {'business_ref': 'businessref_77'}, {'business_ref': 'businessref_27'}, {'business_ref': 'businessref_20'}, {'business_ref': 'businessref_22'}, {'business_ref': 'businessref_14'}, {'business_ref': 'businessref_28'}, {'business_ref': 'businessref_82'}, {'business_ref': 'businessref_35'}, {'business_ref': 'businessref_45'}, {'business_ref': 'businessref_99'}], 'var_call_SkPpomADlEmM7Lt0o4nugVYD': ['businessid_13', 'businessid_79', 'businessid_66', 'businessid_25', 'businessid_59', 'businessid_67', 'businessid_15', 'businessid_91', 'businessid_46', 'businessid_47', 'businessid_73', 'businessid_24', 'businessid_36', 'businessid_17', 'businessid_43', 'businessid_80', 'businessid_86', 'businessid_62', 'businessid_8', 'businessid_57', 'businessid_37', 'businessid_40', 'businessid_83', 'businessid_26', 'businessid_4', 'businessid_68', 'businessid_77', 'businessid_27', 'businessid_20', 'businessid_22', 'businessid_14', 'businessid_28', 'businessid_82', 'businessid_35', 'businessid_45', 'businessid_99'], 'var_call_BjwboPeKOzPLU18IiPiW3TYC': 'file_storage/call_BjwboPeKOzPLU18IiPiW3TYC.json'}

exec(code, env_args)
