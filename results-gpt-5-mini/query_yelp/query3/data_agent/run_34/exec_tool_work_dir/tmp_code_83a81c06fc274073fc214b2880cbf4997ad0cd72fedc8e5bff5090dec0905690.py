code = """import json, ast

# review records from SQL query
review_recs = var_call_dnDwsZ3gKGtEz3OydbQhYgt2
# file path for the full business collection JSON
business_json_path = var_call_qH7qHtKf0apvPziAORW3VBi5

# build set of business ids corresponding to reviews
refs = {r['business_ref'] for r in review_recs}
business_ids = set(r.replace('businessref_', 'businessid_') for r in refs)

# load full business records
with open(business_json_path, 'r') as f:
    businesses = json.load(f)

bid_to_attr = {b.get('business_id'): b.get('attributes') for b in businesses}

count = 0
matched = []
for bid in business_ids:
    attr = bid_to_attr.get(bid)
    has_parking = False
    if isinstance(attr, dict):
        # BikeParking
        bp_val = attr.get('BikeParking')
        if bp_val is not None and 'true' in str(bp_val).lower():
            has_parking = True
        # BusinessParking
        bpkg = attr.get('BusinessParking')
        if not has_parking and bpkg is not None and bpkg != 'None':
            if isinstance(bpkg, dict):
                for v in bpkg.values():
                    if (isinstance(v, bool) and v) or ('true' in str(v).lower()):
                        has_parking = True
                        break
            else:
                s = str(bpkg)
                try:
                    d = ast.literal_eval(s)
                    if isinstance(d, dict):
                        for v in d.values():
                            if (isinstance(v, bool) and v) or ('true' in str(v).lower()):
                                has_parking = True
                                break
                except Exception:
                    if 'True' in s:
                        has_parking = True
    elif isinstance(attr, str):
        s = attr
        if s != 'None':
            try:
                d = ast.literal_eval(s)
                if isinstance(d, dict):
                    bp_val = d.get('BikeParking')
                    if bp_val is not None and 'true' in str(bp_val).lower():
                        has_parking = True
                    bpkg = d.get('BusinessParking')
                    if not has_parking and bpkg is not None:
                        if isinstance(bpkg, dict):
                            for v in bpkg.values():
                                if (isinstance(v, bool) and v) or ('true' in str(v).lower()):
                                    has_parking = True
                                    break
                        else:
                            if 'True' in str(bpkg):
                                has_parking = True
                else:
                    if ('BikeParking' in s and 'True' in s) or ('BusinessParking' in s and 'True' in s):
                        has_parking = True
            except Exception:
                if ('BikeParking' in s and 'True' in s) or ('BusinessParking' in s and 'True' in s):
                    has_parking = True
    # else attr is None or other
    if has_parking:
        count += 1
        matched.append(bid)

print("__RESULT__:")
print(json.dumps(count))"""

env_args = {'var_call_9RqqkgrvMD4qdbq6MWuVkwaa': ['business', 'checkin'], 'var_call_xSRLbA6bBwuHJO6ZckeIYsoa': ['review', 'tip', 'user'], 'var_call_9uEJ3xUygbGUw9avSF4Qo0ND': [{'_id': '6859a000fe8b31cd7362e2ab', 'business_id': 'businessid_49', 'attributes': {'BusinessAcceptsCreditCards': 'True', 'WiFi': "u'no'", 'BusinessAcceptsBitcoin': 'False'}}, {'_id': '6859a000fe8b31cd7362e2ac', 'business_id': 'businessid_47', 'attributes': {'ByAppointmentOnly': 'False', 'BusinessAcceptsCreditCards': 'True', 'GoodForKids': 'True', 'RestaurantsPriceRange2': '2', 'BikeParking': 'False', 'BusinessParking': "{'garage': False, 'street': False, 'validated': False, 'lot': True, 'valet': False}"}}, {'_id': '6859a000fe8b31cd7362e2ad', 'business_id': 'businessid_88', 'attributes': {'BusinessParking': "{'garage': False, 'street': False, 'validated': False, 'lot': False, 'valet': False}", 'GoodForKids': 'True', 'BusinessAcceptsCreditCards': 'True', 'ByAppointmentOnly': 'False', 'BikeParking': 'True'}}, {'_id': '6859a000fe8b31cd7362e2ae', 'business_id': 'businessid_41', 'attributes': 'None'}, {'_id': '6859a000fe8b31cd7362e2af', 'business_id': 'businessid_33', 'attributes': {'BusinessParking': "{'garage': False, 'street': False, 'validated': False, 'lot': False, 'valet': False}", 'BusinessAcceptsCreditCards': 'True', 'AcceptsInsurance': 'False', 'ByAppointmentOnly': 'False', 'RestaurantsPriceRange2': '2', 'WheelchairAccessible': 'True', 'BikeParking': 'False'}}, {'_id': '6859a000fe8b31cd7362e2b0', 'business_id': 'businessid_74', 'attributes': {'BusinessParking': "{'garage': False, 'street': False, 'validated': False, 'lot': False, 'valet': False}", 'RestaurantsPriceRange2': '4', 'BikeParking': 'False'}}, {'_id': '6859a000fe8b31cd7362e2b1', 'business_id': 'businessid_92', 'attributes': {'ByAppointmentOnly': 'False', 'BusinessAcceptsCreditCards': 'True', 'BusinessParking': "{'garage': True, 'street': False, 'validated': False, 'lot': False, 'valet': False}", 'RestaurantsPriceRange2': '2', 'WheelchairAccessible': 'True', 'BikeParking': 'True', 'NoiseLevel': "u'quiet'", 'WiFi': "u'no'"}}, {'_id': '6859a000fe8b31cd7362e2b2', 'business_id': 'businessid_64', 'attributes': {'BusinessParking': "{'garage': True, 'street': False, 'validated': False, 'lot': True, 'valet': False}", 'ByAppointmentOnly': 'False', 'BusinessAcceptsCreditCards': 'True', 'RestaurantsPriceRange2': '2', 'BikeParking': 'True', 'WiFi': "u'free'"}}, {'_id': '6859a000fe8b31cd7362e2b3', 'business_id': 'businessid_52', 'attributes': {'ByAppointmentOnly': 'False', 'BusinessAcceptsCreditCards': 'True', 'BusinessParking': "{'garage': False, 'street': False, 'validated': False, 'lot': False, 'valet': False}", 'RestaurantsPriceRange2': '2', 'BikeParking': 'True'}}, {'_id': '6859a000fe8b31cd7362e2b4', 'business_id': 'businessid_29', 'attributes': {'BikeParking': 'True', 'BusinessAcceptsCreditCards': 'True', 'RestaurantsPriceRange2': '2', 'BusinessParking': "{'garage': False, 'street': True, 'validated': False, 'lot': False, 'valet': False}", 'RestaurantsDelivery': 'None'}}, {'_id': '6859a000fe8b31cd7362e2b5', 'business_id': 'businessid_10', 'attributes': {'RestaurantsGoodForGroups': 'True', 'RestaurantsDelivery': 'False', 'RestaurantsTakeOut': 'True', 'HasTV': 'True', 'BusinessAcceptsCreditCards': 'True', 'Ambience': "{'touristy': False, 'hipster': False, 'romantic': False, 'divey': False, 'intimate': False, 'trendy': False, 'upscale': False, 'classy': False, 'casual': False}", 'GoodForMeal': "{'dessert': False, 'latenight': False, 'lunch': False, 'dinner': False, 'brunch': False, 'breakfast': False}", 'BusinessParking': "{u'valet': False, u'garage': False, u'street': False, u'lot': True, u'validated': False}"}}, {'_id': '6859a000fe8b31cd7362e2b6', 'business_id': 'businessid_61', 'attributes': {'ByAppointmentOnly': 'True', 'BusinessAcceptsCreditCards': 'True'}}, {'_id': '6859a000fe8b31cd7362e2b7', 'business_id': 'businessid_54', 'attributes': {'BusinessParking': "{'garage': False, 'street': False, 'validated': False, 'lot': False, 'valet': False}", 'BusinessAcceptsCreditCards': 'True', 'WheelchairAccessible': 'True', 'RestaurantsDelivery': 'True', 'RestaurantsTakeOut': 'True', 'RestaurantsPriceRange2': '1', 'WiFi': "u'free'"}}, {'_id': '6859a000fe8b31cd7362e2b8', 'business_id': 'businessid_8', 'attributes': {'BusinessAcceptsCreditCards': 'True'}}, {'_id': '6859a000fe8b31cd7362e2b9', 'business_id': 'businessid_59', 'attributes': {'BusinessParking': "{'garage': False, 'street': True, 'validated': False, 'lot': False, 'valet': False}", 'RestaurantsTakeOut': 'None', 'RestaurantsDelivery': 'None', 'HasTV': 'True', 'Ambience': "{'touristy': False, 'hipster': None, 'romantic': None, 'divey': None, 'intimate': None, 'trendy': None, 'upscale': False, 'classy': None, 'casual': True}", 'GoodForMeal': "{'dessert': False, 'latenight': False, 'lunch': False, 'dinner': False, 'brunch': False, 'breakfast': False}"}}, {'_id': '6859a000fe8b31cd7362e2ba', 'business_id': 'businessid_91', 'attributes': {'BusinessParking': "{'garage': False, 'street': True, 'validated': False, 'lot': False, 'valet': False}", 'WiFi': "u'free'", 'WheelchairAccessible': 'True', 'Caters': 'True', 'HasTV': 'True', 'HappyHour': 'False', 'Ambience': "{'touristy': None, 'hipster': None, 'romantic': None, 'divey': None, 'intimate': True, 'trendy': None, 'upscale': None, 'classy': True, 'casual': True}", 'RestaurantsDelivery': 'True', 'RestaurantsPriceRange2': '2', 'GoodForKids': 'True', 'RestaurantsAttire': "u'casual'", 'BikeParking': 'True', 'OutdoorSeating': 'True', 'NoiseLevel': "u'quiet'", 'RestaurantsGoodForGroups': 'True', 'RestaurantsTakeOut': 'True', 'BusinessAcceptsCreditCards': 'True', 'RestaurantsReservations': 'False', 'GoodForMeal': "{'dessert': None, 'latenight': None, 'lunch': True, 'dinner': None, 'brunch': True, 'breakfast': True}", 'Alcohol': "u'beer_and_wine'", 'RestaurantsTableService': 'True', 'Corkage': 'False', 'BYOB': 'True'}}, {'_id': '6859a000fe8b31cd7362e2bb', 'business_id': 'businessid_83', 'attributes': {'RestaurantsPriceRange2': '2', 'AcceptsInsurance': 'True', 'BusinessAcceptsCreditCards': 'True', 'BusinessParking': 'None', 'ByAppointmentOnly': 'False'}}, {'_id': '6859a000fe8b31cd7362e2bc', 'business_id': 'businessid_93', 'attributes': {'RestaurantsGoodForGroups': 'True', 'RestaurantsAttire': "u'casual'", 'BusinessAcceptsCreditCards': 'True', 'RestaurantsPriceRange2': '1', 'Ambience': "{'romantic': False, 'intimate': False, 'touristy': False, 'hipster': False, 'divey': False, 'classy': False, 'trendy': False, 'upscale': False, 'casual': False}", 'RestaurantsReservations': 'False', 'RestaurantsTakeOut': 'True', 'WiFi': "u'free'", 'GoodForKids': 'True', 'HasTV': 'True', 'Alcohol': "u'full_bar'", 'BusinessParking': "{'garage': False, 'street': False, 'validated': False, 'lot': True, 'valet': False}", 'RestaurantsDelivery': 'False', 'NoiseLevel': "u'average'", 'OutdoorSeating': 'True'}}, {'_id': '6859a000fe8b31cd7362e2bd', 'business_id': 'businessid_1', 'attributes': 'None'}, {'_id': '6859a000fe8b31cd7362e2be', 'business_id': 'businessid_24', 'attributes': {'BusinessAcceptsCreditCards': 'True', 'RestaurantsPriceRange2': '1', 'WiFi': "u'no'", 'BikeParking': 'True', 'BusinessParking': "{'garage': False, 'street': True, 'validated': False, 'lot': False, 'valet': False}", 'RestaurantsTakeOut': 'True'}}], 'var_call_dnDwsZ3gKGtEz3OydbQhYgt2': [{'business_ref': 'businessref_13'}, {'business_ref': 'businessref_79'}, {'business_ref': 'businessref_91'}, {'business_ref': 'businessref_46'}, {'business_ref': 'businessref_47'}, {'business_ref': 'businessref_73'}, {'business_ref': 'businessref_66'}, {'business_ref': 'businessref_25'}, {'business_ref': 'businessref_59'}, {'business_ref': 'businessref_24'}, {'business_ref': 'businessref_36'}, {'business_ref': 'businessref_17'}, {'business_ref': 'businessref_99'}, {'business_ref': 'businessref_80'}, {'business_ref': 'businessref_86'}, {'business_ref': 'businessref_62'}, {'business_ref': 'businessref_8'}, {'business_ref': 'businessref_57'}, {'business_ref': 'businessref_37'}, {'business_ref': 'businessref_40'}, {'business_ref': 'businessref_83'}, {'business_ref': 'businessref_26'}, {'business_ref': 'businessref_4'}, {'business_ref': 'businessref_68'}, {'business_ref': 'businessref_67'}, {'business_ref': 'businessref_15'}, {'business_ref': 'businessref_77'}, {'business_ref': 'businessref_27'}, {'business_ref': 'businessref_20'}, {'business_ref': 'businessref_22'}, {'business_ref': 'businessref_14'}, {'business_ref': 'businessref_28'}, {'business_ref': 'businessref_82'}, {'business_ref': 'businessref_35'}, {'business_ref': 'businessref_45'}], 'var_call_qH7qHtKf0apvPziAORW3VBi5': 'file_storage/call_qH7qHtKf0apvPziAORW3VBi5.json'}

exec(code, env_args)
