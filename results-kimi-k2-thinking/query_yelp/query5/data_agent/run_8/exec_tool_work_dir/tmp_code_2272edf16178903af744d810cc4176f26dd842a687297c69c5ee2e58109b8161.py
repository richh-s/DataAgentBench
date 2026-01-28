code = """import json
import re
from collections import defaultdict

# Access the file path from the storage
db_result_key = 'var_functions.query_db:6'
business_data_path = locals()[db_result_key]

# Load the business data from the file
with open(business_data_path, 'r') as f:
    businesses = json.load(f)

print('Total businesses loaded: ' + str(len(businesses)))

# Function to extract state from description
def extract_state(description):
    if not description or 'Located at' not in description:
        return None
    
    # Look for patterns like "in Goleta, CA" or "in Saint Petersburg, FL"
    match = re.search(r',\s*([A-Z]{2})\b', description)
    if match:
        return match.group(1)
    return None

# Check WiFi values to understand the format
wifi_values = set()
for business in businesses[:50]:  # First 50 to sample
    attributes = business.get('attributes')
    if attributes and attributes != 'None':
        wifi = attributes.get('WiFi')
        if wifi:
            wifi_values.add(str(wifi))

print('Sample WiFi values: ' + str(list(wifi_values)))

# Filter businesses with WiFi (free or paid, not 'no')
wifi_businesses = []
state_counts = defaultdict(int)

for business in businesses:
    # Check if business has attributes and WiFi information
    attributes = business.get('attributes')
    if not attributes or attributes == 'None':
        continue
    
    # Check if WiFi attribute exists and indicates WiFi is available (free or paid)
    wifi = attributes.get('WiFi')
    if wifi:
        wifi_str = str(wifi).lower()
        # Check if it contains 'free' or 'paid' but not 'no'
        if ('free' in wifi_str or 'paid' in wifi_str) and 'no' not in wifi_str:
            # Extract state from description
            state = extract_state(business.get('description', ''))
            if state:
                wifi_businesses.append({
                    'business_id': business['business_id'],
                    'state': state,
                    'name': business['name'],
                    'wifi_type': str(wifi)
                })
                state_counts[state] += 1

print('WiFi businesses found: ' + str(len(wifi_businesses)))
print('States represented: ' + str(len(state_counts)))
print('State counts: ' + str(dict(state_counts)))

result_data = {
    'wifi_businesses_count': len(wifi_businesses),
    'state_counts': dict(state_counts)
}

# Find state with most WiFi businesses
if state_counts:
    top_state = max(state_counts.items(), key=lambda x: x[1])
    print('Top state: ' + top_state[0] + ' with ' + str(top_state[1]) + ' businesses')
    
    # Get business IDs for the top state
    top_state_business_ids = [b['business_id'] for b in wifi_businesses if b['state'] == top_state[0]]
    print('Business IDs for top state: ' + str(len(top_state_business_ids)))
    
    # Show sample businesses from top state
    sample_businesses = [b for b in wifi_businesses if b['state'] == top_state[0]][:3]
    print('Sample businesses from ' + top_state[0] + ': ' + str(sample_businesses))
    
    result_data['top_state'] = top_state[0]
    result_data['top_state_count'] = top_state[1]
    result_data['top_state_business_ids'] = top_state_business_ids
else:
    result_data['top_state'] = None
    result_data['top_state_count'] = 0
    result_data['top_state_business_ids'] = []

print('__RESULT__:')
print(json.dumps(result_data))"""

env_args = {'var_functions.query_db:0': [{'_id': '6859a000fe8b31cd7362e2ab', 'business_id': 'businessid_49', 'name': 'Steps to Learning Montessori Preschool', 'review_count': '8', 'is_open': '1', 'attributes': {'BusinessAcceptsCreditCards': 'True', 'WiFi': "u'no'", 'BusinessAcceptsBitcoin': 'False'}, 'hours': {'Monday': '0:0-0:0', 'Tuesday': '8:0-17:0', 'Wednesday': '8:0-17:0', 'Thursday': '8:0-17:0', 'Friday': '8:0-17:0'}, 'description': 'Located at 6901 Phelps Rd in Goleta, CA, this facility offers a nurturing environment for young learners, providing a range of services in Education, Elementary Schools, Child Care & Day Care, Local Services, Preschools, and Montessori Schools.'}, {'_id': '6859a000fe8b31cd7362e2ac', 'business_id': 'businessid_47', 'name': 'Breeze Blow Dry Bar', 'review_count': '81', 'is_open': '0', 'attributes': {'ByAppointmentOnly': 'False', 'BusinessAcceptsCreditCards': 'True', 'GoodForKids': 'True', 'RestaurantsPriceRange2': '2', 'BikeParking': 'False', 'BusinessParking': "{'garage': False, 'street': False, 'validated': False, 'lot': True, 'valet': False}"}, 'hours': {'Monday': '7:0-18:0', 'Tuesday': '7:0-18:0', 'Wednesday': '7:0-18:0', 'Thursday': '7:0-18:0', 'Friday': '7:0-19:0', 'Saturday': '8:0-19:0', 'Sunday': '10:0-17:0'}, 'description': 'Located at 9916 Clayton Rd in St. Louis, MO, this establishment offers a wide range of services, including Hair Salons, Beauty & Spas, Hair Stylists, Skin Care, Blow Dry/Out Services, and Makeup Artists.'}, {'_id': '6859a000fe8b31cd7362e2ad', 'business_id': 'businessid_88', 'name': 'Impact Guns', 'review_count': '39', 'is_open': '1', 'attributes': {'BusinessParking': "{'garage': False, 'street': False, 'validated': False, 'lot': False, 'valet': False}", 'GoodForKids': 'True', 'BusinessAcceptsCreditCards': 'True', 'ByAppointmentOnly': 'False', 'BikeParking': 'True'}, 'hours': {'Monday': '10:0-19:0', 'Tuesday': '10:0-19:0', 'Wednesday': '10:0-19:0', 'Thursday': '10:0-19:0', 'Friday': '10:0-19:0', 'Saturday': '10:0-19:0'}, 'description': 'Located at 11655 W Executive Dr in Boise, ID, this facility offers enthusiasts a premier destination for Gun/Rifle Ranges, Active Life.'}, {'_id': '6859a000fe8b31cd7362e2ae', 'business_id': 'businessid_41', 'name': 'Palms Primary Care', 'review_count': '5', 'is_open': '1', 'attributes': 'None', 'hours': {'Monday': '8:30-17:0', 'Tuesday': '8:30-17:0', 'Wednesday': '8:30-17:0', 'Thursday': '8:30-17:0', 'Friday': '8:30-17:0'}, 'description': 'Located at 1615 Pasadena Ave S, Ste 430 in Saint Petersburg, FL, this facility offers a range of services in Internal Medicine, Doctors, Health & Medical.'}, {'_id': '6859a000fe8b31cd7362e2af', 'business_id': 'businessid_33', 'name': 'J&Q Nails', 'review_count': '28', 'is_open': '1', 'attributes': {'BusinessParking': "{'garage': False, 'street': False, 'validated': False, 'lot': False, 'valet': False}", 'BusinessAcceptsCreditCards': 'True', 'AcceptsInsurance': 'False', 'ByAppointmentOnly': 'False', 'RestaurantsPriceRange2': '2', 'WheelchairAccessible': 'True', 'BikeParking': 'False'}, 'hours': {'Monday': '9:30-19:0', 'Tuesday': '9:30-19:0', 'Wednesday': '9:30-19:0', 'Thursday': '9:30-19:0', 'Friday': '9:30-19:0', 'Saturday': '9:30-17:30'}, 'description': 'Located at 9655 E US Hwy 36, Unit H in Avon, IN, this establishment offers a range of services including Nail Salons, Hair Removal, Beauty & Spas, and Waxing.'}], 'var_functions.query_db:5': [{'review_id': 'reviewid_135', 'user_id': 'userid_548', 'business_ref': 'businessref_34', 'rating': '2', 'useful': '0', 'funny': '0', 'cool': '0', 'text': "Sure, it's cheap, but there isn't much to see. I think you'd have to have a big interest in the topic to find it exciting, and kids would be bored. I think it only lasted maybe 10-15 minutes. Our tour person was somewhat knowledgeable and seemed into it, but he didn't give us much time to read the information on each level. I had to take photos of the plaques to read later, and half of them need replacing, as they are so sun-bleached they're virtually unreadable (tour guide said they're being replaced soon and that the other half were already replaced). I really thought it needed to be higher up to give a good view. The Lewis and Clark State Historic Site just down the road was more interesting and free. If you live around here like I do and have nothing better to do, you might want to give it a go if the topic interests you, but if you're a tourist, this is not something you should waste your time on.", 'date': 'August 01, 2016 at 03:44 AM'}, {'review_id': 'reviewid_1067', 'user_id': 'userid_213', 'business_ref': 'businessref_89', 'rating': '5', 'useful': '2', 'funny': '0', 'cool': '0', 'text': 'Very good service but a little pricey for the services your receive. Clean and sanitary too', 'date': 'June 14, 2021 at 11:39 AM'}, {'review_id': 'reviewid_871', 'user_id': 'userid_616', 'business_ref': 'businessref_82', 'rating': '4', 'useful': '0', 'funny': '0', 'cool': '0', 'text': 'My friend and I enjoyed a fantastic meal at Miles Table and I can\'t wait to return! Given that it was half-price-burger-day, I felt the need to give the falafel burger a shot. It was delicious! I\'m not always a falafel fan, but this "burger" was awesome. The brioche bun was the perfect consistency and the portion of fries was plentiful. My friend enjoyed the cobb salad (though she requested balsamic dressing instead of buttermilk and she received buttermilk). The restaurant is quaint and has ample seating. While you order at the counter, our "server" (I believe her name was Sarah) was fantastic and made sure we had everything we needed. Overall, this is a great spot and I will be back soon...I may have to make it a weekly lunch staple!', 'date': '29 May 2013, 23:01'}, {'review_id': 'reviewid_314', 'user_id': 'userid_1903', 'business_ref': 'businessref_66', 'rating': '2', 'useful': '1', 'funny': '2', 'cool': '1', 'text': "This location is not one of my favorites people here get pretty rude sometimes no one looks happy it's hit or miss with the food sometimes it's awesome other times terrible I always get honey walnut shrimp for an extra 1.25 which is retarded and Beijing beef I enjoy the rice n the noodles but idk do if u dare", 'date': '21 May 2016, 18:48'}, {'review_id': 'reviewid_487', 'user_id': 'None', 'business_ref': 'businessref_95', 'rating': '1', 'useful': '0', 'funny': '0', 'cool': '0', 'text': 'Terrible service. I was charged twice for online order and they refused to refund me. Numerous times this has happened', 'date': 'November 01, 2021 at 05:11 PM'}], 'var_functions.query_db:6': 'file_storage/functions.query_db:6.json', 'var_functions.execute_python:15': {'wifi_businesses_count': 0, 'state_counts': {}, 'top_state': None, 'top_state_count': 0, 'top_state_business_ids': []}}

exec(code, env_args)
