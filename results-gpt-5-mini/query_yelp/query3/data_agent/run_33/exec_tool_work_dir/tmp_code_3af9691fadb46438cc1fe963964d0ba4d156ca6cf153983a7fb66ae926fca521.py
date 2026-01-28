code = """import pandas as pd
import ast

# Load variables from previous tool calls
records = var_call_mSXSyeKcQr0cHuB7IJ1KbEs9
business_docs = var_call_2ap7cn9zKr204DPnPMXxtVta

# Create set of business_ids corresponding to reviews in 2018
business_refs = [r['business_ref'] for r in records]
business_ids_needed = set([br.replace('businessref_', 'businessid_') for br in business_refs])

# Create dict from returned business docs
biz_dict = {b['business_id']: b for b in business_docs}

count = 0
matching_businesses = []

for bid in business_ids_needed:
    b = biz_dict.get(bid)
    if not b:
        continue
    attrs = b.get('attributes') or {}
    has_bike = False
    has_business_parking = False
    # Check BikeParking
    bp = attrs.get('BikeParking')
    if bp is not None:
        if isinstance(bp, bool):
            has_bike = bp
        else:
            s = str(bp).strip()
            if s.lower() == 'true':
                has_bike = True
            else:
                has_bike = False
    # Check BusinessParking
    bpar = attrs.get('BusinessParking')
    if bpar is not None and str(bpar).strip().lower() != 'none':
        # Try to parse dict-like string or accept dict
        parsed = None
        if isinstance(bpar, dict):
            parsed = bpar
        else:
            s = str(bpar).strip()
            try:
                parsed = ast.literal_eval(s)
            except Exception:
                parsed = None
        if isinstance(parsed, dict):
            # If any value is True, consider as having parking
            for v in parsed.values():
                if isinstance(v, bool) and v:
                    has_business_parking = True
                    break
                # sometimes values are strings 'True'/'False'
                if isinstance(v, str) and v.lower() == 'true':
                    has_business_parking = True
                    break
    # If either is True, count
    if has_bike or has_business_parking:
        count += 1
        matching_businesses.append(bid)

# Prepare result
result = {"count": count, "matching_business_ids": sorted(matching_businesses)}

import json
print("__RESULT__:")
print(json.dumps(result))"""

env_args = {'var_call_23YN6jmA0MzbWWmP5lKnsj0n': ['checkin', 'business'], 'var_call_5ujM0hkcXrQysN7C1D55ykv5': ['review', 'tip', 'user'], 'var_call_mSXSyeKcQr0cHuB7IJ1KbEs9': [{'business_ref': 'businessref_13'}, {'business_ref': 'businessref_79'}, {'business_ref': 'businessref_91'}, {'business_ref': 'businessref_46'}, {'business_ref': 'businessref_47'}, {'business_ref': 'businessref_73'}, {'business_ref': 'businessref_59'}, {'business_ref': 'businessref_67'}, {'business_ref': 'businessref_15'}, {'business_ref': 'businessref_24'}, {'business_ref': 'businessref_36'}, {'business_ref': 'businessref_17'}, {'business_ref': 'businessref_66'}, {'business_ref': 'businessref_25'}, {'business_ref': 'businessref_99'}, {'business_ref': 'businessref_86'}, {'business_ref': 'businessref_62'}, {'business_ref': 'businessref_8'}, {'business_ref': 'businessref_57'}, {'business_ref': 'businessref_37'}, {'business_ref': 'businessref_80'}, {'business_ref': 'businessref_40'}, {'business_ref': 'businessref_83'}, {'business_ref': 'businessref_26'}, {'business_ref': 'businessref_4'}, {'business_ref': 'businessref_68'}, {'business_ref': 'businessref_82'}, {'business_ref': 'businessref_35'}, {'business_ref': 'businessref_45'}, {'business_ref': 'businessref_77'}, {'business_ref': 'businessref_27'}, {'business_ref': 'businessref_20'}, {'business_ref': 'businessref_22'}, {'business_ref': 'businessref_14'}, {'business_ref': 'businessref_28'}], 'var_call_2ap7cn9zKr204DPnPMXxtVta': [{'business_id': 'businessid_47', 'name': 'Breeze Blow Dry Bar', 'attributes': {'ByAppointmentOnly': 'False', 'BusinessAcceptsCreditCards': 'True', 'GoodForKids': 'True', 'RestaurantsPriceRange2': '2', 'BikeParking': 'False', 'BusinessParking': "{'garage': False, 'street': False, 'validated': False, 'lot': True, 'valet': False}"}}, {'business_id': 'businessid_8', 'name': 'Uber', 'attributes': {'BusinessAcceptsCreditCards': 'True'}}, {'business_id': 'businessid_59', 'name': 'Chestnut St. Cafe', 'attributes': {'BusinessParking': "{'garage': False, 'street': True, 'validated': False, 'lot': False, 'valet': False}", 'RestaurantsTakeOut': 'None', 'RestaurantsDelivery': 'None', 'HasTV': 'True', 'Ambience': "{'touristy': False, 'hipster': None, 'romantic': None, 'divey': None, 'intimate': None, 'trendy': None, 'upscale': False, 'classy': None, 'casual': True}", 'GoodForMeal': "{'dessert': False, 'latenight': False, 'lunch': False, 'dinner': False, 'brunch': False, 'breakfast': False}"}}, {'business_id': 'businessid_91', 'name': 'Cafe Porche and snowbar', 'attributes': {'BusinessParking': "{'garage': False, 'street': True, 'validated': False, 'lot': False, 'valet': False}", 'WiFi': "u'free'", 'WheelchairAccessible': 'True', 'Caters': 'True', 'HasTV': 'True', 'HappyHour': 'False', 'Ambience': "{'touristy': None, 'hipster': None, 'romantic': None, 'divey': None, 'intimate': True, 'trendy': None, 'upscale': None, 'classy': True, 'casual': True}", 'RestaurantsDelivery': 'True', 'RestaurantsPriceRange2': '2', 'GoodForKids': 'True', 'RestaurantsAttire': "u'casual'", 'BikeParking': 'True', 'OutdoorSeating': 'True', 'NoiseLevel': "u'quiet'", 'RestaurantsGoodForGroups': 'True', 'RestaurantsTakeOut': 'True', 'BusinessAcceptsCreditCards': 'True', 'RestaurantsReservations': 'False', 'GoodForMeal': "{'dessert': None, 'latenight': None, 'lunch': True, 'dinner': None, 'brunch': True, 'breakfast': True}", 'Alcohol': "u'beer_and_wine'", 'RestaurantsTableService': 'True', 'Corkage': 'False', 'BYOB': 'True'}}, {'business_id': 'businessid_83', 'name': 'Eyeglass World', 'attributes': {'RestaurantsPriceRange2': '2', 'AcceptsInsurance': 'True', 'BusinessAcceptsCreditCards': 'True', 'BusinessParking': 'None', 'ByAppointmentOnly': 'False'}}]}

exec(code, env_args)
