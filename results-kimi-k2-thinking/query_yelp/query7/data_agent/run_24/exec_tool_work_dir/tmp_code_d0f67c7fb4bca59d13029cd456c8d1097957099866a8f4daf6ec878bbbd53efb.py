code = """import json
import re
from collections import defaultdict

# Load reviews by 2016 users
reviews_file = locals()['var_functions.query_db:24']
with open(reviews_file) as f:
    reviews = json.load(f)

# Load all businesses
business_file = locals()['var_functions.query_db:30']
with open(business_file) as f:
    businesses = json.load(f)

# Create mapping from business_ref to business_id
business_ref_to_id = {}
for business in businesses:
    business_id = business['business_id']
    business_ref = business_id.replace('businessid_', 'businessref_')
    business_ref_to_id[business_ref] = business_id

# Create business_id to categories mapping
business_id_to_categories = {}
for business in businesses:
    business_id = business['business_id']
    description = business.get('description', '')
    
    categories = []
    
    # Pattern 1: "providing a range of services in A, B, and C."
    match1 = re.search(r'providing a range of services in ([^.]+?)\.', description, re.IGNORECASE)
    if match1:
        cat_text = match1.group(1)
        cat_text = re.sub(r'\s+and\s+', ', ', cat_text)
        cats = [c.strip() for c in cat_text.split(',') if c.strip()]
        categories.extend(cats)
    
    # Pattern 2: "offers a wide range of services, including A, B, and C."
    match2 = re.search(r'offers a wide range of services, including ([^.]+?)\.', description, re.IGNORECASE)
    if match2:
        cat_text = match2.group(1)
        cat_text = re.sub(r'\s+and\s+', ', ', cat_text)
        cats = [c.strip() for c in cat_text.split(',') if c.strip()]
        categories.extend(cats)
    
    # Pattern 3: "offers a range of services including A, B, and C."
    match3 = re.search(r'offers a range of services including ([^.]+?)\.', description, re.IGNORECASE)
    if match3:
        cat_text = match3.group(1)
        cat_text = re.sub(r'\s+and\s+', ', ', cat_text)
        cats = [c.strip() for c in cat_text.split(',') if c.strip()]
        categories.extend(cats)
    
    # Pattern 4: "offers a range of services in A, B, C."
    match4 = re.search(r'offers a range of services in ([^.]+?)\.', description, re.IGNORECASE)
    if match4:
        cat_text = match4.group(1)
        cat_text = re.sub(r'\s+and\s+', ', ', cat_text)
        cats = [c.strip() for c in cat_text.split(',') if c.strip()]
        categories.extend(cats)
    
    # Pattern 5: "offers enthusiasts a premier destination for A, B."
    match5 = re.search(r'offers enthusiasts a premier destination for ([^.]+?)\.', description, re.IGNORECASE)
    if match5:
        cat_text = match5.group(1)
        cat_text = re.sub(r'\s+and\s+', ', ', cat_text)
        cats = [c.strip() for c in cat_text.split(',') if c.strip()]
        categories.extend(cats)
    
    # Pattern 6: General "offers A, B, and C."
    match6 = re.search(r'offers ([^.]+?)\.', description, re.IGNORECASE)
    if match6:
        cat_text = match6.group(1)
        # Check if it's a list separated by commas
        if ',' in cat_text or ' and ' in cat_text:
            cat_text = re.sub(r'\s+and\s+', ', ', cat_text)
            cats = [c.strip() for c in cat_text.split(',') if c.strip()]
            categories.extend(cats)
    
    # Clean up categories
    cleaned_categories = []
    for cat in categories:
        cat = re.sub(r'^including\s+', '', cat, flags=re.IGNORECASE)
        cat = cat.strip()
        if cat and len(cat) > 2:
            cleaned_categories.append(cat)
    
    business_id_to_categories[business_id] = cleaned_categories

# Count reviews per category
category_review_counts = defaultdict(int)
for review in reviews:
    business_ref = review['business_ref']
    business_id = business_ref_to_id.get(business_ref)
    
    if business_id and business_id in business_id_to_categories:
        categories = business_id_to_categories[business_id]
        if categories:
            for category in categories:
                # Count each category separately
                category_review_counts[category] += 1

# Get top 5 categories
top_5_categories = sorted(category_review_counts.items(), key=lambda x: x[1], reverse=True)[:5]

print('__RESULT__:')
print(json.dumps({
    'total_reviews': len(reviews),
    'reviews_with_category_matches': len([r for r in reviews if business_ref_to_id.get(r["business_ref"]) in business_id_to_categories and business_id_to_categories.get(business_ref_to_id.get(r["business_ref"]))]),
    'top_5_categories': top_5_categories,
    'all_categories_sample': list(category_review_counts.items())[:20]
}))"""

env_args = {'var_functions.list_db:0': ['review', 'tip', 'user'], 'var_functions.query_db:2': [{'user_id': 'userid_286', 'name': 'Todd', 'review_count': '376', 'yelping_since': '15 Jan 2009, 16:40', 'useful': '1373', 'funny': '723', 'cool': '639', 'elite': '2010,2011,2012,2013,2014'}, {'user_id': 'userid_1331', 'name': 'Patt', 'review_count': '1028', 'yelping_since': '13 Jul 2010, 15:42', 'useful': '9050', 'funny': '3249', 'cool': '5929', 'elite': '2011,2012,2013,2014,2015,2016,2017,2018,2019,20,20,2021'}, {'user_id': 'userid_1880', 'name': 'Norma', 'review_count': '57', 'yelping_since': '2010-09-07 23:24:36', 'useful': '217', 'funny': '57', 'cool': '115', 'elite': '2012,2013'}, {'user_id': 'userid_271', 'name': 'Antony', 'review_count': '49', 'yelping_since': 'October 23, 2011 at 07:47 PM', 'useful': '116', 'funny': '159', 'cool': '34', 'elite': ''}, {'user_id': 'userid_534', 'name': 'Mandy', 'review_count': '754', 'yelping_since': '2011-08-30 13:46:26', 'useful': '2925', 'funny': '775', 'cool': '988', 'elite': '2011,2012,2013,2014,2015,2016,2017,2018,2019,20,20,2021'}], 'var_functions.query_db:5': [{'_id': '6859a000fe8b31cd7362e2ab', 'business_id': 'businessid_49', 'name': 'Steps to Learning Montessori Preschool', 'review_count': '8', 'is_open': '1', 'attributes': {'BusinessAcceptsCreditCards': 'True', 'WiFi': "u'no'", 'BusinessAcceptsBitcoin': 'False'}, 'hours': {'Monday': '0:0-0:0', 'Tuesday': '8:0-17:0', 'Wednesday': '8:0-17:0', 'Thursday': '8:0-17:0', 'Friday': '8:0-17:0'}, 'description': 'Located at 6901 Phelps Rd in Goleta, CA, this facility offers a nurturing environment for young learners, providing a range of services in Education, Elementary Schools, Child Care & Day Care, Local Services, Preschools, and Montessori Schools.'}, {'_id': '6859a000fe8b31cd7362e2ac', 'business_id': 'businessid_47', 'name': 'Breeze Blow Dry Bar', 'review_count': '81', 'is_open': '0', 'attributes': {'ByAppointmentOnly': 'False', 'BusinessAcceptsCreditCards': 'True', 'GoodForKids': 'True', 'RestaurantsPriceRange2': '2', 'BikeParking': 'False', 'BusinessParking': "{'garage': False, 'street': False, 'validated': False, 'lot': True, 'valet': False}"}, 'hours': {'Monday': '7:0-18:0', 'Tuesday': '7:0-18:0', 'Wednesday': '7:0-18:0', 'Thursday': '7:0-18:0', 'Friday': '7:0-19:0', 'Saturday': '8:0-19:0', 'Sunday': '10:0-17:0'}, 'description': 'Located at 9916 Clayton Rd in St. Louis, MO, this establishment offers a wide range of services, including Hair Salons, Beauty & Spas, Hair Stylists, Skin Care, Blow Dry/Out Services, and Makeup Artists.'}, {'_id': '6859a000fe8b31cd7362e2ad', 'business_id': 'businessid_88', 'name': 'Impact Guns', 'review_count': '39', 'is_open': '1', 'attributes': {'BusinessParking': "{'garage': False, 'street': False, 'validated': False, 'lot': False, 'valet': False}", 'GoodForKids': 'True', 'BusinessAcceptsCreditCards': 'True', 'ByAppointmentOnly': 'False', 'BikeParking': 'True'}, 'hours': {'Monday': '10:0-19:0', 'Tuesday': '10:0-19:0', 'Wednesday': '10:0-19:0', 'Thursday': '10:0-19:0', 'Friday': '10:0-19:0', 'Saturday': '10:0-19:0'}, 'description': 'Located at 11655 W Executive Dr in Boise, ID, this facility offers enthusiasts a premier destination for Gun/Rifle Ranges, Active Life.'}, {'_id': '6859a000fe8b31cd7362e2ae', 'business_id': 'businessid_41', 'name': 'Palms Primary Care', 'review_count': '5', 'is_open': '1', 'attributes': 'None', 'hours': {'Monday': '8:30-17:0', 'Tuesday': '8:30-17:0', 'Wednesday': '8:30-17:0', 'Thursday': '8:30-17:0', 'Friday': '8:30-17:0'}, 'description': 'Located at 1615 Pasadena Ave S, Ste 430 in Saint Petersburg, FL, this facility offers a range of services in Internal Medicine, Doctors, Health & Medical.'}, {'_id': '6859a000fe8b31cd7362e2af', 'business_id': 'businessid_33', 'name': 'J&Q Nails', 'review_count': '28', 'is_open': '1', 'attributes': {'BusinessParking': "{'garage': False, 'street': False, 'validated': False, 'lot': False, 'valet': False}", 'BusinessAcceptsCreditCards': 'True', 'AcceptsInsurance': 'False', 'ByAppointmentOnly': 'False', 'RestaurantsPriceRange2': '2', 'WheelchairAccessible': 'True', 'BikeParking': 'False'}, 'hours': {'Monday': '9:30-19:0', 'Tuesday': '9:30-19:0', 'Wednesday': '9:30-19:0', 'Thursday': '9:30-19:0', 'Friday': '9:30-19:0', 'Saturday': '9:30-17:30'}, 'description': 'Located at 9655 E US Hwy 36, Unit H in Avon, IN, this establishment offers a range of services including Nail Salons, Hair Removal, Beauty & Spas, and Waxing.'}], 'var_functions.query_db:6': [{'user_id': 'userid_1231', 'yelping_since': '14 Sep 2016, 00:32'}, {'user_id': 'userid_343', 'yelping_since': '02 Feb 2016, 04:30'}, {'user_id': 'userid_746', 'yelping_since': '2016-06-23 01:59:28'}, {'user_id': 'userid_505', 'yelping_since': 'September 10, 2016 at 08:02 PM'}, {'user_id': 'userid_898', 'yelping_since': 'January 15, 2016 at 06:33 PM'}, {'user_id': 'userid_144', 'yelping_since': '25 Feb 2016, 04:52'}, {'user_id': 'userid_1927', 'yelping_since': 'October 13, 2016 at 04:29 AM'}, {'user_id': 'userid_1109', 'yelping_since': '2016-10-16 18:32:25'}, {'user_id': 'userid_1950', 'yelping_since': '2016-04-16 03:42:28'}, {'user_id': 'userid_1316', 'yelping_since': '2016-12-29 21:32:44'}], 'var_functions.query_db:8': 'file_storage/functions.query_db:8.json', 'var_functions.query_db:10': 'file_storage/functions.query_db:10.json', 'var_functions.execute_python:14': {'total_users_2016': 168, 'sample_users': ['userid_1231', 'userid_343', 'userid_746', 'userid_505', 'userid_898']}, 'var_functions.query_db:16': 'file_storage/functions.query_db:16.json', 'var_functions.execute_python:18': {'total_users_2016': 168, 'total_reviews_by_2016_users': 126, 'sample_reviews': [{'user_id': 'userid_655', 'business_ref': 'businessref_36', 'date': '22 Oct 2021, 21:44'}, {'user_id': 'userid_1397', 'business_ref': 'businessref_23', 'date': '2016-06-28 02:18:33'}, {'user_id': 'userid_1274', 'business_ref': 'businessref_67', 'date': '2018-01-02 21:35:31'}]}, 'var_functions.execute_python:20': {'total_businesses': 20, 'businesses_with_categories': 6, 'sample_categories': {'businessid_49': ['Education', 'Elementary Schools', 'Child Care & Day Care', 'Local Services', 'Preschools', 'Montessori Schools'], 'businessid_47': [], 'businessid_88': [], 'businessid_41': ['Internal Medicine', 'Doctors', 'Health & Medical'], 'businessid_33': []}}, 'var_functions.execute_python:22': {'total_reviews_processed': 126, 'total_businesses_mapped': 20, 'businesses_with_category_info': 18, 'category_review_counts': {'enthusiasts a premier destination for Gun/Rifle Ranges': 4, 'Active Life': 4, 'a range of': 8, 'a delightful selection of treats': 2, 'making it a must-visit for anyone seeking Candy Stores': 2, 'Specialty Food': 2, 'Food': 2, 'Internal Medicine': 1, 'Doctors': 1, 'Health & Medical': 4, 'a delightful array of options ranging from Food': 2, 'Shaved Ice': 2, 'Cajun/Creole': 2, 'Breakfast & Brunch': 2, 'Party & Event Planning': 2, 'Comfort Food': 2, 'Cafes': 2, 'Restaurants': 3, 'to Event Planning &': 2, 'Chinese': 1, "a delightful array of dishes in the category of 'Restaurants": 1, "Chinese'": 1, 'Cosmetics & Beauty Supply': 2, 'Cosmetic Dentists': 2, 'Tanning': 2, 'Teeth Whitening': 2, 'Beauty & Spas': 2, 'Dentists': 2, 'Shopping': 2, 'Blow Dry/Out Services': 2, 'Spray Tanning': 2, 'Hair Salons': 2, 'a diverse range of': 2, 'the categories of Medical Centers': 1}, 'top_5_categories': [['a range of', 8], ['enthusiasts a premier destination for Gun/Rifle Ranges', 4], ['Active Life', 4], ['Health & Medical', 4], ['Restaurants', 3]]}, 'var_functions.query_db:24': 'file_storage/functions.query_db:24.json', 'var_functions.query_db:26': [{'_id': '6859a000fe8b31cd7362e2ab', 'business_id': 'businessid_49', 'name': 'Steps to Learning Montessori Preschool', 'review_count': '8', 'is_open': '1', 'attributes': {'BusinessAcceptsCreditCards': 'True', 'WiFi': "u'no'", 'BusinessAcceptsBitcoin': 'False'}, 'hours': {'Monday': '0:0-0:0', 'Tuesday': '8:0-17:0', 'Wednesday': '8:0-17:0', 'Thursday': '8:0-17:0', 'Friday': '8:0-17:0'}, 'description': 'Located at 6901 Phelps Rd in Goleta, CA, this facility offers a nurturing environment for young learners, providing a range of services in Education, Elementary Schools, Child Care & Day Care, Local Services, Preschools, and Montessori Schools.'}, {'_id': '6859a000fe8b31cd7362e2ac', 'business_id': 'businessid_47', 'name': 'Breeze Blow Dry Bar', 'review_count': '81', 'is_open': '0', 'attributes': {'ByAppointmentOnly': 'False', 'BusinessAcceptsCreditCards': 'True', 'GoodForKids': 'True', 'RestaurantsPriceRange2': '2', 'BikeParking': 'False', 'BusinessParking': "{'garage': False, 'street': False, 'validated': False, 'lot': True, 'valet': False}"}, 'hours': {'Monday': '7:0-18:0', 'Tuesday': '7:0-18:0', 'Wednesday': '7:0-18:0', 'Thursday': '7:0-18:0', 'Friday': '7:0-19:0', 'Saturday': '8:0-19:0', 'Sunday': '10:0-17:0'}, 'description': 'Located at 9916 Clayton Rd in St. Louis, MO, this establishment offers a wide range of services, including Hair Salons, Beauty & Spas, Hair Stylists, Skin Care, Blow Dry/Out Services, and Makeup Artists.'}, {'_id': '6859a000fe8b31cd7362e2ad', 'business_id': 'businessid_88', 'name': 'Impact Guns', 'review_count': '39', 'is_open': '1', 'attributes': {'BusinessParking': "{'garage': False, 'street': False, 'validated': False, 'lot': False, 'valet': False}", 'GoodForKids': 'True', 'BusinessAcceptsCreditCards': 'True', 'ByAppointmentOnly': 'False', 'BikeParking': 'True'}, 'hours': {'Monday': '10:0-19:0', 'Tuesday': '10:0-19:0', 'Wednesday': '10:0-19:0', 'Thursday': '10:0-19:0', 'Friday': '10:0-19:0', 'Saturday': '10:0-19:0'}, 'description': 'Located at 11655 W Executive Dr in Boise, ID, this facility offers enthusiasts a premier destination for Gun/Rifle Ranges, Active Life.'}, {'_id': '6859a000fe8b31cd7362e2ae', 'business_id': 'businessid_41', 'name': 'Palms Primary Care', 'review_count': '5', 'is_open': '1', 'attributes': 'None', 'hours': {'Monday': '8:30-17:0', 'Tuesday': '8:30-17:0', 'Wednesday': '8:30-17:0', 'Thursday': '8:30-17:0', 'Friday': '8:30-17:0'}, 'description': 'Located at 1615 Pasadena Ave S, Ste 430 in Saint Petersburg, FL, this facility offers a range of services in Internal Medicine, Doctors, Health & Medical.'}, {'_id': '6859a000fe8b31cd7362e2af', 'business_id': 'businessid_33', 'name': 'J&Q Nails', 'review_count': '28', 'is_open': '1', 'attributes': {'BusinessParking': "{'garage': False, 'street': False, 'validated': False, 'lot': False, 'valet': False}", 'BusinessAcceptsCreditCards': 'True', 'AcceptsInsurance': 'False', 'ByAppointmentOnly': 'False', 'RestaurantsPriceRange2': '2', 'WheelchairAccessible': 'True', 'BikeParking': 'False'}, 'hours': {'Monday': '9:30-19:0', 'Tuesday': '9:30-19:0', 'Wednesday': '9:30-19:0', 'Thursday': '9:30-19:0', 'Friday': '9:30-19:0', 'Saturday': '9:30-17:30'}, 'description': 'Located at 9655 E US Hwy 36, Unit H in Avon, IN, this establishment offers a range of services including Nail Salons, Hair Removal, Beauty & Spas, and Waxing.'}], 'var_functions.query_db:28': [{'_id': '6859a000fe8b31cd7362e2ab', 'business_id': 'businessid_49', 'name': 'Steps to Learning Montessori Preschool', 'review_count': '8', 'is_open': '1', 'attributes': {'BusinessAcceptsCreditCards': 'True', 'WiFi': "u'no'", 'BusinessAcceptsBitcoin': 'False'}, 'hours': {'Monday': '0:0-0:0', 'Tuesday': '8:0-17:0', 'Wednesday': '8:0-17:0', 'Thursday': '8:0-17:0', 'Friday': '8:0-17:0'}, 'description': 'Located at 6901 Phelps Rd in Goleta, CA, this facility offers a nurturing environment for young learners, providing a range of services in Education, Elementary Schools, Child Care & Day Care, Local Services, Preschools, and Montessori Schools.'}, {'_id': '6859a000fe8b31cd7362e2ac', 'business_id': 'businessid_47', 'name': 'Breeze Blow Dry Bar', 'review_count': '81', 'is_open': '0', 'attributes': {'ByAppointmentOnly': 'False', 'BusinessAcceptsCreditCards': 'True', 'GoodForKids': 'True', 'RestaurantsPriceRange2': '2', 'BikeParking': 'False', 'BusinessParking': "{'garage': False, 'street': False, 'validated': False, 'lot': True, 'valet': False}"}, 'hours': {'Monday': '7:0-18:0', 'Tuesday': '7:0-18:0', 'Wednesday': '7:0-18:0', 'Thursday': '7:0-18:0', 'Friday': '7:0-19:0', 'Saturday': '8:0-19:0', 'Sunday': '10:0-17:0'}, 'description': 'Located at 9916 Clayton Rd in St. Louis, MO, this establishment offers a wide range of services, including Hair Salons, Beauty & Spas, Hair Stylists, Skin Care, Blow Dry/Out Services, and Makeup Artists.'}, {'_id': '6859a000fe8b31cd7362e2ad', 'business_id': 'businessid_88', 'name': 'Impact Guns', 'review_count': '39', 'is_open': '1', 'attributes': {'BusinessParking': "{'garage': False, 'street': False, 'validated': False, 'lot': False, 'valet': False}", 'GoodForKids': 'True', 'BusinessAcceptsCreditCards': 'True', 'ByAppointmentOnly': 'False', 'BikeParking': 'True'}, 'hours': {'Monday': '10:0-19:0', 'Tuesday': '10:0-19:0', 'Wednesday': '10:0-19:0', 'Thursday': '10:0-19:0', 'Friday': '10:0-19:0', 'Saturday': '10:0-19:0'}, 'description': 'Located at 11655 W Executive Dr in Boise, ID, this facility offers enthusiasts a premier destination for Gun/Rifle Ranges, Active Life.'}, {'_id': '6859a000fe8b31cd7362e2ae', 'business_id': 'businessid_41', 'name': 'Palms Primary Care', 'review_count': '5', 'is_open': '1', 'attributes': 'None', 'hours': {'Monday': '8:30-17:0', 'Tuesday': '8:30-17:0', 'Wednesday': '8:30-17:0', 'Thursday': '8:30-17:0', 'Friday': '8:30-17:0'}, 'description': 'Located at 1615 Pasadena Ave S, Ste 430 in Saint Petersburg, FL, this facility offers a range of services in Internal Medicine, Doctors, Health & Medical.'}, {'_id': '6859a000fe8b31cd7362e2af', 'business_id': 'businessid_33', 'name': 'J&Q Nails', 'review_count': '28', 'is_open': '1', 'attributes': {'BusinessParking': "{'garage': False, 'street': False, 'validated': False, 'lot': False, 'valet': False}", 'BusinessAcceptsCreditCards': 'True', 'AcceptsInsurance': 'False', 'ByAppointmentOnly': 'False', 'RestaurantsPriceRange2': '2', 'WheelchairAccessible': 'True', 'BikeParking': 'False'}, 'hours': {'Monday': '9:30-19:0', 'Tuesday': '9:30-19:0', 'Wednesday': '9:30-19:0', 'Thursday': '9:30-19:0', 'Friday': '9:30-19:0', 'Saturday': '9:30-17:30'}, 'description': 'Located at 9655 E US Hwy 36, Unit H in Avon, IN, this establishment offers a range of services including Nail Salons, Hair Removal, Beauty & Spas, and Waxing.'}], 'var_functions.query_db:30': 'file_storage/functions.query_db:30.json', 'var_functions.execute_python:32': {'total_reviews': 126, 'matched_reviews': 63, 'unmatched_reviews': 63, 'total_businesses': 100, 'businesses_with_categories': 47, 'top_5_categories': [['range of', 25], ['comprehensive range of', 10], ['Shopping', 8], ['wide range of', 8], ['diverse range of products and', 7]], 'all_categories': [['range of', 25], ['comprehensive range of', 10], ['Shopping', 8], ['wide range of', 8], ['diverse range of products and', 7], ['Fitness & Instruction', 6], ['Gyms', 6], ['Boot Camps', 6], ['Trainers', 6], ['Active Life', 6], ['Interval Training Gyms', 6], ['Restaurants', 6], ['the categories of Food', 5], ['Grocery', 5], ['Food', 5], ['Health & Medical', 5], ['Breakfast & Brunch', 4], ['Real Estate', 3], ['Apartments', 3], ['Home Services', 3]]}}

exec(code, env_args)
