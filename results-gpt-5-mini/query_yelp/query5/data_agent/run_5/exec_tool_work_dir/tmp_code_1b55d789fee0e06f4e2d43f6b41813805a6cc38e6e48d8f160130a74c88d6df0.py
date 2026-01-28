code = """import json
import pandas as pd

# load helper to read storage vars
def load_json_var(v):
    if isinstance(v, str):
        with open(v, 'r', encoding='utf-8') as f:
            return json.load(f)
    return v

business_records = load_json_var(var_call_UVZR7709LPZF23DgUxE2dmxz)
review_records = load_json_var(var_call_a7dKfCyZqiBGcFKsysbkg3Rk)

bdf = pd.DataFrame(business_records)
rdf = pd.DataFrame(review_records)

# normalize review ratings
if 'rating' in rdf.columns:
    rdf['rating'] = pd.to_numeric(rdf['rating'], errors='coerce')
else:
    rdf['rating'] = pd.NA

# improved state extraction: split by commas and look for 2-letter token
import re

def extract_state(desc):
    if not desc or not isinstance(desc, str):
        return None
    parts = [p.strip() for p in desc.split(',') if p.strip()]
    # look for a token that is exactly 2 letters and all alpha
    for part in parts:
        if re.fullmatch(r'[A-Z]{2}', part):
            return part
    # sometimes state may be like 'King of Prussia, PA' -> parts may include 'King of Prussia' and 'PA' so covered
    # try to find last two-letter uppercase inside the string
    m = re.search(r'\b([A-Z]{2})\b', desc)
    if m:
        return m.group(1)
    return None

# detect wifi

def has_wifi(attrs):
    if not attrs or attrs == 'None':
        return False
    if isinstance(attrs, dict):
        for k, v in attrs.items():
            if str(k).lower() == 'wifi':
                if v is None:
                    return False
                sval = str(v).lower()
                if 'no' in sval:
                    return False
                return True
        return False
    else:
        s = str(attrs).lower()
        if 'wifi' in s and 'no' not in s:
            return True
        return False

bdf['state'] = bdf['description'].apply(extract_state)
bdf['has_wifi'] = bdf['attributes'].apply(has_wifi)

# Filter wifi businesses with state
wifi_biz = bdf[bdf['has_wifi'] & bdf['state'].notna()].copy()

# count unique businesses by state
state_counts = wifi_biz.groupby('state')['business_id'].nunique().reset_index(name='wifi_business_count')

# map business_id to business_ref
wifi_biz['business_ref'] = wifi_biz['business_id'].str.replace('businessid_', 'businessref_')

# filter reviews for these businesses
wifi_review = rdf[rdf['business_ref'].isin(wifi_biz['business_ref'])].copy()

# merge to get state for each review
merged = wifi_review.merge(wifi_biz[['business_ref','state']], on='business_ref', how='left')

# compute average rating per state
avg_rating = merged.groupby('state')['rating'].mean().reset_index(name='average_rating')

summary = state_counts.merge(avg_rating, on='state', how='left')

# choose state with max count; tie-breaker: higher average_rating, then state alphabetically
if not summary.empty:
    # ensure average_rating numeric
    summary['average_rating'] = pd.to_numeric(summary['average_rating'], errors='coerce')
    summary_sorted = summary.sort_values(by=['wifi_business_count','average_rating','state'], ascending=[False, False, True])
    top = summary_sorted.iloc[0]
    result = {
        'state': top['state'],
        'wifi_business_count': int(top['wifi_business_count']),
        'average_rating': None if pd.isna(top['average_rating']) else float(round(top['average_rating'], 3))
    }
else:
    result = {'state': None, 'wifi_business_count': 0, 'average_rating': None}

print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_call_TXbD5C2P6pEcS4aWn6Z30ewF': ['checkin', 'business'], 'var_call_UVZR7709LPZF23DgUxE2dmxz': 'file_storage/call_UVZR7709LPZF23DgUxE2dmxz.json', 'var_call_a7dKfCyZqiBGcFKsysbkg3Rk': 'file_storage/call_a7dKfCyZqiBGcFKsysbkg3Rk.json', 'var_call_T5OsPZHrNmbYXs0kBPfXFVFf': {'state': None, 'wifi_business_count': 0, 'average_rating': None}, 'var_call_kLyG3ZGEUZvIHk7WEQZqLnWI': {'total_business_records': 100, 'states_found_count': 0, 'states_sample': [], 'wifi_businesses_detected': 22, 'sample_wifi_businesses': [{'business_id': 'businessid_64', 'attributes': {'BusinessParking': "{'garage': True, 'street': False, 'validated': False, 'lot': True, 'valet': False}", 'ByAppointmentOnly': 'False', 'BusinessAcceptsCreditCards': 'True', 'RestaurantsPriceRange2': '2', 'BikeParking': 'True', 'WiFi': "u'free'"}, 'description': 'Located at 12337 Olive Blvd in Creve Coeur, MO, this establishment offers a range of services in Nail Salons, Beauty & Spas.', 'state': None}, {'business_id': 'businessid_54', 'attributes': {'BusinessParking': "{'garage': False, 'street': False, 'validated': False, 'lot': False, 'valet': False}", 'BusinessAcceptsCreditCards': 'True', 'WheelchairAccessible': 'True', 'RestaurantsDelivery': 'True', 'RestaurantsTakeOut': 'True', 'RestaurantsPriceRange2': '1', 'WiFi': "u'free'"}, 'description': 'Located at 13151 Race Track Rd in Tampa, FL, this establishment offers a variety of services including Service Stations, Coffee & Tea, Gas Stations, Automotive, Gas Stations, Food, and Convenience Stores.', 'state': None}, {'business_id': 'businessid_91', 'attributes': {'BusinessParking': "{'garage': False, 'street': True, 'validated': False, 'lot': False, 'valet': False}", 'WiFi': "u'free'", 'WheelchairAccessible': 'True', 'Caters': 'True', 'HasTV': 'True', 'HappyHour': 'False', 'Ambience': "{'touristy': None, 'hipster': None, 'romantic': None, 'divey': None, 'intimate': True, 'trendy': None, 'upscale': None, 'classy': True, 'casual': True}", 'RestaurantsDelivery': 'True', 'RestaurantsPriceRange2': '2', 'GoodForKids': 'True', 'RestaurantsAttire': "u'casual'", 'BikeParking': 'True', 'OutdoorSeating': 'True', 'NoiseLevel': "u'quiet'", 'RestaurantsGoodForGroups': 'True', 'RestaurantsTakeOut': 'True', 'BusinessAcceptsCreditCards': 'True', 'RestaurantsReservations': 'False', 'GoodForMeal': "{'dessert': None, 'latenight': None, 'lunch': True, 'dinner': None, 'brunch': True, 'breakfast': True}", 'Alcohol': "u'beer_and_wine'", 'RestaurantsTableService': 'True', 'Corkage': 'False', 'BYOB': 'True'}, 'description': 'Located at 1625 Baronne St in New Orleans, LA, this vibrant establishment offers a delightful array of options ranging from Food, Shaved Ice, Cajun/Creole, Breakfast & Brunch, Party & Event Planning, Comfort Food, Cafes, Restaurants, to Event Planning & Services, making it a perfect spot for any occasion.', 'state': None}, {'business_id': 'businessid_93', 'attributes': {'RestaurantsGoodForGroups': 'True', 'RestaurantsAttire': "u'casual'", 'BusinessAcceptsCreditCards': 'True', 'RestaurantsPriceRange2': '1', 'Ambience': "{'romantic': False, 'intimate': False, 'touristy': False, 'hipster': False, 'divey': False, 'classy': False, 'trendy': False, 'upscale': False, 'casual': False}", 'RestaurantsReservations': 'False', 'RestaurantsTakeOut': 'True', 'WiFi': "u'free'", 'GoodForKids': 'True', 'HasTV': 'True', 'Alcohol': "u'full_bar'", 'BusinessParking': "{'garage': False, 'street': False, 'validated': False, 'lot': True, 'valet': False}", 'RestaurantsDelivery': 'False', 'NoiseLevel': "u'average'", 'OutdoorSeating': 'True'}, 'description': 'Located at 914 Edwardsville Rd in Troy, IL, this vibrant spot offers a diverse menu featuring American (New) cuisine, along with a lively atmosphere perfect for nightlife, bars, restaurants, and sports bars.', 'state': None}, {'business_id': 'businessid_26', 'attributes': {'WiFi': "u'free'", 'RestaurantsReservations': 'False', 'GoodForKids': 'True', 'Caters': 'False', 'RestaurantsPriceRange2': '1', 'OutdoorSeating': 'False', 'RestaurantsAttire': "u'casual'", 'HasTV': 'True', 'Alcohol': "u'none'", 'RestaurantsTakeOut': 'True', 'RestaurantsTableService': 'False', 'DriveThru': 'True', 'RestaurantsGoodForGroups': 'False', 'BusinessAcceptsCreditCards': 'True', 'BikeParking': 'True', 'RestaurantsDelivery': 'True', 'NoiseLevel': "u'average'", 'BusinessParking': "{'garage': False, 'street': False, 'validated': False, 'lot': False, 'valet': False}", 'Ambience': "{'romantic': False, 'intimate': False, 'touristy': False, 'hipster': False, 'divey': False, 'classy': False, 'trendy': False, 'upscale': False, 'casual': False}", 'GoodForMeal': "{'dessert': False, 'latenight': False, 'lunch': False, 'dinner': False, 'brunch': False, 'breakfast': False}"}, 'description': 'Located at 7003 Seminole Blvd in Seminole, FL, this establishment specializes in a variety of offerings, including Fast Food, Restaurants, Coffee & Tea, Food, and Burgers, making it a convenient stop for a quick meal or a refreshing beverage.', 'state': None}, {'business_id': 'businessid_89', 'attributes': {'BikeParking': 'True', 'WiFi': "u'free'", 'RestaurantsPriceRange2': '1', 'BusinessAcceptsCreditCards': 'True', 'BusinessParking': "{'garage': False, 'street': False, 'validated': False, 'lot': True, 'valet': False}"}, 'description': 'Located at 540 Shoemaker Rd in King of Prussia, PA, this establishment offers a range of services including Dry Cleaning & Laundry, Laundromat, Local Services, and Laundry Services.', 'state': None}, {'business_id': 'businessid_97', 'attributes': {'WiFi': "u'free'", 'BusinessAcceptsCreditCards': 'True'}, 'description': 'Located at 560 Cottman Ave in Cheltenham, PA, this establishment specializes in Body Shops, Automotive services to meet all your vehicle repair needs.', 'state': None}, {'business_id': 'businessid_67', 'attributes': {'WheelchairAccessible': 'True', 'DogsAllowed': 'False', 'RestaurantsTakeOut': 'True', 'HappyHour': 'False', 'RestaurantsDelivery': 'True', 'BusinessAcceptsCreditCards': 'True', 'Corkage': 'False', 'HasTV': 'True', 'BusinessAcceptsBitcoin': 'False', 'BusinessParking': "{'garage': False, 'street': False, 'validated': False, 'lot': True, 'valet': False}", 'RestaurantsTableService': 'True', 'Alcohol': "u'none'", 'RestaurantsGoodForGroups': 'True', 'WiFi': "u'free'", 'NoiseLevel': "u'average'", 'RestaurantsReservations': 'True', 'BYOB': 'True', 'OutdoorSeating': 'False', 'GoodForMeal': "{'dessert': False, 'latenight': False, 'lunch': False, 'dinner': False, 'brunch': False, 'breakfast': False}", 'BikeParking': 'True', 'Ambience': "{u'divey': False, u'hipster': None, u'casual': True, u'touristy': None, u'trendy': None, u'intimate': None, u'romantic': False, u'classy': None, u'upscale': None}", 'Caters': 'True'}, 'description': 'Located at 1501 W Chester Pike in Havertown, PA, this eatery specializes in Vietnamese, Soup, Restaurants, Noodles, offering a delightful array of flavorful dishes.', 'state': None}, {'business_id': 'businessid_51', 'attributes': {'RestaurantsPriceRange2': '2', 'WiFi': "u'free'"}, 'description': 'Situated at 3109 N Ola Ave in Tampa, FL, this establishment offers a range of services in the hospitality sector, including Hotels & Travel, Hostels, Bed & Breakfast, Hotels, and Event Planning & Services.', 'state': None}, {'business_id': 'businessid_6', 'attributes': {'OutdoorSeating': 'True', 'WiFi': "'free'", 'RestaurantsPriceRange2': '1', 'BusinessParking': "{'garage': False, 'street': True, 'validated': False, 'lot': False, 'valet': False}", 'Smoking': "u'outdoor'", 'HappyHour': 'True', 'RestaurantsTakeOut': 'True', 'BestNights': "{'monday': True, 'tuesday': False, 'friday': True, 'wednesday': False, 'thursday': False, 'sunday': False, 'saturday': True}", 'HasTV': 'True', 'CoatCheck': 'False', 'Ambience': "{'romantic': False, 'intimate': False, 'classy': False, 'hipster': True, 'divey': False, 'touristy': False, 'trendy': False, 'upscale': False, 'casual': True}", 'BusinessAcceptsBitcoin': 'False', 'RestaurantsAttire': "'casual'", 'Music': "{'dj': False, 'background_music': False, 'no_music': False, 'jukebox': False, 'live': False, 'video': False, 'karaoke': False}", 'RestaurantsTableService': 'False', 'Alcohol': "u'full_bar'", 'GoodForMeal': "{'dessert': False, 'latenight': False, 'lunch': False, 'dinner': False, 'brunch': False, 'breakfast': True}", 'Caters': 'True', 'GoodForKids': 'True', 'BikeParking': 'True', 'RestaurantsReservations': 'False', 'BusinessAcceptsCreditCards': 'True', 'DogsAllowed': 'True', 'NoiseLevel': "u'average'", 'WheelchairAccessible': 'True', 'RestaurantsGoodForGroups': 'True', 'RestaurantsDelivery': 'False'}, 'description': 'Located at 246 W 1st St in Reno, NV, this vibrant destination offers a delightful mix of Restaurants, Breakfast & Brunch, Bars, Wine Bars, Coffee & Tea, Food, Cafes, Sandwiches, and Nightlife, making it an ideal spot for any meal or occasion.', 'state': None}]}}

exec(code, env_args)
