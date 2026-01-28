code = """import json
import pandas as pd

with open(var_call_By0YsQSKO0TUH7HYGOuh2IE3, 'r') as f:
    businesses = json.load(f)

b = pd.DataFrame(businesses)

# ensure columns
for col in ['description','attributes','business_id','name']:
    if col not in b.columns:
        b[col] = None

# detect accepts cc

def accepts_cc(attr):
    if attr is None:
        return False
    if isinstance(attr, dict):
        v = attr.get('BusinessAcceptsCreditCards')
        if v is None:
            return False
        return 'true' in str(v).lower()
    s = str(attr).lower()
    return ('businessacceptscreditcards' in s and 'true' in s)

b['accepts_cc'] = b['attributes'].apply(accepts_cc)

# counts
total = len(b)
desc_nonnull = int(b['description'].notna().sum())
accepts = b[b['accepts_cc']==True]
accepts_with_desc = accepts['description'].notna().sum()

# show up to 10 descriptions from accepts
sample_desc = accepts[accepts['description'].notna()].head(10)['description'].tolist()

res = {'total_businesses': int(total), 'descriptions_nonnull': desc_nonnull, 'accepts_cc_total': int(len(accepts)), 'accepts_with_desc': int(accepts_with_desc), 'sample_descriptions': sample_desc}

print('__RESULT__:')
print(json.dumps(res))"""

env_args = {'var_call_zYWWfxdtpjIy5owlOM4SaGDn': ['business', 'checkin'], 'var_call_mHA3vgr16eyfCZYaS9qPg3uP': ['review', 'tip', 'user'], 'var_call_By0YsQSKO0TUH7HYGOuh2IE3': 'file_storage/call_By0YsQSKO0TUH7HYGOuh2IE3.json', 'var_call_TlPasEwRwrpoipslO3NtzTX9': 'file_storage/call_TlPasEwRwrpoipslO3NtzTX9.json', 'var_call_y3E5KsRHzfEDIvVCCDQoNDKU': {'category': None, 'business_count': 0, 'average_rating': None}, 'var_call_4EyBBhMx0IX87GBMEIVF9q5X': 'file_storage/call_4EyBBhMx0IX87GBMEIVF9q5X.json', 'var_call_5gb3J7A0uHjJTrUuB8IRGuPQ': {'category': None, 'business_count': 0, 'average_rating': None}, 'var_call_SQnWJqlQg4SiEy3h3gQSfFwa': {'total_businesses': 100, 'attributes_nonnull': 100, 'accepts_cc_count': 75, 'sample_accepts': [{'business_id': 'businessid_49', 'name': 'Steps to Learning Montessori Preschool', 'attributes': {'BusinessAcceptsCreditCards': 'True', 'WiFi': "u'no'", 'BusinessAcceptsBitcoin': 'False'}}, {'business_id': 'businessid_47', 'name': 'Breeze Blow Dry Bar', 'attributes': {'ByAppointmentOnly': 'False', 'BusinessAcceptsCreditCards': 'True', 'GoodForKids': 'True', 'RestaurantsPriceRange2': '2', 'BikeParking': 'False', 'BusinessParking': "{'garage': False, 'street': False, 'validated': False, 'lot': True, 'valet': False}"}}, {'business_id': 'businessid_88', 'name': 'Impact Guns', 'attributes': {'BusinessParking': "{'garage': False, 'street': False, 'validated': False, 'lot': False, 'valet': False}", 'GoodForKids': 'True', 'BusinessAcceptsCreditCards': 'True', 'ByAppointmentOnly': 'False', 'BikeParking': 'True'}}, {'business_id': 'businessid_33', 'name': 'J&Q Nails', 'attributes': {'BusinessParking': "{'garage': False, 'street': False, 'validated': False, 'lot': False, 'valet': False}", 'BusinessAcceptsCreditCards': 'True', 'AcceptsInsurance': 'False', 'ByAppointmentOnly': 'False', 'RestaurantsPriceRange2': '2', 'WheelchairAccessible': 'True', 'BikeParking': 'False'}}, {'business_id': 'businessid_92', 'name': 'Luminosity', 'attributes': {'ByAppointmentOnly': 'False', 'BusinessAcceptsCreditCards': 'True', 'BusinessParking': "{'garage': True, 'street': False, 'validated': False, 'lot': False, 'valet': False}", 'RestaurantsPriceRange2': '2', 'WheelchairAccessible': 'True', 'BikeParking': 'True', 'NoiseLevel': "u'quiet'", 'WiFi': "u'no'"}}, {'business_id': 'businessid_64', 'name': 'Nail Care Salon', 'attributes': {'BusinessParking': "{'garage': True, 'street': False, 'validated': False, 'lot': True, 'valet': False}", 'ByAppointmentOnly': 'False', 'BusinessAcceptsCreditCards': 'True', 'RestaurantsPriceRange2': '2', 'BikeParking': 'True', 'WiFi': "u'free'"}}, {'business_id': 'businessid_52', 'name': 'Architectural Antiques of Indianapolis', 'attributes': {'ByAppointmentOnly': 'False', 'BusinessAcceptsCreditCards': 'True', 'BusinessParking': "{'garage': False, 'street': False, 'validated': False, 'lot': False, 'valet': False}", 'RestaurantsPriceRange2': '2', 'BikeParking': 'True'}}, {'business_id': 'businessid_29', 'name': "Aster's Floral Shop", 'attributes': {'BikeParking': 'True', 'BusinessAcceptsCreditCards': 'True', 'RestaurantsPriceRange2': '2', 'BusinessParking': "{'garage': False, 'street': True, 'validated': False, 'lot': False, 'valet': False}", 'RestaurantsDelivery': 'None'}}, {'business_id': 'businessid_10', 'name': 'China Wok', 'attributes': {'RestaurantsGoodForGroups': 'True', 'RestaurantsDelivery': 'False', 'RestaurantsTakeOut': 'True', 'HasTV': 'True', 'BusinessAcceptsCreditCards': 'True', 'Ambience': "{'touristy': False, 'hipster': False, 'romantic': False, 'divey': False, 'intimate': False, 'trendy': False, 'upscale': False, 'classy': False, 'casual': False}", 'GoodForMeal': "{'dessert': False, 'latenight': False, 'lunch': False, 'dinner': False, 'brunch': False, 'breakfast': False}", 'BusinessParking': "{u'valet': False, u'garage': False, u'street': False, u'lot': True, u'validated': False}"}}, {'business_id': 'businessid_61', 'name': 'Brandon Family Medical Care', 'attributes': {'ByAppointmentOnly': 'True', 'BusinessAcceptsCreditCards': 'True'}}]}, 'var_call_mtkKqs0lblHhO2TvWWqLpXkL': {'category': None, 'business_count': 0, 'average_rating': None}, 'var_call_Y4v8c9P9W7YcoZ8YUYzdOApX': [{'business_id': 'businessid_49', 'name': 'Steps to Learning Montessori Preschool', 'description': None, 'extracted': []}, {'business_id': 'businessid_47', 'name': 'Breeze Blow Dry Bar', 'description': None, 'extracted': []}, {'business_id': 'businessid_88', 'name': 'Impact Guns', 'description': None, 'extracted': []}, {'business_id': 'businessid_33', 'name': 'J&Q Nails', 'description': None, 'extracted': []}, {'business_id': 'businessid_92', 'name': 'Luminosity', 'description': None, 'extracted': []}, {'business_id': 'businessid_64', 'name': 'Nail Care Salon', 'description': None, 'extracted': []}, {'business_id': 'businessid_52', 'name': 'Architectural Antiques of Indianapolis', 'description': None, 'extracted': []}, {'business_id': 'businessid_29', 'name': "Aster's Floral Shop", 'description': None, 'extracted': []}, {'business_id': 'businessid_10', 'name': 'China Wok', 'description': None, 'extracted': []}, {'business_id': 'businessid_61', 'name': 'Brandon Family Medical Care', 'description': None, 'extracted': []}, {'business_id': 'businessid_54', 'name': '7-Eleven', 'description': None, 'extracted': []}, {'business_id': 'businessid_8', 'name': 'Uber', 'description': None, 'extracted': []}, {'business_id': 'businessid_91', 'name': 'Cafe Porche and snowbar', 'description': None, 'extracted': []}, {'business_id': 'businessid_83', 'name': 'Eyeglass World', 'description': None, 'extracted': []}, {'business_id': 'businessid_93', 'name': "Callahan's Corner", 'description': None, 'extracted': []}, {'business_id': 'businessid_24', 'name': 'FroYo Frozen Yogurt', 'description': None, 'extracted': []}, {'business_id': 'businessid_95', 'name': 'Subway', 'description': None, 'extracted': []}, {'business_id': 'businessid_26', 'name': "McDonald's", 'description': None, 'extracted': []}, {'business_id': 'businessid_84', 'name': 'Gamestop', 'description': None, 'extracted': []}, {'business_id': 'businessid_89', 'name': 'King of Prussia Laundromat', 'description': None, 'extracted': []}]}

exec(code, env_args)
