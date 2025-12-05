code = """import json, os
path = var_call_xbS6VbyyNkkhimaSgjihREov
with open(path) as f:
    data = json.load(f)
count = 0
seen = set()
for r in data:
    bid = r.get('business_id')
    if bid in seen:
        continue
    seen.add(bid)
    attrs = r.get('attributes')
    if not attrs or attrs == 'None':
        continue
    if isinstance(attrs, dict):
        if 'BusinessParking' in attrs or 'BikeParking' in attrs:
            count += 1
result = json.dumps(count)
print("__RESULT__:")
print(result)"""

env_args = {'var_call_X7rmgobvmMpDDa99d7wTWahw': ['checkin', 'business'], 'var_call_XjFf8lzFDbchH7tZAZMqtQu1': [{'business_ref': 'businessref_79'}, {'business_ref': 'businessref_13'}, {'business_ref': 'businessref_44'}, {'business_ref': 'businessref_59'}, {'business_ref': 'businessref_29'}, {'business_ref': 'businessref_25'}, {'business_ref': 'businessref_66'}, {'business_ref': 'businessref_67'}, {'business_ref': 'businessref_15'}, {'business_ref': 'businessref_81'}, {'business_ref': 'businessref_33'}, {'business_ref': 'businessref_43'}, {'business_ref': 'businessref_17'}, {'business_ref': 'businessref_80'}, {'business_ref': 'businessref_51'}, {'business_ref': 'businessref_24'}, {'business_ref': 'businessref_52'}, {'business_ref': 'businessref_89'}, {'business_ref': 'businessref_36'}, {'business_ref': 'businessref_60'}, {'business_ref': 'businessref_12'}, {'business_ref': 'businessref_86'}, {'business_ref': 'businessref_8'}, {'business_ref': 'businessref_72'}, {'business_ref': 'businessref_62'}, {'business_ref': 'businessref_85'}, {'business_ref': 'businessref_57'}, {'business_ref': 'businessref_56'}, {'business_ref': 'businessref_90'}, {'business_ref': 'businessref_97'}, {'business_ref': 'businessref_37'}, {'business_ref': 'businessref_26'}, {'business_ref': 'businessref_68'}, {'business_ref': 'businessref_34'}, {'business_ref': 'businessref_21'}, {'business_ref': 'businessref_4'}, {'business_ref': 'businessref_49'}, {'business_ref': 'businessref_10'}, {'business_ref': 'businessref_23'}, {'business_ref': 'businessref_45'}, {'business_ref': 'businessref_82'}, {'business_ref': 'businessref_35'}, {'business_ref': 'businessref_77'}, {'business_ref': 'businessref_50'}, {'business_ref': 'businessref_76'}, {'business_ref': 'businessref_27'}, {'business_ref': 'businessref_3'}, {'business_ref': 'businessref_20'}, {'business_ref': 'businessref_28'}, {'business_ref': 'businessref_22'}, {'business_ref': 'businessref_69'}, {'business_ref': 'businessref_14'}, {'business_ref': 'businessref_70'}, {'business_ref': 'businessref_18'}, {'business_ref': 'businessref_40'}, {'business_ref': 'businessref_92'}, {'business_ref': 'businessref_83'}, {'business_ref': 'businessref_95'}, {'business_ref': 'businessref_61'}, {'business_ref': 'businessref_6'}, {'business_ref': 'businessref_47'}, {'business_ref': 'businessref_91'}, {'business_ref': 'businessref_71'}, {'business_ref': 'businessref_46'}, {'business_ref': 'businessref_73'}, {'business_ref': 'businessref_99'}, {'business_ref': 'businessref_31'}], 'var_call_9ODraW4qdy1MpEGRlymzvNU2': ['businessid_10', 'businessid_12', 'businessid_13', 'businessid_14', 'businessid_15', 'businessid_17', 'businessid_18', 'businessid_20', 'businessid_21', 'businessid_22', 'businessid_23', 'businessid_24', 'businessid_25', 'businessid_26', 'businessid_27', 'businessid_28', 'businessid_29', 'businessid_3', 'businessid_31', 'businessid_33', 'businessid_34', 'businessid_35', 'businessid_36', 'businessid_37', 'businessid_4', 'businessid_40', 'businessid_43', 'businessid_44', 'businessid_45', 'businessid_46', 'businessid_47', 'businessid_49', 'businessid_50', 'businessid_51', 'businessid_52', 'businessid_56', 'businessid_57', 'businessid_59', 'businessid_6', 'businessid_60', 'businessid_61', 'businessid_62', 'businessid_66', 'businessid_67', 'businessid_68', 'businessid_69', 'businessid_70', 'businessid_71', 'businessid_72', 'businessid_73', 'businessid_76', 'businessid_77', 'businessid_79', 'businessid_8', 'businessid_80', 'businessid_81', 'businessid_82', 'businessid_83', 'businessid_85', 'businessid_86', 'businessid_89', 'businessid_90', 'businessid_91', 'businessid_92', 'businessid_95', 'businessid_97', 'businessid_99'], 'var_call_xbS6VbyyNkkhimaSgjihREov': 'file_storage/call_xbS6VbyyNkkhimaSgjihREov.json'}

exec(code, env_args)
