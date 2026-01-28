code = """import json

with open(var_call_NAqUUrEjnmpiDdYHYZai6POw, 'r') as f:
    businesses = json.load(f)

# Find all unique top-level keys
top_keys = set()
for b in businesses:
    for k in b.keys():
        top_keys.add(k)

# Check for presence of categories, description
has_categories = any('categories' in b for b in businesses)
has_description = any('description' in b for b in businesses)

# Check nested in attributes for any key that seems like category info
attr_keys = set()
for b in businesses:
    attrs = b.get('attributes') or {}
    for k in attrs.keys():
        attr_keys.add(k)

# Print some sample businesses fully for inspection (first 5)
sample_full = businesses[:5]

out = {
    'total': len(businesses),
    'top_keys': sorted(list(top_keys)),
    'has_categories': has_categories,
    'has_description': has_description,
    'attribute_keys_sample': sorted(list(attr_keys))[:50],
    'sample_full_first5': sample_full
}

print('__RESULT__:')
print(json.dumps(out))"""

env_args = {'var_call_D7CD2DQCTa8jHGewhSkVZids': ['business', 'checkin'], 'var_call_oegT4QrYcZ0vHVix0AWApWFP': ['review', 'tip', 'user'], 'var_call_NAqUUrEjnmpiDdYHYZai6POw': 'file_storage/call_NAqUUrEjnmpiDdYHYZai6POw.json', 'var_call_ew33PuycLWh81QohJv7XOYLK': 'file_storage/call_ew33PuycLWh81QohJv7XOYLK.json', 'var_call_pyDZEAtTowFcGE2c5OZb7cI1': {'top_category': None, 'business_count': 0, 'avg_rating': None}, 'var_call_CSSBZ4Gi40C0nw1sqga3RIgt': [], 'var_call_0AmL1oCMuh1kFU62LZB4SpND': [], 'var_call_l57M6IGOX9vm9FPXRuJn5Eku': {'total_business_records': 75, 'sample': [{'business_id': 'businessid_49', 'keys': ['business_id', 'attributes'], 'attributes_keys': ['BusinessAcceptsCreditCards', 'WiFi', 'BusinessAcceptsBitcoin'], 'description_present': False, 'description_sample': None}, {'business_id': 'businessid_47', 'keys': ['business_id', 'attributes'], 'attributes_keys': ['ByAppointmentOnly', 'BusinessAcceptsCreditCards', 'GoodForKids', 'RestaurantsPriceRange2', 'BikeParking', 'BusinessParking'], 'description_present': False, 'description_sample': None}, {'business_id': 'businessid_88', 'keys': ['business_id', 'attributes'], 'attributes_keys': ['BusinessParking', 'GoodForKids', 'BusinessAcceptsCreditCards', 'ByAppointmentOnly', 'BikeParking'], 'description_present': False, 'description_sample': None}, {'business_id': 'businessid_33', 'keys': ['business_id', 'attributes'], 'attributes_keys': ['BusinessParking', 'BusinessAcceptsCreditCards', 'AcceptsInsurance', 'ByAppointmentOnly', 'RestaurantsPriceRange2', 'WheelchairAccessible', 'BikeParking'], 'description_present': False, 'description_sample': None}, {'business_id': 'businessid_92', 'keys': ['business_id', 'attributes'], 'attributes_keys': ['ByAppointmentOnly', 'BusinessAcceptsCreditCards', 'BusinessParking', 'RestaurantsPriceRange2', 'WheelchairAccessible', 'BikeParking', 'NoiseLevel', 'WiFi'], 'description_present': False, 'description_sample': None}, {'business_id': 'businessid_64', 'keys': ['business_id', 'attributes'], 'attributes_keys': ['BusinessParking', 'ByAppointmentOnly', 'BusinessAcceptsCreditCards', 'RestaurantsPriceRange2', 'BikeParking', 'WiFi'], 'description_present': False, 'description_sample': None}, {'business_id': 'businessid_52', 'keys': ['business_id', 'attributes'], 'attributes_keys': ['ByAppointmentOnly', 'BusinessAcceptsCreditCards', 'BusinessParking', 'RestaurantsPriceRange2', 'BikeParking'], 'description_present': False, 'description_sample': None}, {'business_id': 'businessid_29', 'keys': ['business_id', 'attributes'], 'attributes_keys': ['BikeParking', 'BusinessAcceptsCreditCards', 'RestaurantsPriceRange2', 'BusinessParking', 'RestaurantsDelivery'], 'description_present': False, 'description_sample': None}, {'business_id': 'businessid_10', 'keys': ['business_id', 'attributes'], 'attributes_keys': ['RestaurantsGoodForGroups', 'RestaurantsDelivery', 'RestaurantsTakeOut', 'HasTV', 'BusinessAcceptsCreditCards', 'Ambience', 'GoodForMeal', 'BusinessParking'], 'description_present': False, 'description_sample': None}, {'business_id': 'businessid_61', 'keys': ['business_id', 'attributes'], 'attributes_keys': ['ByAppointmentOnly', 'BusinessAcceptsCreditCards'], 'description_present': False, 'description_sample': None}]}}

exec(code, env_args)
