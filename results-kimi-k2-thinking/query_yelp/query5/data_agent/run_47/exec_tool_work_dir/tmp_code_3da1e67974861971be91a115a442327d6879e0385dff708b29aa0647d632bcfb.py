code = """import json
import re
from collections import Counter

# Load WiFi businesses data
wifi_businesses_file = locals()['var_functions.query_db:18']
with open(wifi_businesses_file, 'r') as f:
    wifi_businesses = json.load(f)

print('Total WiFi businesses retrieved: ' + str(len(wifi_businesses)))

# Function to extract state from description
def extract_state(description):
    if not description or description == 'None':
        return None
    
    desc_str = str(description)
    # Look for pattern: "in City, State" or similar
    # Match 2-letter US state codes
    match = re.search(r'\bin [^,]+,? ([A-Z]{2})\b', desc_str)
    if match:
        state = match.group(1)
        # Filter for US states only
        us_states = {'AL', 'AK', 'AZ', 'AR', 'CA', 'CO', 'CT', 'DE', 'FL', 'GA', 
                     'HI', 'ID', 'IL', 'IN', 'IA', 'KS', 'KY', 'LA', 'ME', 'MD', 
                     'MA', 'MI', 'MN', 'MS', 'MO', 'MT', 'NE', 'NV', 'NH', 'NJ', 
                     'NM', 'NY', 'NC', 'ND', 'OH', 'OK', 'OR', 'PA', 'RI', 'SC', 
                     'SD', 'TN', 'TX', 'UT', 'VT', 'VA', 'WA', 'WV', 'WI', 'WY', 'DC'}
        if state in us_states:
            return state
    return None

# Process all WiFi businesses
businesses_with_state = []
for biz in wifi_businesses:
    state = extract_state(biz.get('description', ''))
    if state:
        # Convert business_id to business_ref format for later join
        business_id = biz['business_id']
        business_ref = business_id.replace('businessid_', 'businessref_')
        
        businesses_with_state.append({
            'business_id': business_id,
            'business_ref': business_ref,
            'state': state,
            'name': biz.get('name', ''),
            'description': biz.get('description', '')
        })

print('Successfully extracted states for ' + str(len(businesses_with_state)) + ' businesses')

# Count by state
state_counts = Counter([b['state'] for b in businesses_with_state])
sorted_states = state_counts.most_common()

print('State distribution:')
for state, count in sorted_states:
    print('  ' + state + ': ' + str(count))

# Prepare result
result = {
    'businesses_with_state': businesses_with_state,
    'state_counts': sorted_states
}

print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.list_db:0': ['checkin', 'business'], 'var_functions.query_db:2': [{'_id': '6859a000fe8b31cd7362e2ab', 'business_id': 'businessid_49', 'name': 'Steps to Learning Montessori Preschool', 'review_count': '8', 'is_open': '1', 'attributes': {'BusinessAcceptsCreditCards': 'True', 'WiFi': "u'no'", 'BusinessAcceptsBitcoin': 'False'}, 'hours': {'Monday': '0:0-0:0', 'Tuesday': '8:0-17:0', 'Wednesday': '8:0-17:0', 'Thursday': '8:0-17:0', 'Friday': '8:0-17:0'}, 'description': 'Located at 6901 Phelps Rd in Goleta, CA, this facility offers a nurturing environment for young learners, providing a range of services in Education, Elementary Schools, Child Care & Day Care, Local Services, Preschools, and Montessori Schools.'}, {'_id': '6859a000fe8b31cd7362e2ac', 'business_id': 'businessid_47', 'name': 'Breeze Blow Dry Bar', 'review_count': '81', 'is_open': '0', 'attributes': {'ByAppointmentOnly': 'False', 'BusinessAcceptsCreditCards': 'True', 'GoodForKids': 'True', 'RestaurantsPriceRange2': '2', 'BikeParking': 'False', 'BusinessParking': "{'garage': False, 'street': False, 'validated': False, 'lot': True, 'valet': False}"}, 'hours': {'Monday': '7:0-18:0', 'Tuesday': '7:0-18:0', 'Wednesday': '7:0-18:0', 'Thursday': '7:0-18:0', 'Friday': '7:0-19:0', 'Saturday': '8:0-19:0', 'Sunday': '10:0-17:0'}, 'description': 'Located at 9916 Clayton Rd in St. Louis, MO, this establishment offers a wide range of services, including Hair Salons, Beauty & Spas, Hair Stylists, Skin Care, Blow Dry/Out Services, and Makeup Artists.'}, {'_id': '6859a000fe8b31cd7362e2ad', 'business_id': 'businessid_88', 'name': 'Impact Guns', 'review_count': '39', 'is_open': '1', 'attributes': {'BusinessParking': "{'garage': False, 'street': False, 'validated': False, 'lot': False, 'valet': False}", 'GoodForKids': 'True', 'BusinessAcceptsCreditCards': 'True', 'ByAppointmentOnly': 'False', 'BikeParking': 'True'}, 'hours': {'Monday': '10:0-19:0', 'Tuesday': '10:0-19:0', 'Wednesday': '10:0-19:0', 'Thursday': '10:0-19:0', 'Friday': '10:0-19:0', 'Saturday': '10:0-19:0'}, 'description': 'Located at 11655 W Executive Dr in Boise, ID, this facility offers enthusiasts a premier destination for Gun/Rifle Ranges, Active Life.'}, {'_id': '6859a000fe8b31cd7362e2ae', 'business_id': 'businessid_41', 'name': 'Palms Primary Care', 'review_count': '5', 'is_open': '1', 'attributes': 'None', 'hours': {'Monday': '8:30-17:0', 'Tuesday': '8:30-17:0', 'Wednesday': '8:30-17:0', 'Thursday': '8:30-17:0', 'Friday': '8:30-17:0'}, 'description': 'Located at 1615 Pasadena Ave S, Ste 430 in Saint Petersburg, FL, this facility offers a range of services in Internal Medicine, Doctors, Health & Medical.'}, {'_id': '6859a000fe8b31cd7362e2af', 'business_id': 'businessid_33', 'name': 'J&Q Nails', 'review_count': '28', 'is_open': '1', 'attributes': {'BusinessParking': "{'garage': False, 'street': False, 'validated': False, 'lot': False, 'valet': False}", 'BusinessAcceptsCreditCards': 'True', 'AcceptsInsurance': 'False', 'ByAppointmentOnly': 'False', 'RestaurantsPriceRange2': '2', 'WheelchairAccessible': 'True', 'BikeParking': 'False'}, 'hours': {'Monday': '9:30-19:0', 'Tuesday': '9:30-19:0', 'Wednesday': '9:30-19:0', 'Thursday': '9:30-19:0', 'Friday': '9:30-19:0', 'Saturday': '9:30-17:30'}, 'description': 'Located at 9655 E US Hwy 36, Unit H in Avon, IN, this establishment offers a range of services including Nail Salons, Hair Removal, Beauty & Spas, and Waxing.'}], 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json', 'var_functions.query_db:6': 'file_storage/functions.query_db:6.json', 'var_functions.execute_python:8': {'businesses_with_state': [{'business_id': 'businessid_64', 'state': 'MO', 'description': 'Located at 12337 Olive Blvd in Creve Coeur, MO, this establishment offers a range of services in Nail Salons, Beauty & Spas.'}, {'business_id': 'businessid_54', 'state': 'FL', 'description': 'Located at 13151 Race Track Rd in Tampa, FL, this establishment offers a variety of services including Service Stations, Coffee & Tea, Gas Stations, Automotive, Gas Stations, Food, and Convenience Stores.'}, {'business_id': 'businessid_91', 'state': 'LA', 'description': 'Located at 1625 Baronne St in New Orleans, LA, this vibrant establishment offers a delightful array of options ranging from Food, Shaved Ice, Cajun/Creole, Breakfast & Brunch, Party & Event Planning, Comfort Food, Cafes, Restaurants, to Event Planning & Services, making it a perfect spot for any occasion.'}, {'business_id': 'businessid_93', 'state': 'IL', 'description': 'Located at 914 Edwardsville Rd in Troy, IL, this vibrant spot offers a diverse menu featuring American (New) cuisine, along with a lively atmosphere perfect for nightlife, bars, restaurants, and sports bars.'}, {'business_id': 'businessid_26', 'state': 'FL', 'description': 'Located at 7003 Seminole Blvd in Seminole, FL, this establishment specializes in a variety of offerings, including Fast Food, Restaurants, Coffee & Tea, Food, and Burgers, making it a convenient stop for a quick meal or a refreshing beverage.'}, {'business_id': 'businessid_89', 'state': 'PA', 'description': 'Located at 540 Shoemaker Rd in King of Prussia, PA, this establishment offers a range of services including Dry Cleaning & Laundry, Laundromat, Local Services, and Laundry Services.'}, {'business_id': 'businessid_97', 'state': 'PA', 'description': 'Located at 560 Cottman Ave in Cheltenham, PA, this establishment specializes in Body Shops, Automotive services to meet all your vehicle repair needs.'}, {'business_id': 'businessid_67', 'state': 'PA', 'description': 'Located at 1501 W Chester Pike in Havertown, PA, this eatery specializes in Vietnamese, Soup, Restaurants, Noodles, offering a delightful array of flavorful dishes.'}, {'business_id': 'businessid_51', 'state': 'FL', 'description': 'Situated at 3109 N Ola Ave in Tampa, FL, this establishment offers a range of services in the hospitality sector, including Hotels & Travel, Hostels, Bed & Breakfast, Hotels, and Event Planning & Services.'}, {'business_id': 'businessid_55', 'state': 'FL', 'description': 'Located at 1003 4th St N in St. Petersburg, FL, this delightful spot offers a variety of treats including Ice Cream & Frozen Yogurt, Shaved Ice, Food, and Desserts.'}, {'business_id': 'businessid_77', 'state': 'PA', 'description': 'Located at 900 Packer Ave in Philadelphia, PA, this establishment offers a range of services in Hotels & Travel, Venues & Event Spaces, Hotels, and Event Planning & Services, making it an ideal choice for travelers and event organizers alike.'}, {'business_id': 'businessid_86', 'state': 'PA', 'description': 'Located at 705 East Passyunk Ave in Philadelphia, PA, this vibrant eatery offers a diverse menu featuring American (New), Restaurants, American (Traditional), Asian Fusion, Noodles, Dim Sum, Fast Food, Chinese, catering to a variety of tastes and preferences.'}, {'business_id': 'businessid_40', 'state': 'PA', 'description': 'Located at 4457 Main St in Philadelphia, PA, this establishment specializes in Venues & Event Spaces, Event Planning & Services, making it an ideal choice for hosting memorable gatherings and celebrations.'}, {'business_id': 'businessid_44', 'state': 'PA', 'description': 'Located at 2424 E York St in Philadelphia, PA, this vibrant establishment offers a delightful array of options, including Restaurants, Diners, Breakfast & Brunch, American (New), American (Traditional), Burgers, making it a perfect spot for any meal of the day.'}, {'business_id': 'businessid_25', 'state': 'ID', 'description': 'Located at 5608 W Fairview Ave in Boise, ID, this charming establishment offers a delightful array of options in the categories of Food, Restaurants, Sandwiches, Breakfast & Brunch, and Bakeries.'}, {'business_id': 'businessid_82', 'state': 'PA', 'description': 'Located at 1620 South St in Philadelphia, PA, this vibrant establishment offers a delightful array of options, perfect for any occasion, including Restaurants, Coffee & Tea, Food, Breakfast & Brunch, Event Planning & Services, American (Traditional), and Caterers.'}, {'business_id': 'businessid_12', 'state': 'AB', 'description': 'Located at 7704 Calgary Trail S in Edmonton, AB, this vibrant spot offers a diverse experience with options for Pubs, Restaurants, Nightlife, Burgers, Seafood, and Bars.'}, {'business_id': 'businessid_16', 'state': 'IN', 'description': 'Located at 4901 E 82nd St, Ste 900 in Indianapolis, IN, this vibrant establishment offers a fantastic experience for those seeking American (New), Nightlife, Bars, Restaurants, Pubs.'}, {'business_id': 'businessid_46', 'state': 'MO', 'description': 'Located at 6525 Delmar Blvd in Saint Louis, MO, this vibrant establishment offers a diverse experience with options for Restaurants, American (Traditional), Barbeque, Cocktail Bars, Bars, and Nightlife.'}], 'state_counts': [['PA', 8], ['FL', 4], ['MO', 2], ['LA', 1], ['IL', 1], ['ID', 1], ['AB', 1], ['IN', 1]], 'top_state': ['PA', 8]}, 'var_functions.execute_python:16': {'businesses_with_state': [], 'state_counts': [], 'top_state': None}, 'var_functions.query_db:18': 'file_storage/functions.query_db:18.json'}

exec(code, env_args)
