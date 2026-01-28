code = """import json
# load all business attribute query results
r1 = var_call_npv77qbodUulrE0afAwit0Nk
r2 = var_call_AdarKVGRoiFr1iEjQS3IHKIP
r3 = var_call_iWnzAlKu58G4kGrN45lZ6MBm
all_rows = r1 + r2 + r3
# mapping of businesses we found attributes for
business_attrs = {row['business_id']: row.get('attributes') for row in all_rows}
# list of all businesses that had reviews in 2018 (from earlier)
biz_list = var_call_hfa9E3a0KuTTb1ItRdmzUB8X
# determine which businesses offer bike or business parking
result = []
for b in biz_list:
    attrs = business_attrs.get(b)
    has_bike = False
    has_parking = False
    if attrs and isinstance(attrs, dict):
        # BikeParking may be string 'True'/'False' or missing
        bp = attrs.get('BikeParking')
        if bp is not None:
            # normalize strings
            s = str(bp).lower()
            if 'true' in s:
                has_bike = True
        # BusinessParking may be 'None' or a string representation of dict
        bpar = attrs.get('BusinessParking')
        if bpar and isinstance(bpar, str):
            s = bpar.lower()
            # detect if any parking type true
            if 'true' in s or 'lot':
                # crude check: if 'true' or 'lot' present and not explicitly False
                if 'false' in s and 'true' not in s:
                    has_parking = False
                else:
                    # if 'true' exists or 'lot' exists and not explicitly false for all
                    # check specific keys
                    if 'garage' in s or 'street' in s or 'lot' in s or 'valet' in s or 'validated' in s:
                        # find any ': True' pattern
                        if "'lot': True" in bpar or "'street': True" in bpar or "'garage': True" in bpar or "'valet': True" in bpar or "'validated': True" in bpar:
                            has_parking = True
                        else:
                            # if mention of lot without explicit True and contains "lot": True earlier? fallback
                            # treat presence of "lot": True or "street": True only
                            has_parking = ('"lot": True' in bpar) or ("'lot': True" in bpar) or ("'street': True" in bpar) or ("'garage': True" in bpar)
                    else:
                        has_parking = False
        elif bpar is None:
            has_parking = False
        elif isinstance(bpar, dict):
            # if it's real dict
            for v in bpar.values():
                if isinstance(v, bool) and v:
                    has_parking = True
                if isinstance(v, str) and v.lower()=='true':
                    has_parking = True
    # If attributes is the string 'None' treat as no info
    # count business if either bike or parking
    if has_bike or has_parking:
        result.append({'business_id': b, 'bike_parking': has_bike, 'business_parking': has_parking})
# compute count
count = len(result)
print('__RESULT__:')
print(json.dumps({'count': count, 'details': result}))"""

env_args = {'var_call_N3LoAZwhmoTehv9CSP6C8LCP': ['business', 'checkin'], 'var_call_9jrPHdOoxE6DYvbugLssYmfH': ['review', 'tip', 'user'], 'var_call_aEPnqKEpCB5ZyHSMQjaQbNUx': [{'business_ref': 'businessref_13'}, {'business_ref': 'businessref_79'}, {'business_ref': 'businessref_66'}, {'business_ref': 'businessref_25'}, {'business_ref': 'businessref_91'}, {'business_ref': 'businessref_46'}, {'business_ref': 'businessref_47'}, {'business_ref': 'businessref_73'}, {'business_ref': 'businessref_59'}, {'business_ref': 'businessref_67'}, {'business_ref': 'businessref_15'}, {'business_ref': 'businessref_24'}, {'business_ref': 'businessref_36'}, {'business_ref': 'businessref_17'}, {'business_ref': 'businessref_43'}, {'business_ref': 'businessref_99'}, {'business_ref': 'businessref_80'}, {'business_ref': 'businessref_40'}, {'business_ref': 'businessref_83'}, {'business_ref': 'businessref_26'}, {'business_ref': 'businessref_4'}, {'business_ref': 'businessref_68'}, {'business_ref': 'businessref_82'}, {'business_ref': 'businessref_35'}, {'business_ref': 'businessref_45'}, {'business_ref': 'businessref_77'}, {'business_ref': 'businessref_27'}, {'business_ref': 'businessref_20'}, {'business_ref': 'businessref_22'}, {'business_ref': 'businessref_14'}, {'business_ref': 'businessref_28'}, {'business_ref': 'businessref_86'}, {'business_ref': 'businessref_62'}, {'business_ref': 'businessref_8'}, {'business_ref': 'businessref_57'}, {'business_ref': 'businessref_37'}], 'var_call_hfa9E3a0KuTTb1ItRdmzUB8X': ['businessid_13', 'businessid_79', 'businessid_66', 'businessid_25', 'businessid_91', 'businessid_46', 'businessid_47', 'businessid_73', 'businessid_59', 'businessid_67', 'businessid_15', 'businessid_24', 'businessid_36', 'businessid_17', 'businessid_43', 'businessid_99', 'businessid_80', 'businessid_40', 'businessid_83', 'businessid_26', 'businessid_4', 'businessid_68', 'businessid_82', 'businessid_35', 'businessid_45', 'businessid_77', 'businessid_27', 'businessid_20', 'businessid_22', 'businessid_14', 'businessid_28', 'businessid_86', 'businessid_62', 'businessid_8', 'businessid_57', 'businessid_37'], 'var_call_npv77qbodUulrE0afAwit0Nk': [{'business_id': 'businessid_47', 'attributes': {'ByAppointmentOnly': 'False', 'BusinessAcceptsCreditCards': 'True', 'GoodForKids': 'True', 'RestaurantsPriceRange2': '2', 'BikeParking': 'False', 'BusinessParking': "{'garage': False, 'street': False, 'validated': False, 'lot': True, 'valet': False}"}}, {'business_id': 'businessid_59', 'attributes': {'BusinessParking': "{'garage': False, 'street': True, 'validated': False, 'lot': False, 'valet': False}", 'RestaurantsTakeOut': 'None', 'RestaurantsDelivery': 'None', 'HasTV': 'True', 'Ambience': "{'touristy': False, 'hipster': None, 'romantic': None, 'divey': None, 'intimate': None, 'trendy': None, 'upscale': False, 'classy': None, 'casual': True}", 'GoodForMeal': "{'dessert': False, 'latenight': False, 'lunch': False, 'dinner': False, 'brunch': False, 'breakfast': False}"}}, {'business_id': 'businessid_91', 'attributes': {'BusinessParking': "{'garage': False, 'street': True, 'validated': False, 'lot': False, 'valet': False}", 'WiFi': "u'free'", 'WheelchairAccessible': 'True', 'Caters': 'True', 'HasTV': 'True', 'HappyHour': 'False', 'Ambience': "{'touristy': None, 'hipster': None, 'romantic': None, 'divey': None, 'intimate': True, 'trendy': None, 'upscale': None, 'classy': True, 'casual': True}", 'RestaurantsDelivery': 'True', 'RestaurantsPriceRange2': '2', 'GoodForKids': 'True', 'RestaurantsAttire': "u'casual'", 'BikeParking': 'True', 'OutdoorSeating': 'True', 'NoiseLevel': "u'quiet'", 'RestaurantsGoodForGroups': 'True', 'RestaurantsTakeOut': 'True', 'BusinessAcceptsCreditCards': 'True', 'RestaurantsReservations': 'False', 'GoodForMeal': "{'dessert': None, 'latenight': None, 'lunch': True, 'dinner': None, 'brunch': True, 'breakfast': True}", 'Alcohol': "u'beer_and_wine'", 'RestaurantsTableService': 'True', 'Corkage': 'False', 'BYOB': 'True'}}, {'business_id': 'businessid_67', 'attributes': {'WheelchairAccessible': 'True', 'DogsAllowed': 'False', 'RestaurantsTakeOut': 'True', 'HappyHour': 'False', 'RestaurantsDelivery': 'True', 'BusinessAcceptsCreditCards': 'True', 'Corkage': 'False', 'HasTV': 'True', 'BusinessAcceptsBitcoin': 'False', 'BusinessParking': "{'garage': False, 'street': False, 'validated': False, 'lot': True, 'valet': False}", 'RestaurantsTableService': 'True', 'Alcohol': "u'none'", 'RestaurantsGoodForGroups': 'True', 'WiFi': "u'free'", 'NoiseLevel': "u'average'", 'RestaurantsReservations': 'True', 'BYOB': 'True', 'OutdoorSeating': 'False', 'GoodForMeal': "{'dessert': False, 'latenight': False, 'lunch': False, 'dinner': False, 'brunch': False, 'breakfast': False}", 'BikeParking': 'True', 'Ambience': "{u'divey': False, u'hipster': None, u'casual': True, u'touristy': None, u'trendy': None, u'intimate': None, u'romantic': False, u'classy': None, u'upscale': None}", 'Caters': 'True'}}, {'business_id': 'businessid_79', 'attributes': 'None'}], 'var_call_AdarKVGRoiFr1iEjQS3IHKIP': [{'business_id': 'businessid_83', 'attributes': {'RestaurantsPriceRange2': '2', 'AcceptsInsurance': 'True', 'BusinessAcceptsCreditCards': 'True', 'BusinessParking': 'None', 'ByAppointmentOnly': 'False'}}, {'business_id': 'businessid_24', 'attributes': {'BusinessAcceptsCreditCards': 'True', 'RestaurantsPriceRange2': '1', 'WiFi': "u'no'", 'BikeParking': 'True', 'BusinessParking': "{'garage': False, 'street': True, 'validated': False, 'lot': False, 'valet': False}", 'RestaurantsTakeOut': 'True'}}, {'business_id': 'businessid_26', 'attributes': {'WiFi': "u'free'", 'RestaurantsReservations': 'False', 'GoodForKids': 'True', 'Caters': 'False', 'RestaurantsPriceRange2': '1', 'OutdoorSeating': 'False', 'RestaurantsAttire': "u'casual'", 'HasTV': 'True', 'Alcohol': "u'none'", 'RestaurantsTakeOut': 'True', 'RestaurantsTableService': 'False', 'DriveThru': 'True', 'RestaurantsGoodForGroups': 'False', 'BusinessAcceptsCreditCards': 'True', 'BikeParking': 'True', 'RestaurantsDelivery': 'True', 'NoiseLevel': "u'average'", 'BusinessParking': "{'garage': False, 'street': False, 'validated': False, 'lot': False, 'valet': False}", 'Ambience': "{'romantic': False, 'intimate': False, 'touristy': False, 'hipster': False, 'divey': False, 'classy': False, 'trendy': False, 'upscale': False, 'casual': False}", 'GoodForMeal': "{'dessert': False, 'latenight': False, 'lunch': False, 'dinner': False, 'brunch': False, 'breakfast': False}"}}, {'business_id': 'businessid_80', 'attributes': {'ByAppointmentOnly': 'True'}}, {'business_id': 'businessid_15', 'attributes': {'BusinessAcceptsCreditCards': 'True'}}], 'var_call_iWnzAlKu58G4kGrN45lZ6MBm': [{'business_id': 'businessid_8', 'attributes': {'BusinessAcceptsCreditCards': 'True'}}, {'business_id': 'businessid_14', 'attributes': {'BikeParking': 'False', 'BusinessParking': "{'garage': False, 'street': False, 'validated': False, 'lot': True, 'valet': False}", 'BusinessAcceptsCreditCards': 'True', 'RestaurantsPriceRange2': '1'}}, {'business_id': 'businessid_35', 'attributes': {'NoiseLevel': "u'quiet'", 'BusinessParking': "{'garage': False, 'street': False, 'validated': False, 'lot': False, 'valet': False}", 'RestaurantsAttire': "u'casual'", 'RestaurantsPriceRange2': '2', 'RestaurantsTakeOut': 'True'}}, {'business_id': 'businessid_28', 'attributes': 'None'}, {'business_id': 'businessid_57', 'attributes': {'BusinessAcceptsCreditCards': 'False', 'BusinessAcceptsBitcoin': 'False', 'ByAppointmentOnly': 'False'}}]}

exec(code, env_args)
