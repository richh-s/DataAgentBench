code = """import json
import re
import os
from datetime import datetime
import pandas as pd

# Load business mapping from previous step
business_mapping_key = 'var_functions.execute_python:30'
mapping_result = locals()[business_mapping_key]
print('Loaded business mapping result:', mapping_result)

# Recreate the business_ref_to_categories mapping
business_key = 'var_functions.query_db:24'
business_path = locals()[business_key]

with open(business_path, 'r') as f:
    business_data = json.load(f)

def extract_categories(description):
    if not description or not isinstance(description, str):
        return []
    
    patterns = [
        r'services in ([^.]+)',
        r'including ([^.]+)',
        r'offers?(?: a (?:wide )?range of)? services,? including ([^.]+)',
    ]
    
    for pattern in patterns:
        match = re.search(pattern, description, re.IGNORECASE)
        if match:
            text = match.group(1)
            text = re.sub(r'^a (?:wide )?range of ', '', text, flags=re.IGNORECASE)
            text = re.sub(r'^services in ', '', text, flags=re.IGNORECASE)
            parts = re.split(r',\s*and\s*|,\s*|\s+and\s+', text)
            
            cleaned = []
            for part in parts:
                part = part.strip()
                if part.endswith('.'):
                    part = part[:-1]
                if part and len(part) > 2 and part.lower() not in ['services', 'the', 'a', 'an']:
                    cleaned.append(part)
            return cleaned if cleaned else []
    
    return []

business_ref_to_categories = {}
for business in business_data:
    business_id = business['business_id']
    business_ref = business_id.replace('businessid_', 'businessref_')
    categories = extract_categories(business.get('description', ''))
    if categories:  # Only add if we found categories
        business_ref_to_categories[business_ref] = categories

print('Final mapping has', len(business_ref_to_categories), 'businesses with categories')

# Load users registered in 2016
users_key = 'var_functions.query_db:18'
users_path = locals()[users_key]

with open(users_path, 'r') as f:
    users_data = json.load(f)

users_2016_df = pd.DataFrame(users_data)
user_ids_2016 = set(users_2016_df['user_id'].tolist())
print('Loaded', len(user_ids_2016), 'users registered in 2016')

# Load all reviews
reviews_key = 'var_functions.query_db:16'
reviews_path = locals()[reviews_key]

with open(reviews_path, 'r') as f:
    reviews_data = json.load(f)

reviews_df = pd.DataFrame(reviews_data)
print('Loaded', len(reviews_df), 'total reviews')

# Parse review dates
def parse_date(date_str):
    if pd.isna(date_str) or not date_str:
        return None
    
    date_str = str(date_str).strip()
    formats = [
        '%B %d, %Y at %I:%M %p',
        '%d %B %Y, %H:%M',
        '%Y-%m-%d %H:%M:%S',
        '%B %d, %Y at %H:%M %p',
        '%Y-%m-%d %H:%M',
        '%B %d, %Y',
        '%Y-%m-%d'
    ]
    
    for fmt in formats:
        try:
            return datetime.strptime(date_str, fmt)
        except:
            continue
    
    return None

reviews_df['parsed_date'] = reviews_df['date'].apply(parse_date)
reviews_2016_plus = reviews_df[reviews_df['parsed_date'] >= datetime(2016, 1, 1)]
print('Reviews from 2016 onwards:', len(reviews_2016_plus))

# Filter by users registered in 2016
reviews_by_2016_users = reviews_2016_plus[
    reviews_2016_plus['user_id'].isin(user_ids_2016) & 
    reviews_2016_plus['business_ref'].notna()
]
print('Reviews by 2016 users since 2016:', len(reviews_by_2016_users))

# Count reviews by category
category_review_counts = {}
reviews_mapped = 0

for _, review in reviews_by_2016_users.iterrows():
    business_ref = review['business_ref']
    if business_ref in business_ref_to_categories:
        categories = business_ref_to_categories[business_ref]
        reviews_mapped += 1
        for category in categories:
            category_review_counts[category] = category_review_counts.get(category, 0) + 1

print('Reviews successfully mapped to categories:', reviews_mapped)
print('Unique categories found:', len(category_review_counts))

# Get top 5 categories
sorted_categories = sorted(category_review_counts.items(), key=lambda x: x[1], reverse=True)
top_5 = sorted_categories[:5]

print('Top 5 categories:')
for i, (cat, count) in enumerate(top_5, 1):
    print(f"  {i}. {cat}: {count} reviews")

result_dict = {
    'top_5_categories': top_5,
    'total_categories': len(category_review_counts),
    'reviews_mapped': reviews_mapped,
    'total_reviews_by_2016_users': len(reviews_by_2016_users)
}

print('__RESULT__:')
print(json.dumps(result_dict, default=str))"""

env_args = {'var_functions.list_db:0': ['checkin', 'business'], 'var_functions.query_db:2': [{'user_id': 'userid_286', 'name': 'Todd', 'review_count': '376', 'yelping_since': '15 Jan 2009, 16:40', 'useful': '1373', 'funny': '723', 'cool': '639', 'elite': '2010,2011,2012,2013,2014'}, {'user_id': 'userid_1331', 'name': 'Patt', 'review_count': '1028', 'yelping_since': '13 Jul 2010, 15:42', 'useful': '9050', 'funny': '3249', 'cool': '5929', 'elite': '2011,2012,2013,2014,2015,2016,2017,2018,2019,20,20,2021'}, {'user_id': 'userid_1880', 'name': 'Norma', 'review_count': '57', 'yelping_since': '2010-09-07 23:24:36', 'useful': '217', 'funny': '57', 'cool': '115', 'elite': '2012,2013'}, {'user_id': 'userid_271', 'name': 'Antony', 'review_count': '49', 'yelping_since': 'October 23, 2011 at 07:47 PM', 'useful': '116', 'funny': '159', 'cool': '34', 'elite': ''}, {'user_id': 'userid_534', 'name': 'Mandy', 'review_count': '754', 'yelping_since': '2011-08-30 13:46:26', 'useful': '2925', 'funny': '775', 'cool': '988', 'elite': '2011,2012,2013,2014,2015,2016,2017,2018,2019,20,20,2021'}], 'var_functions.query_db:5': [{'review_id': 'reviewid_135', 'user_id': 'userid_548', 'business_ref': 'businessref_34', 'rating': '2', 'useful': '0', 'funny': '0', 'cool': '0', 'text': "Sure, it's cheap, but there isn't much to see. I think you'd have to have a big interest in the topic to find it exciting, and kids would be bored. I think it only lasted maybe 10-15 minutes. Our tour person was somewhat knowledgeable and seemed into it, but he didn't give us much time to read the information on each level. I had to take photos of the plaques to read later, and half of them need replacing, as they are so sun-bleached they're virtually unreadable (tour guide said they're being replaced soon and that the other half were already replaced). I really thought it needed to be higher up to give a good view. The Lewis and Clark State Historic Site just down the road was more interesting and free. If you live around here like I do and have nothing better to do, you might want to give it a go if the topic interests you, but if you're a tourist, this is not something you should waste your time on.", 'date': 'August 01, 2016 at 03:44 AM'}, {'review_id': 'reviewid_1067', 'user_id': 'userid_213', 'business_ref': 'businessref_89', 'rating': '5', 'useful': '2', 'funny': '0', 'cool': '0', 'text': 'Very good service but a little pricey for the services your receive. Clean and sanitary too', 'date': 'June 14, 2021 at 11:39 AM'}, {'review_id': 'reviewid_871', 'user_id': 'userid_616', 'business_ref': 'businessref_82', 'rating': '4', 'useful': '0', 'funny': '0', 'cool': '0', 'text': 'My friend and I enjoyed a fantastic meal at Miles Table and I can\'t wait to return! Given that it was half-price-burger-day, I felt the need to give the falafel burger a shot. It was delicious! I\'m not always a falafel fan, but this "burger" was awesome. The brioche bun was the perfect consistency and the portion of fries was plentiful. My friend enjoyed the cobb salad (though she requested balsamic dressing instead of buttermilk and she received buttermilk). The restaurant is quaint and has ample seating. While you order at the counter, our "server" (I believe her name was Sarah) was fantastic and made sure we had everything we needed. Overall, this is a great spot and I will be back soon...I may have to make it a weekly lunch staple!', 'date': '29 May 2013, 23:01'}, {'review_id': 'reviewid_314', 'user_id': 'userid_1903', 'business_ref': 'businessref_66', 'rating': '2', 'useful': '1', 'funny': '2', 'cool': '1', 'text': "This location is not one of my favorites people here get pretty rude sometimes no one looks happy it's hit or miss with the food sometimes it's awesome other times terrible I always get honey walnut shrimp for an extra 1.25 which is retarded and Beijing beef I enjoy the rice n the noodles but idk do if u dare", 'date': '21 May 2016, 18:48'}, {'review_id': 'reviewid_487', 'user_id': 'None', 'business_ref': 'businessref_95', 'rating': '1', 'useful': '0', 'funny': '0', 'cool': '0', 'text': 'Terrible service. I was charged twice for online order and they refused to refund me. Numerous times this has happened', 'date': 'November 01, 2021 at 05:11 PM'}], 'var_functions.query_db:6': [{'_id': '6859a000fe8b31cd7362e2ab', 'business_id': 'businessid_49', 'name': 'Steps to Learning Montessori Preschool', 'review_count': '8', 'is_open': '1', 'attributes': {'BusinessAcceptsCreditCards': 'True', 'WiFi': "u'no'", 'BusinessAcceptsBitcoin': 'False'}, 'hours': {'Monday': '0:0-0:0', 'Tuesday': '8:0-17:0', 'Wednesday': '8:0-17:0', 'Thursday': '8:0-17:0', 'Friday': '8:0-17:0'}, 'description': 'Located at 6901 Phelps Rd in Goleta, CA, this facility offers a nurturing environment for young learners, providing a range of services in Education, Elementary Schools, Child Care & Day Care, Local Services, Preschools, and Montessori Schools.'}, {'_id': '6859a000fe8b31cd7362e2ac', 'business_id': 'businessid_47', 'name': 'Breeze Blow Dry Bar', 'review_count': '81', 'is_open': '0', 'attributes': {'ByAppointmentOnly': 'False', 'BusinessAcceptsCreditCards': 'True', 'GoodForKids': 'True', 'RestaurantsPriceRange2': '2', 'BikeParking': 'False', 'BusinessParking': "{'garage': False, 'street': False, 'validated': False, 'lot': True, 'valet': False}"}, 'hours': {'Monday': '7:0-18:0', 'Tuesday': '7:0-18:0', 'Wednesday': '7:0-18:0', 'Thursday': '7:0-18:0', 'Friday': '7:0-19:0', 'Saturday': '8:0-19:0', 'Sunday': '10:0-17:0'}, 'description': 'Located at 9916 Clayton Rd in St. Louis, MO, this establishment offers a wide range of services, including Hair Salons, Beauty & Spas, Hair Stylists, Skin Care, Blow Dry/Out Services, and Makeup Artists.'}, {'_id': '6859a000fe8b31cd7362e2ad', 'business_id': 'businessid_88', 'name': 'Impact Guns', 'review_count': '39', 'is_open': '1', 'attributes': {'BusinessParking': "{'garage': False, 'street': False, 'validated': False, 'lot': False, 'valet': False}", 'GoodForKids': 'True', 'BusinessAcceptsCreditCards': 'True', 'ByAppointmentOnly': 'False', 'BikeParking': 'True'}, 'hours': {'Monday': '10:0-19:0', 'Tuesday': '10:0-19:0', 'Wednesday': '10:0-19:0', 'Thursday': '10:0-19:0', 'Friday': '10:0-19:0', 'Saturday': '10:0-19:0'}, 'description': 'Located at 11655 W Executive Dr in Boise, ID, this facility offers enthusiasts a premier destination for Gun/Rifle Ranges, Active Life.'}, {'_id': '6859a000fe8b31cd7362e2ae', 'business_id': 'businessid_41', 'name': 'Palms Primary Care', 'review_count': '5', 'is_open': '1', 'attributes': 'None', 'hours': {'Monday': '8:30-17:0', 'Tuesday': '8:30-17:0', 'Wednesday': '8:30-17:0', 'Thursday': '8:30-17:0', 'Friday': '8:30-17:0'}, 'description': 'Located at 1615 Pasadena Ave S, Ste 430 in Saint Petersburg, FL, this facility offers a range of services in Internal Medicine, Doctors, Health & Medical.'}, {'_id': '6859a000fe8b31cd7362e2af', 'business_id': 'businessid_33', 'name': 'J&Q Nails', 'review_count': '28', 'is_open': '1', 'attributes': {'BusinessParking': "{'garage': False, 'street': False, 'validated': False, 'lot': False, 'valet': False}", 'BusinessAcceptsCreditCards': 'True', 'AcceptsInsurance': 'False', 'ByAppointmentOnly': 'False', 'RestaurantsPriceRange2': '2', 'WheelchairAccessible': 'True', 'BikeParking': 'False'}, 'hours': {'Monday': '9:30-19:0', 'Tuesday': '9:30-19:0', 'Wednesday': '9:30-19:0', 'Thursday': '9:30-19:0', 'Friday': '9:30-19:0', 'Saturday': '9:30-17:30'}, 'description': 'Located at 9655 E US Hwy 36, Unit H in Avon, IN, this establishment offers a range of services including Nail Salons, Hair Removal, Beauty & Spas, and Waxing.'}], 'var_functions.execute_python:14': {'mapping_created': 5}, 'var_functions.query_db:16': 'file_storage/functions.query_db:16.json', 'var_functions.query_db:18': 'file_storage/functions.query_db:18.json', 'var_functions.execute_python:20': {'businesses_mapped': 5, 'users_2016_count': 168}, 'var_functions.execute_python:22': {'top_5_categories': [['Nail Salons', 3], ['Hair Removal', 3], ['Beauty & Spas', 3], ['Waxing', 3], ['enthusiasts a premier destination for Gun/Rifle Ranges', 3]], 'total_categories': 9, 'total_reviews_mapped': 7}, 'var_functions.query_db:24': 'file_storage/functions.query_db:24.json', 'var_functions.execute_python:30': {'businesses_total': 100, 'businesses_with_categories': 44, 'sample_mapping': {'businessref_49': ['Education', 'Elementary Schools', 'Child Care & Day Care', 'Local Services', 'Preschools', 'Montessori Schools'], 'businessref_47': ['Hair Salons', 'Beauty & Spas', 'Hair Stylists', 'Skin Care', 'Blow Dry/Out Services', 'Makeup Artists'], 'businessref_88': [], 'businessref_41': ['Internal Medicine', 'Doctors', 'Health & Medical'], 'businessref_33': ['Nail Salons', 'Hair Removal', 'Beauty & Spas', 'Waxing']}}}

exec(code, env_args)
