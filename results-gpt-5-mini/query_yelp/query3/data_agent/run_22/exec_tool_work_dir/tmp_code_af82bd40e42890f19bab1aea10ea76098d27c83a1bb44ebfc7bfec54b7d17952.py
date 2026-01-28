code = """import json
import pandas as pd
# Load results from previous query_db calls
r1 = var_call_A7khjPurPC1RMieooenL56rx
r2 = var_call_hv7YmDvJOuf7jYNZ9UqXyJrt
r3 = var_call_y7KFeC5pnrbmfOopbic1i3Ub
r4 = var_call_XbM5EgyxM463BIiVUqNDPkzj

# Combine business_refs from reviews (strip prefix)
df_reviews = pd.DataFrame(r1)
# map businessref_x -> businessid_x
df_reviews['business_id'] = df_reviews['business_ref'].str.replace('businessref_','businessid_')

# Combine business attributes
rows = r2 + r3 + r4
df_biz = pd.DataFrame(rows)
# ensure attributes exist
df_biz['attributes'] = df_biz['attributes'].fillna('None')

# Simplify: detect BikeParking True or BusinessParking not None/None and indicating parking available (street/lot/garage/valet True)
def has_business_parking(attr):
    if not isinstance(attr, dict):
        return False
    bp = attr.get('BusinessParking')
    if not bp or bp in ['None', 'None']:
        return False
    # bp is a string like "{'garage': False, 'street': True, ...}"
    try:
        bp_dict = eval(bp)
        # if any of the parking spots are True
        return any(v is True for v in bp_dict.values())
    except Exception:
        return False

def has_bike_parking(attr):
    if not isinstance(attr, dict):
        return False
    bp = attr.get('BikeParking')
    if bp in [None, 'None']:
        return False
    # values may be 'True' or True or "True"
    if isinstance(bp, bool):
        return bp
    v = str(bp).strip().lower()
    return v == 'true' or v == "u'true'"

# compute flags
df_biz['has_business_parking'] = df_biz['attributes'].apply(has_business_parking)
df_biz['has_bike_parking'] = df_biz['attributes'].apply(has_bike_parking)

# merge with reviewed businesses
df_merged = df_reviews.merge(df_biz[['business_id','has_business_parking','has_bike_parking']], on='business_id', how='left')
# count businesses that have either business or bike parking
# treat missing as False
df_merged['has_business_parking'] = df_merged['has_business_parking'].fillna(False)
df_merged['has_bike_parking'] = df_merged['has_bike_parking'].fillna(False)

# unique businesses
df_unique = df_merged.drop_duplicates(subset=['business_id'])
count = int((df_unique['has_business_parking'] | df_unique['has_bike_parking']).sum())

result = {'count': count}
print("__RESULT__:")
print(json.dumps(result))"""

env_args = {'var_call_A7khjPurPC1RMieooenL56rx': [{'business_ref': 'businessref_13'}, {'business_ref': 'businessref_79'}, {'business_ref': 'businessref_66'}, {'business_ref': 'businessref_25'}, {'business_ref': 'businessref_59'}, {'business_ref': 'businessref_67'}, {'business_ref': 'businessref_15'}, {'business_ref': 'businessref_24'}, {'business_ref': 'businessref_36'}, {'business_ref': 'businessref_17'}, {'business_ref': 'businessref_43'}, {'business_ref': 'businessref_80'}, {'business_ref': 'businessref_86'}, {'business_ref': 'businessref_62'}, {'business_ref': 'businessref_8'}, {'business_ref': 'businessref_57'}, {'business_ref': 'businessref_37'}, {'business_ref': 'businessref_40'}, {'business_ref': 'businessref_83'}, {'business_ref': 'businessref_26'}, {'business_ref': 'businessref_4'}, {'business_ref': 'businessref_68'}, {'business_ref': 'businessref_99'}, {'business_ref': 'businessref_82'}, {'business_ref': 'businessref_35'}, {'business_ref': 'businessref_45'}, {'business_ref': 'businessref_77'}, {'business_ref': 'businessref_27'}, {'business_ref': 'businessref_20'}, {'business_ref': 'businessref_22'}, {'business_ref': 'businessref_14'}, {'business_ref': 'businessref_28'}, {'business_ref': 'businessref_91'}, {'business_ref': 'businessref_46'}, {'business_ref': 'businessref_47'}, {'business_ref': 'businessref_73'}], 'var_call_hv7YmDvJOuf7jYNZ9UqXyJrt': [{'_id': '6859a000fe8b31cd7362e2b9', 'business_id': 'businessid_59', 'attributes': {'BusinessParking': "{'garage': False, 'street': True, 'validated': False, 'lot': False, 'valet': False}", 'RestaurantsTakeOut': 'None', 'RestaurantsDelivery': 'None', 'HasTV': 'True', 'Ambience': "{'touristy': False, 'hipster': None, 'romantic': None, 'divey': None, 'intimate': None, 'trendy': None, 'upscale': False, 'classy': None, 'casual': True}", 'GoodForMeal': "{'dessert': False, 'latenight': False, 'lunch': False, 'dinner': False, 'brunch': False, 'breakfast': False}"}}, {'_id': '6859a000fe8b31cd7362e2d4', 'business_id': 'businessid_67', 'attributes': {'WheelchairAccessible': 'True', 'DogsAllowed': 'False', 'RestaurantsTakeOut': 'True', 'HappyHour': 'False', 'RestaurantsDelivery': 'True', 'BusinessAcceptsCreditCards': 'True', 'Corkage': 'False', 'HasTV': 'True', 'BusinessAcceptsBitcoin': 'False', 'BusinessParking': "{'garage': False, 'street': False, 'validated': False, 'lot': True, 'valet': False}", 'RestaurantsTableService': 'True', 'Alcohol': "u'none'", 'RestaurantsGoodForGroups': 'True', 'WiFi': "u'free'", 'NoiseLevel': "u'average'", 'RestaurantsReservations': 'True', 'BYOB': 'True', 'OutdoorSeating': 'False', 'GoodForMeal': "{'dessert': False, 'latenight': False, 'lunch': False, 'dinner': False, 'brunch': False, 'breakfast': False}", 'BikeParking': 'True', 'Ambience': "{u'divey': False, u'hipster': None, u'casual': True, u'touristy': None, u'trendy': None, u'intimate': None, u'romantic': False, u'classy': None, u'upscale': None}", 'Caters': 'True'}}, {'_id': '6859a000fe8b31cd7362e2e0', 'business_id': 'businessid_79', 'attributes': 'None'}, {'_id': '6859a000fe8b31cd7362e2e1', 'business_id': 'businessid_66', 'attributes': {'BusinessAcceptsCreditCards': 'True', 'RestaurantsReservations': 'False', 'RestaurantsGoodForGroups': 'True', 'NoiseLevel': "u'average'", 'RestaurantsAttire': "'casual'", 'OutdoorSeating': 'True', 'Alcohol': "u'none'", 'GoodForKids': 'True', 'RestaurantsPriceRange2': '1', 'Ambience': "{'touristy': False, 'hipster': False, 'romantic': False, 'divey': False, 'intimate': False, 'trendy': False, 'upscale': False, 'classy': False, 'casual': False}", 'RestaurantsTakeOut': 'True', 'BikeParking': 'True', 'GoodForMeal': "{'dessert': False, 'latenight': False, 'lunch': False, 'dinner': False, 'brunch': False, 'breakfast': False}", 'HasTV': 'True', 'RestaurantsDelivery': 'True', 'DriveThru': 'False', 'Caters': 'True', 'BusinessParking': "{'garage': False, 'street': False, 'validated': False, 'lot': True, 'valet': False}"}}, {'_id': '6859a000fe8b31cd7362e2fd', 'business_id': 'businessid_25', 'attributes': {'Alcohol': "'none'", 'RestaurantsDelivery': 'True', 'RestaurantsReservations': 'False', 'Ambience': "{'romantic': False, 'intimate': False, 'classy': False, 'hipster': False, 'divey': False, 'touristy': False, 'trendy': False, 'upscale': False, 'casual': False}", 'RestaurantsAttire': "'casual'", 'BusinessParking': "{'garage': False, 'street': False, 'validated': False, 'lot': True, 'valet': False}", 'GoodForKids': 'True', 'BusinessAcceptsCreditCards': 'True', 'RestaurantsTakeOut': 'True', 'OutdoorSeating': 'True', 'Caters': 'True', 'DogsAllowed': 'False', 'RestaurantsTableService': 'False', 'WheelchairAccessible': 'True', 'HappyHour': 'False', 'NoiseLevel': "u'average'", 'HasTV': 'False', 'RestaurantsPriceRange2': '1', 'BusinessAcceptsBitcoin': 'False', 'BikeParking': 'True', 'RestaurantsGoodForGroups': 'False', 'GoodForMeal': "{'dessert': False, 'latenight': False, 'lunch': True, 'dinner': False, 'brunch': True, 'breakfast': False}", 'WiFi': "u'free'"}}], 'var_call_y7KFeC5pnrbmfOopbic1i3Ub': [{'_id': '6859a000fe8b31cd7362e2ac', 'business_id': 'businessid_47', 'attributes': {'ByAppointmentOnly': 'False', 'BusinessAcceptsCreditCards': 'True', 'GoodForKids': 'True', 'RestaurantsPriceRange2': '2', 'BikeParking': 'False', 'BusinessParking': "{'garage': False, 'street': False, 'validated': False, 'lot': True, 'valet': False}"}}, {'_id': '6859a000fe8b31cd7362e2b8', 'business_id': 'businessid_8', 'attributes': {'BusinessAcceptsCreditCards': 'True'}}, {'_id': '6859a000fe8b31cd7362e2ba', 'business_id': 'businessid_91', 'attributes': {'BusinessParking': "{'garage': False, 'street': True, 'validated': False, 'lot': False, 'valet': False}", 'WiFi': "u'free'", 'WheelchairAccessible': 'True', 'Caters': 'True', 'HasTV': 'True', 'HappyHour': 'False', 'Ambience': "{'touristy': None, 'hipster': None, 'romantic': None, 'divey': None, 'intimate': True, 'trendy': None, 'upscale': None, 'classy': True, 'casual': True}", 'RestaurantsDelivery': 'True', 'RestaurantsPriceRange2': '2', 'GoodForKids': 'True', 'RestaurantsAttire': "u'casual'", 'BikeParking': 'True', 'OutdoorSeating': 'True', 'NoiseLevel': "u'quiet'", 'RestaurantsGoodForGroups': 'True', 'RestaurantsTakeOut': 'True', 'BusinessAcceptsCreditCards': 'True', 'RestaurantsReservations': 'False', 'GoodForMeal': "{'dessert': None, 'latenight': None, 'lunch': True, 'dinner': None, 'brunch': True, 'breakfast': True}", 'Alcohol': "u'beer_and_wine'", 'RestaurantsTableService': 'True', 'Corkage': 'False', 'BYOB': 'True'}}, {'_id': '6859a000fe8b31cd7362e2bb', 'business_id': 'businessid_83', 'attributes': {'RestaurantsPriceRange2': '2', 'AcceptsInsurance': 'True', 'BusinessAcceptsCreditCards': 'True', 'BusinessParking': 'None', 'ByAppointmentOnly': 'False'}}, {'_id': '6859a000fe8b31cd7362e2be', 'business_id': 'businessid_24', 'attributes': {'BusinessAcceptsCreditCards': 'True', 'RestaurantsPriceRange2': '1', 'WiFi': "u'no'", 'BikeParking': 'True', 'BusinessParking': "{'garage': False, 'street': True, 'validated': False, 'lot': False, 'valet': False}", 'RestaurantsTakeOut': 'True'}}], 'var_call_XbM5EgyxM463BIiVUqNDPkzj': [{'_id': '6859a000fe8b31cd7362e2c1', 'business_id': 'businessid_26', 'attributes': {'WiFi': "u'free'", 'RestaurantsReservations': 'False', 'GoodForKids': 'True', 'Caters': 'False', 'RestaurantsPriceRange2': '1', 'OutdoorSeating': 'False', 'RestaurantsAttire': "u'casual'", 'HasTV': 'True', 'Alcohol': "u'none'", 'RestaurantsTakeOut': 'True', 'RestaurantsTableService': 'False', 'DriveThru': 'True', 'RestaurantsGoodForGroups': 'False', 'BusinessAcceptsCreditCards': 'True', 'BikeParking': 'True', 'RestaurantsDelivery': 'True', 'NoiseLevel': "u'average'", 'BusinessParking': "{'garage': False, 'street': False, 'validated': False, 'lot': False, 'valet': False}", 'Ambience': "{'romantic': False, 'intimate': False, 'touristy': False, 'hipster': False, 'divey': False, 'classy': False, 'trendy': False, 'upscale': False, 'casual': False}", 'GoodForMeal': "{'dessert': False, 'latenight': False, 'lunch': False, 'dinner': False, 'brunch': False, 'breakfast': False}"}}, {'_id': '6859a000fe8b31cd7362e2c9', 'business_id': 'businessid_14', 'attributes': {'BikeParking': 'False', 'BusinessParking': "{'garage': False, 'street': False, 'validated': False, 'lot': True, 'valet': False}", 'BusinessAcceptsCreditCards': 'True', 'RestaurantsPriceRange2': '1'}}, {'_id': '6859a000fe8b31cd7362e2cb', 'business_id': 'businessid_35', 'attributes': {'NoiseLevel': "u'quiet'", 'BusinessParking': "{'garage': False, 'street': False, 'validated': False, 'lot': False, 'valet': False}", 'RestaurantsAttire': "u'casual'", 'RestaurantsPriceRange2': '2', 'RestaurantsTakeOut': 'True'}}, {'_id': '6859a000fe8b31cd7362e2cc', 'business_id': 'businessid_28', 'attributes': 'None'}, {'_id': '6859a000fe8b31cd7362e2ce', 'business_id': 'businessid_27', 'attributes': {'RestaurantsAttire': "u'casual'", 'Alcohol': "u'none'", 'OutdoorSeating': 'False', 'RestaurantsGoodForGroups': 'True', 'WiFi': "u'no'", 'RestaurantsTakeOut': 'True', 'RestaurantsPriceRange2': '1', 'BusinessAcceptsCreditCards': 'True', 'RestaurantsDelivery': 'False', 'BikeParking': 'True', 'NoiseLevel': "u'average'", 'GoodForKids': 'True', 'Caters': 'True', 'RestaurantsReservations': 'False', 'BusinessParking': "{'garage': False, 'street': False, 'validated': False, 'lot': False, 'valet': False}", 'GoodForMeal': "{'dessert': False, 'latenight': None, 'lunch': True, 'dinner': None, 'brunch': None, 'breakfast': None}", 'HasTV': 'True', 'Ambience': "{'touristy': False, 'hipster': False, 'romantic': False, 'divey': None, 'intimate': False, 'trendy': False, 'upscale': False, 'classy': False, 'casual': None}"}}]}

exec(code, env_args)
