code = """import json
import pandas as pd
import re

# Load the business data from the file
business_file_path = locals()['var_functions.query_db:2']
with open(business_file_path, 'r') as f:
    businesses = json.load(f)

# Extract categories from business descriptions
def extract_categories(description):
    if not description:
        return ['Other']
    
    desc_lower = description.lower()
    categories = []
    
    if 'restaurant' in desc_lower or 'food' in desc_lower or 'cafe' in desc_lower:
        categories.append('Restaurants')
    if 'salon' in desc_lower or 'hair' in desc_lower or 'stylist' in desc_lower or 'beauty' in desc_lower:
        categories.append('Beauty & Spas')
    if 'nail' in desc_lower:
        categories.append('Nail Salons')
    if 'coffee' in desc_lower or 'tea' in desc_lower:
        categories.append('Coffee & Tea')
    if 'hotel' in desc_lower or 'travel' in desc_lower or 'taxi' in desc_lower or 'transportation' in desc_lower:
        categories.append('Hotels & Travel')
    if 'medical' in desc_lower or 'doctor' in desc_lower or 'health' in desc_lower or 'dentist' in desc_lower:
        categories.append('Health & Medical')
    if 'preschool' in desc_lower or 'school' in desc_lower or 'education' in desc_lower:
        categories.append('Education')
    if 'shopping' in desc_lower or 'store' in desc_lower or 'antique' in desc_lower:
        categories.append('Shopping')
    if 'gas' in desc_lower or 'station' in desc_lower:
        categories.append('Gas Stations')
    if 'gun' in desc_lower or 'range' in desc_lower or 'active life' in desc_lower:
        categories.append('Active Life')
    if 'flowers' in desc_lower or 'floral' in desc_lower:
        categories.append('Flowers & Gifts')
    if 'convenience' in desc_lower:
        categories.append('Convenience Stores')
    if 'child care' in desc_lower or 'day care' in desc_lower:
        categories.append('Child Care & Day Care')
    
    if not categories:
        categories.append('Other')
    
    return categories

# Create business dataframe with categories
business_data = []
for business in businesses:
    business_id = business['business_id']
    business_ref = business_id.replace('businessid_', 'businessref_')
    
    description = business.get('description', '')
    categories = extract_categories(description)
    
    for category in categories:
        business_data.append({
            'business_ref': business_ref,
            'business_id': business_id,
            'category': category,
            'name': business.get('name', '')
        })

business_df = pd.DataFrame(business_data)
business_df = business_df.drop_duplicates(subset=['business_ref', 'category'])

# Identify restaurants that accept credit cards
restaurant_businesses = business_df[business_df['category'] == 'Restaurants']
restaurant_business_refs = restaurant_businesses['business_ref'].tolist()

result = {
    'restaurant_count': len(restaurant_businesses),
    'restaurant_businesses': restaurant_business_refs[:5]
}

print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.query_db:0': [{'_id': '6859a000fe8b31cd7362e2ab', 'business_id': 'businessid_49', 'name': 'Steps to Learning Montessori Preschool', 'review_count': '8', 'is_open': '1', 'attributes': {'BusinessAcceptsCreditCards': 'True', 'WiFi': "u'no'", 'BusinessAcceptsBitcoin': 'False'}, 'hours': {'Monday': '0:0-0:0', 'Tuesday': '8:0-17:0', 'Wednesday': '8:0-17:0', 'Thursday': '8:0-17:0', 'Friday': '8:0-17:0'}, 'description': 'Located at 6901 Phelps Rd in Goleta, CA, this facility offers a nurturing environment for young learners, providing a range of services in Education, Elementary Schools, Child Care & Day Care, Local Services, Preschools, and Montessori Schools.'}, {'_id': '6859a000fe8b31cd7362e2ac', 'business_id': 'businessid_47', 'name': 'Breeze Blow Dry Bar', 'review_count': '81', 'is_open': '0', 'attributes': {'ByAppointmentOnly': 'False', 'BusinessAcceptsCreditCards': 'True', 'GoodForKids': 'True', 'RestaurantsPriceRange2': '2', 'BikeParking': 'False', 'BusinessParking': "{'garage': False, 'street': False, 'validated': False, 'lot': True, 'valet': False}"}, 'hours': {'Monday': '7:0-18:0', 'Tuesday': '7:0-18:0', 'Wednesday': '7:0-18:0', 'Thursday': '7:0-18:0', 'Friday': '7:0-19:0', 'Saturday': '8:0-19:0', 'Sunday': '10:0-17:0'}, 'description': 'Located at 9916 Clayton Rd in St. Louis, MO, this establishment offers a wide range of services, including Hair Salons, Beauty & Spas, Hair Stylists, Skin Care, Blow Dry/Out Services, and Makeup Artists.'}, {'_id': '6859a000fe8b31cd7362e2ad', 'business_id': 'businessid_88', 'name': 'Impact Guns', 'review_count': '39', 'is_open': '1', 'attributes': {'BusinessParking': "{'garage': False, 'street': False, 'validated': False, 'lot': False, 'valet': False}", 'GoodForKids': 'True', 'BusinessAcceptsCreditCards': 'True', 'ByAppointmentOnly': 'False', 'BikeParking': 'True'}, 'hours': {'Monday': '10:0-19:0', 'Tuesday': '10:0-19:0', 'Wednesday': '10:0-19:0', 'Thursday': '10:0-19:0', 'Friday': '10:0-19:0', 'Saturday': '10:0-19:0'}, 'description': 'Located at 11655 W Executive Dr in Boise, ID, this facility offers enthusiasts a premier destination for Gun/Rifle Ranges, Active Life.'}, {'_id': '6859a000fe8b31cd7362e2ae', 'business_id': 'businessid_41', 'name': 'Palms Primary Care', 'review_count': '5', 'is_open': '1', 'attributes': 'None', 'hours': {'Monday': '8:30-17:0', 'Tuesday': '8:30-17:0', 'Wednesday': '8:30-17:0', 'Thursday': '8:30-17:0', 'Friday': '8:30-17:0'}, 'description': 'Located at 1615 Pasadena Ave S, Ste 430 in Saint Petersburg, FL, this facility offers a range of services in Internal Medicine, Doctors, Health & Medical.'}, {'_id': '6859a000fe8b31cd7362e2af', 'business_id': 'businessid_33', 'name': 'J&Q Nails', 'review_count': '28', 'is_open': '1', 'attributes': {'BusinessParking': "{'garage': False, 'street': False, 'validated': False, 'lot': False, 'valet': False}", 'BusinessAcceptsCreditCards': 'True', 'AcceptsInsurance': 'False', 'ByAppointmentOnly': 'False', 'RestaurantsPriceRange2': '2', 'WheelchairAccessible': 'True', 'BikeParking': 'False'}, 'hours': {'Monday': '9:30-19:0', 'Tuesday': '9:30-19:0', 'Wednesday': '9:30-19:0', 'Thursday': '9:30-19:0', 'Friday': '9:30-19:0', 'Saturday': '9:30-17:30'}, 'description': 'Located at 9655 E US Hwy 36, Unit H in Avon, IN, this establishment offers a range of services including Nail Salons, Hair Removal, Beauty & Spas, and Waxing.'}], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:4': [{'review_id': 'reviewid_135', 'user_id': 'userid_548', 'business_ref': 'businessref_34', 'rating': '2', 'useful': '0', 'funny': '0', 'cool': '0', 'text': "Sure, it's cheap, but there isn't much to see. I think you'd have to have a big interest in the topic to find it exciting, and kids would be bored. I think it only lasted maybe 10-15 minutes. Our tour person was somewhat knowledgeable and seemed into it, but he didn't give us much time to read the information on each level. I had to take photos of the plaques to read later, and half of them need replacing, as they are so sun-bleached they're virtually unreadable (tour guide said they're being replaced soon and that the other half were already replaced). I really thought it needed to be higher up to give a good view. The Lewis and Clark State Historic Site just down the road was more interesting and free. If you live around here like I do and have nothing better to do, you might want to give it a go if the topic interests you, but if you're a tourist, this is not something you should waste your time on.", 'date': 'August 01, 2016 at 03:44 AM'}, {'review_id': 'reviewid_1067', 'user_id': 'userid_213', 'business_ref': 'businessref_89', 'rating': '5', 'useful': '2', 'funny': '0', 'cool': '0', 'text': 'Very good service but a little pricey for the services your receive. Clean and sanitary too', 'date': 'June 14, 2021 at 11:39 AM'}, {'review_id': 'reviewid_871', 'user_id': 'userid_616', 'business_ref': 'businessref_82', 'rating': '4', 'useful': '0', 'funny': '0', 'cool': '0', 'text': 'My friend and I enjoyed a fantastic meal at Miles Table and I can\'t wait to return! Given that it was half-price-burger-day, I felt the need to give the falafel burger a shot. It was delicious! I\'m not always a falafel fan, but this "burger" was awesome. The brioche bun was the perfect consistency and the portion of fries was plentiful. My friend enjoyed the cobb salad (though she requested balsamic dressing instead of buttermilk and she received buttermilk). The restaurant is quaint and has ample seating. While you order at the counter, our "server" (I believe her name was Sarah) was fantastic and made sure we had everything we needed. Overall, this is a great spot and I will be back soon...I may have to make it a weekly lunch staple!', 'date': '29 May 2013, 23:01'}, {'review_id': 'reviewid_314', 'user_id': 'userid_1903', 'business_ref': 'businessref_66', 'rating': '2', 'useful': '1', 'funny': '2', 'cool': '1', 'text': "This location is not one of my favorites people here get pretty rude sometimes no one looks happy it's hit or miss with the food sometimes it's awesome other times terrible I always get honey walnut shrimp for an extra 1.25 which is retarded and Beijing beef I enjoy the rice n the noodles but idk do if u dare", 'date': '21 May 2016, 18:48'}, {'review_id': 'reviewid_487', 'user_id': 'None', 'business_ref': 'businessref_95', 'rating': '1', 'useful': '0', 'funny': '0', 'cool': '0', 'text': 'Terrible service. I was charged twice for online order and they refused to refund me. Numerous times this has happened', 'date': 'November 01, 2021 at 05:11 PM'}], 'var_functions.execute_python:12': {'total_businesses': 75, 'sample': {'_id': '6859a000fe8b31cd7362e2ab', 'business_id': 'businessid_49', 'name': 'Steps to Learning Montessori Preschool', 'review_count': '8', 'is_open': '1', 'attributes': {'BusinessAcceptsCreditCards': 'True', 'WiFi': "u'no'", 'BusinessAcceptsBitcoin': 'False'}, 'hours': {'Monday': '0:0-0:0', 'Tuesday': '8:0-17:0', 'Wednesday': '8:0-17:0', 'Thursday': '8:0-17:0', 'Friday': '8:0-17:0'}, 'description': 'Located at 6901 Phelps Rd in Goleta, CA, this facility offers a nurturing environment for young learners, providing a range of services in Education, Elementary Schools, Child Care & Day Care, Local Services, Preschools, and Montessori Schools.'}}, 'var_functions.execute_python:16': {'total_businesses': 75, 'categories_found': 14, 'sample_categories': ['Education', 'Hair Salons', 'Other', 'Nail Salons', 'the categories of Medical Centers', 'the categories of Home & Garden', 'the categories of Food', 'the categories of Beauty & Spas', 'Cosmetic Dentists', 'Hotels & Travel'], 'business_rows': 75}, 'var_functions.execute_python:20': {'total_businesses': 75, 'category_counts': {'Restaurants': 35, 'Shopping': 12, 'Active Life': 7, 'Beauty & Spas': 7, 'Health & Medical': 5, 'Other': 5, 'Hotels & Travel': 2, 'Education': 1, 'Gas Stations': 1}, 'categories_found': 9, 'top_categories': {'Restaurants': 35, 'Shopping': 12, 'Active Life': 7, 'Beauty & Spas': 7, 'Health & Medical': 5, 'Other': 5, 'Hotels & Travel': 2, 'Education': 1, 'Gas Stations': 1}}, 'var_functions.query_db:22': 'file_storage/functions.query_db:22.json'}

exec(code, env_args)
