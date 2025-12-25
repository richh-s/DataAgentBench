code = """import json, pandas as pd

reviews_2018 = var_call_EFBglayqzh1CEjRZLOctdZUd

# map businessref_X -> businessid_X
business_ids_2018 = set()
for r in reviews_2018:
    bref = r['business_ref']
    if bref.startswith('businessref_'):
        suffix = bref.split('businessref_')[1]
        business_ids_2018.add('businessid_' + suffix)

# load full business attributes file
with open(var_call_Sz0OSGIMXghl09YnZczhInKK, 'r') as f:
    business_records = json.load(f)

count = 0
for b in business_records:
    bid = b.get('business_id')
    if bid not in business_ids_2018:
        continue
    attrs = b.get('attributes')
    if not isinstance(attrs, dict):
        continue
    has_bike = attrs.get('BikeParking') == 'True'
    has_business_parking = False
    bp = attrs.get('BusinessParking')
    if isinstance(bp, str) and bp not in ("None", "null", "NULL"):
        # consider any non-empty parking dict as offering business parking
        if bp.strip().startswith('{') and 'True' in bp:
            has_business_parking = True
    if has_bike or has_business_parking:
        count += 1

result = json.dumps(count)
print("__RESULT__:")
print(result)"""

env_args = {'var_call_z3z6cwRQJ690NrKEa8La8BtS': ['business', 'checkin'], 'var_call_EFBglayqzh1CEjRZLOctdZUd': [{'business_ref': 'businessref_13'}, {'business_ref': 'businessref_79'}, {'business_ref': 'businessref_91'}, {'business_ref': 'businessref_46'}, {'business_ref': 'businessref_47'}, {'business_ref': 'businessref_73'}, {'business_ref': 'businessref_66'}, {'business_ref': 'businessref_25'}, {'business_ref': 'businessref_59'}, {'business_ref': 'businessref_24'}, {'business_ref': 'businessref_36'}, {'business_ref': 'businessref_17'}, {'business_ref': 'businessref_43'}, {'business_ref': 'businessref_99'}, {'business_ref': 'businessref_80'}, {'business_ref': 'businessref_86'}, {'business_ref': 'businessref_62'}, {'business_ref': 'businessref_8'}, {'business_ref': 'businessref_57'}, {'business_ref': 'businessref_37'}, {'business_ref': 'businessref_67'}, {'business_ref': 'businessref_15'}, {'business_ref': 'businessref_40'}, {'business_ref': 'businessref_83'}, {'business_ref': 'businessref_82'}, {'business_ref': 'businessref_35'}, {'business_ref': 'businessref_45'}, {'business_ref': 'businessref_77'}, {'business_ref': 'businessref_27'}, {'business_ref': 'businessref_20'}, {'business_ref': 'businessref_22'}, {'business_ref': 'businessref_14'}, {'business_ref': 'businessref_28'}, {'business_ref': 'businessref_26'}, {'business_ref': 'businessref_4'}, {'business_ref': 'businessref_68'}], 'var_call_Sz0OSGIMXghl09YnZczhInKK': 'file_storage/call_Sz0OSGIMXghl09YnZczhInKK.json'}

exec(code, env_args)
