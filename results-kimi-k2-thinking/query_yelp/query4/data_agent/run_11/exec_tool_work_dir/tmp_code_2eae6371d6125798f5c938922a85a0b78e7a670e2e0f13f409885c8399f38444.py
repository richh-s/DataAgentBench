code = """import json

# Read the business data
file_path = locals()['var_functions.query_db:8']
with open(file_path, 'r') as f:
    businesses = json.load(f)

# Filter businesses that accept credit cards
credit_card_businesses = []
for business in businesses:
    if 'attributes' in business and business['attributes'] != 'None' and business['attributes'] is not None:
        attributes = business['attributes']
        if isinstance(attributes, dict) and 'BusinessAcceptsCreditCards' in attributes:
            if attributes['BusinessAcceptsCreditCards'] == 'True':
                credit_card_businesses.append(business)

print('Total credit card businesses:', len(credit_card_businesses))

# Let's examine the description field patterns more carefully
print('\nSample descriptions for analysis:')
for i, biz in enumerate(credit_card_businesses[:5]):
    print(f'{i+1}: {biz.get("description")}')
    print('---')

# Extract categories - look for the common pattern in Yelp descriptions
from collections import defaultdict
category_count = defaultdict(int)
business_to_categories = {}

import re

for business in credit_card_businesses:
    if 'description' in business and business['description']:
        desc = business['description']
        categories = []
        
        # Pattern 1: Look for common Yelp category patterns
        # Often ends with "in Category1, Category2, Category3" or "Category1, Category2, and Category3"
        
        # Try to extract from common patterns
        patterns = [
            r'(?:in|including|such as|and|for)\s+([A-Z][^\.\n,]+(?:,\s*[A-Z][^\.\n,]+)+)',  # Comma list after keywords
            r'([A-Z][a-z]+(?:,\s*[A-Z][a-z]+)+)\s*(?:\.|$)',  # Simple comma-separated caps
        ]
        
        for pattern in patterns:
            matches = re.findall(pattern, desc)
            for match in matches:
                # Split by comma and clean up
                items = re.split(r',|\s+and\s+|\s+&\s+', match)
                for item in items:
                    item = item.strip()
                    # Clean up
                    item = re.sub(r'^[\s\'"]+|[\s\'"]+$', '', item)
                    item = re.sub(r'[\.\,;]$', '', item)
                    if item and len(item) > 2 and not item.lower() in ['located', 'this']:
                        categories.append(item)
        
        # Pattern 2: Look for explicit category lists that might be in quotes or at the end
        # Check for "Category1, Category2" patterns where each word starts with capital letter
        all_capitals = re.findall(r'\b([A-Z][a-z]+(?:\s+[A-Z][a-z]+)*)\b', desc)
        
        # Look for sequences of these with commas between them
        for i, word in enumerate(all_capitals):
            # Check if this is part of a comma-separated list
            if i < len(all_capitals) - 1:
                # Look ahead to see if there are more cap words
                next_words = []
                for j in range(i+1, min(i+5, len(all_capitals))):
                    # Check if there's a comma between these in the original text
                    start_pos = desc.find(word) + len(word)
                    end_pos = desc.find(all_capitals[j])
                    between = desc[start_pos:end_pos]
                    
                    if ',' in between or 'and' in between.lower():
                        next_words.append(all_capitals[j])
                    else:
                        break
                
                if next_words:
                    # Found a potential list
                    current_list = [word] + next_words
                    for cat in current_list:
                        cat_clean = cat.strip()
                        if cat_clean and len(cat_clean) > 2:
                            categories.append(cat_clean)
        
        # Deduplicate within this business
        unique_categories = list(set(categories))
        business_to_categories[business['business_id']] = unique_categories
        
        # Count
        for cat in unique_categories:
            category_count[cat.lower()] += 1

print('\nCategory extraction results:')
print(f'Found {len(category_count)} unique categories')

# Sort categories by count
sorted_categories = sorted(category_count.items(), key=lambda x: x[1], reverse=True)
print('\nTop 10 categories:')
for cat, count in sorted_categories[:10]:
    print(f'  {cat}: {count}')

# Get the top category
if sorted_categories:
    top_category_name = sorted_categories[0][0]
    top_category_count = sorted_categories[0][1]
else:
    top_category_name = None
    top_category_count = 0

result = {
    'total_credit_card_businesses': len(credit_card_businesses),
    'top_category': top_category_name,
    'top_category_count': top_category_count,
    'all_categories': sorted_categories[:20]
}

print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.list_db:0': ['checkin', 'business'], 'var_functions.query_db:2': [{'_id': '6859a000fe8b31cd7362e2ab', 'business_id': 'businessid_49', 'name': 'Steps to Learning Montessori Preschool', 'review_count': '8', 'is_open': '1', 'attributes': {'BusinessAcceptsCreditCards': 'True', 'WiFi': "u'no'", 'BusinessAcceptsBitcoin': 'False'}, 'hours': {'Monday': '0:0-0:0', 'Tuesday': '8:0-17:0', 'Wednesday': '8:0-17:0', 'Thursday': '8:0-17:0', 'Friday': '8:0-17:0'}, 'description': 'Located at 6901 Phelps Rd in Goleta, CA, this facility offers a nurturing environment for young learners, providing a range of services in Education, Elementary Schools, Child Care & Day Care, Local Services, Preschools, and Montessori Schools.'}, {'_id': '6859a000fe8b31cd7362e2ac', 'business_id': 'businessid_47', 'name': 'Breeze Blow Dry Bar', 'review_count': '81', 'is_open': '0', 'attributes': {'ByAppointmentOnly': 'False', 'BusinessAcceptsCreditCards': 'True', 'GoodForKids': 'True', 'RestaurantsPriceRange2': '2', 'BikeParking': 'False', 'BusinessParking': "{'garage': False, 'street': False, 'validated': False, 'lot': True, 'valet': False}"}, 'hours': {'Monday': '7:0-18:0', 'Tuesday': '7:0-18:0', 'Wednesday': '7:0-18:0', 'Thursday': '7:0-18:0', 'Friday': '7:0-19:0', 'Saturday': '8:0-19:0', 'Sunday': '10:0-17:0'}, 'description': 'Located at 9916 Clayton Rd in St. Louis, MO, this establishment offers a wide range of services, including Hair Salons, Beauty & Spas, Hair Stylists, Skin Care, Blow Dry/Out Services, and Makeup Artists.'}, {'_id': '6859a000fe8b31cd7362e2ad', 'business_id': 'businessid_88', 'name': 'Impact Guns', 'review_count': '39', 'is_open': '1', 'attributes': {'BusinessParking': "{'garage': False, 'street': False, 'validated': False, 'lot': False, 'valet': False}", 'GoodForKids': 'True', 'BusinessAcceptsCreditCards': 'True', 'ByAppointmentOnly': 'False', 'BikeParking': 'True'}, 'hours': {'Monday': '10:0-19:0', 'Tuesday': '10:0-19:0', 'Wednesday': '10:0-19:0', 'Thursday': '10:0-19:0', 'Friday': '10:0-19:0', 'Saturday': '10:0-19:0'}, 'description': 'Located at 11655 W Executive Dr in Boise, ID, this facility offers enthusiasts a premier destination for Gun/Rifle Ranges, Active Life.'}, {'_id': '6859a000fe8b31cd7362e2ae', 'business_id': 'businessid_41', 'name': 'Palms Primary Care', 'review_count': '5', 'is_open': '1', 'attributes': 'None', 'hours': {'Monday': '8:30-17:0', 'Tuesday': '8:30-17:0', 'Wednesday': '8:30-17:0', 'Thursday': '8:30-17:0', 'Friday': '8:30-17:0'}, 'description': 'Located at 1615 Pasadena Ave S, Ste 430 in Saint Petersburg, FL, this facility offers a range of services in Internal Medicine, Doctors, Health & Medical.'}, {'_id': '6859a000fe8b31cd7362e2af', 'business_id': 'businessid_33', 'name': 'J&Q Nails', 'review_count': '28', 'is_open': '1', 'attributes': {'BusinessParking': "{'garage': False, 'street': False, 'validated': False, 'lot': False, 'valet': False}", 'BusinessAcceptsCreditCards': 'True', 'AcceptsInsurance': 'False', 'ByAppointmentOnly': 'False', 'RestaurantsPriceRange2': '2', 'WheelchairAccessible': 'True', 'BikeParking': 'False'}, 'hours': {'Monday': '9:30-19:0', 'Tuesday': '9:30-19:0', 'Wednesday': '9:30-19:0', 'Thursday': '9:30-19:0', 'Friday': '9:30-19:0', 'Saturday': '9:30-17:30'}, 'description': 'Located at 9655 E US Hwy 36, Unit H in Avon, IN, this establishment offers a range of services including Nail Salons, Hair Removal, Beauty & Spas, and Waxing.'}], 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json', 'var_functions.list_db:6': ['review', 'tip', 'user'], 'var_functions.query_db:8': 'file_storage/functions.query_db:8.json', 'var_functions.execute_python:40': {'total_credit_card_businesses': 75, 'top_category': 'restaurants', 'top_category_count': 2, 'top_category_business_ids': ['businessid_10', 'businessid_36']}, 'var_functions.query_db:52': [{'review_id': 'reviewid_135', 'user_id': 'userid_548', 'business_ref': 'businessref_34', 'rating': '2', 'useful': '0', 'funny': '0', 'cool': '0', 'text': "Sure, it's cheap, but there isn't much to see. I think you'd have to have a big interest in the topic to find it exciting, and kids would be bored. I think it only lasted maybe 10-15 minutes. Our tour person was somewhat knowledgeable and seemed into it, but he didn't give us much time to read the information on each level. I had to take photos of the plaques to read later, and half of them need replacing, as they are so sun-bleached they're virtually unreadable (tour guide said they're being replaced soon and that the other half were already replaced). I really thought it needed to be higher up to give a good view. The Lewis and Clark State Historic Site just down the road was more interesting and free. If you live around here like I do and have nothing better to do, you might want to give it a go if the topic interests you, but if you're a tourist, this is not something you should waste your time on.", 'date': 'August 01, 2016 at 03:44 AM'}, {'review_id': 'reviewid_1067', 'user_id': 'userid_213', 'business_ref': 'businessref_89', 'rating': '5', 'useful': '2', 'funny': '0', 'cool': '0', 'text': 'Very good service but a little pricey for the services your receive. Clean and sanitary too', 'date': 'June 14, 2021 at 11:39 AM'}, {'review_id': 'reviewid_871', 'user_id': 'userid_616', 'business_ref': 'businessref_82', 'rating': '4', 'useful': '0', 'funny': '0', 'cool': '0', 'text': 'My friend and I enjoyed a fantastic meal at Miles Table and I can\'t wait to return! Given that it was half-price-burger-day, I felt the need to give the falafel burger a shot. It was delicious! I\'m not always a falafel fan, but this "burger" was awesome. The brioche bun was the perfect consistency and the portion of fries was plentiful. My friend enjoyed the cobb salad (though she requested balsamic dressing instead of buttermilk and she received buttermilk). The restaurant is quaint and has ample seating. While you order at the counter, our "server" (I believe her name was Sarah) was fantastic and made sure we had everything we needed. Overall, this is a great spot and I will be back soon...I may have to make it a weekly lunch staple!', 'date': '29 May 2013, 23:01'}]}

exec(code, env_args)
