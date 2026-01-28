code = """import json, ast
# Access previous tool results
review_records = var_call_kn3ZxO8OXPafTcJTzRQGkoTY
parking_records = var_call_uCK6h8ApW8FAzTHd7GNsfUJE

# Build set of business_ids that had reviews in 2018
reviewed_ids = set()
for r in review_records:
    br = r.get('business_ref')
    if br and br.startswith('businessref_'):
        reviewed_ids.add(br.replace('businessref_', 'businessid_'))

# Check which parking records correspond to reviewed businesses and offer parking
matching = set()
for rec in parking_records:
    bid = rec.get('business_id')
    if bid not in reviewed_ids:
        continue
    attrs = rec.get('attributes') or {}
    offers = False
    # Check BikeParking
    bp = attrs.get('BikeParking')
    if isinstance(bp, str):
        if bp.lower() == 'true':
            offers = True
    elif bp is True:
        offers = True
    # Check BusinessParking
    bp_str = attrs.get('BusinessParking')
    if not offers and bp_str:
        try:
            parsed = ast.literal_eval(bp_str)
            if isinstance(parsed, dict):
                for v in parsed.values():
                    if v is True or (isinstance(v, str) and v.lower() == 'true'):
                        offers = True
                        break
        except Exception:
            # If parsing fails, do a textual check for 'True'
            if 'True' in str(bp_str):
                offers = True
    if offers:
        matching.add(bid)

count = len(matching)

print("__RESULT__:")
print(json.dumps(count))"""

env_args = {'var_call_RSXHHdw8XPSta4jRSPo0foVt': ['checkin', 'business'], 'var_call_kVOpg2TMmo6IeUKQdoeAXkCL': ['review', 'tip', 'user'], 'var_call_kn3ZxO8OXPafTcJTzRQGkoTY': [{'business_ref': 'businessref_13'}, {'business_ref': 'businessref_79'}, {'business_ref': 'businessref_66'}, {'business_ref': 'businessref_25'}, {'business_ref': 'businessref_59'}, {'business_ref': 'businessref_67'}, {'business_ref': 'businessref_15'}, {'business_ref': 'businessref_91'}, {'business_ref': 'businessref_46'}, {'business_ref': 'businessref_47'}, {'business_ref': 'businessref_73'}, {'business_ref': 'businessref_24'}, {'business_ref': 'businessref_36'}, {'business_ref': 'businessref_99'}, {'business_ref': 'businessref_17'}, {'business_ref': 'businessref_43'}, {'business_ref': 'businessref_80'}, {'business_ref': 'businessref_86'}, {'business_ref': 'businessref_62'}, {'business_ref': 'businessref_8'}, {'business_ref': 'businessref_57'}, {'business_ref': 'businessref_37'}, {'business_ref': 'businessref_40'}, {'business_ref': 'businessref_83'}, {'business_ref': 'businessref_26'}, {'business_ref': 'businessref_4'}, {'business_ref': 'businessref_68'}, {'business_ref': 'businessref_82'}, {'business_ref': 'businessref_35'}, {'business_ref': 'businessref_45'}, {'business_ref': 'businessref_77'}, {'business_ref': 'businessref_27'}, {'business_ref': 'businessref_20'}, {'business_ref': 'businessref_22'}, {'business_ref': 'businessref_14'}, {'business_ref': 'businessref_28'}], 'var_call_uCK6h8ApW8FAzTHd7GNsfUJE': [{'business_id': 'businessid_47', 'attributes': {'ByAppointmentOnly': 'False', 'BusinessAcceptsCreditCards': 'True', 'GoodForKids': 'True', 'RestaurantsPriceRange2': '2', 'BikeParking': 'False', 'BusinessParking': "{'garage': False, 'street': False, 'validated': False, 'lot': True, 'valet': False}"}}, {'business_id': 'businessid_88', 'attributes': {'BusinessParking': "{'garage': False, 'street': False, 'validated': False, 'lot': False, 'valet': False}", 'GoodForKids': 'True', 'BusinessAcceptsCreditCards': 'True', 'ByAppointmentOnly': 'False', 'BikeParking': 'True'}}, {'business_id': 'businessid_33', 'attributes': {'BusinessParking': "{'garage': False, 'street': False, 'validated': False, 'lot': False, 'valet': False}", 'BusinessAcceptsCreditCards': 'True', 'AcceptsInsurance': 'False', 'ByAppointmentOnly': 'False', 'RestaurantsPriceRange2': '2', 'WheelchairAccessible': 'True', 'BikeParking': 'False'}}, {'business_id': 'businessid_74', 'attributes': {'BusinessParking': "{'garage': False, 'street': False, 'validated': False, 'lot': False, 'valet': False}", 'RestaurantsPriceRange2': '4', 'BikeParking': 'False'}}, {'business_id': 'businessid_92', 'attributes': {'ByAppointmentOnly': 'False', 'BusinessAcceptsCreditCards': 'True', 'BusinessParking': "{'garage': True, 'street': False, 'validated': False, 'lot': False, 'valet': False}", 'RestaurantsPriceRange2': '2', 'WheelchairAccessible': 'True', 'BikeParking': 'True', 'NoiseLevel': "u'quiet'", 'WiFi': "u'no'"}}]}

exec(code, env_args)
