code = """import json, ast
# reviews from 2018
reviews = var_call_01uVwWVX1Hg7lzxNhBQOuAys
# full business list file path
business_file = var_call_4mVwWU7wA6fXtzAujglY1g7f
# load businesses
with open(business_file, 'r') as f:
    businesses = json.load(f)
# map business_id to attributes
biz_map = {b.get('business_id'): b.get('attributes') for b in businesses}
# convert review business_refs to business_id format
review_bids = set()
for r in reviews:
    br = r.get('business_ref')
    if not br:
        continue
    parts = br.split('_', 1)
    if len(parts) == 2:
        review_bids.add('businessid_' + parts[1])

count = 0
for bid in review_bids:
    attr = biz_map.get(bid)
    offers = False
    if attr and attr != "None":
        # if it's a dict
        if isinstance(attr, dict):
            # check BikeParking
            if 'BikeParking' in attr:
                v = attr['BikeParking']
                if v is True or (isinstance(v, str) and 'true' in v.lower()):
                    offers = True
            # check BusinessParking
            if not offers and 'BusinessParking' in attr:
                bp = attr['BusinessParking']
                if bp and bp != "None":
                    if isinstance(bp, str):
                        s = bp.replace("u'", "'")
                        try:
                            d = ast.literal_eval(s)
                            if isinstance(d, dict):
                                for val in d.values():
                                    if val is True or (isinstance(val, str) and 'true' in val.lower()):
                                        offers = True
                                        break
                        except Exception:
                            # if parsing fails but string not 'None', assume offering
                            offers = True
                    elif isinstance(bp, dict):
                        for val in bp.values():
                            if val is True or (isinstance(val, str) and 'true' in val.lower()):
                                offers = True
                                break
                    else:
                        offers = True
        # if attr is a string that may contain keys
        elif isinstance(attr, str):
            s = attr
            if 'BikeParking' in s and 'True' in s:
                offers = True
            if not offers and 'BusinessParking' in s and 'True' in s:
                offers = True
    if offers:
        count += 1

print("__RESULT__:")
print(json.dumps(count))"""

env_args = {'var_call_01uVwWVX1Hg7lzxNhBQOuAys': [{'business_ref': 'businessref_13'}, {'business_ref': 'businessref_79'}, {'business_ref': 'businessref_66'}, {'business_ref': 'businessref_25'}, {'business_ref': 'businessref_91'}, {'business_ref': 'businessref_46'}, {'business_ref': 'businessref_47'}, {'business_ref': 'businessref_73'}, {'business_ref': 'businessref_59'}, {'business_ref': 'businessref_67'}, {'business_ref': 'businessref_15'}, {'business_ref': 'businessref_17'}, {'business_ref': 'businessref_43'}, {'business_ref': 'businessref_99'}, {'business_ref': 'businessref_80'}, {'business_ref': 'businessref_86'}, {'business_ref': 'businessref_62'}, {'business_ref': 'businessref_8'}, {'business_ref': 'businessref_57'}, {'business_ref': 'businessref_37'}, {'business_ref': 'businessref_26'}, {'business_ref': 'businessref_4'}, {'business_ref': 'businessref_68'}, {'business_ref': 'businessref_82'}, {'business_ref': 'businessref_35'}, {'business_ref': 'businessref_45'}, {'business_ref': 'businessref_77'}, {'business_ref': 'businessref_27'}, {'business_ref': 'businessref_40'}, {'business_ref': 'businessref_83'}, {'business_ref': 'businessref_20'}, {'business_ref': 'businessref_22'}, {'business_ref': 'businessref_14'}, {'business_ref': 'businessref_28'}, {'business_ref': 'businessref_24'}, {'business_ref': 'businessref_36'}], 'var_call_SrxX2i1L97TYcviKucej0mrL': [{'business_id': 'businessid_47', 'attributes': {'ByAppointmentOnly': 'False', 'BusinessAcceptsCreditCards': 'True', 'GoodForKids': 'True', 'RestaurantsPriceRange2': '2', 'BikeParking': 'False', 'BusinessParking': "{'garage': False, 'street': False, 'validated': False, 'lot': True, 'valet': False}"}}, {'business_id': 'businessid_8', 'attributes': {'BusinessAcceptsCreditCards': 'True'}}, {'business_id': 'businessid_59', 'attributes': {'BusinessParking': "{'garage': False, 'street': True, 'validated': False, 'lot': False, 'valet': False}", 'RestaurantsTakeOut': 'None', 'RestaurantsDelivery': 'None', 'HasTV': 'True', 'Ambience': "{'touristy': False, 'hipster': None, 'romantic': None, 'divey': None, 'intimate': None, 'trendy': None, 'upscale': False, 'classy': None, 'casual': True}", 'GoodForMeal': "{'dessert': False, 'latenight': False, 'lunch': False, 'dinner': False, 'brunch': False, 'breakfast': False}"}}, {'business_id': 'businessid_91', 'attributes': {'BusinessParking': "{'garage': False, 'street': True, 'validated': False, 'lot': False, 'valet': False}", 'WiFi': "u'free'", 'WheelchairAccessible': 'True', 'Caters': 'True', 'HasTV': 'True', 'HappyHour': 'False', 'Ambience': "{'touristy': None, 'hipster': None, 'romantic': None, 'divey': None, 'intimate': True, 'trendy': None, 'upscale': None, 'classy': True, 'casual': True}", 'RestaurantsDelivery': 'True', 'RestaurantsPriceRange2': '2', 'GoodForKids': 'True', 'RestaurantsAttire': "u'casual'", 'BikeParking': 'True', 'OutdoorSeating': 'True', 'NoiseLevel': "u'quiet'", 'RestaurantsGoodForGroups': 'True', 'RestaurantsTakeOut': 'True', 'BusinessAcceptsCreditCards': 'True', 'RestaurantsReservations': 'False', 'GoodForMeal': "{'dessert': None, 'latenight': None, 'lunch': True, 'dinner': None, 'brunch': True, 'breakfast': True}", 'Alcohol': "u'beer_and_wine'", 'RestaurantsTableService': 'True', 'Corkage': 'False', 'BYOB': 'True'}}, {'business_id': 'businessid_83', 'attributes': {'RestaurantsPriceRange2': '2', 'AcceptsInsurance': 'True', 'BusinessAcceptsCreditCards': 'True', 'BusinessParking': 'None', 'ByAppointmentOnly': 'False'}}], 'var_call_4mVwWU7wA6fXtzAujglY1g7f': 'file_storage/call_4mVwWU7wA6fXtzAujglY1g7f.json'}

exec(code, env_args)
