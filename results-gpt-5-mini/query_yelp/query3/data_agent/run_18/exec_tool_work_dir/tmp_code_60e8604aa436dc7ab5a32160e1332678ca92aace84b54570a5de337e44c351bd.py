code = """import json
# data from previous queries
reviews = var_call_etjbVjnCNmfPbscqCP8OeN3J
businesses = var_call_KuppnjVJcQZ0DsE6bLlaxJgr

# Build set of business_ids corresponding to reviews in 2018
target_ids = set()
for r in reviews:
    br = r.get('business_ref')
    if not br: 
        continue
    parts = br.split('_', 1)
    if len(parts) == 2:
        target_ids.add('businessid_' + parts[1])

# Helper to determine if attributes indicate bike or business parking
def offers_parking(attrs):
    if not attrs:
        return False
    # sometimes attributes may be the string "None"
    if isinstance(attrs, str):
        if attrs.strip().lower() == 'none':
            return False
        # attempt to look for parking indicators in the string
        s = attrs.lower()
        if 'bike' in s and 'true' in s:
            return True
        if 'parking' in s and 'true' in s:
            return True
        return False
    # if dict-like
    try:
        for k, v in attrs.items():
            kl = str(k).lower()
            vs = str(v).lower()
            if 'bike' in kl:
                if 'true' in vs or 'yes' in vs:
                    return True
            if 'parking' in kl:
                # value might be a stringified dict; check if any True present
                if 'true' in vs or 'yes' in vs:
                    return True
        return False
    except Exception:
        return False

# Count businesses among target_ids that offer either business parking or bike parking
count = 0
matched_ids = set()
for b in businesses:
    bid = b.get('business_id')
    if bid in target_ids:
        attrs = b.get('attributes')
        if offers_parking(attrs):
            count += 1
            matched_ids.add(bid)

# Prepare result
result = json.dumps(count)
print("__RESULT__:")
print(result)"""

env_args = {'var_call_etjbVjnCNmfPbscqCP8OeN3J': [{'business_ref': 'businessref_91'}, {'business_ref': 'businessref_46'}, {'business_ref': 'businessref_47'}, {'business_ref': 'businessref_73'}, {'business_ref': 'businessref_13'}, {'business_ref': 'businessref_79'}, {'business_ref': 'businessref_66'}, {'business_ref': 'businessref_25'}, {'business_ref': 'businessref_67'}, {'business_ref': 'businessref_15'}, {'business_ref': 'businessref_59'}, {'business_ref': 'businessref_24'}, {'business_ref': 'businessref_36'}, {'business_ref': 'businessref_99'}, {'business_ref': 'businessref_17'}, {'business_ref': 'businessref_43'}, {'business_ref': 'businessref_80'}, {'business_ref': 'businessref_86'}, {'business_ref': 'businessref_62'}, {'business_ref': 'businessref_8'}, {'business_ref': 'businessref_57'}, {'business_ref': 'businessref_37'}, {'business_ref': 'businessref_40'}, {'business_ref': 'businessref_83'}, {'business_ref': 'businessref_26'}, {'business_ref': 'businessref_4'}, {'business_ref': 'businessref_68'}, {'business_ref': 'businessref_82'}, {'business_ref': 'businessref_35'}, {'business_ref': 'businessref_45'}, {'business_ref': 'businessref_77'}, {'business_ref': 'businessref_27'}, {'business_ref': 'businessref_20'}, {'business_ref': 'businessref_22'}, {'business_ref': 'businessref_14'}, {'business_ref': 'businessref_28'}], 'var_call_KuppnjVJcQZ0DsE6bLlaxJgr': [{'business_id': 'businessid_49', 'attributes': {'BusinessAcceptsCreditCards': 'True', 'WiFi': "u'no'", 'BusinessAcceptsBitcoin': 'False'}}, {'business_id': 'businessid_47', 'attributes': {'ByAppointmentOnly': 'False', 'BusinessAcceptsCreditCards': 'True', 'GoodForKids': 'True', 'RestaurantsPriceRange2': '2', 'BikeParking': 'False', 'BusinessParking': "{'garage': False, 'street': False, 'validated': False, 'lot': True, 'valet': False}"}}, {'business_id': 'businessid_88', 'attributes': {'BusinessParking': "{'garage': False, 'street': False, 'validated': False, 'lot': False, 'valet': False}", 'GoodForKids': 'True', 'BusinessAcceptsCreditCards': 'True', 'ByAppointmentOnly': 'False', 'BikeParking': 'True'}}, {'business_id': 'businessid_41', 'attributes': 'None'}, {'business_id': 'businessid_33', 'attributes': {'BusinessParking': "{'garage': False, 'street': False, 'validated': False, 'lot': False, 'valet': False}", 'BusinessAcceptsCreditCards': 'True', 'AcceptsInsurance': 'False', 'ByAppointmentOnly': 'False', 'RestaurantsPriceRange2': '2', 'WheelchairAccessible': 'True', 'BikeParking': 'False'}}]}

exec(code, env_args)
