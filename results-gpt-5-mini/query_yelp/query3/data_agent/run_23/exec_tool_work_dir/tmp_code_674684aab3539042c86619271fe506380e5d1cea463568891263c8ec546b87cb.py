code = """import json
# Access previous tool results
reviews = var_call_NiHEO90rjW63ZljbjMoOuVhg
businesses = var_call_s61JwcQOmqRpgNaf3RfxwYmA

# Build set of business_ids corresponding to reviews in 2018
biz_ids_in_reviews = set()
for r in reviews:
    br = r.get('business_ref')
    if br and br.startswith('businessref_'):
        num = br.split('_',1)[1]
        biz_ids_in_reviews.add(f'businessid_{num}')

# Check each business record for BikeParking or BusinessParking
matched = []
for b in businesses:
    bid = b.get('business_id')
    if bid not in biz_ids_in_reviews:
        continue
    attrs = b.get('attributes')
    has_parking = False
    if attrs is None:
        has_parking = False
    else:
        # attrs might be the string "None"
        if isinstance(attrs, str):
            attrs_str = attrs
            # try to detect BikeParking or BusinessParking in the string
            if 'BikeParking' in attrs_str:
                # extract value after 'BikeParking':
                # simple check for 'True' substring
                if 'True' in attrs_str or 'true' in attrs_str or 'Yes' in attrs_str or "'yes'" in attrs_str:
                    has_parking = True
            if not has_parking and 'BusinessParking' in attrs_str:
                if 'True' in attrs_str or 'true' in attrs_str or 'Yes' in attrs_str or "'yes'" in attrs_str:
                    has_parking = True
        elif isinstance(attrs, dict):
            # check BikeParking
            bp = attrs.get('BikeParking')
            if bp is not None:
                if isinstance(bp, bool):
                    if bp:
                        has_parking = True
                else:
                    if str(bp).lower().strip() in ('true','yes','1',"'yes'","u'yes'","" ):
                        has_parking = True
                    else:
                        # sometimes BikeParking is like "u'no'"
                        if 'true' in str(bp).lower() or 'yes' in str(bp).lower():
                            has_parking = True
            # check BusinessParking
            if not has_parking and 'BusinessParking' in attrs:
                bpv = attrs.get('BusinessParking')
                if bpv is None:
                    pass
                elif isinstance(bpv, dict):
                    # any True values
                    for v in bpv.values():
                        if v is True or str(v).lower()=='true':
                            has_parking = True
                            break
                else:
                    # string repr
                    if 'True' in str(bpv) or 'true' in str(bpv) or 'Yes' in str(bpv) or "'yes'" in str(bpv):
                        has_parking = True
    if has_parking:
        matched.append(bid)

count = len(set(matched))

print("__RESULT__:")
print(json.dumps(count))"""

env_args = {'var_call_qc19TY4lXcZTYOqFIgHmUSLg': ['business', 'checkin'], 'var_call_2REA1WXYVoX8sWBzDy0afddw': ['review', 'tip', 'user'], 'var_call_NiHEO90rjW63ZljbjMoOuVhg': [{'business_ref': 'businessref_13'}, {'business_ref': 'businessref_79'}, {'business_ref': 'businessref_91'}, {'business_ref': 'businessref_46'}, {'business_ref': 'businessref_47'}, {'business_ref': 'businessref_73'}, {'business_ref': 'businessref_59'}, {'business_ref': 'businessref_67'}, {'business_ref': 'businessref_15'}, {'business_ref': 'businessref_66'}, {'business_ref': 'businessref_25'}, {'business_ref': 'businessref_24'}, {'business_ref': 'businessref_36'}, {'business_ref': 'businessref_17'}, {'business_ref': 'businessref_43'}, {'business_ref': 'businessref_99'}, {'business_ref': 'businessref_80'}, {'business_ref': 'businessref_40'}, {'business_ref': 'businessref_83'}, {'business_ref': 'businessref_86'}, {'business_ref': 'businessref_62'}, {'business_ref': 'businessref_8'}, {'business_ref': 'businessref_57'}, {'business_ref': 'businessref_37'}, {'business_ref': 'businessref_26'}, {'business_ref': 'businessref_4'}, {'business_ref': 'businessref_68'}, {'business_ref': 'businessref_82'}, {'business_ref': 'businessref_35'}, {'business_ref': 'businessref_45'}, {'business_ref': 'businessref_77'}, {'business_ref': 'businessref_27'}, {'business_ref': 'businessref_20'}, {'business_ref': 'businessref_22'}, {'business_ref': 'businessref_14'}, {'business_ref': 'businessref_28'}], 'var_call_s61JwcQOmqRpgNaf3RfxwYmA': [{'business_id': 'businessid_49', 'attributes': {'BusinessAcceptsCreditCards': 'True', 'WiFi': "u'no'", 'BusinessAcceptsBitcoin': 'False'}}, {'business_id': 'businessid_47', 'attributes': {'ByAppointmentOnly': 'False', 'BusinessAcceptsCreditCards': 'True', 'GoodForKids': 'True', 'RestaurantsPriceRange2': '2', 'BikeParking': 'False', 'BusinessParking': "{'garage': False, 'street': False, 'validated': False, 'lot': True, 'valet': False}"}}, {'business_id': 'businessid_88', 'attributes': {'BusinessParking': "{'garage': False, 'street': False, 'validated': False, 'lot': False, 'valet': False}", 'GoodForKids': 'True', 'BusinessAcceptsCreditCards': 'True', 'ByAppointmentOnly': 'False', 'BikeParking': 'True'}}, {'business_id': 'businessid_41', 'attributes': 'None'}, {'business_id': 'businessid_33', 'attributes': {'BusinessParking': "{'garage': False, 'street': False, 'validated': False, 'lot': False, 'valet': False}", 'BusinessAcceptsCreditCards': 'True', 'AcceptsInsurance': 'False', 'ByAppointmentOnly': 'False', 'RestaurantsPriceRange2': '2', 'WheelchairAccessible': 'True', 'BikeParking': 'False'}}]}

exec(code, env_args)
