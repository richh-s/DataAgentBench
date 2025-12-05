code = """import json
import pandas as pd

# Load full Mongo result from file
with open(var_call_YbTWu32tQ7Xg9aIYROVo7xdK, 'r') as f:
    business_attrs = json.load(f)

# Convert to DataFrame
biz_df = pd.DataFrame(business_attrs)

# Normalize attributes column: ensure dict, handle 'None' and nulls
import ast

def has_parking_or_bike(attrs):
    if attrs is None or attrs == "None":
        return False
    if isinstance(attrs, str):
        try:
            # Some attributes fields are stringified dicts, but we only care about keys existing
            attrs_dict = ast.literal_eval(attrs)
            attrs = attrs_dict
        except Exception:
            return False
    if not isinstance(attrs, dict):
        return False
    bike = attrs.get('BikeParking')
    bizpark = attrs.get('BusinessParking')
    # BikeParking is stored as "True"/"False" strings
    has_bike = str(bike) == 'True'
    # BusinessParking is often a stringified dict; treat non-None / non-'None' as available
    has_bizpark = False
    if bizpark is not None and bizpark != 'None':
        # If it's a dict, check if any value is True
        if isinstance(bizpark, dict):
            has_bizpark = any(bool(v) for v in bizpark.values())
        else:
            # It's a string; check if it contains 'True'
            has_bizpark = 'True' in str(bizpark)
    return has_bike or has_bizpark

biz_df['has_parking_or_bike'] = biz_df['attributes'].apply(has_parking_or_bike)

count = int(biz_df['has_parking_or_bike'].sum())

result = json.dumps(count)

print("__RESULT__:")
print(result)"""

env_args = {'var_call_kjdag9xQw8y3Ew2FCpqsReEk': ['business', 'checkin'], 'var_call_HRS0vTGYjSUXlZUBl73MfZMw': [{'business_ref': 'businessref_79'}, {'business_ref': 'businessref_13'}, {'business_ref': 'businessref_44'}, {'business_ref': 'businessref_25'}, {'business_ref': 'businessref_66'}, {'business_ref': 'businessref_6'}, {'business_ref': 'businessref_47'}, {'business_ref': 'businessref_91'}, {'business_ref': 'businessref_71'}, {'business_ref': 'businessref_46'}, {'business_ref': 'businessref_73'}, {'business_ref': 'businessref_59'}, {'business_ref': 'businessref_29'}, {'business_ref': 'businessref_24'}, {'business_ref': 'businessref_52'}, {'business_ref': 'businessref_89'}, {'business_ref': 'businessref_36'}, {'business_ref': 'businessref_60'}, {'business_ref': 'businessref_12'}, {'business_ref': 'businessref_67'}, {'business_ref': 'businessref_15'}, {'business_ref': 'businessref_81'}, {'business_ref': 'businessref_33'}, {'business_ref': 'businessref_43'}, {'business_ref': 'businessref_17'}, {'business_ref': 'businessref_99'}, {'business_ref': 'businessref_31'}, {'business_ref': 'businessref_80'}, {'business_ref': 'businessref_51'}, {'business_ref': 'businessref_86'}, {'business_ref': 'businessref_8'}, {'business_ref': 'businessref_72'}, {'business_ref': 'businessref_62'}, {'business_ref': 'businessref_85'}, {'business_ref': 'businessref_57'}, {'business_ref': 'businessref_56'}, {'business_ref': 'businessref_90'}, {'business_ref': 'businessref_97'}, {'business_ref': 'businessref_37'}, {'business_ref': 'businessref_40'}, {'business_ref': 'businessref_92'}, {'business_ref': 'businessref_83'}, {'business_ref': 'businessref_95'}, {'business_ref': 'businessref_61'}, {'business_ref': 'businessref_26'}, {'business_ref': 'businessref_68'}, {'business_ref': 'businessref_34'}, {'business_ref': 'businessref_21'}, {'business_ref': 'businessref_4'}, {'business_ref': 'businessref_49'}, {'business_ref': 'businessref_10'}, {'business_ref': 'businessref_23'}, {'business_ref': 'businessref_45'}, {'business_ref': 'businessref_82'}, {'business_ref': 'businessref_35'}, {'business_ref': 'businessref_77'}, {'business_ref': 'businessref_50'}, {'business_ref': 'businessref_76'}, {'business_ref': 'businessref_27'}, {'business_ref': 'businessref_3'}, {'business_ref': 'businessref_20'}, {'business_ref': 'businessref_28'}, {'business_ref': 'businessref_22'}, {'business_ref': 'businessref_69'}, {'business_ref': 'businessref_14'}, {'business_ref': 'businessref_70'}, {'business_ref': 'businessref_18'}], 'var_call_hbiYFCebbhohAXblzN9k4tGu': {'business_ids': ['businessid_79', 'businessid_13', 'businessid_44', 'businessid_25', 'businessid_66', 'businessid_6', 'businessid_47', 'businessid_91', 'businessid_71', 'businessid_46', 'businessid_73', 'businessid_59', 'businessid_29', 'businessid_24', 'businessid_52', 'businessid_89', 'businessid_36', 'businessid_60', 'businessid_12', 'businessid_67', 'businessid_15', 'businessid_81', 'businessid_33', 'businessid_43', 'businessid_17', 'businessid_99', 'businessid_31', 'businessid_80', 'businessid_51', 'businessid_86', 'businessid_8', 'businessid_72', 'businessid_62', 'businessid_85', 'businessid_57', 'businessid_56', 'businessid_90', 'businessid_97', 'businessid_37', 'businessid_40', 'businessid_92', 'businessid_83', 'businessid_95', 'businessid_61', 'businessid_26', 'businessid_68', 'businessid_34', 'businessid_21', 'businessid_4', 'businessid_49', 'businessid_10', 'businessid_23', 'businessid_45', 'businessid_82', 'businessid_35', 'businessid_77', 'businessid_50', 'businessid_76', 'businessid_27', 'businessid_3', 'businessid_20', 'businessid_28', 'businessid_22', 'businessid_69', 'businessid_14', 'businessid_70', 'businessid_18']}, 'var_call_YbTWu32tQ7Xg9aIYROVo7xdK': 'file_storage/call_YbTWu32tQ7Xg9aIYROVo7xdK.json'}

exec(code, env_args)
