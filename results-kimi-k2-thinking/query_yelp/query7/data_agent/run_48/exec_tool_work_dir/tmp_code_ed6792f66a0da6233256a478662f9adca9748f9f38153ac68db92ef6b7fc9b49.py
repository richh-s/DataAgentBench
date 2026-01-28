code = """import json
import re

# Read the data from storage files
with open('/home/user/.tmp/rl6.json', 'r') as f:
    users_2016 = json.load(f)

with open('/home/user/.tmp/rl8.json', 'r') as f:
    reviews_2016_users = json.load(f)

with open('/home/user/.tmp/rl10.json', 'r') as f:
    businesses_data = json.load(f)

user_ids_2016 = {user['user_id'] for user in users_2016}
print(f"Total users who registered in 2016: {len(user_ids_2016)}")
print(f"Total reviews from these users: {len(reviews_2016_users)}")

# Count reviews per business_ref
business_ref_counts = {}
for review in reviews_2016_users:
    business_ref = review['business_ref']
    business_ref_counts[business_ref] = business_ref_counts.get(business_ref, 0) + 1

# Get unique business_refs that need category information
unique_business_refs = set(business_ref_counts.keys())
print(f"Unique businesses reviewed: {len(unique_business_refs)}")

# Create a mapping from business_ref to business_id
business_ref_to_id = {}
for business_ref in unique_business_refs:
    if business_ref.startswith('businessref_'):
        num = business_ref.split('_')[1]
        business_id = f'businessid_{num}'
        business_ref_to_id[business_ref] = business_id

# Create mapping from business_id to categories
business_id_to_categories = {}
for business in businesses_data:
    business_id = business['business_id']
    description = business.get('description', '')
    
    categories = []
    if description:
        desc_lower = description.lower()
        
        # Try to extract category list from description using patterns
        patterns = [
            r'services in ([^.]+)',
            r'including ([^.]+)',
            r'offers? ([^.]+)',
            r'range of services including ([^.]+)',
            r'services, including ([^.]+)'
        ]
        
        categories_found = []
        for pattern in patterns:
            match = re.search(pattern, desc_lower)
            if match:
                category_text = match.group(1)
                # Split by comma if multiple categories
                if ',' in category_text:
                    cats = [cat.strip() for cat in category_text.split(',')]
                    categories_found.extend(cats)
                else:
                    categories_found.append(category_text.strip())
        
        # If no pattern matched, try a simpler approach
        if not categories_found:
            # Extract capitalized phrases
            words = description.split()
            potential_categories = []
            current_cat = []
            
            for word in words:
                if word and word[0].isupper():
                    current_cat.append(word)
                elif current_cat:
                    if len(current_cat) >= 2:
                        cat = ' '.join(current_cat).strip('.,')
                        if cat and not any(loc in cat.lower() for loc in ['located', 'this', 'that', 'and', 'the', 'for']):
                            potential_categories.append(cat)
                    current_cat = []
            
            if current_cat and len(current_cat) >= 2:
                cat = ' '.join(current_cat).strip('.,')
                if cat and not any(loc in cat.lower() for loc in ['located', 'this', 'that', 'and', 'the', 'for']):
                    potential_categories.append(cat)
            
            categories_found = potential_categories
        
        business_id_to_categories[business_id] = categories_found if categories_found else ['Miscellaneous']

print(f"Businesses with category info: {len(business_id_to_categories)}")
print("First 5 businesses with categories:")
for i, (bid, cats) in enumerate(list(business_id_to_categories.items())[:5]):
    print(f"  {bid}: {cats}")

# Now count reviews per category
category_counts = {}
for business_ref, review_count in business_ref_counts.items():
    business_id = business_ref_to_id.get(business_ref)
    if business_id and business_id in business_id_to_categories:
        categories = business_id_to_categories[business_id]
        for category in categories:
            category_counts[category] = category_counts.get(category, 0) + review_count

# Sort categories by review count
top_categories = sorted(category_counts.items(), key=lambda x: x[1], reverse=True)

print(f"\nTotal unique categories found: {len(category_counts)}")
print("\nTop 10 categories:")
for i, (category, count) in enumerate(top_categories[:10]):
    print(f"{i+1}. {category}: {count} reviews")

# Get top 5
top_5 = top_categories[:5]
result = json.dumps([{"category": cat, "review_count": count} for cat, count in top_5])

print('__RESULT__:')
print(result)"""

env_args = {'var_functions.query_db:0': [{'user_id': 'userid_286', 'name': 'Todd', 'review_count': '376', 'yelping_since': '15 Jan 2009, 16:40', 'useful': '1373', 'funny': '723', 'cool': '639', 'elite': '2010,2011,2012,2013,2014'}, {'user_id': 'userid_1331', 'name': 'Patt', 'review_count': '1028', 'yelping_since': '13 Jul 2010, 15:42', 'useful': '9050', 'funny': '3249', 'cool': '5929', 'elite': '2011,2012,2013,2014,2015,2016,2017,2018,2019,20,20,2021'}, {'user_id': 'userid_1880', 'name': 'Norma', 'review_count': '57', 'yelping_since': '2010-09-07 23:24:36', 'useful': '217', 'funny': '57', 'cool': '115', 'elite': '2012,2013'}, {'user_id': 'userid_271', 'name': 'Antony', 'review_count': '49', 'yelping_since': 'October 23, 2011 at 07:47 PM', 'useful': '116', 'funny': '159', 'cool': '34', 'elite': ''}, {'user_id': 'userid_534', 'name': 'Mandy', 'review_count': '754', 'yelping_since': '2011-08-30 13:46:26', 'useful': '2925', 'funny': '775', 'cool': '988', 'elite': '2011,2012,2013,2014,2015,2016,2017,2018,2019,20,20,2021'}], 'var_functions.query_db:2': [{'review_id': 'reviewid_135', 'user_id': 'userid_548', 'business_ref': 'businessref_34', 'rating': '2', 'useful': '0', 'funny': '0', 'cool': '0', 'text': "Sure, it's cheap, but there isn't much to see. I think you'd have to have a big interest in the topic to find it exciting, and kids would be bored. I think it only lasted maybe 10-15 minutes. Our tour person was somewhat knowledgeable and seemed into it, but he didn't give us much time to read the information on each level. I had to take photos of the plaques to read later, and half of them need replacing, as they are so sun-bleached they're virtually unreadable (tour guide said they're being replaced soon and that the other half were already replaced). I really thought it needed to be higher up to give a good view. The Lewis and Clark State Historic Site just down the road was more interesting and free. If you live around here like I do and have nothing better to do, you might want to give it a go if the topic interests you, but if you're a tourist, this is not something you should waste your time on.", 'date': 'August 01, 2016 at 03:44 AM'}, {'review_id': 'reviewid_1067', 'user_id': 'userid_213', 'business_ref': 'businessref_89', 'rating': '5', 'useful': '2', 'funny': '0', 'cool': '0', 'text': 'Very good service but a little pricey for the services your receive. Clean and sanitary too', 'date': 'June 14, 2021 at 11:39 AM'}, {'review_id': 'reviewid_871', 'user_id': 'userid_616', 'business_ref': 'businessref_82', 'rating': '4', 'useful': '0', 'funny': '0', 'cool': '0', 'text': 'My friend and I enjoyed a fantastic meal at Miles Table and I can\'t wait to return! Given that it was half-price-burger-day, I felt the need to give the falafel burger a shot. It was delicious! I\'m not always a falafel fan, but this "burger" was awesome. The brioche bun was the perfect consistency and the portion of fries was plentiful. My friend enjoyed the cobb salad (though she requested balsamic dressing instead of buttermilk and she received buttermilk). The restaurant is quaint and has ample seating. While you order at the counter, our "server" (I believe her name was Sarah) was fantastic and made sure we had everything we needed. Overall, this is a great spot and I will be back soon...I may have to make it a weekly lunch staple!', 'date': '29 May 2013, 23:01'}, {'review_id': 'reviewid_314', 'user_id': 'userid_1903', 'business_ref': 'businessref_66', 'rating': '2', 'useful': '1', 'funny': '2', 'cool': '1', 'text': "This location is not one of my favorites people here get pretty rude sometimes no one looks happy it's hit or miss with the food sometimes it's awesome other times terrible I always get honey walnut shrimp for an extra 1.25 which is retarded and Beijing beef I enjoy the rice n the noodles but idk do if u dare", 'date': '21 May 2016, 18:48'}, {'review_id': 'reviewid_487', 'user_id': 'None', 'business_ref': 'businessref_95', 'rating': '1', 'useful': '0', 'funny': '0', 'cool': '0', 'text': 'Terrible service. I was charged twice for online order and they refused to refund me. Numerous times this has happened', 'date': 'November 01, 2021 at 05:11 PM'}], 'var_functions.query_db:4': [{'_id': '6859a000fe8b31cd7362e2ab', 'business_id': 'businessid_49', 'name': 'Steps to Learning Montessori Preschool', 'review_count': '8', 'is_open': '1', 'attributes': {'BusinessAcceptsCreditCards': 'True', 'WiFi': "u'no'", 'BusinessAcceptsBitcoin': 'False'}, 'hours': {'Monday': '0:0-0:0', 'Tuesday': '8:0-17:0', 'Wednesday': '8:0-17:0', 'Thursday': '8:0-17:0', 'Friday': '8:0-17:0'}, 'description': 'Located at 6901 Phelps Rd in Goleta, CA, this facility offers a nurturing environment for young learners, providing a range of services in Education, Elementary Schools, Child Care & Day Care, Local Services, Preschools, and Montessori Schools.'}, {'_id': '6859a000fe8b31cd7362e2ac', 'business_id': 'businessid_47', 'name': 'Breeze Blow Dry Bar', 'review_count': '81', 'is_open': '0', 'attributes': {'ByAppointmentOnly': 'False', 'BusinessAcceptsCreditCards': 'True', 'GoodForKids': 'True', 'RestaurantsPriceRange2': '2', 'BikeParking': 'False', 'BusinessParking': "{'garage': False, 'street': False, 'validated': False, 'lot': True, 'valet': False}"}, 'hours': {'Monday': '7:0-18:0', 'Tuesday': '7:0-18:0', 'Wednesday': '7:0-18:0', 'Thursday': '7:0-18:0', 'Friday': '7:0-19:0', 'Saturday': '8:0-19:0', 'Sunday': '10:0-17:0'}, 'description': 'Located at 9916 Clayton Rd in St. Louis, MO, this establishment offers a wide range of services, including Hair Salons, Beauty & Spas, Hair Stylists, Skin Care, Blow Dry/Out Services, and Makeup Artists.'}, {'_id': '6859a000fe8b31cd7362e2ad', 'business_id': 'businessid_88', 'name': 'Impact Guns', 'review_count': '39', 'is_open': '1', 'attributes': {'BusinessParking': "{'garage': False, 'street': False, 'validated': False, 'lot': False, 'valet': False}", 'GoodForKids': 'True', 'BusinessAcceptsCreditCards': 'True', 'ByAppointmentOnly': 'False', 'BikeParking': 'True'}, 'hours': {'Monday': '10:0-19:0', 'Tuesday': '10:0-19:0', 'Wednesday': '10:0-19:0', 'Thursday': '10:0-19:0', 'Friday': '10:0-19:0', 'Saturday': '10:0-19:0'}, 'description': 'Located at 11655 W Executive Dr in Boise, ID, this facility offers enthusiasts a premier destination for Gun/Rifle Ranges, Active Life.'}, {'_id': '6859a000fe8b31cd7362e2ae', 'business_id': 'businessid_41', 'name': 'Palms Primary Care', 'review_count': '5', 'is_open': '1', 'attributes': 'None', 'hours': {'Monday': '8:30-17:0', 'Tuesday': '8:30-17:0', 'Wednesday': '8:30-17:0', 'Thursday': '8:30-17:0', 'Friday': '8:30-17:0'}, 'description': 'Located at 1615 Pasadena Ave S, Ste 430 in Saint Petersburg, FL, this facility offers a range of services in Internal Medicine, Doctors, Health & Medical.'}, {'_id': '6859a000fe8b31cd7362e2af', 'business_id': 'businessid_33', 'name': 'J&Q Nails', 'review_count': '28', 'is_open': '1', 'attributes': {'BusinessParking': "{'garage': False, 'street': False, 'validated': False, 'lot': False, 'valet': False}", 'BusinessAcceptsCreditCards': 'True', 'AcceptsInsurance': 'False', 'ByAppointmentOnly': 'False', 'RestaurantsPriceRange2': '2', 'WheelchairAccessible': 'True', 'BikeParking': 'False'}, 'hours': {'Monday': '9:30-19:0', 'Tuesday': '9:30-19:0', 'Wednesday': '9:30-19:0', 'Thursday': '9:30-19:0', 'Friday': '9:30-19:0', 'Saturday': '9:30-17:30'}, 'description': 'Located at 9655 E US Hwy 36, Unit H in Avon, IN, this establishment offers a range of services including Nail Salons, Hair Removal, Beauty & Spas, and Waxing.'}], 'var_functions.query_db:6': 'file_storage/functions.query_db:6.json', 'var_functions.query_db:8': 'file_storage/functions.query_db:8.json', 'var_functions.query_db:10': [{'business_id': 'businessid_49', 'description': 'Located at 6901 Phelps Rd in Goleta, CA, this facility offers a nurturing environment for young learners, providing a range of services in Education, Elementary Schools, Child Care & Day Care, Local Services, Preschools, and Montessori Schools.'}, {'business_id': 'businessid_47', 'description': 'Located at 9916 Clayton Rd in St. Louis, MO, this establishment offers a wide range of services, including Hair Salons, Beauty & Spas, Hair Stylists, Skin Care, Blow Dry/Out Services, and Makeup Artists.'}, {'business_id': 'businessid_88', 'description': 'Located at 11655 W Executive Dr in Boise, ID, this facility offers enthusiasts a premier destination for Gun/Rifle Ranges, Active Life.'}, {'business_id': 'businessid_41', 'description': 'Located at 1615 Pasadena Ave S, Ste 430 in Saint Petersburg, FL, this facility offers a range of services in Internal Medicine, Doctors, Health & Medical.'}, {'business_id': 'businessid_33', 'description': 'Located at 9655 E US Hwy 36, Unit H in Avon, IN, this establishment offers a range of services including Nail Salons, Hair Removal, Beauty & Spas, and Waxing.'}], 'var_functions.query_db:12': [{'business_ref': 'businessref_79'}, {'business_ref': 'businessref_44'}, {'business_ref': 'businessref_13'}, {'business_ref': 'businessref_6'}, {'business_ref': 'businessref_71'}, {'business_ref': 'businessref_91'}, {'business_ref': 'businessref_46'}, {'business_ref': 'businessref_1'}, {'business_ref': 'businessref_47'}, {'business_ref': 'businessref_16'}, {'business_ref': 'businessref_55'}, {'business_ref': 'businessref_29'}, {'business_ref': 'businessref_39'}, {'business_ref': 'businessref_67'}, {'business_ref': 'businessref_15'}, {'business_ref': 'businessref_33'}, {'business_ref': 'businessref_81'}, {'business_ref': 'businessref_17'}, {'business_ref': 'businessref_43'}, {'business_ref': 'businessref_53'}, {'business_ref': 'businessref_51'}, {'business_ref': 'businessref_37'}, {'business_ref': 'businessref_57'}, {'business_ref': 'businessref_8'}, {'business_ref': 'businessref_56'}, {'business_ref': 'businessref_62'}, {'business_ref': 'businessref_86'}, {'business_ref': 'businessref_97'}, {'business_ref': 'businessref_72'}, {'business_ref': 'businessref_85'}, {'business_ref': 'businessref_42'}, {'business_ref': 'businessref_9'}, {'business_ref': 'businessref_74'}, {'business_ref': 'businessref_25'}, {'business_ref': 'businessref_66'}, {'business_ref': 'businessref_31'}, {'business_ref': 'businessref_99'}, {'business_ref': 'businessref_88'}, {'business_ref': 'businessref_21'}, {'business_ref': 'businessref_26'}, {'business_ref': 'businessref_68'}, {'business_ref': 'businessref_4'}, {'business_ref': 'businessref_36'}, {'business_ref': 'businessref_12'}, {'business_ref': 'businessref_60'}, {'business_ref': 'businessref_89'}, {'business_ref': 'businessref_45'}, {'business_ref': 'businessref_82'}, {'business_ref': 'businessref_23'}, {'business_ref': 'businessref_41'}, {'business_ref': 'businessref_10'}, {'business_ref': 'businessref_14'}, {'business_ref': 'businessref_3'}, {'business_ref': 'businessref_96'}, {'business_ref': 'businessref_98'}, {'business_ref': 'businessref_22'}, {'business_ref': 'businessref_20'}, {'business_ref': 'businessref_40'}, {'business_ref': 'businessref_7'}, {'business_ref': 'businessref_92'}, {'business_ref': 'businessref_61'}, {'business_ref': 'businessref_76'}]}

exec(code, env_args)
