code = """import json
import ast

# Data from previous tool calls
business_refs = var_call_r2w9MULHxTd2XZkhyeE0hRNF
business_docs = var_call_YnMbPLTBZvxZiyR6u1U26znE

# Build mapping from business_id to attributes
attr_map = {doc.get('business_id'): doc.get('attributes') for doc in business_docs}

count = 0
matched_businesses = []

for brec in business_refs:
    bref = brec.get('business_ref')
    if not bref or not bref.startswith('businessref_'):
        continue
    bid = 'businessid_' + bref.split('_', 1)[1]
    attrs = attr_map.get(bid)
    has_parking = False
    if attrs:
        # Check BikeParking
        bp = attrs.get('BikeParking')
        if isinstance(bp, bool):
            if bp:
                has_parking = True
        elif isinstance(bp, str):
            if bp.lower() == 'true':
                has_parking = True
        # Check BusinessParking if not yet
        if not has_parking:
            bpark = attrs.get('BusinessParking')
            if bpark is None or (isinstance(bpark, str) and bpark.lower() == 'none'):
                pass
            else:
                # Attempt to parse dict-like string
                try:
                    if isinstance(bpark, dict):
                        parkdict = bpark
                    elif isinstance(bpark, str):
                        parkdict = ast.literal_eval(bpark)
                    else:
                        parkdict = None
                except Exception:
                    parkdict = None
                if isinstance(parkdict, dict):
                    # if any value is truthy (True or 'True') count
                    for v in parkdict.values():
                        if isinstance(v, bool) and v:
                            has_parking = True
                            break
                        if isinstance(v, str) and v.lower() == 'true':
                            has_parking = True
                            break
                else:
                    # fallback: if string contains 'True'
                    if isinstance(bpark, str) and 'True' in bpark:
                        has_parking = True
    if has_parking:
        count += 1
        matched_businesses.append(bid)

# Prepare result as a simple integer
print("__RESULT__:")
print(json.dumps(count))"""

env_args = {'var_call_r2w9MULHxTd2XZkhyeE0hRNF': [{'business_ref': 'businessref_13'}, {'business_ref': 'businessref_79'}, {'business_ref': 'businessref_91'}, {'business_ref': 'businessref_46'}, {'business_ref': 'businessref_47'}, {'business_ref': 'businessref_73'}, {'business_ref': 'businessref_66'}, {'business_ref': 'businessref_25'}, {'business_ref': 'businessref_59'}, {'business_ref': 'businessref_67'}, {'business_ref': 'businessref_15'}, {'business_ref': 'businessref_24'}, {'business_ref': 'businessref_36'}, {'business_ref': 'businessref_17'}, {'business_ref': 'businessref_43'}, {'business_ref': 'businessref_99'}, {'business_ref': 'businessref_80'}, {'business_ref': 'businessref_86'}, {'business_ref': 'businessref_62'}, {'business_ref': 'businessref_8'}, {'business_ref': 'businessref_57'}, {'business_ref': 'businessref_37'}, {'business_ref': 'businessref_40'}, {'business_ref': 'businessref_83'}, {'business_ref': 'businessref_26'}, {'business_ref': 'businessref_4'}, {'business_ref': 'businessref_68'}, {'business_ref': 'businessref_82'}, {'business_ref': 'businessref_35'}, {'business_ref': 'businessref_45'}, {'business_ref': 'businessref_77'}, {'business_ref': 'businessref_27'}, {'business_ref': 'businessref_20'}, {'business_ref': 'businessref_22'}, {'business_ref': 'businessref_14'}, {'business_ref': 'businessref_28'}], 'var_call_YnMbPLTBZvxZiyR6u1U26znE': [{'business_id': 'businessid_47', 'attributes': {'ByAppointmentOnly': 'False', 'BusinessAcceptsCreditCards': 'True', 'GoodForKids': 'True', 'RestaurantsPriceRange2': '2', 'BikeParking': 'False', 'BusinessParking': "{'garage': False, 'street': False, 'validated': False, 'lot': True, 'valet': False}"}}, {'business_id': 'businessid_8', 'attributes': {'BusinessAcceptsCreditCards': 'True'}}, {'business_id': 'businessid_59', 'attributes': {'BusinessParking': "{'garage': False, 'street': True, 'validated': False, 'lot': False, 'valet': False}", 'RestaurantsTakeOut': 'None', 'RestaurantsDelivery': 'None', 'HasTV': 'True', 'Ambience': "{'touristy': False, 'hipster': None, 'romantic': None, 'divey': None, 'intimate': None, 'trendy': None, 'upscale': False, 'classy': None, 'casual': True}", 'GoodForMeal': "{'dessert': False, 'latenight': False, 'lunch': False, 'dinner': False, 'brunch': False, 'breakfast': False}"}}, {'business_id': 'businessid_91', 'attributes': {'BusinessParking': "{'garage': False, 'street': True, 'validated': False, 'lot': False, 'valet': False}", 'WiFi': "u'free'", 'WheelchairAccessible': 'True', 'Caters': 'True', 'HasTV': 'True', 'HappyHour': 'False', 'Ambience': "{'touristy': None, 'hipster': None, 'romantic': None, 'divey': None, 'intimate': True, 'trendy': None, 'upscale': None, 'classy': True, 'casual': True}", 'RestaurantsDelivery': 'True', 'RestaurantsPriceRange2': '2', 'GoodForKids': 'True', 'RestaurantsAttire': "u'casual'", 'BikeParking': 'True', 'OutdoorSeating': 'True', 'NoiseLevel': "u'quiet'", 'RestaurantsGoodForGroups': 'True', 'RestaurantsTakeOut': 'True', 'BusinessAcceptsCreditCards': 'True', 'RestaurantsReservations': 'False', 'GoodForMeal': "{'dessert': None, 'latenight': None, 'lunch': True, 'dinner': None, 'brunch': True, 'breakfast': True}", 'Alcohol': "u'beer_and_wine'", 'RestaurantsTableService': 'True', 'Corkage': 'False', 'BYOB': 'True'}}, {'business_id': 'businessid_83', 'attributes': {'RestaurantsPriceRange2': '2', 'AcceptsInsurance': 'True', 'BusinessAcceptsCreditCards': 'True', 'BusinessParking': 'None', 'ByAppointmentOnly': 'False'}}]}

exec(code, env_args)
