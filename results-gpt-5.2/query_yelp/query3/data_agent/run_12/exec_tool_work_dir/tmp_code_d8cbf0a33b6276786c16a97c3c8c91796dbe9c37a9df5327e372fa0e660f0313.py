code = """import json, ast
recs = var_call_6DKZlsBqoXpg72EoPtBI8uah
count=0
for r in recs:
    attrs = r.get('attributes') or {}
    has=False
    # BikeParking
    bp = attrs.get('BikeParking')
    if isinstance(bp,str) and bp.lower()=='true':
        has=True
    # BusinessParking
    bpark = attrs.get('BusinessParking')
    if not has and bpark is not None:
        if isinstance(bpark,str):
            if bpark.lower()=='none':
                pass
            else:
                try:
                    d = ast.literal_eval(bpark)
                    if isinstance(d,dict) and any(bool(v) for v in d.values()):
                        has=True
                except Exception:
                    # if unparsable but present, treat as offered
                    has=True
        elif isinstance(bpark,dict):
            if any(bool(v) for v in bpark.values()):
                has=True
        else:
            has=True
    if has:
        count += 1
print('__RESULT__:')
print(json.dumps({'count': count, 'total_reviewed_businesses_2018': len(recs)}))"""

env_args = {'var_call_fyKco2i0i96C00vvlDuMeS6Y': [{'business_ref': 'businessref_91'}, {'business_ref': 'businessref_46'}, {'business_ref': 'businessref_47'}, {'business_ref': 'businessref_73'}, {'business_ref': 'businessref_66'}, {'business_ref': 'businessref_25'}, {'business_ref': 'businessref_59'}, {'business_ref': 'businessref_67'}, {'business_ref': 'businessref_15'}, {'business_ref': 'businessref_24'}, {'business_ref': 'businessref_36'}, {'business_ref': 'businessref_17'}, {'business_ref': 'businessref_43'}, {'business_ref': 'businessref_99'}, {'business_ref': 'businessref_80'}, {'business_ref': 'businessref_86'}, {'business_ref': 'businessref_62'}, {'business_ref': 'businessref_8'}, {'business_ref': 'businessref_57'}, {'business_ref': 'businessref_37'}, {'business_ref': 'businessref_40'}, {'business_ref': 'businessref_83'}, {'business_ref': 'businessref_26'}, {'business_ref': 'businessref_4'}, {'business_ref': 'businessref_68'}, {'business_ref': 'businessref_82'}, {'business_ref': 'businessref_35'}, {'business_ref': 'businessref_45'}, {'business_ref': 'businessref_77'}, {'business_ref': 'businessref_27'}, {'business_ref': 'businessref_20'}, {'business_ref': 'businessref_22'}, {'business_ref': 'businessref_14'}, {'business_ref': 'businessref_28'}, {'business_ref': 'businessref_13'}, {'business_ref': 'businessref_79'}], 'var_call_k1XWG5bw9QIHoxXOXO3H4emr': ['business', 'checkin'], 'var_call_59rsPso7vwwshz9XScf3MyWo': {'business_ids': ['businessid_91', 'businessid_46', 'businessid_47', 'businessid_73', 'businessid_66', 'businessid_25', 'businessid_59', 'businessid_67', 'businessid_15', 'businessid_24', 'businessid_36', 'businessid_17', 'businessid_43', 'businessid_99', 'businessid_80', 'businessid_86', 'businessid_62', 'businessid_8', 'businessid_57', 'businessid_37', 'businessid_40', 'businessid_83', 'businessid_26', 'businessid_4', 'businessid_68', 'businessid_82', 'businessid_35', 'businessid_45', 'businessid_77', 'businessid_27', 'businessid_20', 'businessid_22', 'businessid_14', 'businessid_28', 'businessid_13', 'businessid_79']}, 'var_call_6DKZlsBqoXpg72EoPtBI8uah': [{'business_id': 'businessid_47', 'attributes': {'ByAppointmentOnly': 'False', 'BusinessAcceptsCreditCards': 'True', 'GoodForKids': 'True', 'RestaurantsPriceRange2': '2', 'BikeParking': 'False', 'BusinessParking': "{'garage': False, 'street': False, 'validated': False, 'lot': True, 'valet': False}"}}, {'business_id': 'businessid_8', 'attributes': {'BusinessAcceptsCreditCards': 'True'}}, {'business_id': 'businessid_59', 'attributes': {'BusinessParking': "{'garage': False, 'street': True, 'validated': False, 'lot': False, 'valet': False}", 'RestaurantsTakeOut': 'None', 'RestaurantsDelivery': 'None', 'HasTV': 'True', 'Ambience': "{'touristy': False, 'hipster': None, 'romantic': None, 'divey': None, 'intimate': None, 'trendy': None, 'upscale': False, 'classy': None, 'casual': True}", 'GoodForMeal': "{'dessert': False, 'latenight': False, 'lunch': False, 'dinner': False, 'brunch': False, 'breakfast': False}"}}, {'business_id': 'businessid_91', 'attributes': {'BusinessParking': "{'garage': False, 'street': True, 'validated': False, 'lot': False, 'valet': False}", 'WiFi': "u'free'", 'WheelchairAccessible': 'True', 'Caters': 'True', 'HasTV': 'True', 'HappyHour': 'False', 'Ambience': "{'touristy': None, 'hipster': None, 'romantic': None, 'divey': None, 'intimate': True, 'trendy': None, 'upscale': None, 'classy': True, 'casual': True}", 'RestaurantsDelivery': 'True', 'RestaurantsPriceRange2': '2', 'GoodForKids': 'True', 'RestaurantsAttire': "u'casual'", 'BikeParking': 'True', 'OutdoorSeating': 'True', 'NoiseLevel': "u'quiet'", 'RestaurantsGoodForGroups': 'True', 'RestaurantsTakeOut': 'True', 'BusinessAcceptsCreditCards': 'True', 'RestaurantsReservations': 'False', 'GoodForMeal': "{'dessert': None, 'latenight': None, 'lunch': True, 'dinner': None, 'brunch': True, 'breakfast': True}", 'Alcohol': "u'beer_and_wine'", 'RestaurantsTableService': 'True', 'Corkage': 'False', 'BYOB': 'True'}}, {'business_id': 'businessid_83', 'attributes': {'RestaurantsPriceRange2': '2', 'AcceptsInsurance': 'True', 'BusinessAcceptsCreditCards': 'True', 'BusinessParking': 'None', 'ByAppointmentOnly': 'False'}}]}

exec(code, env_args)
