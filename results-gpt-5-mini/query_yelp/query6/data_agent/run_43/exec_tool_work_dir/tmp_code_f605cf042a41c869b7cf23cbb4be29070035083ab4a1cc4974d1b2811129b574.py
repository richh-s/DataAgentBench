code = """import json
# Access the stored results from previous query_db calls
records = var_call_X6KJZTUSwtQgZnBOeN0VC7YL
biz = var_call_r2gRsXiyqIt1ZKn5QffvCwxT

# Extract info
rec = records[0] if records else {}
ref = rec.get('business_ref')
try:
    avg_rating = float(rec.get('avg_rating')) if rec.get('avg_rating') is not None else None
except:
    avg_rating = None
try:
    cnt = int(rec.get('cnt')) if rec.get('cnt') is not None else None
except:
    cnt = None

biz_doc = biz[0] if biz else {}
name = biz_doc.get('name')
description = biz_doc.get('description')
# Attempt to parse categories from description if present (after "featuring" or "menu featuring" or just listing)
# Fallback to empty list
categories = None
if description:
    # The example description contains: "...offers a delightful menu featuring Restaurants, Breakfast & Brunch, American (New), Cafes, perfect..."
    # We'll try to extract the comma-separated segment between "featuring" and the next ", perfect" or end.
    desc_lower = description
    if 'featuring' in desc_lower:
        try:
            part = desc_lower.split('featuring',1)[1]
            # split on 'perfect' or '.' or 'located' etc
            end_markers = ['perfect', 'perfect for', 'located at', '.']
            end_idx = None
            for m in end_markers:
                if m in part:
                    idx = part.find(m)
                    if end_idx is None or idx < end_idx:
                        end_idx = idx
            if end_idx is not None:
                cat_segment = part[:end_idx]
            else:
                cat_segment = part
            # Clean and split by commas
            cats = [c.strip().strip('.') for c in cat_segment.split(',') if c.strip()]
            # Remove leading words like 'a', 'offers', 'a delightful menu' if present
            # If first element contains words not category-like, drop until element has no spaces at start? Keep as is for simplicity.
            categories = cats
        except Exception:
            categories = None
    else:
        categories = None

result = {
    'business_ref': ref,
    'business_name': name,
    'categories': categories,
    'average_rating': avg_rating,
    'reviews_in_period': cnt
}

print("__RESULT__:")
print(json.dumps(result))"""

env_args = {'var_call_X6KJZTUSwtQgZnBOeN0VC7YL': [{'business_ref': 'businessref_9', 'cnt': '5', 'avg_rating': '4.0'}], 'var_call_r2gRsXiyqIt1ZKn5QffvCwxT': [{'_id': '6859a000fe8b31cd7362e2f3', 'business_id': 'businessid_9', 'name': 'Coffee House Too Cafe', 'review_count': '53', 'is_open': '0', 'attributes': {'HasTV': 'False', 'GoodForKids': 'True', 'Ambience': "{'romantic': False, 'intimate': False, 'classy': False, 'hipster': False, 'divey': False, 'touristy': False, 'trendy': False, 'upscale': False, 'casual': True}", 'NoiseLevel': "u'average'", 'RestaurantsTakeOut': 'True', 'BusinessParking': "{'garage': False, 'street': True, 'validated': False, 'lot': False, 'valet': False}", 'GoodForMeal': "{'dessert': False, 'latenight': False, 'lunch': True, 'dinner': False, 'brunch': True, 'breakfast': True}", 'WheelchairAccessible': 'True', 'OutdoorSeating': 'False', 'WiFi': "u'no'", 'RestaurantsReservations': 'True', 'BusinessAcceptsBitcoin': 'False', 'RestaurantsAttire': "u'casual'", 'RestaurantsDelivery': 'True', 'Alcohol': "u'none'", 'RestaurantsTableService': 'True', 'Caters': 'True', 'BikeParking': 'False', 'RestaurantsPriceRange2': '2', 'DogsAllowed': 'True', 'RestaurantsGoodForGroups': 'True', 'BusinessAcceptsCreditCards': 'True'}, 'hours': {'Monday': '7:0-15:0', 'Tuesday': '7:0-15:0', 'Wednesday': '7:0-15:0', 'Thursday': '7:0-15:0', 'Friday': '7:0-15:0', 'Saturday': '8:30-15:0', 'Sunday': '8:30-15:0'}, 'description': 'Located at 501 Fairmount Ave in Philadelphia, PA, this inviting establishment offers a delightful menu featuring Restaurants, Breakfast & Brunch, American (New), Cafes, perfect for a cozy meal any time of the day.'}]}

exec(code, env_args)
