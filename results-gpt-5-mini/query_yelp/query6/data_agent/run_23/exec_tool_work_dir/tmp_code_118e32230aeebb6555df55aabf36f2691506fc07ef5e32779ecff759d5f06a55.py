code = """import json
# Access the query results stored in the provided variables
reviews = var_call_Jkzm26pXyhpHGFEJarvhk1n5
business_docs = var_call_STspqtUbvdjUGloNC5EUtlcp

row = reviews[0] if reviews else None
bdoc = business_docs[0] if business_docs else None

if not row or not bdoc:
    out = {"error": "Missing data from prior queries"}
else:
    business_name = bdoc.get('name')
    business_id = bdoc.get('business_id')
    avg_rating = float(row.get('avg_rating'))
    review_count = int(row.get('cnt'))
    # attempt to parse categories from description
    desc = bdoc.get('description','')
    categories = []
    key = 'featuring '
    idx = desc.find(key)
    if idx != -1:
        sub = desc[idx+len(key):]
        # truncate at common sentence breaks
        for sep in ['.',' perfect',' located',' in ']:
            pos = sub.find(sep)
            if pos != -1:
                sub = sub[:pos]
                break
        # split by commas
        categories = [s.strip() for s in sub.split(',') if s.strip()]
    # fallback: empty list
    out = {
        'business_name': business_name,
        'business_id': business_id,
        'categories': categories,
        'average_rating': avg_rating,
        'review_count_in_period': review_count,
        'period_start': '2016-01-01',
        'period_end': '2016-06-30'
    }

print("__RESULT__:")
print(json.dumps(out))"""

env_args = {'var_call_Jkzm26pXyhpHGFEJarvhk1n5': [{'business_ref': 'businessref_9', 'cnt': '5', 'avg_rating': '4.0'}], 'var_call_STspqtUbvdjUGloNC5EUtlcp': [{'_id': '6859a000fe8b31cd7362e2f3', 'business_id': 'businessid_9', 'name': 'Coffee House Too Cafe', 'attributes': {'HasTV': 'False', 'GoodForKids': 'True', 'Ambience': "{'romantic': False, 'intimate': False, 'classy': False, 'hipster': False, 'divey': False, 'touristy': False, 'trendy': False, 'upscale': False, 'casual': True}", 'NoiseLevel': "u'average'", 'RestaurantsTakeOut': 'True', 'BusinessParking': "{'garage': False, 'street': True, 'validated': False, 'lot': False, 'valet': False}", 'GoodForMeal': "{'dessert': False, 'latenight': False, 'lunch': True, 'dinner': False, 'brunch': True, 'breakfast': True}", 'WheelchairAccessible': 'True', 'OutdoorSeating': 'False', 'WiFi': "u'no'", 'RestaurantsReservations': 'True', 'BusinessAcceptsBitcoin': 'False', 'RestaurantsAttire': "u'casual'", 'RestaurantsDelivery': 'True', 'Alcohol': "u'none'", 'RestaurantsTableService': 'True', 'Caters': 'True', 'BikeParking': 'False', 'RestaurantsPriceRange2': '2', 'DogsAllowed': 'True', 'RestaurantsGoodForGroups': 'True', 'BusinessAcceptsCreditCards': 'True'}, 'description': 'Located at 501 Fairmount Ave in Philadelphia, PA, this inviting establishment offers a delightful menu featuring Restaurants, Breakfast & Brunch, American (New), Cafes, perfect for a cozy meal any time of the day.'}]}

exec(code, env_args)
