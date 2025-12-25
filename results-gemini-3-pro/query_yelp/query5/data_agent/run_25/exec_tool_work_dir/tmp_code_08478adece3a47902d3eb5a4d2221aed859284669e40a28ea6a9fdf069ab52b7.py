code = """import json
import re

# Load business data
businesses = locals()['var_function-call-17505946435478560429']

# Load review data
with open(locals()['var_function-call-9204549464474788302'], 'r') as f:
    reviews = json.load(f)

US_STATES = {
    'AL', 'AK', 'AZ', 'AR', 'CA', 'CO', 'CT', 'DE', 'FL', 'GA', 
    'HI', 'ID', 'IL', 'IN', 'IA', 'KS', 'KY', 'LA', 'ME', 'MD', 
    'MA', 'MI', 'MN', 'MS', 'MO', 'MT', 'NE', 'NV', 'NH', 'NJ', 
    'NM', 'NY', 'NC', 'ND', 'OH', 'OK', 'OR', 'PA', 'RI', 'SC', 
    'SD', 'TN', 'TX', 'UT', 'VT', 'VA', 'WA', 'WV', 'WI', 'WY', 'DC'
}

# Helper to check WiFi (already filtered by query, but double check)
def has_wifi(attrs):
    if not attrs: return False
    wifi = attrs.get('WiFi')
    if not wifi: return False
    # Check if 'free' or 'paid' in value
    # Value format is "u'free'", "'free'", etc.
    return 'free' in str(wifi).lower() or 'paid' in str(wifi).lower()

# Helper to extract state
def get_state(desc):
    match = re.search(r",\s([A-Z]{2}),\sthis", desc)
    if match:
        return match.group(1)
    return None

# Map business_id suffix to state
wifi_biz_state = {} 

for b in businesses:
    if has_wifi(b.get('attributes')):
        bid = b.get('business_id')
        if bid.startswith('businessid_'):
            suffix = bid.split('_')[1]
            state = get_state(b.get('description', ''))
            if state in US_STATES:
                wifi_biz_state[suffix] = state

# Count businesses per state
state_counts = {}
for suffix, state in wifi_biz_state.items():
    state_counts[state] = state_counts.get(state, 0) + 1

if not state_counts:
    print("__RESULT__:")
    print(json.dumps("No US businesses with WiFi found"))
    exit()

# Find top state
# If tie, picking one is usually fine, or I can list.
# But max() picks the first one encountered in case of ties usually.
top_state = max(state_counts, key=state_counts.get)
top_count = state_counts[top_state]

# Group ratings for businesses in top state
biz_ratings = {} # suffix -> [ratings]

for r in reviews:
    bref = r.get('business_ref')
    if bref and bref.startswith('businessref_'):
        suffix = bref.split('_')[1]
        
        # Check if this business is in top state
        if suffix in wifi_biz_state and wifi_biz_state[suffix] == top_state:
            if suffix not in biz_ratings:
                biz_ratings[suffix] = []
            biz_ratings[suffix].append(float(r['rating']))

# Calculate average rating
# Average of business averages
avg_ratings = []
for suffix in biz_ratings:
    ratings = biz_ratings[suffix]
    if ratings:
        avg_ratings.append(sum(ratings) / len(ratings))

final_avg_rating = 0
if avg_ratings:
    final_avg_rating = sum(avg_ratings) / len(avg_ratings)

result = {
    "top_state": top_state,
    "business_count": top_count,
    "average_rating": final_avg_rating,
    "state_counts": state_counts # for debugging
}

print("__RESULT__:")
print(json.dumps(result))"""

env_args = {'var_function-call-1384464540767786372': [{'_id': '6859a000fe8b31cd7362e2ab', 'business_id': 'businessid_49', 'name': 'Steps to Learning Montessori Preschool', 'review_count': '8', 'is_open': '1', 'attributes': {'BusinessAcceptsCreditCards': 'True', 'WiFi': "u'no'", 'BusinessAcceptsBitcoin': 'False'}, 'hours': {'Monday': '0:0-0:0', 'Tuesday': '8:0-17:0', 'Wednesday': '8:0-17:0', 'Thursday': '8:0-17:0', 'Friday': '8:0-17:0'}, 'description': 'Located at 6901 Phelps Rd in Goleta, CA, this facility offers a nurturing environment for young learners, providing a range of services in Education, Elementary Schools, Child Care & Day Care, Local Services, Preschools, and Montessori Schools.'}, {'_id': '6859a000fe8b31cd7362e2ac', 'business_id': 'businessid_47', 'name': 'Breeze Blow Dry Bar', 'review_count': '81', 'is_open': '0', 'attributes': {'ByAppointmentOnly': 'False', 'BusinessAcceptsCreditCards': 'True', 'GoodForKids': 'True', 'RestaurantsPriceRange2': '2', 'BikeParking': 'False', 'BusinessParking': "{'garage': False, 'street': False, 'validated': False, 'lot': True, 'valet': False}"}, 'hours': {'Monday': '7:0-18:0', 'Tuesday': '7:0-18:0', 'Wednesday': '7:0-18:0', 'Thursday': '7:0-18:0', 'Friday': '7:0-19:0', 'Saturday': '8:0-19:0', 'Sunday': '10:0-17:0'}, 'description': 'Located at 9916 Clayton Rd in St. Louis, MO, this establishment offers a wide range of services, including Hair Salons, Beauty & Spas, Hair Stylists, Skin Care, Blow Dry/Out Services, and Makeup Artists.'}, {'_id': '6859a000fe8b31cd7362e2ad', 'business_id': 'businessid_88', 'name': 'Impact Guns', 'review_count': '39', 'is_open': '1', 'attributes': {'BusinessParking': "{'garage': False, 'street': False, 'validated': False, 'lot': False, 'valet': False}", 'GoodForKids': 'True', 'BusinessAcceptsCreditCards': 'True', 'ByAppointmentOnly': 'False', 'BikeParking': 'True'}, 'hours': {'Monday': '10:0-19:0', 'Tuesday': '10:0-19:0', 'Wednesday': '10:0-19:0', 'Thursday': '10:0-19:0', 'Friday': '10:0-19:0', 'Saturday': '10:0-19:0'}, 'description': 'Located at 11655 W Executive Dr in Boise, ID, this facility offers enthusiasts a premier destination for Gun/Rifle Ranges, Active Life.'}, {'_id': '6859a000fe8b31cd7362e2ae', 'business_id': 'businessid_41', 'name': 'Palms Primary Care', 'review_count': '5', 'is_open': '1', 'attributes': 'None', 'hours': {'Monday': '8:30-17:0', 'Tuesday': '8:30-17:0', 'Wednesday': '8:30-17:0', 'Thursday': '8:30-17:0', 'Friday': '8:30-17:0'}, 'description': 'Located at 1615 Pasadena Ave S, Ste 430 in Saint Petersburg, FL, this facility offers a range of services in Internal Medicine, Doctors, Health & Medical.'}, {'_id': '6859a000fe8b31cd7362e2af', 'business_id': 'businessid_33', 'name': 'J&Q Nails', 'review_count': '28', 'is_open': '1', 'attributes': {'BusinessParking': "{'garage': False, 'street': False, 'validated': False, 'lot': False, 'valet': False}", 'BusinessAcceptsCreditCards': 'True', 'AcceptsInsurance': 'False', 'ByAppointmentOnly': 'False', 'RestaurantsPriceRange2': '2', 'WheelchairAccessible': 'True', 'BikeParking': 'False'}, 'hours': {'Monday': '9:30-19:0', 'Tuesday': '9:30-19:0', 'Wednesday': '9:30-19:0', 'Thursday': '9:30-19:0', 'Friday': '9:30-19:0', 'Saturday': '9:30-17:30'}, 'description': 'Located at 9655 E US Hwy 36, Unit H in Avon, IN, this establishment offers a range of services including Nail Salons, Hair Removal, Beauty & Spas, and Waxing.'}], 'var_function-call-5300744252068254687': [{'_id': '6859a000fe8b31cd7362e2ab', 'business_id': 'businessid_49', 'attributes': {'BusinessAcceptsCreditCards': 'True', 'WiFi': "u'no'", 'BusinessAcceptsBitcoin': 'False'}, 'description': 'Located at 6901 Phelps Rd in Goleta, CA, this facility offers a nurturing environment for young learners, providing a range of services in Education, Elementary Schools, Child Care & Day Care, Local Services, Preschools, and Montessori Schools.'}, {'_id': '6859a000fe8b31cd7362e2ac', 'business_id': 'businessid_47', 'attributes': {'ByAppointmentOnly': 'False', 'BusinessAcceptsCreditCards': 'True', 'GoodForKids': 'True', 'RestaurantsPriceRange2': '2', 'BikeParking': 'False', 'BusinessParking': "{'garage': False, 'street': False, 'validated': False, 'lot': True, 'valet': False}"}, 'description': 'Located at 9916 Clayton Rd in St. Louis, MO, this establishment offers a wide range of services, including Hair Salons, Beauty & Spas, Hair Stylists, Skin Care, Blow Dry/Out Services, and Makeup Artists.'}, {'_id': '6859a000fe8b31cd7362e2ad', 'business_id': 'businessid_88', 'attributes': {'BusinessParking': "{'garage': False, 'street': False, 'validated': False, 'lot': False, 'valet': False}", 'GoodForKids': 'True', 'BusinessAcceptsCreditCards': 'True', 'ByAppointmentOnly': 'False', 'BikeParking': 'True'}, 'description': 'Located at 11655 W Executive Dr in Boise, ID, this facility offers enthusiasts a premier destination for Gun/Rifle Ranges, Active Life.'}, {'_id': '6859a000fe8b31cd7362e2ae', 'business_id': 'businessid_41', 'attributes': 'None', 'description': 'Located at 1615 Pasadena Ave S, Ste 430 in Saint Petersburg, FL, this facility offers a range of services in Internal Medicine, Doctors, Health & Medical.'}, {'_id': '6859a000fe8b31cd7362e2af', 'business_id': 'businessid_33', 'attributes': {'BusinessParking': "{'garage': False, 'street': False, 'validated': False, 'lot': False, 'valet': False}", 'BusinessAcceptsCreditCards': 'True', 'AcceptsInsurance': 'False', 'ByAppointmentOnly': 'False', 'RestaurantsPriceRange2': '2', 'WheelchairAccessible': 'True', 'BikeParking': 'False'}, 'description': 'Located at 9655 E US Hwy 36, Unit H in Avon, IN, this establishment offers a range of services including Nail Salons, Hair Removal, Beauty & Spas, and Waxing.'}], 'var_function-call-9204549464474788302': 'file_storage/function-call-9204549464474788302.json', 'var_function-call-11504517562728626786': 'No businesses with WiFi found', 'var_function-call-13547425221245814823': ["u'no'", 'None'], 'var_function-call-956821256664704147': 5, 'var_function-call-17505946435478560429': [{'_id': '6859a000fe8b31cd7362e2b2', 'business_id': 'businessid_64', 'attributes': {'WiFi': "u'free'"}, 'description': 'Located at 12337 Olive Blvd in Creve Coeur, MO, this establishment offers a range of services in Nail Salons, Beauty & Spas.'}, {'_id': '6859a000fe8b31cd7362e2b7', 'business_id': 'businessid_54', 'attributes': {'WiFi': "u'free'"}, 'description': 'Located at 13151 Race Track Rd in Tampa, FL, this establishment offers a variety of services including Service Stations, Coffee & Tea, Gas Stations, Automotive, Gas Stations, Food, and Convenience Stores.'}, {'_id': '6859a000fe8b31cd7362e2ba', 'business_id': 'businessid_91', 'attributes': {'WiFi': "u'free'"}, 'description': 'Located at 1625 Baronne St in New Orleans, LA, this vibrant establishment offers a delightful array of options ranging from Food, Shaved Ice, Cajun/Creole, Breakfast & Brunch, Party & Event Planning, Comfort Food, Cafes, Restaurants, to Event Planning & Services, making it a perfect spot for any occasion.'}, {'_id': '6859a000fe8b31cd7362e2bc', 'business_id': 'businessid_93', 'attributes': {'WiFi': "u'free'"}, 'description': 'Located at 914 Edwardsville Rd in Troy, IL, this vibrant spot offers a diverse menu featuring American (New) cuisine, along with a lively atmosphere perfect for nightlife, bars, restaurants, and sports bars.'}, {'_id': '6859a000fe8b31cd7362e2c1', 'business_id': 'businessid_26', 'attributes': {'WiFi': "u'free'"}, 'description': 'Located at 7003 Seminole Blvd in Seminole, FL, this establishment specializes in a variety of offerings, including Fast Food, Restaurants, Coffee & Tea, Food, and Burgers, making it a convenient stop for a quick meal or a refreshing beverage.'}, {'_id': '6859a000fe8b31cd7362e2c3', 'business_id': 'businessid_89', 'attributes': {'WiFi': "u'free'"}, 'description': 'Located at 540 Shoemaker Rd in King of Prussia, PA, this establishment offers a range of services including Dry Cleaning & Laundry, Laundromat, Local Services, and Laundry Services.'}, {'_id': '6859a000fe8b31cd7362e2c8', 'business_id': 'businessid_97', 'attributes': {'WiFi': "u'free'"}, 'description': 'Located at 560 Cottman Ave in Cheltenham, PA, this establishment specializes in Body Shops, Automotive services to meet all your vehicle repair needs.'}, {'_id': '6859a000fe8b31cd7362e2d4', 'business_id': 'businessid_67', 'attributes': {'WiFi': "u'free'"}, 'description': 'Located at 1501 W Chester Pike in Havertown, PA, this eatery specializes in Vietnamese, Soup, Restaurants, Noodles, offering a delightful array of flavorful dishes.'}, {'_id': '6859a000fe8b31cd7362e2d6', 'business_id': 'businessid_51', 'attributes': {'WiFi': "u'free'"}, 'description': 'Situated at 3109 N Ola Ave in Tampa, FL, this establishment offers a range of services in the hospitality sector, including Hotels & Travel, Hostels, Bed & Breakfast, Hotels, and Event Planning & Services.'}, {'_id': '6859a000fe8b31cd7362e2dd', 'business_id': 'businessid_6', 'attributes': {'WiFi': "'free'"}, 'description': 'Located at 246 W 1st St in Reno, NV, this vibrant destination offers a delightful mix of Restaurants, Breakfast & Brunch, Bars, Wine Bars, Coffee & Tea, Food, Cafes, Sandwiches, and Nightlife, making it an ideal spot for any meal or occasion.'}, {'_id': '6859a000fe8b31cd7362e2e2', 'business_id': 'businessid_55', 'attributes': {'WiFi': "u'free'"}, 'description': 'Located at 1003 4th St N in St. Petersburg, FL, this delightful spot offers a variety of treats including Ice Cream & Frozen Yogurt, Shaved Ice, Food, and Desserts.'}, {'_id': '6859a000fe8b31cd7362e2ea', 'business_id': 'businessid_77', 'attributes': {'WiFi': "u'free'"}, 'description': 'Located at 900 Packer Ave in Philadelphia, PA, this establishment offers a range of services in Hotels & Travel, Venues & Event Spaces, Hotels, and Event Planning & Services, making it an ideal choice for travelers and event organizers alike.'}, {'_id': '6859a000fe8b31cd7362e2ed', 'business_id': 'businessid_86', 'attributes': {'WiFi': "u'free'"}, 'description': 'Located at 705 East Passyunk Ave in Philadelphia, PA, this vibrant eatery offers a diverse menu featuring American (New), Restaurants, American (Traditional), Asian Fusion, Noodles, Dim Sum, Fast Food, Chinese, catering to a variety of tastes and preferences.'}, {'_id': '6859a000fe8b31cd7362e2ef', 'business_id': 'businessid_40', 'attributes': {'WiFi': "u'free'"}, 'description': 'Located at 4457 Main St in Philadelphia, PA, this establishment specializes in Venues & Event Spaces, Event Planning & Services, making it an ideal choice for hosting memorable gatherings and celebrations.'}, {'_id': '6859a000fe8b31cd7362e2f0', 'business_id': 'businessid_44', 'attributes': {'WiFi': "u'free'"}, 'description': 'Located at 2424 E York St in Philadelphia, PA, this vibrant establishment offers a delightful array of options, including Restaurants, Diners, Breakfast & Brunch, American (New), American (Traditional), Burgers, making it a perfect spot for any meal of the day.'}, {'_id': '6859a000fe8b31cd7362e2f1', 'business_id': 'businessid_43', 'attributes': {'WiFi': "'free'"}, 'description': 'Located at 11425 Allisonville Road in Fishers, IN, this vibrant eatery offers a delightful menu featuring Tex-Mex, Tacos, Restaurants, Breakfast & Brunch, Sandwiches, Mexican, Fast Food, perfect for satisfying any craving at any time of day.'}, {'_id': '6859a000fe8b31cd7362e2f4', 'business_id': 'businessid_20', 'attributes': {'WiFi': "'free'"}, 'description': 'Located at 9040 State Road 54 in Trinity, FL, this establishment offers a diverse array of options, including Restaurants, American (New), Caterers, Fast Food, Chicken Shop, Event Planning & Services, and American (Traditional).'}, {'_id': '6859a000fe8b31cd7362e2fd', 'business_id': 'businessid_25', 'attributes': {'WiFi': "u'free'"}, 'description': 'Located at 5608 W Fairview Ave in Boise, ID, this charming establishment offers a delightful array of options in the categories of Food, Restaurants, Sandwiches, Breakfast & Brunch, and Bakeries.'}, {'_id': '6859a000fe8b31cd7362e2fe', 'business_id': 'businessid_82', 'attributes': {'WiFi': "u'free'"}, 'description': 'Located at 1620 South St in Philadelphia, PA, this vibrant establishment offers a delightful array of options, perfect for any occasion, including Restaurants, Coffee & Tea, Food, Breakfast & Brunch, Event Planning & Services, American (Traditional), and Caterers.'}, {'_id': '6859a000fe8b31cd7362e300', 'business_id': 'businessid_12', 'attributes': {'WiFi': "u'paid'"}, 'description': 'Located at 7704 Calgary Trail S in Edmonton, AB, this vibrant spot offers a diverse experience with options for Pubs, Restaurants, Nightlife, Burgers, Seafood, and Bars.'}, {'_id': '6859a000fe8b31cd7362e305', 'business_id': 'businessid_16', 'attributes': {'WiFi': "u'free'"}, 'description': 'Located at 4901 E 82nd St, Ste 900 in Indianapolis, IN, this vibrant establishment offers a fantastic experience for those seeking American (New), Nightlife, Bars, Restaurants, Pubs.'}, {'_id': '6859a000fe8b31cd7362e306', 'business_id': 'businessid_46', 'attributes': {'WiFi': "u'free'"}, 'description': 'Located at 6525 Delmar Blvd in Saint Louis, MO, this vibrant establishment offers a diverse experience with options for Restaurants, American (Traditional), Barbeque, Cocktail Bars, Bars, and Nightlife.'}]}

exec(code, env_args)
