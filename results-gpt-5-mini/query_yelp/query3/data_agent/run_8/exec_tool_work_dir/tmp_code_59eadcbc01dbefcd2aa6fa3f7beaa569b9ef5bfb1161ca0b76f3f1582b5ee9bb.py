code = """import json
import ast
# available variables from storage: var_call_fx0FhwpQsvDHSBCQErnXLWe1, var_call_ckxpnwJoEYB4SLJfnZTHbxmM
review_refs = [r['business_ref'] for r in var_call_fx0FhwpQsvDHSBCQErnXLWe1]
review_ids = [r.replace('businessref_','businessid_') for r in review_refs]
# build dict of business attributes from business collection
biz_docs = {d['business_id']: d.get('attributes') for d in var_call_ckxpnwJoEYB4SLJfnZTHbxmM}

def parse_bool_val(v):
    if isinstance(v, bool):
        return v
    if v is None:
        return False
    # v might be strings like "True", "False", "u'no'", "" or numeric
    s = str(v).lower()
    if 'true' in s:
        return True
    if 'yes' in s:
        return True
    if '1' == s:
        return True
    return False

count = 0
matching_biz_ids = []
for bid in review_ids:
    if bid not in biz_docs:
        continue
    attrs = biz_docs[bid]
    has_parking = False
    if not attrs or attrs == 'None':
        pass
    else:
        # attrs may be a dict
        if isinstance(attrs, dict):
            # BikeParking check
            if 'BikeParking' in attrs:
                if parse_bool_val(attrs['BikeParking']):
                    has_parking = True
            # BusinessParking or BusinessParking variants
            for k in attrs:
                if 'parking' in k.lower() and k.lower() != 'bikeparking':
                    val = attrs[k]
                    # val may be string repr of dict
                    if isinstance(val, dict):
                        for vv in val.values():
                            if parse_bool_val(vv):
                                has_parking = True
                                break
                    else:
                        # try to literal_eval
                        try:
                            parsed = ast.literal_eval(val)
                            if isinstance(parsed, dict):
                                for vv in parsed.values():
                                    if parse_bool_val(vv):
                                        has_parking = True
                                        break
                        except Exception:
                            # fallback: check string
                            if parse_bool_val(val):
                                has_parking = True
        else:
            # attrs is a string that might contain entries
            s = str(attrs)
            # look for BikeParking True
            if 'bikeparking' in s.lower() and 'true' in s.lower():
                has_parking = True
            if 'businessparking' in s.lower() and 'true' in s.lower():
                has_parking = True
    if has_parking:
        count += 1
        matching_biz_ids.append(bid)

result = {'count': count, 'business_ids': matching_biz_ids}
print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_call_fx0FhwpQsvDHSBCQErnXLWe1': [{'business_ref': 'businessref_91'}, {'business_ref': 'businessref_46'}, {'business_ref': 'businessref_47'}, {'business_ref': 'businessref_73'}, {'business_ref': 'businessref_66'}, {'business_ref': 'businessref_25'}, {'business_ref': 'businessref_59'}, {'business_ref': 'businessref_67'}, {'business_ref': 'businessref_15'}, {'business_ref': 'businessref_24'}, {'business_ref': 'businessref_36'}, {'business_ref': 'businessref_99'}, {'business_ref': 'businessref_80'}, {'business_ref': 'businessref_86'}, {'business_ref': 'businessref_62'}, {'business_ref': 'businessref_8'}, {'business_ref': 'businessref_57'}, {'business_ref': 'businessref_37'}, {'business_ref': 'businessref_40'}, {'business_ref': 'businessref_83'}, {'business_ref': 'businessref_17'}, {'business_ref': 'businessref_43'}, {'business_ref': 'businessref_26'}, {'business_ref': 'businessref_4'}, {'business_ref': 'businessref_68'}, {'business_ref': 'businessref_77'}, {'business_ref': 'businessref_27'}, {'business_ref': 'businessref_82'}, {'business_ref': 'businessref_35'}, {'business_ref': 'businessref_45'}, {'business_ref': 'businessref_20'}, {'business_ref': 'businessref_22'}, {'business_ref': 'businessref_14'}, {'business_ref': 'businessref_28'}, {'business_ref': 'businessref_13'}, {'business_ref': 'businessref_79'}], 'var_call_TTOQuSawLxJqGnUScx1SKlQZ': ['businessid_91', 'businessid_46', 'businessid_47', 'businessid_73', 'businessid_66', 'businessid_25', 'businessid_59', 'businessid_67', 'businessid_15', 'businessid_24', 'businessid_36', 'businessid_99', 'businessid_80', 'businessid_86', 'businessid_62', 'businessid_8', 'businessid_57', 'businessid_37', 'businessid_40', 'businessid_83', 'businessid_17', 'businessid_43', 'businessid_26', 'businessid_4', 'businessid_68', 'businessid_77', 'businessid_27', 'businessid_82', 'businessid_35', 'businessid_45', 'businessid_20', 'businessid_22', 'businessid_14', 'businessid_28', 'businessid_13', 'businessid_79'], 'var_call_ckxpnwJoEYB4SLJfnZTHbxmM': [{'business_id': 'businessid_49', 'attributes': {'BusinessAcceptsCreditCards': 'True', 'WiFi': "u'no'", 'BusinessAcceptsBitcoin': 'False'}}, {'business_id': 'businessid_47', 'attributes': {'ByAppointmentOnly': 'False', 'BusinessAcceptsCreditCards': 'True', 'GoodForKids': 'True', 'RestaurantsPriceRange2': '2', 'BikeParking': 'False', 'BusinessParking': "{'garage': False, 'street': False, 'validated': False, 'lot': True, 'valet': False}"}}, {'business_id': 'businessid_88', 'attributes': {'BusinessParking': "{'garage': False, 'street': False, 'validated': False, 'lot': False, 'valet': False}", 'GoodForKids': 'True', 'BusinessAcceptsCreditCards': 'True', 'ByAppointmentOnly': 'False', 'BikeParking': 'True'}}, {'business_id': 'businessid_41', 'attributes': 'None'}, {'business_id': 'businessid_33', 'attributes': {'BusinessParking': "{'garage': False, 'street': False, 'validated': False, 'lot': False, 'valet': False}", 'BusinessAcceptsCreditCards': 'True', 'AcceptsInsurance': 'False', 'ByAppointmentOnly': 'False', 'RestaurantsPriceRange2': '2', 'WheelchairAccessible': 'True', 'BikeParking': 'False'}}]}

exec(code, env_args)
