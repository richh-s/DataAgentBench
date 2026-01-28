code = """import pandas as pd
import ast
import json

# Data from previous queries
reviews = var_call_2d8ieAUtb3C1tEw8oURDQWIL
businesses = var_call_NTqtfrcYg90WwtUV28UdY6Ib

# Build set of businessids corresponding to reviews in 2018
review_businessids = set()
for r in reviews:
    br = r.get('business_ref')
    if br and br.startswith('businessref_'):
        review_businessids.add('businessid_' + br.split('_', 1)[1])

# Helper to determine if attributes indicate offering parking
def offers_parking(attrs):
    if attrs is None:
        return False
    # If attributes is the string "None"
    if isinstance(attrs, str):
        s = attrs.strip()
        if s == 'None':
            return False
        # Try to parse string representation of dict
        try:
            parsed = ast.literal_eval(s)
            attrs = parsed
        except Exception:
            # cannot parse, inspect raw string for indicators
            if 'BikeParking' in s and 'True' in s:
                return True
            if 'BusinessParking' in s and 'True' in s:
                return True
            return False
    # Now attrs should be a dict-like
    if isinstance(attrs, dict):
        # Check BikeParking key
        bike = None
        for key in ['BikeParking', 'bikeparking', 'Bike parking', 'bike_parking']:
            if key in attrs:
                bike = attrs.get(key)
                break
        if bike is not None:
            if isinstance(bike, bool):
                if bike:
                    return True
            else:
                # string values like 'True', 'False', "u'no'"
                bstr = str(bike).lower()
                if 'true' in bstr or 'yes' in bstr or 'y' == bstr:
                    return True
        # Check BusinessParking
        for key in ['BusinessParking', 'businessparking', 'Business Parking']:
            if key in attrs:
                bp = attrs.get(key)
                # bp might be a dict or string containing a dict
                if isinstance(bp, dict):
                    for v in bp.values():
                        if isinstance(v, bool) and v:
                            return True
                        if isinstance(v, str) and ('true' in v.lower() or 'yes' in v.lower()):
                            return True
                elif isinstance(bp, str):
                    # try parse
                    try:
                        parsed_bp = ast.literal_eval(bp)
                        if isinstance(parsed_bp, dict):
                            for v in parsed_bp.values():
                                if isinstance(v, bool) and v:
                                    return True
                                if isinstance(v, str) and ('true' in v.lower() or 'yes' in v.lower()):
                                    return True
                    except Exception:
                        # fallback: check if 'True' present
                        if 'True' in bp or 'true' in bp or 'Yes' in bp:
                            return True
        return False
    return False

# Count businesses that are in review list and offer either parking
count = 0
matching_businesses = []
for b in businesses:
    bid = b.get('business_id')
    if bid in review_businessids:
        attrs = b.get('attributes')
        if offers_parking(attrs):
            count += 1
            matching_businesses.append(bid)

result = {"count": count, "businesses": matching_businesses}
print("__RESULT__:")
print(json.dumps(result))"""

env_args = {'var_call_2d8ieAUtb3C1tEw8oURDQWIL': [{'business_ref': 'businessref_13'}, {'business_ref': 'businessref_79'}, {'business_ref': 'businessref_66'}, {'business_ref': 'businessref_25'}, {'business_ref': 'businessref_91'}, {'business_ref': 'businessref_46'}, {'business_ref': 'businessref_47'}, {'business_ref': 'businessref_73'}, {'business_ref': 'businessref_59'}, {'business_ref': 'businessref_67'}, {'business_ref': 'businessref_15'}, {'business_ref': 'businessref_17'}, {'business_ref': 'businessref_43'}, {'business_ref': 'businessref_99'}, {'business_ref': 'businessref_80'}, {'business_ref': 'businessref_86'}, {'business_ref': 'businessref_62'}, {'business_ref': 'businessref_8'}, {'business_ref': 'businessref_57'}, {'business_ref': 'businessref_37'}, {'business_ref': 'businessref_26'}, {'business_ref': 'businessref_4'}, {'business_ref': 'businessref_68'}, {'business_ref': 'businessref_82'}, {'business_ref': 'businessref_35'}, {'business_ref': 'businessref_45'}, {'business_ref': 'businessref_77'}, {'business_ref': 'businessref_27'}, {'business_ref': 'businessref_20'}, {'business_ref': 'businessref_22'}, {'business_ref': 'businessref_14'}, {'business_ref': 'businessref_28'}, {'business_ref': 'businessref_40'}, {'business_ref': 'businessref_83'}, {'business_ref': 'businessref_24'}, {'business_ref': 'businessref_36'}], 'var_call_NTqtfrcYg90WwtUV28UdY6Ib': [{'business_id': 'businessid_49', 'attributes': {'BusinessAcceptsCreditCards': 'True', 'WiFi': "u'no'", 'BusinessAcceptsBitcoin': 'False'}}, {'business_id': 'businessid_47', 'attributes': {'ByAppointmentOnly': 'False', 'BusinessAcceptsCreditCards': 'True', 'GoodForKids': 'True', 'RestaurantsPriceRange2': '2', 'BikeParking': 'False', 'BusinessParking': "{'garage': False, 'street': False, 'validated': False, 'lot': True, 'valet': False}"}}, {'business_id': 'businessid_88', 'attributes': {'BusinessParking': "{'garage': False, 'street': False, 'validated': False, 'lot': False, 'valet': False}", 'GoodForKids': 'True', 'BusinessAcceptsCreditCards': 'True', 'ByAppointmentOnly': 'False', 'BikeParking': 'True'}}, {'business_id': 'businessid_41', 'attributes': 'None'}, {'business_id': 'businessid_33', 'attributes': {'BusinessParking': "{'garage': False, 'street': False, 'validated': False, 'lot': False, 'valet': False}", 'BusinessAcceptsCreditCards': 'True', 'AcceptsInsurance': 'False', 'ByAppointmentOnly': 'False', 'RestaurantsPriceRange2': '2', 'WheelchairAccessible': 'True', 'BikeParking': 'False'}}]}

exec(code, env_args)
