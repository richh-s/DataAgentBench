code = """import json
import re

# Read the business data from the file path stored in the variable
file_path = locals()['var_functions.query_db:5']
with open(file_path, 'r') as f:
    businesses = json.load(f)

print(f"Processing {len(businesses)} businesses...")

# Parse state from description and check WiFi
wifi_businesses = []
for business in businesses:
    description = business.get('description', '')
    wifi_info = business.get('attributes', {}).get('WiFi', '')
    business_id = business.get('business_id', '')
    
    # Check if WiFi is offered (not 'no')
    wifi_offered = False
    wifi_str = str(wifi_info).lower()
    if wifi_info and 'no' not in wifi_str:
        wifi_offered = True
    elif wifi_info and ('free' in wifi_str or 'paid' in wifi_str or 'yes' in wifi_str):
        wifi_offered = True
    
    # Extract state (2-letter code before zip code)
    state_match = re.search(r' ([A-Z]{2})\s+\d{5}', description)
    if not state_match:
        state_match = re.search(r' ([A-Z]{2})', description)
    
    state = state_match.group(1) if state_match else None
    
    if wifi_offered and state:
        wifi_businesses.append({
            'business_id': business_id,
            'state': state,
            'wifi_status': str(wifi_info)
        })

print(f"Found {len(wifi_businesses)} businesses with WiFi")

# Count per state
from collections import Counter
state_counts = Counter([b['state'] for b in wifi_businesses])
top_states = state_counts.most_common(5)

print("Top 5 states with WiFi businesses:")
for state, count in top_states:
    print(f"  {state}: {count}")

# Get the top state
top_state = top_states[0] if top_states else None
wifi_business_ids = [b['business_id'] for b in wifi_businesses]

result = {
    'wifi_business_count': len(wifi_businesses),
    'state_counts': dict(state_counts),
    'top_state': top_state,
    'wifi_business_ids': wifi_business_ids
}

print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.query_db:0': [{'_id': '6859a000fe8b31cd7362e2ab', 'business_id': 'businessid_49', 'name': 'Steps to Learning Montessori Preschool', 'attributes': {'BusinessAcceptsCreditCards': 'True', 'WiFi': "u'no'", 'BusinessAcceptsBitcoin': 'False'}, 'description': 'Located at 6901 Phelps Rd in Goleta, CA, this facility offers a nurturing environment for young learners, providing a range of services in Education, Elementary Schools, Child Care & Day Care, Local Services, Preschools, and Montessori Schools.'}, {'_id': '6859a000fe8b31cd7362e2b1', 'business_id': 'businessid_92', 'name': 'Luminosity', 'attributes': {'ByAppointmentOnly': 'False', 'BusinessAcceptsCreditCards': 'True', 'BusinessParking': "{'garage': True, 'street': False, 'validated': False, 'lot': False, 'valet': False}", 'RestaurantsPriceRange2': '2', 'WheelchairAccessible': 'True', 'BikeParking': 'True', 'NoiseLevel': "u'quiet'", 'WiFi': "u'no'"}, 'description': 'Located at 690 W Dekalb Pike in King of Prussia, PA, this business offers a diverse range of services and products in the fields of Cosmetics & Beauty Supply, Cosmetic Dentists, Tanning, Teeth Whitening, Beauty & Spas, Dentists, Shopping, Blow Dry/Out Services, Health & Medical, Spray Tanning, and Hair Salons.'}, {'_id': '6859a000fe8b31cd7362e2b2', 'business_id': 'businessid_64', 'name': 'Nail Care Salon', 'attributes': {'BusinessParking': "{'garage': True, 'street': False, 'validated': False, 'lot': True, 'valet': False}", 'ByAppointmentOnly': 'False', 'BusinessAcceptsCreditCards': 'True', 'RestaurantsPriceRange2': '2', 'BikeParking': 'True', 'WiFi': "u'free'"}, 'description': 'Located at 12337 Olive Blvd in Creve Coeur, MO, this establishment offers a range of services in Nail Salons, Beauty & Spas.'}, {'_id': '6859a000fe8b31cd7362e2b7', 'business_id': 'businessid_54', 'name': '7-Eleven', 'attributes': {'BusinessParking': "{'garage': False, 'street': False, 'validated': False, 'lot': False, 'valet': False}", 'BusinessAcceptsCreditCards': 'True', 'WheelchairAccessible': 'True', 'RestaurantsDelivery': 'True', 'RestaurantsTakeOut': 'True', 'RestaurantsPriceRange2': '1', 'WiFi': "u'free'"}, 'description': 'Located at 13151 Race Track Rd in Tampa, FL, this establishment offers a variety of services including Service Stations, Coffee & Tea, Gas Stations, Automotive, Gas Stations, Food, and Convenience Stores.'}, {'_id': '6859a000fe8b31cd7362e2ba', 'business_id': 'businessid_91', 'name': 'Cafe Porche and snowbar', 'attributes': {'BusinessParking': "{'garage': False, 'street': True, 'validated': False, 'lot': False, 'valet': False}", 'WiFi': "u'free'", 'WheelchairAccessible': 'True', 'Caters': 'True', 'HasTV': 'True', 'HappyHour': 'False', 'Ambience': "{'touristy': None, 'hipster': None, 'romantic': None, 'divey': None, 'intimate': True, 'trendy': None, 'upscale': None, 'classy': True, 'casual': True}", 'RestaurantsDelivery': 'True', 'RestaurantsPriceRange2': '2', 'GoodForKids': 'True', 'RestaurantsAttire': "u'casual'", 'BikeParking': 'True', 'OutdoorSeating': 'True', 'NoiseLevel': "u'quiet'", 'RestaurantsGoodForGroups': 'True', 'RestaurantsTakeOut': 'True', 'BusinessAcceptsCreditCards': 'True', 'RestaurantsReservations': 'False', 'GoodForMeal': "{'dessert': None, 'latenight': None, 'lunch': True, 'dinner': None, 'brunch': True, 'breakfast': True}", 'Alcohol': "u'beer_and_wine'", 'RestaurantsTableService': 'True', 'Corkage': 'False', 'BYOB': 'True'}, 'description': 'Located at 1625 Baronne St in New Orleans, LA, this vibrant establishment offers a delightful array of options ranging from Food, Shaved Ice, Cajun/Creole, Breakfast & Brunch, Party & Event Planning, Comfort Food, Cafes, Restaurants, to Event Planning & Services, making it a perfect spot for any occasion.'}, {'_id': '6859a000fe8b31cd7362e2bc', 'business_id': 'businessid_93', 'name': "Callahan's Corner", 'attributes': {'RestaurantsGoodForGroups': 'True', 'RestaurantsAttire': "u'casual'", 'BusinessAcceptsCreditCards': 'True', 'RestaurantsPriceRange2': '1', 'Ambience': "{'romantic': False, 'intimate': False, 'touristy': False, 'hipster': False, 'divey': False, 'classy': False, 'trendy': False, 'upscale': False, 'casual': False}", 'RestaurantsReservations': 'False', 'RestaurantsTakeOut': 'True', 'WiFi': "u'free'", 'GoodForKids': 'True', 'HasTV': 'True', 'Alcohol': "u'full_bar'", 'BusinessParking': "{'garage': False, 'street': False, 'validated': False, 'lot': True, 'valet': False}", 'RestaurantsDelivery': 'False', 'NoiseLevel': "u'average'", 'OutdoorSeating': 'True'}, 'description': 'Located at 914 Edwardsville Rd in Troy, IL, this vibrant spot offers a diverse menu featuring American (New) cuisine, along with a lively atmosphere perfect for nightlife, bars, restaurants, and sports bars.'}, {'_id': '6859a000fe8b31cd7362e2be', 'business_id': 'businessid_24', 'name': 'FroYo Frozen Yogurt', 'attributes': {'BusinessAcceptsCreditCards': 'True', 'RestaurantsPriceRange2': '1', 'WiFi': "u'no'", 'BikeParking': 'True', 'BusinessParking': "{'garage': False, 'street': True, 'validated': False, 'lot': False, 'valet': False}", 'RestaurantsTakeOut': 'True'}, 'description': 'Located at 4663 Maryland Ave in Saint Louis, MO, this delightful spot offers a tempting selection of treats in the categories of Food, Ice Cream & Frozen Yogurt.'}, {'_id': '6859a000fe8b31cd7362e2c1', 'business_id': 'businessid_26', 'name': "McDonald's", 'attributes': {'WiFi': "u'free'", 'RestaurantsReservations': 'False', 'GoodForKids': 'True', 'Caters': 'False', 'RestaurantsPriceRange2': '1', 'OutdoorSeating': 'False', 'RestaurantsAttire': "u'casual'", 'HasTV': 'True', 'Alcohol': "u'none'", 'RestaurantsTakeOut': 'True', 'RestaurantsTableService': 'False', 'DriveThru': 'True', 'RestaurantsGoodForGroups': 'False', 'BusinessAcceptsCreditCards': 'True', 'BikeParking': 'True', 'RestaurantsDelivery': 'True', 'NoiseLevel': "u'average'", 'BusinessParking': "{'garage': False, 'street': False, 'validated': False, 'lot': False, 'valet': False}", 'Ambience': "{'romantic': False, 'intimate': False, 'touristy': False, 'hipster': False, 'divey': False, 'classy': False, 'trendy': False, 'upscale': False, 'casual': False}", 'GoodForMeal': "{'dessert': False, 'latenight': False, 'lunch': False, 'dinner': False, 'brunch': False, 'breakfast': False}"}, 'description': 'Located at 7003 Seminole Blvd in Seminole, FL, this establishment specializes in a variety of offerings, including Fast Food, Restaurants, Coffee & Tea, Food, and Burgers, making it a convenient stop for a quick meal or a refreshing beverage.'}, {'_id': '6859a000fe8b31cd7362e2c3', 'business_id': 'businessid_89', 'name': 'King of Prussia Laundromat', 'attributes': {'BikeParking': 'True', 'WiFi': "u'free'", 'RestaurantsPriceRange2': '1', 'BusinessAcceptsCreditCards': 'True', 'BusinessParking': "{'garage': False, 'street': False, 'validated': False, 'lot': True, 'valet': False}"}, 'description': 'Located at 540 Shoemaker Rd in King of Prussia, PA, this establishment offers a range of services including Dry Cleaning & Laundry, Laundromat, Local Services, and Laundry Services.'}, {'_id': '6859a000fe8b31cd7362e2c4', 'business_id': 'businessid_32', 'name': 'The Recovery Room Bar & Grill', 'attributes': {'RestaurantsPriceRange2': '1', 'GoodForKids': 'False', 'Caters': 'False', 'Ambience': "{'romantic': False, 'intimate': False, 'touristy': False, 'hipster': False, 'divey': False, 'classy': False, 'trendy': False, 'upscale': False, 'casual': False}", 'HasTV': 'True', 'BusinessParking': "{'garage': False, 'street': False, 'validated': False, 'lot': False, 'valet': False}", 'RestaurantsReservations': 'False', 'RestaurantsGoodForGroups': 'True', 'Alcohol': "u'full_bar'", 'RestaurantsTakeOut': 'True', 'NoiseLevel': "u'quiet'", 'RestaurantsDelivery': 'False', 'OutdoorSeating': 'False', 'BusinessAcceptsCreditCards': 'True', 'WiFi': "u'no'", 'RestaurantsAttire': "u'casual'", 'BikeParking': 'False'}, 'description': 'Located at 1715 Jefferson Hwy in New Orleans, LA, this lively establishment offers a great atmosphere for enjoying Bars, Dive Bars, Burgers, Nightlife, and Restaurants.'}], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json'}

exec(code, env_args)
