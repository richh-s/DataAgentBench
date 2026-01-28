code = """import json

# Access previous python result and business info
res = var_call_qyydMbzmrLNmjtTEOfeEMwGS
biz = var_call_acSrYcWFvz8Wys1YyUJoYGRI

output = {
    'business_id': res['business_id'],
    'business_ref': res['business_ref'],
    'name': biz[0].get('name'),
    'category': None,
    'avg_rating': res['avg_rating'],
    'review_count_in_period': res['review_count_in_period']
}

# Try to infer category from description
desc = biz[0].get('description') or ''
# Look for common separators
if desc:
    # crude extraction: take words after 'featuring' or after last comma list
    if 'featuring' in desc:
        cat = desc.split('featuring',1)[1]
        # take up to period
        cat = cat.split('.',1)[0]
        output['category'] = cat.strip()
    else:
        # try to extract last part after comma
        parts = desc.split(',')
        if parts:
            last = parts[-1]
            output['category'] = last.strip()

print('__RESULT__:')
print(json.dumps(output))"""

env_args = {'var_call_KQBxdG2747m3smLJmBLncixS': ['checkin', 'business'], 'var_call_ntTOrFGkEtp4mAZgtNUDTygk': ['review', 'tip', 'user'], 'var_call_eodFZgiCk2MAnJxGGDBoIAdi': 'file_storage/call_eodFZgiCk2MAnJxGGDBoIAdi.json', 'var_call_qyydMbzmrLNmjtTEOfeEMwGS': {'business_ref': 'businessref_9', 'business_id': 'businessid_9', 'avg_rating': 4.375, 'review_count_in_period': 16}, 'var_call_acSrYcWFvz8Wys1YyUJoYGRI': [{'business_id': 'businessid_9', 'name': 'Coffee House Too Cafe', 'attributes': {'HasTV': 'False', 'GoodForKids': 'True', 'Ambience': "{'romantic': False, 'intimate': False, 'classy': False, 'hipster': False, 'divey': False, 'touristy': False, 'trendy': False, 'upscale': False, 'casual': True}", 'NoiseLevel': "u'average'", 'RestaurantsTakeOut': 'True', 'BusinessParking': "{'garage': False, 'street': True, 'validated': False, 'lot': False, 'valet': False}", 'GoodForMeal': "{'dessert': False, 'latenight': False, 'lunch': True, 'dinner': False, 'brunch': True, 'breakfast': True}", 'WheelchairAccessible': 'True', 'OutdoorSeating': 'False', 'WiFi': "u'no'", 'RestaurantsReservations': 'True', 'BusinessAcceptsBitcoin': 'False', 'RestaurantsAttire': "u'casual'", 'RestaurantsDelivery': 'True', 'Alcohol': "u'none'", 'RestaurantsTableService': 'True', 'Caters': 'True', 'BikeParking': 'False', 'RestaurantsPriceRange2': '2', 'DogsAllowed': 'True', 'RestaurantsGoodForGroups': 'True', 'BusinessAcceptsCreditCards': 'True'}, 'description': 'Located at 501 Fairmount Ave in Philadelphia, PA, this inviting establishment offers a delightful menu featuring Restaurants, Breakfast & Brunch, American (New), Cafes, perfect for a cozy meal any time of the day.'}]}

exec(code, env_args)
